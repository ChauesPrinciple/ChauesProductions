import re
import os

html_path = 'c:/Users/rober/.gemini/antigravity/scratch/chaues-productions/japan-itinerary-map.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the CSS for day-card border inconsistencies
css_to_replace = """        .day-card.arrival::before,
        .day-card.travel::before {
            background: var(--amber)
        }

        .day-card.partner::before {
            background: var(--partner)
        }

        .day-card.cultural::before {
            background: var(--cultural)
        }

        .day-card.festival::before {
            background: var(--festival)
        }

        .day-card.finale::before {
            background: var(--finale)
        }

        .day-card.active {
            border-color: rgba(245, 158, 11, 0.35);
            background: #152342;
            transform: translateX(3px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4)
        }"""
new_css = """        .day-card::before {
            background: var(--amber);
        }

        .day-card.active {
            border-color: rgba(236, 72, 153, 0.35); /* bold pink */
            background: #152342;
            transform: translateX(3px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4)
        }"""
content = content.replace(css_to_replace, new_css)

# Fix the timeline badge colors
badge_css_to_replace = """        .day-card.active .day-num {
            background: var(--amber);
            color: #000;
            border-color: var(--amber)
        }"""
badge_new_css = """        .day-card.partner .day-num { border-color: rgba(167, 139, 250, 0.4); color: var(--partner); }
        .day-card.cultural .day-num { border-color: rgba(52, 211, 153, 0.4); color: var(--cultural); }
        .day-card.festival .day-num { border-color: rgba(239, 68, 68, 0.4); color: var(--festival); }
        .day-card.finale .day-num { border-color: rgba(251, 146, 60, 0.4); color: var(--finale); }
        
        .day-card.active.arrival .day-num, .day-card.active.travel .day-num { background: var(--amber); color: #000; border-color: var(--amber); }
        .day-card.active.partner .day-num { background: var(--partner); color: #000; border-color: var(--partner); }
        .day-card.active.cultural .day-num { background: var(--cultural); color: #000; border-color: var(--cultural); }
        .day-card.active.festival .day-num { background: var(--festival); color: #000; border-color: var(--festival); }
        .day-card.active.finale .day-num { background: var(--finale); color: #000; border-color: var(--finale); }"""
content = content.replace(badge_css_to_replace, badge_new_css)

# 2. Fix the line base colors so 'loc' is dim gray instead of blue "#1e3a5f"
content = content.replace("const loc = { color: '#1e3a5f', weight: 1.2, opacity: 0.45 };", "const loc = { color: '#334155', weight: 1.2, opacity: 0.45 };")

# 3. Make active map lines highly visible (bold pink for all trains, orange dash for flight)
active_lines_to_replace = """        const aSkn = L.polyline([], { color: '#ec4899', weight: 3.5, opacity: 0.95, lineCap: 'round' }).addTo(map);
        const aLoc = L.polyline([], { color: '#be185d', weight: 2.5, opacity: 0.9, lineCap: 'round' }).addTo(map);
        const aFlt = L.polyline([], { color: '#ea580c', weight: 2, opacity: 0.95, dashArray: '5,7' }).addTo(map);"""
active_lines_new = """        const aSkn = L.polyline([], { color: '#ec4899', weight: 3.5, opacity: 0.95, lineCap: 'round' }).addTo(map);
        const aLoc = L.polyline([], { color: '#ec4899', weight: 3.5, opacity: 0.95, lineCap: 'round' }).addTo(map);
        const aFlt = L.polyline([], { color: '#ea580c', weight: 3.5, opacity: 0.95, dashArray: '5,7' }).addTo(map);"""
content = content.replace(active_lines_to_replace, active_lines_new)

# Update flight background arc to be visible but dimmed
content = content.replace("L.polyline(FLT, { color: 'rgba(234,88,12,0.15)', weight: 1.5, dashArray: '4,6' }).addTo(map);", "L.polyline(FLT, { color: 'rgba(234,88,12,0.45)', weight: 1.5, dashArray: '4,6' }).addTo(map);")

# 5. Fix the ROUTE_SEGS accumulation and missing day points so routes don't vanish on later days.
# Ensure Day 1 starts with EMPTY arrays so there is no small portion of active trace before actually travelling.
route_segs_original = """        const ROUTE_SEGS = [
            { day: 1, s: SKN_TOHOKU.slice(0, 2), l: [], f: [] },
            { day: 4, s: SKN_TOHOKU.slice(0, 8), l: [], f: [] },
            { day: 5, s: SKN_TOHOKU, l: [], f: [] },
            { day: 7, s: SKN_TOHOKU, l: [...OU, ...GONO], f: [] },
            { day: 8, s: SKN_TOHOKU, l: [...OU, ...GONO, ...HACHI], f: [] },
            { day: 10, s: [...SKN_TOHOKU, ...SKN_HKD], l: [], f: [] },
            { day: 11, s: [...SKN_TOHOKU, ...SKN_HKD], l: HOKUTO, f: [] },
            { day: 12, s: [...SKN_TOHOKU, ...SKN_HKD], l: [...HOKUTO, ...OTARU_L], f: [] },
            { day: 13, s: [], l: [], f: FLT.slice(0, 10) },
            { day: 14, s: [], l: [], f: FLT },
        ];"""
route_segs_new = """        const ROUTE_SEGS = [
            { day: 1, s: [], l: [], f: [] },
            { day: 4, s: [SKN_TOHOKU.slice(0, 8)], l: [], f: [] },
            { day: 5, s: [SKN_TOHOKU], l: [], f: [] },
            { day: 7, s: [SKN_TOHOKU], l: [OU, GONO], f: [] },
            { day: 8, s: [SKN_TOHOKU], l: [OU, GONO, HACHI], f: [] },
            { day: 10, s: [SKN_TOHOKU, SKN_HKD], l: [OU, GONO, HACHI], f: [] },
            { day: 11, s: [SKN_TOHOKU, SKN_HKD], l: [OU, GONO, HACHI, HOKUTO], f: [] },
            { day: 12, s: [SKN_TOHOKU, SKN_HKD], l: [OU, GONO, HACHI, HOKUTO, OTARU_L], f: [] },
            { day: 13, s: [SKN_TOHOKU, SKN_HKD], l: [OU, GONO, HACHI, HOKUTO, OTARU_L], f: [FLT.slice(0, 12)] },
            { day: 14, s: [SKN_TOHOKU, SKN_HKD], l: [OU, GONO, HACHI, HOKUTO, OTARU_L], f: [FLT] },
        ];"""
content = content.replace(route_segs_original, route_segs_new)

# 6. Update Legend color for Local/Ltd. Express to match the bright pink aLoc style
legend_loc_original = """<div class="leg-l" style="background:#be185d"></div>Local / Ltd. Express"""
legend_loc_new = """<div class="leg-l" style="background:#ec4899"></div>Local / Ltd. Express"""
content = content.replace(legend_loc_original, legend_loc_new)

# Save
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
