import os

files = [
    "guides/action-units-worksheet.html",
    "guides/fight-scene-structure-worksheet.html",
    "guides/local-business-commercial-guide.html",
    "guides/location-exploration-guide.html",
    "guides/motivated-camera-movement.html",
    "guides/TOKYO THREE-SHOT WORKSHEET.html"
]

replacements = [
    ('\u00e8\u00a2\'\u201a\u00ac\'\u201e\u00a2', "'"),  # Smart apostrophe
    ('\u00e8\u00a2\'\u201a\u00ac\'\u20ac\u0153', '—'),  # Em dash
    ('\u00e8\u00a2\'\u201a\u00ac\'\u20ac', '—'),       # Em dash variant
    ('\u00e8\u00a2\'\u201a\u00ac\u00c5"', '"'),        # Left smart quote
    ('\u00e8\u00a2\'\u201a\u00ac\u00ef\u00bf\u00bd', '"'),  # Right smart quote
    ('\u00e8\u00a2\'\u201a\u00ac', "'"),              # Apostrophe variant
]

for file in files:
    print(f"Fixing {file}...")
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old, new in replacements:
            content = content.replace(old, new)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Fixed {file}")
    except Exception as e:
        print(f"✗ Error fixing {file}: {e}")

print("\nAll files processed!")
