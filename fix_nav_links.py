import os
import re

root_dir = r"c:\Users\rober\.gemini\antigravity\scratch\tokyo-in-film"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Navbar Home link (Root level)
    # <li><a href="index.html" class="active">Home</a></li> -> tokyo-in-film.html
    # Note: tokyo-in-film.html already has correct link, so this targets siblings like scene-project.html
    content = re.sub(r'href="index\.html"([^>]*)>Home</a>', r'href="tokyo-in-film.html"\1>Home</a>', content)
    
    # 2. Navbar Home link (Subdirectory level)
    # <li><a href="../index.html">Home</a></li> -> ../tokyo-in-film.html
    content = re.sub(r'href="\.\./index\.html"([^>]*)>Home</a>', r'href="../tokyo-in-film.html"\1>Home</a>', content)
    
    # 3. Footer/Body "Previous: Home" buttons or loose links
    # <a href="../index.html" class="btn">&larr; Previous: Home</a>
    content = re.sub(r'href="\.\./index\.html"([^>]*)>\s*&larr; Previous: Home</a>', r'href="../tokyo-in-film.html"\1>&larr; Previous: Home</a>', content)
    
    # 4. Just in case text is "Previous: Home" without arrow entity
    content = re.sub(r'href="\.\./index\.html"([^>]*)>\s*Previous: Home</a>', r'href="../tokyo-in-film.html"\1>Previous: Home</a>', content)

    if content != original_content:
        print(f"Fixed: {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.lower().endswith('.html'):
            # Skip the main index.html if it exists (don't want to break the actual landing page if it's there)
            if file.lower() == 'index.html' and subdir == root_dir:
                continue 
            
            fix_file(os.path.join(subdir, file))
