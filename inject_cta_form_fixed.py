import re
import os

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
            color: var(--form-text);
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
            color: var(--form-text);
            transition: border-color 0.2s, background 0.2s;
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

js_func = """
    <script>
        function sendEmail(form) {
            const name = form.querySelector('#contact-name').value;
            const email = form.querySelector('#contact-email').value;
            const message = form.querySelector('#contact-message').value;
            
            const subject = encodeURIComponent("Interest in Chaues Productions Trip");
            const body = encodeURIComponent(`Name: ${name}\\nEmail: ${email}\\n\\nMessage:\\n${message}`);
            
            window.location.href = `mailto:factum.est.illud@gmail.com?subject=${subject}&body=${body}`;
        }
    </script>
"""

form_html = """<form class="cta-form" onsubmit="event.preventDefault(); sendEmail(this);"><div class="cta-input-group"><label class="cta-label" for="contact-name">Name</label><input type="text" id="contact-name" class="cta-input" placeholder="Your name" required></div><div class="cta-input-group"><label class="cta-label" for="contact-email">Email</label><input type="email" id="contact-email" class="cta-input" placeholder="your.email@example.com" required></div><div class="cta-input-group"><label class="cta-label" for="contact-message">Message</label><textarea id="contact-message" class="cta-input cta-textarea" placeholder="Tell me about your interest in this trip..." required></textarea></div><button type="submit" class="cta-btn cta-submit">Send Message &rarr;</button></form>"""

for file in files_to_patch:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Determine theme color and inject CSS
    if 'var(--text)' in content and '--text: #1e293b' in content: 
         txt_color = "var(--text, #1e293b)"
    else:
         txt_color = "#fff"

    # Add the text variable definition for the form
    body_override = f"\\n        body {{ --form-text: {txt_color}; }}\\n"
    full_css = form_css.replace('var(--form-text)', txt_color) + body_override
    
    if '.cta-form {' not in content:
        # Replace only the first occurrence of </style> (which is in the <head>)
        content = content.replace('    </style>', f'{full_css}    </style>', 1)

    # 2. Inject form HTML
    # We replace the closing </p> and the entire <a> tag.
    # The regex targets `</p><a href="https://docs.google.com/forms...</a>'`
    # Because of unicode escapes in raw strings we use a safe regex pattern
    pattern = r'</p><a href="https://docs\.google\.com/forms[^>]+>.*?</a>'
    replacement = f'</p>{form_html}'
    
    if '<form class="cta-form"' not in content:
        content = re.sub(pattern, replacement, content)
        
    # 3. Inject JS function
    if 'function sendEmail' not in content:
        content = content.replace('</body>', f'{js_func}</body>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {file}")
