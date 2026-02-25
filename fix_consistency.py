import re

html_path = 'c:/Users/rober/.gemini/antigravity/scratch/chaues-productions/japan-itinerary-map.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the wildly inconsistent day links in the CSS
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
        }

        .day-card.active::before {
            width: 4px
        }"""

new_css = """        .day-card::before {
            background: var(--amber); /* Make ALL boundaries bold pink for consistency of the day link */
        }

        .day-card.active {
            border-color: rgba(236, 72, 153, 0.35); /* Bold pink active border instead of orange */
            background: #152342;
            transform: translateX(3px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4)
        }

        .day-card.active::before {
            width: 4px
        }

        /* Standardize color-coding of badges based on type */
        .day-card.partner .day-num { border-color: rgba(167, 139, 250, 0.4); color: var(--partner); }
        .day-card.cultural .day-num { border-color: rgba(52, 211, 153, 0.4); color: var(--cultural); }
        .day-card.festival .day-num { border-color: rgba(239, 68, 68, 0.4); color: var(--festival); }
        .day-card.finale .day-num { border-color: rgba(251, 146, 60, 0.4); color: var(--finale); }
        
        .day-card.active.arrival .day-num, .day-card.active.travel .day-num { background: var(--amber); color: #000; border-color: var(--amber); }
        .day-card.active.partner .day-num { background: var(--partner); color: #000; border-color: var(--partner); }
        .day-card.active.cultural .day-num { background: var(--cultural); color: #000; border-color: var(--cultural); }
        .day-card.active.festival .day-num { background: var(--festival); color: #000; border-color: var(--festival); }
        .day-card.active.finale .day-num { background: var(--finale); color: #000; border-color: var(--finale); }"""

if css_to_replace in content:
    content = content.replace(css_to_replace, new_css)
else:
    print("FAILED TO FIND CSS TO REPLACE")

# 2. Fix the missing bold pink badge CSS text replace gap
content = content.replace('.day-card.active .day-num {\n            background: var(--amber);\n            color: #000;\n            border-color: var(--amber)\n        }', '')

# 3. Fix the mapping route segments accumulation so links don't disappear on later days
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

if route_segs_original in content:
    content = content.replace(route_segs_original, route_segs_new)
else:
    print("FAILED TO FIND ROUTE_SEGS TO REPLACE")

# Make the return flight arc more opaque per browser subagent finding
content = content.replace("color: 'rgba(234,88,12,0.15)'", "color: 'rgba(234,88,12,0.45)'")
content = content.replace("opacity: 0.75, dashArray: '5,7'", "opacity: 0.95, dashArray: '5,7'")

# Remove empty CSS block
content = re.sub(r'\.day-card\.active\s*\.day-num\s*\{\s*\}', '', content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("SUCCESS")
