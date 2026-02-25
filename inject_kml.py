import os

def patch_html(filepath, map_id, is_dark):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add script tag in head
    if '<script src="assets/js/kml_data.js"></script>' not in html:
        html = html.replace('</head>', '    <script src="assets/js/kml_data.js"></script>\n</head>')

    # 2. Add styles for KML popup
    if '.kml-popup' not in html:
        styles = f"""
        .kml-popup .leaflet-popup-content-wrapper {{
            background: {"rgba(7, 16, 31, 0.92)" if is_dark else "var(--card)"};
            border: 1px solid {"rgba(255, 255, 255, 0.1)" if is_dark else "var(--border)"};
            border-radius: 8px;
            box-shadow: 0 4px 16px rgba(0,0,0,{"0.5" if is_dark else "0.1"});
            padding: 0;
            backdrop-filter: blur(10px);
        }}
        .kml-popup .leaflet-popup-tip {{
            background: {"rgba(7, 16, 31, 0.92)" if is_dark else "var(--card)"};
            border-top: 1px solid {"rgba(255, 255, 255, 0.1)" if is_dark else "var(--border)"};
            border-left: 1px solid {"rgba(255, 255, 255, 0.1)" if is_dark else "var(--border)"};
        }}
        .kml-popup .leaflet-popup-content {{
            margin: 0;
            padding: 12px 14px;
            font-family: 'Inter', sans-serif;
            color: {"#fff" if is_dark else "var(--text)"};
            line-height: 1.4;
        }}
        .kml-category {{
            font-size: 8.5px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: {"var(--muted)" if is_dark else "var(--muted)"};
            margin-bottom: 4px;
        }}
        .kml-name {{
            font-size: 13px;
            font-weight: 700;
            color: {"#fff" if is_dark else "var(--text)"};
            margin-bottom: 6px;
        }}
        .kml-desc {{
            font-family: 'Lato', sans-serif;
            font-size: 12px;
            color: {"var(--prose)" if is_dark else "var(--prose)"};
        }}
"""
        html = html.replace('</style>', styles + '    </style>')

    # 3. Add to Legend
    if "Chaues' Map (KML)" not in html:
        legend_marker_color = "rgba(71,85,105,0.6)" if is_dark else "rgba(100,116,139,0.3)"
        legend_border_color = "#475569" if is_dark else "#64748b"
        legendHtml = f"""
                <div class="leg-h" style="margin-top:6px">Places</div>
                <div class="leg-r">
                    <div class="leg-poi" style="background:{legend_marker_color};border-color:{legend_border_color}"></div>Chaues' Map (KML)
                </div>
"""
        html = html.replace('            </div>\n            <div id="trip-nav">', legendHtml + '            </div>\n            <div id="trip-nav">')

    # 4. Add logic to render markers
    if 'getDistance(' not in html:
        marker_color = "rgba(71, 85, 105, 0.6)" if is_dark else "#64748b"
        marker_border = "#475569" if is_dark else "#64748b"
        
        logic = f"""
        // Haversine distance formula
        function getDistance(lat1, lon1, lat2, lon2) {{
            const R = 6371; // km
            const dLat = (lat2 - lat1) * Math.PI / 180;
            const dLon = (lon2 - lon1) * Math.PI / 180;
            const a = Math.sin(dLat/2) * Math.sin(dLat/2) +
                      Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
                      Math.sin(dLon/2) * Math.sin(dLon/2);
            const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
            return R * c;
        }}

        if (typeof KML_DATA !== 'undefined') {{
            KML_DATA.forEach(p => {{
                if (!p.coordinates) return;

                const isAccommodation = p.folder.toLowerCase().includes('accommodation');
                const isTokyo = p.coordinates.lat > 35.5 && p.coordinates.lat < 35.9 && p.coordinates.lng > 139.5 && p.coordinates.lng < 140.0;
                
                // Filter trivial accomodations entirely unless in Tokyo
                if (isAccommodation && !isTokyo) return;

                let tooClose = false;
                if (typeof CITIES !== 'undefined') {{
                    Object.values(CITIES).forEach(c => {{
                        if (getDistance(p.coordinates.lat, p.coordinates.lng, c.lat, c.lng) < 0.2) tooClose = true;
                    }});
                }}
                if (typeof ALL !== 'undefined') {{
                    ALL.forEach(d => {{
                        if (d.lat && d.lng && getDistance(p.coordinates.lat, p.coordinates.lng, d.lat, d.lng) < 0.2) tooClose = true;
                    }});
                }}
                
                if (tooClose) return;

                const m = L.circleMarker([p.coordinates.lat, p.coordinates.lng], {{
                    radius: 3.5,
                    fillColor: '{marker_color}',
                    color: '{marker_border}',
                    weight: 1.5,
                    opacity: 0.6,
                    fillOpacity: 0.4
                }}).addTo(map);
                
                m.bindTooltip('<b>' + p.name + '</b>', {{
                    className: 'ct',
                    permanent: false,
                    direction: 'top'
                }});
                
                // Only bind popup if we have a description or a specific folder
                const popupContent = '<div class="kml-category">' + p.folder + '</div><div class="kml-name">' + p.name + '</div>' + 
                                     (p.description ? '<div class="kml-desc">' + p.description + '</div>' : '');
                
                m.bindPopup(popupContent, {{
                    className: 'kml-popup',
                    maxWidth: 280
                }});
                
                m.on('mouseover', function() {{
                    this.setStyle({{ fillOpacity: 0.9, opacity: 1, radius: 5 }});
                }});
                m.on('mouseout', function() {{
                    this.setStyle({{ fillOpacity: 0.4, opacity: 0.6, radius: 3.5 }});
                }});
            }});
        }}
"""
        html = html.replace("const tl = document.getElementById('timeline');", logic + "\n        const tl = document.getElementById('timeline');")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Patched {filepath}")

patch_html(r"c:\Users\rober\.gemini\antigravity\scratch\chaues-productions\japan-bushido-map.html", "map", False)
patch_html(r"c:\Users\rober\.gemini\antigravity\scratch\chaues-productions\japan-itinerary-map.html", "map", True)
