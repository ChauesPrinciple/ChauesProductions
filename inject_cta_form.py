import re

files_to_patch = [
    "japan-bushido-map.html",
    "japan-itinerary-map.html",
    "ireland-map.html"
]

form_css = """
        .cta-form {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-top: 20px;
            text-align: left;
        }

        .cta-input-group {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .cta-label {
            font-size: 11px;
            font-weight: 600;
            color: var(--text, #fff);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .cta-input {
            width: 100%;
            padding: 10px 12px;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(150, 150, 150, 0.2);
            border-radius: 6px;
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            color: var(--text, #fff);
            transition: border-color 0.2s, background 0.2s;
        }
        
        /* Ireland map specific light text override if var text isn't set */
        body {
            --form-text: var(--text, #fff);
        }

        .cta-input:focus {
            outline: none;
            border-color: var(--accent);
            background: rgba(255, 255, 255, 0.1);
        }

        .cta-input::placeholder {
            color: rgba(150, 150, 150, 0.5);
        }

        .cta-textarea {
            resize: vertical;
            min-height: 80px;
        }

        .cta-submit {
            margin-top: 8px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            width: 100%;
            cursor: pointer;
            border: none;
        }
"""

for file in files_to_patch:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine theme specific values based on the file content (dark vs light mode text variables)
    if 'var(--text)' in content and '--text: #1e293b' in content: 
         # Bushido map is light mode
         form_css_themed = form_css.replace('var(--text, #fff)', 'var(--text, #1e293b)')
    else:
         # Rassera and Ireland maps are dark mode
         form_css_themed = form_css.replace('var(--text, #fff)', '#fff')
         

    if '.cta-form' not in content:
        content = content.replace('    <script src=', f'{form_css_themed}    </style>\n    <script src=')
        content = content.replace('.cta-btn:hover {', '.cta-form {').replace('</style>', '') # Cleanup if replaced directly earlier in some edge cases.
        content = content.replace("    </style>\n    </style>", "    </style>")

    
    # Replace the innerHTML injection logic for the JS timeline generation.
    # Searching for: cta.innerHTML = '<h3>Join This Trip</h3>... <a href="..." class="cta-btn">Express Interest \u2192</a>';
    
    match = re.search(r"cta\.innerHTML = '(.*?)<a href=.*?class=\"cta-btn\">Express Interest \\u2192</a>';", content, re.DOTALL)
    if match:
        original_header_text = match.group(1)
        
        # Build the form HTML
        form_html = f"""{original_header_text}
        <form class="cta-form" onsubmit="event.preventDefault(); sendEmail(this);">
            <div class="cta-input-group">
                <label class="cta-label" for="contact-name">Name</label>
                <input type="text" id="contact-name" class="cta-input" placeholder="Your name" required>
            </div>
            <div class="cta-input-group">
                <label class="cta-label" for="contact-email">Email</label>
                <input type="email" id="contact-email" class="cta-input" placeholder="your.email@example.com" required>
            </div>
            <div class="cta-input-group">
                <label class="cta-label" for="contact-message">Message</label>
                <textarea id="contact-message" class="cta-input cta-textarea" placeholder="Tell me about your interest in this trip..." required></textarea>
            </div>
            <button type="submit" class="cta-btn cta-submit">Send Message \u2192</button>
        </form>
        """
        # Compress the HTML to a single line string to comply with the JS injection format without breaking JS
        form_html_single_line = re.sub(r'>\s+<', '><', form_html).replace('\n', '').replace('    ', '')
        
        # Replace the full cta.innerHTML exact match
        content = content.replace(match.group(0), f"cta.innerHTML = '{form_html_single_line}';")
        
    js_func = """
        function sendEmail(form) {
            const name = form.querySelector('#contact-name').value;
            const email = form.querySelector('#contact-email').value;
            const message = form.querySelector('#contact-message').value;
            
            const subject = encodeURIComponent("Interest in Chaues Productions Trip");
            const body = encodeURIComponent(`Name: ${name}\\nEmail: ${email}\\n\\nMessage:\\n${message}`);
            
            window.location.href = `mailto:factum.est.illud@gmail.com?subject=${subject}&body=${body}`;
        }
    """
    
    if 'function sendEmail' not in content:
        content = content.replace('</script>\n</body>', f'{js_func}</script>\n</body>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {file}")
