---
description: Edit, update, or add content to any of the interactive Leaflet travel or anime location map pages. Invoke when asked to work on japan-bushido-map.html, japan-itinerary-map.html, ireland-map.html, chainsaw-man-reze-map.html, tokyo-ghoul-map.html, jjk-culling-game-map.html, or any map page using Leaflet.js with a sidebar and info panel.
---

# Update Maps Skill

## BARRIER — Read Before Any Edit

Map pages are part of **Chaues Productions**, not Tokyo in Film. Do not apply Tokyo in Film styles or curriculum structure to map pages.

Do not confuse `style.css` (Tokyo in Film, dark cinematic) with the inline CSS inside each map file. Map pages are self-contained single-file HTML — all CSS and JS is inline. There is no shared stylesheet for map pages.

---

## Map Pages Inventory

| File | Subject | Theme |
|---|---|---|
| `japan-bushido-map.html` | Bushido travel itinerary, Kumano Kodo, martial arts | Dark navy, amber accent |
| `japan-itinerary-map.html` | Japan general travel itinerary | Dark navy, amber accent |
| `ireland-map.html` | Ireland travel itinerary | Dark green, teal accent |
| `chainsaw-man-reze-map.html` | Chainsaw Man / Reze Arc anime locations | Dark, red accent |
| `tokyo-ghoul-map.html` | Tokyo Ghoul anime locations | Dark, purple/red |
| `jjk-culling-game-map.html` | Jujutsu Kaisen Culling Game locations | Dark, blue accent |

---

## Standard Map Page Architecture

Every map page follows this layout pattern:

```
<body> (display: flex, height: 100vh)
  ├── #sidebar (fixed width, scrollable)
  │   ├── #trip-header (title, eyebrow label)
  │   ├── #timeline (scrollable day cards)
  │   │   └── .day-card (one per day/location)
  │   │       ├── .eyebrow (day label)
  │   │       ├── .trip-h (location name)
  │   │       ├── .evts (event list)
  │   │       └── .card-prose-mb (mobile prose, hidden on desktop)
  │   └── .sec-label (section dividers)
  └── #map-wrap (flex: 1)
      ├── #map (Leaflet instance)
      ├── #info (floating info panel, desktop only)
      │   ├── #info-bar (day label + location name)
      │   └── #info-text (prose + events detail)
      ├── #legend (bottom-left)
      └── #trip-nav (bottom-center, page navigation between maps)
```

---

## Brand Fonts (ALL map pages)

```html
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&display=swap" rel="stylesheet">
```

| Element | Font | Usage |
|---|---|---|
| `html, body` | `Raleway` | Base font |
| `.eyebrow` | `Cinzel` | Day labels, section labels |
| `.trip-h` | `Cinzel` | Location headings |
| `.sec-label` | `Cinzel` | Sidebar section dividers |
| `.info-day-lbl` | `Cinzel` | Info panel day label |
| `.info-loc-lbl` / `.info-loc` | `Cinzel` | Info panel location name |
| `#info-prose`, `.prose-p`, `.card-prose-mb` | `Raleway` | Body prose |
| `.ct` (tooltip) | `Raleway` | Map tooltip |
| `#trip-nav` | `Raleway` | Navigation bar |
| `.kml-popup`, `.kml-desc`, `.cta-input` | `Raleway` | Popups and form inputs |

**Note:** Cinzel maxes at weight 700. Change any `font-weight: 800` or `900` to `700` when using Cinzel.

---

## Leaflet.js Conventions

- Leaflet CSS linked from CDN before the inline `<style>` block
- Map initialized as: `const map = L.map('map', { ... })`
- Tile layer: typically CartoDB Dark Matter or similar dark tile
- Custom markers: SVG-based via `L.divIcon`
- Tooltip class: `.ct` (custom tooltip)
- Popup class: `.kml-popup` / `.kml-desc`
- Day card click → `map.flyTo()` + info panel update
- Map pin click → sidebar scroll + info panel update

---

## Itinerary Data Structure (Japan travel maps)

Itinerary data is stored as a JS array inside the HTML file, typically:

```js
const DAYS = [
  {
    id: 'day-1',
    label: 'DAY 1',
    city: 'Tokyo',
    title: 'Arrival',
    lat: 35.6762, lng: 139.6503,
    events: ['Event 1', 'Event 2'],
    prose: 'Descriptive paragraph...',
  },
  // ...
];
```

When editing itinerary content:
- `label` → appears in `.eyebrow`
- `title` → appears in `.trip-h` and `#info-loc-lbl`
- `events` → rendered as `<ul class="evts">`
- `prose` → rendered in `#info-prose` and `.card-prose-mb`
- `lat`/`lng` → used for `map.flyTo()` and pin placement

---

## Procedure for Map Edits

### Adding or editing a day/stop
1. Locate the `DAYS` array (or equivalent data structure) in the JS section
2. Edit the relevant object — `title`, `events`, `prose`, `lat`, `lng`
3. Verify coordinates against a real map source if modifying location
4. Check that the corresponding Leaflet marker exists or add one

### Changing the visual theme / colors
1. Edit the `:root` CSS variables at the top of the `<style>` block
2. Common variables: `--accent`, `--bg`, `--card`, `--border`, `--text`, `--prose`, `--muted`

### Adding a new map pin (POI)
1. Add an entry to the markers/POI array in the JS section
2. Use `L.marker([lat, lng], { icon: L.divIcon({ ... }) })` pattern
3. Bind tooltip and click handler consistent with existing pins

### Font updates (if not yet applied)
- Check the Google Fonts `<link>` tag — must include Cinzel and Raleway
- Grep for `Inter` and `Lato` in the file — replace with Raleway (body) or Cinzel (headers)
- See `FONT-UPDATE-TOKYO-IN-FILM.md` for the exact swap pattern (same logic applies to anime maps)

---

## Mobile Behavior

All map pages have a `@media(max-width:760px)` block that:
- Stacks sidebar (50vh) above map (50vh)
- Hides `#info` panel (prose shown in `.card-prose-mb` instead)
- Moves `#trip-nav` to `position: fixed; bottom: 24px`

Do not remove or break this block when editing.

---

## KML / External Data

- `Chaues' Map of Japan.kml` — source of Japan location data
- `parsed_map_data.json` — pre-parsed KML for use in map pages
- `inject_kml.py` — script that injects KML data into map HTML
- `parse_kml.py` — converts KML to JSON

When adding new Japan locations, update `parsed_map_data.json` first, then reference in the map HTML.
