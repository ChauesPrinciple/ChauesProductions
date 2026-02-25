import re

html_path = 'c:/Users/rober/.gemini/antigravity/scratch/chaues-productions/japan-itinerary-map.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the Day Card Border which was still orange
content = re.sub(r'rgba\(245,\s*158,\s*11,\s*0\.18\)', 'rgba(236,72,153,0.18)', content)

# Fix amber-text which was still yellow #fcd34d -> light pink #fbcfe8
content = content.replace('#fcd34d', '#fbcfe8')

# Fix the Legend Return Flight which was pink instead of orange
content = content.replace('border-color:rgba(236,72,153,0.45)', 'border-color:rgba(234,88,12,0.45)')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
