import os

base = 'c:/Users/rober/.gemini/antigravity/scratch/chaues-productions/'
files = ['index.html', 'index-jp.html', 'japan-itinerary-map.html']

for f in files:
    path = os.path.join(base, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('—', ':').replace('–', 'to')
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Replaced all dashes")
