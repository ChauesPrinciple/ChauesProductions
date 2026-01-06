
import os

# Define the root directory
ROOT_DIR = r"c:\Users\rober\.gemini\antigravity\scratch\tokyo-in-film"

# Define the target string (what to find)
TARGET_HTML = '<div class="logo">Tokyo in Film</div>'

# Define the replacement HTML (what to replace with)
REPLACEMENT_HTML = """<div class="logo">
            Tokyo in Film
            <div class="dropdown-menu">
                <a href="https://chauesprinciple.github.io/Tokyo-in-Film/" class="dropdown-item current">Tokyo in Film</a>
                <a href="https://chauesprinciple.github.io/Ancient-literature/" class="dropdown-item">Ancient Literature</a>
            </div>
        </div>"""

def update_files():
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if TARGET_HTML in content:
                        new_content = content.replace(TARGET_HTML, REPLACEMENT_HTML)
                        
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated: {file_path}")
                        count += 1
                    else:
                        # Check if it was already updated to avoid double processing or if hidden in different formatting
                        pass
                        
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    print(f"Total files updated: {count}")

if __name__ == "__main__":
    update_files()
