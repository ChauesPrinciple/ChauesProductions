import re
import os
import shutil

html_path = 'japan-itinerary-map.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove emojis
content = re.sub(r"emoji:\s*'.*?',\s*", "", content)
content = re.sub(r'<div class="card-em">\$\{d\.emoji\}</div>', '', content)

# 2. Add film sites markers and right column visuals
# Add visual to prose:
prose_replace = r"`<img src=\"${d.img}\" style=\"width:100%; border-radius:8px; margin-bottom:15px; border:1px solid var(--border);\">` + day.prose"
content = content.replace("document.getElementById('info-prose').innerHTML = day.prose || '';", f"document.getElementById('info-prose').innerHTML = {prose_replace};")

# Add map markers for film sites
film_sites_code = """
        const FILM_SITES = [
            { lat: 35.7050, lng: 139.6496, name: 'Mabashi Inari Shrine (Tokyo In Film)' },
            { lat: 35.7049, lng: 139.6497, name: 'Live Music JIROKICHI (Tokyo In Film)' },
            { lat: 35.7334, lng: 139.8827, name: 'KOIWA BUSH BASH (Tokyo In Film)' }
        ];
        FILM_SITES.forEach(s => {
            L.circleMarker([s.lat, s.lng], { radius: 6, fillColor: '#10b981', color: '#fff', weight: 2, opacity: 0.9, fillOpacity: 0.9 }).addTo(map)
                .bindTooltip(`<b>${s.name}</b>`, { className: 'ct', permanent: false, direction: 'top' });
        });
"""
if "FILM_SITES" not in content:
    content = content.replace("        const cMkrs = {};", film_sites_code + "\n        const cMkrs = {};")

# 3. Replace Image constants to point to proper files, including the new generated ones.
images_repl = """        const I = {
            tokyo_arrive: 'assets/images/bg.jpg',
            tokyo_night: 'assets/images/image07.png',
            tokyo_street: 'assets/images/image07.png',
            racing: 'assets/images/image01.png',
            shinkansen: 'assets/images/bg.jpg',
            morioka: 'assets/images/bg.jpg',
            nebuta: 'assets/images/image02.png',
            castle: 'assets/images/gosho_float.webp',
            coast: 'assets/images/bg.jpg',
            fireworks: 'assets/images/image02.png',
            hokkaido: 'assets/images/bg.jpg',
            sapporo: 'assets/images/bg.jpg',
            otaru: 'assets/images/bg.jpg',
            vintage: 'assets/images/tokyo_finale.webp',
        };"""

content = re.sub(r'        const I = \{.*?\};', images_repl, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("HTML processing complete.")

