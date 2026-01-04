import os

root_dir = r"c:\Users\rober\.gemini\antigravity\scratch\tokyo-in-film"
target_string = " Adapted from Humanities LibreTexts."
replacement_string = ""

print(f"Scanning {root_dir}...")

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(subdir, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if target_string in content:
                    print(f"Fixing {file}...")
                    new_content = content.replace(target_string, replacement_string)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
            except Exception as e:
                print(f"Error processing {file}: {e}")

print("Done.")
