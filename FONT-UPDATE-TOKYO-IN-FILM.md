# Font Update — Tokyo in Film

Apply the same Chaues Productions brand font system used on the three map pages.

## Current fonts (to remove)
- `Inter` — body/UI
- `Outfit` — headings/display

## Replace with
- `Cinzel` — headings, labels, display elements
- `Raleway` — body text, UI, prose, form inputs

## Google Fonts URL (swap this in `<head>`)

**Remove:**
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Outfit:wght@700;900&display=swap" rel="stylesheet">
```

**Replace with:**
```html
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&display=swap" rel="stylesheet">
```

## CSS changes (in `style.css`)

| Find | Replace with |
|------|-------------|
| `font-family: 'Inter'` | `font-family: 'Raleway'` |
| `font-family: 'Outfit'` | `font-family: 'Cinzel'` |

## Where to apply Cinzel
Heading-level elements: `h1`, `h2`, `h3`, `.logo`, section labels, nav titles, any element currently using `Outfit`.  
Note: Cinzel's max weight is 700 — change any `font-weight: 800` or `font-weight: 900` to `700`.

## Where to apply Raleway
Everything else: body copy, nav links, captions, UI labels, form inputs — anything currently using `Inter`.
