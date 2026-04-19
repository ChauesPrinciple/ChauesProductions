---
description: Edit, research, or build Japan travel itinerary content. Invoke when asked to update Japan day-by-day itineraries, add transit details, update accommodation info, add cultural context, work with KML location data, or plan Japan travel routes. Covers japan-bushido-map.html, japan-itinerary-map.html, japan-summer-2026-itinerary.md, aomori-nebuta-festival-2026.md, Chaues' Map of Japan.kml, and parsed_map_data.json.
---

# Japan Travel Content Skill

## Content Identity

This content represents **Robert Ladd's firsthand Japan fieldwork** — not generic tourism copy. All itinerary prose should reflect on-the-ground specificity: actual trail distances, real transit options, authentic cultural context, specific accommodation villages/areas (not individual hotel names unless confirmed). The content serves two audiences simultaneously: travelers who will use it as a planning resource, and readers who experience it as travel writing.

**Tone:** Direct, specific, observational. No filler phrases. No vague praise. No contact info unless verified.

---

## File Map

| File | Role |
|---|---|
| `japan-bushido-map.html` | Bushido itinerary — embedded JS data array (`DAYS`) + Leaflet map |
| `japan-itinerary-map.html` | General Japan itinerary — embedded JS data array + Leaflet map |
| `japan-summer-2026-itinerary.md` | Summer 2026 planning document (markdown, not deployed) |
| `aomori-nebuta-festival-2026.md` | Nebuta festival 2026 research notes |
| `Chaues' Map of Japan.kml` | Master KML — all Japan location pins |
| `parsed_map_data.json` | KML parsed to JSON for programmatic use |
| `inject_kml.py` | Injects KML data into map HTML |
| `parse_kml.py` | Converts KML → JSON |

---

## Bushido Itinerary — Key Facts

The Bushido trip is a martial arts + pilgrimage route through Japan. Core anchors:

| Day | Location | Focus |
|---|---|---|
| Days 1-2 | Tokyo | Arrival, martial arts context |
| Days 3-4 | Kyoto | Sword history, dojo |
| Days 5-6 | Osaka / Nara | Cultural stops |
| Day 7 | Wakayama → Tanabe | Kumano Kodo entry point |
| Day 8 | Nakahechi trail | Takijiri-oji → Chikatsuyu walk (~15 km) |
| Day 9 | Chikatsuyu → Near Chikatsuyu | **Musuhi Budojo session** + overnight in village |
| Day 10 | Continue Nakahechi | Chikatsuyu → Hosshinmon-oji |

### Musuhi Budojo (Day 9) — Confirmed Details
- **Coordinates:** 33.8580° N, 135.6090° E
- **Address:** 和歌山県田辺市中辺路町近露1038
- **Location:** Near Chikatsuyu village, Nakaheri route
- **Note:** Overnight accommodation is in **Chikatsuyu village minshuku** (guesthouses), NOT at the dojo itself

### Kumano Kodo — Nakahechi Route Standards
- Trail distances are in **km**, not miles
- Transit: Ryujin Bus connects Tanabe ↔ trailheads
- Minshuku (民宿) = family-run guesthouses — the correct accommodation type for trail villages
- Do not recommend specific named properties unless verified by fieldwork
- The trail is a UNESCO World Heritage Site

---

## Japan Transit Reference

| Route | Method | Notes |
|---|---|---|
| Tokyo → Kyoto | Shinkansen (Hikari/Nozomi) | ~2.5 hrs |
| Kyoto → Osaka | JR Osaka Loop / Shinkansen | 15-30 min |
| Osaka → Tanabe (Wakayama) | JR Kinokuni Line (Limited Express Kuroshio) | ~2 hrs |
| Tanabe → Takijiri-oji | Ryujin Bus | ~1 hr, seasonal schedule |
| Tanabe → Shingu | JR Kinokuni Line | ~2.5 hrs |
| Along Nakahechi | Walk or Ryujin Bus | Bus frequency varies by season |

---

## Content Standards for Itinerary Prose

### Do
- Specific distances: "15 km from Takijiri-oji to Chikatsuyu"
- Real transit options: "Ryujin Bus from Tanabe Station, ~50 min"
- Accommodation type: "minshuku in Chikatsuyu village" or "tozan-goya (mountain hut)"
- Cultural specificity: reference actual practices, not generalized "Japanese culture"
- Elevation and terrain notes where relevant to trail planning

### Do not
- Vague praise: "beautiful scenery," "amazing experience," "unique opportunity"
- Contact information for specific businesses unless confirmed
- Booking links or endorsements
- Approximate coordinates — use real ones
- Conflate different days or trails

---

## KML Data Workflow

When adding new Japan locations to the map:

1. Add coordinates to `Chaues' Map of Japan.kml` (or note them for manual addition)
2. Run `parse_kml.py` to regenerate `parsed_map_data.json`
3. Run `inject_kml.py` (or manually update the `DAYS`/markers array in the HTML)
4. Verify pin appears correctly on the Leaflet map

For quick one-off additions directly to a map HTML file:
- Find the markers array in the `<script>` section
- Add `{ name: '...', lat: XX.XXXX, lng: XXX.XXXX, type: '...', desc: '...' }`
- Add a corresponding Leaflet marker with the correct icon class

---

## Procedure for Itinerary Edits

### Editing existing day content
1. Open the target map HTML file
2. Find the `DAYS` array entry for the relevant day (search by `id` or `label`)
3. Edit `events` (bullet list items) or `prose` (narrative paragraph)
4. Keep `lat`/`lng` accurate — verify against known coordinates if changing location
5. Ensure `city` and `title` match the info panel display

### Adding a new day/stop
1. Add new object to `DAYS` array with all required fields
2. Add corresponding map marker in the markers section
3. Add sidebar `.day-card` HTML (or verify it's generated from the data)

### Updating transit details
- Transit goes in `events` array as a bullet item
- Format: `"Transit: [method], [duration/distance] from [origin]"`
- Cross-reference with Japan Transit Reference table above

### Updating accommodation
- Accommodation goes in `events` as final bullet: `"Overnight: [village/area], [accommodation type]"`
- Do not name specific properties unless confirmed
