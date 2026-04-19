---
description: Edit, debug, or extend the lead capture and contact form system. Invoke when asked to work on contact forms, Google Forms integration, form generation scripts, the 3-form system, or the contact-form-embedded.html page.
---

# Forms System Skill

## System Overview

Chaues Productions uses a **3-form system** via Google Forms. Each form targets a distinct audience. Forms are external (Google-hosted) and linked from `index.html` as `<a href="...">` buttons — they are not embedded iframes on the main page.

| Form | Audience | Key Fields |
|---|---|---|
| Video & Production | Clients needing videography, editing, writing | Service type, location, project description, budget |
| Trip Planning & Guides | Travelers wanting Japan itineraries or on-site guide | Service type, travel dates, group size, interests |
| Tokyo & Partnerships | Japanese businesses, schools, sponsors | Inquiry type, org name, proposal |

---

## File Map

| File | Role |
|---|---|
| `index.html` | Links to all 3 Google Form URLs in the `contact-grid` section |
| `contact-form-embedded.html` | Standalone embeddable contact form (single form, lightweight) |
| `FORMS_STRATEGY.md` | Human-readable 3-form strategy guide |
| `GOOGLE_FORM_SETUP.md` | Step-by-step setup instructions for Google Forms + Apps Script |
| `generate_form.js` | Google Apps Script — generates all 3 forms programmatically |
| `scripts/` | Additional utility scripts |

---

## Current Form URLs (in index.html)

```
Video & Production:
https://docs.google.com/forms/d/e/1FAIpQLSdgPml3YpzJD4UhFtxM_PbYwfqgGsLJwObNiFaCEVLu1tzTFg/viewform

Trip Planning & Guides:
https://docs.google.com/forms/d/e/1FAIpQLSfdWWbpqfl-k4JKedyTJF-JhbWG8_l2zguDloL9ea1veMnNxw/viewform

Tokyo & Partnerships:
https://docs.google.com/forms/d/e/1FAIpQLScX4WYdnTzry-I3kw5iioerv7q0JZuA1bhkjzFkD25niC_FYg/viewform
```

These are live. Do not replace them unless the user explicitly provides new form URLs.

---

## index.html Contact Grid Structure

The three form buttons live in `.contact-grid` inside `.collab-text`:

```html
<div class="collab-text">
  <div class="contact-grid">
    <a href="[VIDEO_FORM_URL]" class="contact-card" target="_blank" rel="noopener noreferrer">
      <svg>...</svg>
      <strong>Video &amp; Production</strong>
      <span>Editing, Writing, Videography</span>
    </a>
    <a href="[PLANNING_FORM_URL]" class="contact-card" ...>
      <strong>Trip Planning &amp; Guides</strong>
      ...
    </a>
    <a href="[TOKYO_FORM_URL]" class="contact-card" ...>
      <strong>Tokyo &amp; Partnerships</strong>
      ...
    </a>
  </div>
</div>
```

All form links use `target="_blank" rel="noopener noreferrer"` — keep this pattern.

---

## Generating New Forms (Apps Script)

If forms need to be regenerated or new forms created:

1. Open [Google Apps Script](https://script.google.com)
2. Create a new project
3. Paste contents of `generate_form.js`
4. Click **Run** and grant permissions
5. The script prints 3 form URLs in the Execution Log
6. Copy the URLs and update `index.html` `contact-grid` hrefs

---

## contact-form-embedded.html

A lightweight standalone form for embedding in other contexts (partner sites, email, etc.). Does not use the 3-form system — it's a single general-purpose contact form. Maintains the Chaues Productions aesthetic (white/clean, not dark mode).

When editing `contact-form-embedded.html`:
- Use `landing-style.css` conventions (white background, minimalist)
- Do not apply dark/map/Tokyo-in-Film styles
- Keep it embeddable — no fixed `height: 100vh`, no sidebar layouts

---

## Procedure for Form Edits

### Updating a form link
1. Get the new Google Form URL (viewform endpoint)
2. In `index.html`, find the relevant `<a href="...">` in `.contact-grid`
3. Replace the `href` value only
4. Verify `target="_blank" rel="noopener noreferrer"` is still present

### Adding a fourth form button
1. Add new `<a class="contact-card">` block to `.contact-grid`
2. Follow the existing SVG icon + `<strong>` + `<span>` pattern
3. Verify the grid layout still works at mobile widths (`.contact-grid` uses CSS Grid)

### Changing form button labels
- `<strong>` = primary label (bold, larger)
- `<span>` = subtitle (smaller, muted color)
- Match the audience description in `FORMS_STRATEGY.md`

### Modifying the Apps Script generator
- `generate_form.js` uses the Google Forms API via Apps Script
- Each form is defined as an object with `title`, `description`, and `fields` array
- Field types: `TEXT`, `PARAGRAPH_TEXT`, `MULTIPLE_CHOICE`, `CHECKBOX`, `DROPDOWN`, `DATE`
- After modifying the script, re-run it to get new form URLs and update `index.html`
