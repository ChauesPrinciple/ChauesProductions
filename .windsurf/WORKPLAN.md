# Chaues Productions — Agent Workplan

Full map of every domain in this repo, the files that belong to each, the skill that governs it, and current state.

---

## Domain Map

| Domain | Skill File | Primary Files | State |
|---|---|---|---|
| Chaues Productions landing page | `skills/update-chaues-website/` | `index.html`, `landing-style.css`, `index-jp.html` | Stable |
| Tokyo in Film courseware | `skills/update-tokyo-in-film/` | `tokyo-in-film.html`, `style.css`, `pre-production/`, `production/`, `post-production/`, `guides/`, `glossary.html` | Stable; font update pending (see `FONT-UPDATE-TOKYO-IN-FILM.md`) |
| Interactive travel maps | `skills/update-maps/` | `japan-bushido-map.html`, `japan-itinerary-map.html`, `ireland-map.html`, `chainsaw-man-reze-map.html`, `tokyo-ghoul-map.html`, `jjk-culling-game-map.html` | Active development |
| Japan travel content | `skills/japan-travel/` | `japan-bushido-map.html` (embedded data), `japan-itinerary-map.html`, `japan-summer-2026-itinerary.md`, `aomori-nebuta-festival-2026.md`, `Chaues' Map of Japan.kml`, `parsed_map_data.json` | Active; Summer 2026 itinerary in progress |
| Interactive visualizations | `skills/interactive-viz/` | `closure_axiom(1).html`, `filter_test.html` | Stable post bug-fix |
| Forms & lead capture | `skills/forms-system/` | `contact-form-embedded.html`, `FORMS_STRATEGY.md`, `GOOGLE_FORM_SETUP.md`, `generate_form.js`, `scripts/` | Stable; 3-form system deployed |

---

## Project Separation Rule (BARRIER)

This repo hosts **two publicly deployed websites** from one root. Mixing their files breaks both.

| Project | Entry point | CSS | Live URL |
|---|---|---|---|
| Chaues Productions | `index.html` | `landing-style.css` | https://chauesprinciple.github.io/ChauesProductions/ |
| Tokyo in Film | `tokyo-in-film.html` | `style.css` | https://chauesprinciple.github.io/ChauesProductions/tokyo-in-film.html |

The map pages, visualizations, and guides are **part of Chaues Productions**, not Tokyo in Film, even though they live at the same root.

---

## Brand System

### Chaues Productions (landing page)
- Fonts: `Nunito Sans` (body) + `Lato` (light text)
- Colors: white background, clean/minimalist
- Style: round profile image, link-tree layout

### Map Pages
- Fonts: **`Cinzel`** (headers, labels, display) + **`Raleway`** (body, prose, UI)
- Colors: dark backgrounds, amber (`#EF9F27` / `--accent`), teal (`#5DCAA5`)
- Tech: Leaflet.js + custom sidebar + info panel

### Tokyo in Film
- Fonts: `Inter` (body) + `Outfit` (headings) — **pending swap to Cinzel/Raleway** (see `FONT-UPDATE-TOKYO-IN-FILM.md`)
- Colors: dark/cinematic, neon pink/cyan
- Style: full courseware, multi-page

---

## File Inventory by Type

### HTML — Public pages
```
index.html                      Landing page (Chaues Productions)
index-jp.html                   Japanese language landing page
tokyo-in-film.html              Tokyo in Film course hub
japan-bushido-map.html          Bushido travel itinerary map
japan-itinerary-map.html        Japan general itinerary map
ireland-map.html                Ireland travel map
chainsaw-man-reze-map.html      Chainsaw Man / Reze Arc anime locations
tokyo-ghoul-map.html            Tokyo Ghoul anime locations
jjk-culling-game-map.html       Jujutsu Kaisen Culling Game map
closure_axiom(1).html           Sacred geometry / S³ interactive visualization
glossary.html                   Tokyo in Film glossary
free-guides.html                Filmmaking guides index
scene-project.html              Student scene project page
filter_test.html                Filter test (dev/experimental)
contact-form-embedded.html      Embeddable contact form
```

### HTML — Curriculum (Tokyo in Film)
```
pre-production/index.html        Pre-production hub
pre-production/cinematography.html
pre-production/mise-en-scene.html
pre-production/narrative.html
pre-production/how-to-watch.html
pre-production/catharsis.html
production/index.html            Production hub
production/cinematography.html
production/mise-en-scene.html
production/sound-design.html
production/visual-foreshadowing.html
post-production/index.html       Post-production hub
post-production/editing-and-animation.html
post-production/sound-design.html
post-production/animated-films.html
post-production/rhythm-of-process.html
guides/ (15 standalone worksheets)
```

### Data & KML
```
Chaues' Map of Japan.kml         Full Japan location dataset
parsed_map_data.json             Parsed KML → JSON
japan-summer-2026-itinerary.md   Summer 2026 trip planning doc
aomori-nebuta-festival-2026.md   Nebuta festival research
josh-johnson-structural-analysis.md  Film analysis
josh-johnson-bad-bunny-halftime.md   Film/performance analysis
```

### Scripts (utility, not deployed)
```
generate_form.js                 Google Forms generation script
inject_kml.py                    KML data injection into map HTML
parse_kml.py                     KML → JSON parser
rewrite_map.py / rewrite_map_2.py  Map HTML rewriter
fix_*.py / fix_*.ps1             Encoding/content fix utilities
apply_fixes.py                   Batch fix runner
create_landing.py                Landing page generator
inject_cta_form.py               CTA form injection
```

---

## Pending Tasks (as of last session)

### Map pages
- [ ] Apply Cinzel/Raleway font update to `chainsaw-man-reze-map.html`, `tokyo-ghoul-map.html`, `jjk-culling-game-map.html` (same logic as the three travel maps — see `FONT-UPDATE-TOKYO-IN-FILM.md` for the swap pattern)
- [ ] Verify `chainsaw-man-reze-map.html` mobile layout

### Tokyo in Film
- [ ] Apply Cinzel/Raleway font swap (Inter → Raleway, Outfit → Cinzel) per `FONT-UPDATE-TOKYO-IN-FILM.md`
- [ ] Apply SEO/perf improvements per `workflows/tokyo-in-film-seo.md`

### Chaues Productions landing
- [ ] `index.html` font stack still uses Nunito Sans + Lato — consider whether to unify with brand fonts or keep separate identity

### Interactive visualizations
- [ ] `closure_axiom(1).html` — all six bugs fixed; no outstanding issues

### Cleanup
- [ ] Remove stale utility scripts (`fix_*.py`, `temp_*` folders, `.bak` files) after confirming they are no longer needed
- [ ] `git_diff_output.txt`, `git_log_output.txt`, `git_status_output.txt` are temp debug files — safe to delete

---

## Deployment

- Static site, deployed via GitHub Pages from `main` branch
- Push to `main` = live immediately
- No build step required
- Commit pattern: `git add [files]; git commit -m "[scope]: [description]"; git push`
