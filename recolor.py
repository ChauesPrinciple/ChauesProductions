import re
import os

html_path = 'c:/Users/rober/.gemini/antigravity/scratch/chaues-productions/japan-itinerary-map.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS Variables
# --amber 
content = content.replace('--amber: #f59e0b;', '--amber: #ec4899;')
content = content.replace('rgba(245,158,11,', 'rgba(236,72,153,')
content = content.replace('#f59e0b', '#ec4899')
content = content.replace('#d97706', '#be185d') # Darker amber variant to darker pink variant

# Replace inline styles and script variables
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(content.count('#ec4899'))
print("Color changed")
