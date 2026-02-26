import os

files_to_patch = [
    "japan-bushido-map.html",
    "japan-itinerary-map.html",
    "ireland-map.html"
]

css_injection = """
        details#legend-details summary::-webkit-details-marker {
            display: none;
        }
        details#legend-details summary {
            list-style: none;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0;
            user-select: none;
        }
        details#legend-details summary::after {
            content: '▼';
            font-size: 8px;
            opacity: 0.6;
        }
        details#legend-details[open] summary::after {
            content: '▲';
        }
        .legend-inner {
            margin-top: 8px;
            padding-top: 8px;
            border-top: 1px solid rgba(150, 150, 150, 0.2);
        }
"""

js_injection = """
    <script>
        // Collapse legend on mobile
        if (window.innerWidth <= 760) {
            const legDetails = document.getElementById('legend-details');
            if (legDetails) legDetails.removeAttribute('open');
        }
    </script>
</body>"""

for file in files_to_patch:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Inject CSS
    if 'details#legend-details' not in content:
        content = content.replace("</style>", css_injection + "    </style>")
        modified = True

    # 2. Wrap Legend HTML
    start_tag = '<div id="legend">'
    end_tag = '            <div id="trip-nav">'
    
    if start_tag in content and end_tag in content and '<details id="legend-details"' not in content:
        start_idx = content.find(start_tag) + len(start_tag)
        end_idx = content.rfind('</div>', start_idx, content.find(end_tag))
        
        inner_content = content[start_idx:end_idx]
        
        wrapped_content = f"""
                <details id="legend-details" open>
                    <summary class="leg-h">Map Key</summary>
                    <div class="legend-inner">{inner_content}</div>
                </details>
            """
        content = content[:start_idx] + wrapped_content + content[end_idx:]
        modified = True

    # 3. Inject JS
    if 'legDetails.removeAttribute' not in content:
        content = content.replace("</body>", js_injection)
        modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully patched {file}")
    else:
        print(f"Skipped {file} (already patched)")
