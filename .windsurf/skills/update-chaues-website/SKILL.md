---
description: Update or edit the Chaues Productions landing page website. Invoke when asked to edit index.html, the landing page, Robert Ladd's portfolio, contact forms, partner grid, gallery, or the Chaues Productions brand website.
---

# Update Chaues Productions Website Skill

## BARRIER — Read Before Any Edit

This repository contains TWO completely separate projects. Mixing them destroys both.

- **Chaues Productions (landing page)**: `index.html` + `landing-style.css`
- **Tokyo in Film (courseware)**: `tokyo-in-film.html` + `style.css` + `production/`, `pre-production/`, `post-production/`

**If editing `index.html`: use `landing-style.css` ONLY. Never link `style.css` to it.**
**If editing `tokyo-in-film.html`: use `style.css` ONLY. Never overwrite `index.html` with courseware content.**

## Chaues Productions — Project Identity

- **Owner**: Robert Ladd (filmmaker, professor, content creator)
- **Audience**: Collaborators, sponsors, students seeking the filmmaker
- **Style**: Minimalist, white/clean, round profile picture
- **Live URL**: https://chauesprinciple.github.io/ChauesProductions/
- **Files**: `index.html`, `landing-style.css`, contact form, partner grid, gallery

## Procedure for Website Edits

### Step 1: Identify which project is being edited
- Chaues Productions landing page → `index.html` + `landing-style.css`
- Tokyo in Film courseware → see update-tokyo-in-film skill

### Step 2: Check style sheet linkage
- Confirm `index.html` only references `landing-style.css`
- Never add `style.css` (neon/dark) references to the landing page

### Step 3: Make the edit
- Maintain minimalist aesthetic: white background, clean typography, no dark mode
- Contact forms: Google Forms embed (see `GOOGLE_FORM_SETUP.md`)
- Partner grid, gallery: HTML section structure, maintain existing patterns

### Step 4: Verify separation
- Did this edit touch any Tokyo in Film files? It should not have.
- Are both projects' HTML files still linking to their correct CSS?
