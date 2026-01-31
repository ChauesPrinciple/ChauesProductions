---
description: CRITICAL SAFETY BARRIER - PREVENT LANDING PAGE OVERWRITE
---
# PROJECT SAFETY RULES

## 🛑 STOP AND READ

This project contains **TWO SEPARATE WEBSITES** in the same root.

1.  **Chaues Productions** (`index.html`)
    -   **CSS:** `landing-style.css`
    -   **Content:** Robert Ladd Bio, Forms, Gallery.
    -   **RULE:** NEVER apply "Tokyo in Film" themes or content to this file.

2.  **Tokyo in Film** (`tokyo-in-film.html`)
    -   **CSS:** `style.css`
    -   **Content:** Courseware, Chapters, Modules.

## INSTRUCTIONS FOR AGENTS
-   Before editing `index.html`, verify you are NOT using `style.css`.
-   Before editing `style.css`, verify you are NOT checking `index.html` for visual changes (it won't affect it).
-   **DO NOT MERGE** these two projects.

// turbo
echo "Safety rules checked."
