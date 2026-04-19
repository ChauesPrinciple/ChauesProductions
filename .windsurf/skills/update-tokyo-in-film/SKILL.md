---
description: Update, edit, or add content to the Tokyo in Film courseware website. Invoke when asked to edit the filmmaking curriculum, production guides, glossary, pre-production pages, production pages, post-production pages, scene projects, maps, or the tokyo-in-film.html page.
---

# Update Tokyo in Film Website Skill

## BARRIER — Read Before Any Edit

This repository contains TWO completely separate projects. Mixing them destroys both.

- **Tokyo in Film (courseware)**: `tokyo-in-film.html` + `style.css` + `production/`, `pre-production/`, `post-production/`, `guides/`, `glossary.html`
- **Chaues Productions (landing page)**: `index.html` + `landing-style.css`

**If editing Tokyo in Film: use `style.css` (cinematic, dark mode, neon pink/cyan) ONLY.**
**NEVER overwrite or modify `index.html` when working on Tokyo in Film content.**

## Tokyo in Film — Project Identity

- **Course**: Location-based filmmaking curriculum for study abroad in Tokyo
- **Audience**: Students, filmmakers, educators
- **Style**: Cinematic, dark mode, neon pink/cyan (`style.css`)
- **Live URL**: https://chauesprinciple.github.io/ChauesProductions/tokyo-in-film.html
- **Adapted from**: *Moving Pictures* by Russell Sharman

## Curriculum Structure

| Phase | Directory | Focus |
|-------|-----------|-------|
| Pre-Production | `pre-production/` | Screenwriting, storyboarding, location scouting |
| Production | `production/` | Cinematography, lighting, sound, directing |
| Post-Production | `post-production/` | Editing, sound design, color grading |

Additional: `guides/` (standalone filmmaking worksheets), `glossary.html`, `scene-project.html`, `free-guides.html`

## Procedure for Content Edits

### Step 1: Identify the target file
- Curriculum phase page? → find correct subdirectory
- Guide/worksheet? → `guides/`
- Glossary? → `glossary.html`
- Scene project? → `scene-project.html`

### Step 2: Check style consistency
- Dark mode, cinematic aesthetic — not minimalist/white
- Neon pink/cyan color scheme for headings, accents
- `style.css` linked, NOT `landing-style.css`

### Step 3: Content standards
- All production content is practical and workshop-ready
- Guides are standalone: each guide should work without the full site
- Terminology consistent with professional film production vocabulary
- H5P interactive content embedded from LibreTexts where applicable
- Google Forms for student submissions (see `GOOGLE_FORM_SETUP.md`)

### Step 4: Verify separation
- Did this edit touch `index.html` or `landing-style.css`? It should not have.
