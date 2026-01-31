# 🛑 BARRIER - DO NOT TOUCH WITHOUT READING

**CRITICAL ARCHITECTURE RULES**

There are **TWO DISTINCT PROJECTS** in this repository. 
**DO NOT MIX THEM.**

---

## 1. Chaues Productions (The Landing Page)
- **Target:** `index.html`
- **Style:** `landing-style.css` (Minimalist, White/Clean, Round Profile Pic)
- **Content:** Robert Ladd Personal Bio, Gallery, Partner Grid, Contact Forms.
- **RULE:** NEVER overwrite `index.html` with "Tokyo in Film" content.
- **RULE:** NEVER link `style.css` (Neon theme) to `index.html`.

## 2. Tokyo in Film (The Courseware)
- **Target:** `tokyo-in-film.html`, `production/`, `pre-production/`, etc.
- **Style:** `style.css` (Cinematic, Dark Mode, Neon Pink/Cyan)
- **RULE:** This is a SUB-PROJECT. It lives happily alongside the landing page but **MUST NOT CONSUME IT**.

---

**IF YOU ARE EDITING `index.html`, YOU MUST USE `landing-style.css`.**
**IF YOU ARE EDITING `tokyo-in-film.html`, YOU MUST USE `style.css`.**
