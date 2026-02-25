import re

html_path = 'c:/Users/rober/.gemini/antigravity/scratch/chaues-productions/japan-itinerary-map.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("Yoshitomo Nara's Aomori Dog", "Yoshitomo Nara\\'s Aomori Dog")
content = content.replace("Shirohige's Cream Puff Factory", "Shirohige\\'s Cream Puff Factory")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
