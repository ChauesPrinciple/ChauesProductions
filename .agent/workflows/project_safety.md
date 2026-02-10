---
description: CRITICAL SAFETY BARRIER - PREVENT LANDING PAGE OVERWRITE
---
# PROJECT SAFETY RULES

## 🛑 STOP AND READ BEFORE EVERY CHANGE

This repo (`ChauesProductions.git`) contains **TWO SEPARATE WEBSITES** sharing the same root directory.

### 1. Chaues Productions (Robert Ladd's Portfolio)
-   **Homepage:** `index.html`
-   **CSS:** `landing-style.css`
-   **Content:** Robert Ladd bio, forms, gallery, filmmaker portfolio.
-   **Live URL:** https://chauesprinciple.github.io/ChauesProductions/

### 2. Tokyo in Film (Open Courseware)
-   **Homepage:** `tokyo-in-film.html`
-   **CSS:** `style.css`
-   **Content:** Courseware, chapters, modules, filmmaking guides.
-   **Live URL:** https://chauesprinciple.github.io/ChauesProductions/tokyo-in-film.html

## 🚨 ABSOLUTE RULES

1.  **NEVER** overwrite `index.html` with Tokyo in Film content. `index.html` is ALWAYS the Chaues Productions portfolio.
2.  **NEVER** apply `style.css` themes to `index.html`. That file uses `landing-style.css`.
3.  **NEVER** use `git add .` — always stage specific files by name to avoid accidentally committing deletions or unrelated changes.
4.  **ALWAYS** verify which file you are editing before making changes:
    -   If editing Tokyo in Film → edit `tokyo-in-film.html` (NOT `index.html`)
    -   If editing Chaues Productions → edit `index.html` with `landing-style.css`
5.  **NEVER** merge or cross-contaminate these two projects.

## INSTRUCTIONS FOR AGENTS
-   Before editing ANY file, re-read this safety workflow.
-   Before any `git push`, run `git diff --stat` to verify what you are about to push.
-   If in doubt, ASK THE USER before pushing.

// turbo
echo "Safety rules checked."
