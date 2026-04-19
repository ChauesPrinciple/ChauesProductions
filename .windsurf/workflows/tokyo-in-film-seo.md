---
description: Apply SEO, performance, and UX improvements to the Tokyo in Film project
---

# Tokyo in Film — SEO & Performance Improvement Script

## Project location
The Tokyo in Film project lives at:
`c:\Users\rober\CascadeProjects\chaues-productions\tokyo-in-film.html`
and subdirectories: `pre-production/`, `production/`, `post-production/`

The deployed GitHub Pages URL base is:
`https://chauesprinciple.github.io/Tokyo-in-Film/`

---

## Step 1 — Add `<link rel="canonical">` to every page

Each page needs a canonical link pointing to its own absolute URL. Add to `<head>`:

```html
<!-- tokyo-in-film.html -->
<link rel="canonical" href="https://chauesprinciple.github.io/Tokyo-in-Film/index.html" />

<!-- pre-production/index.html -->
<link rel="canonical" href="https://chauesprinciple.github.io/Tokyo-in-Film/pre-production/" />

<!-- production/index.html -->
<link rel="canonical" href="https://chauesprinciple.github.io/Tokyo-in-Film/production/" />

<!-- post-production/index.html -->
<link rel="canonical" href="https://chauesprinciple.github.io/Tokyo-in-Film/post-production/" />
```
Repeat the pattern for every sub-page (individual lesson pages, glossary, scene-project, etc.)

---

## Step 2 — Add `<link rel="preconnect">` for Google Fonts

Before any `<link href="https://fonts.googleapis.com/...">` stylesheet link, add:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

---

## Step 3 — Upgrade Open Graph meta tags

Replace or supplement the existing OG tags on each page. Template for `tokyo-in-film.html`:

```html
<meta property="og:type" content="website" />
<meta property="og:locale" content="en_US" />
<meta property="og:site_name" content="Tokyo in Film" />
<meta property="og:title" content="Tokyo in Film — Filmmaking Course by Robert Ladd" />
<meta property="og:description" content="An on-location filmmaking course set in Tokyo. Pre-production, production, and post-production taught through real cinematic fieldwork." />
<meta property="og:image" content="https://chauesprinciple.github.io/Tokyo-in-Film/[hero-image.jpg]" />
<meta property="og:image:alt" content="Tokyo in Film — students filming on location in Tokyo" />
<meta property="og:url" content="https://chauesprinciple.github.io/Tokyo-in-Film/index.html" />
```

For module pages (e.g. pre-production), adjust `og:title`, `og:description`, `og:url`, and `og:image` to match the specific module.

Add Twitter card tags:
```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="[page title]" />
<meta name="twitter:description" content="[page description]" />
<meta name="twitter:image" content="[absolute image URL]" />
<!-- For content pages, add author/topic labels -->
<meta name="twitter:label1" content="Instructor" />
<meta name="twitter:data1" content="Robert Ladd" />
<meta name="twitter:label2" content="Module" />
<meta name="twitter:data2" content="[Pre-Production | Production | Post-Production]" />
```

---

## Step 4 — Add `decoding="async"` to all non-hero images

For any `<img>` that uses `loading="lazy"`, also add `decoding="async"`:

```html
<img src="..." alt="..." loading="lazy" decoding="async">
```

The hero/above-fold image should NOT have `loading="lazy"` — keep it eager (default) but can add `decoding="async"`.

---

## Step 5 — Reading progress bar (long-form pages only)

Add to `pre-production/`, `production/`, and `post-production/` index pages and any long lesson pages.

**HTML** (immediately after `<body>`):
```html
<style>
  progress.read-progress {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 3px;
    appearance: none;
    border: none;
    background: transparent;
    z-index: 9999;
  }
  progress.read-progress::-webkit-progress-bar { background: transparent; }
  progress.read-progress::-webkit-progress-value { background: #e63946; }
  progress.read-progress::-moz-progress-bar { background: #e63946; }
</style>
<progress class="read-progress" value="0" max="100"></progress>
```

**JS** (before `</body>`):
```html
<script>
  (function() {
    var bar = document.querySelector('progress.read-progress');
    if (!bar) return;
    function update() {
      var s = document.documentElement;
      var pct = (s.scrollTop / (s.scrollHeight - s.clientHeight)) * 100;
      bar.value = Math.min(pct, 100);
    }
    window.addEventListener('scroll', update, { passive: true });
  })();
</script>
```

Replace `#e63946` with the site's accent color.

---

## Step 6 — JSON-LD structured data (`Course` + `Person`)

Add to `tokyo-in-film.html` before `</head>`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Course",
      "name": "Tokyo in Film",
      "description": "An on-location filmmaking course set in Tokyo covering pre-production, production, and post-production through real cinematic fieldwork.",
      "url": "https://chauesprinciple.github.io/Tokyo-in-Film/index.html",
      "provider": {
        "@type": "Person",
        "name": "Robert Ladd",
        "url": "https://chauesprinciple.github.io/ChauesProductions/",
        "sameAs": [
          "https://www.instagram.com/chaues/"
        ]
      },
      "inLanguage": "en",
      "educationalLevel": "University",
      "hasCourseInstance": [
        {
          "@type": "CourseInstance",
          "courseMode": "onsite",
          "location": {
            "@type": "Place",
            "name": "Tokyo, Japan"
          }
        }
      ]
    },
    {
      "@type": "Person",
      "@id": "https://chauesprinciple.github.io/ChauesProductions/#robert-ladd",
      "name": "Robert Ladd",
      "jobTitle": "Filmmaker & Educator",
      "url": "https://chauesprinciple.github.io/ChauesProductions/",
      "sameAs": [
        "https://www.instagram.com/chaues/"
      ]
    }
  ]
}
</script>
```

For individual module pages, use `@type: "LearningResource"` or `@type: "WebPage"` with `"isPartOf"` pointing to the Course URL.

---

## Step 7 — Speculation Rules prefetch (multi-page navigation)

Add before `</body>` on `tokyo-in-film.html` and any page with links to multiple module pages:

```html
<script type="speculationrules">
{
  "prefetch": [{
    "source": "document",
    "where": {
      "and": [
        { "href_matches": "/*" },
        { "not": { "selector_matches": "a[rel~='nofollow']" } }
      ]
    },
    "eagerness": "conservative"
  }]
}
</script>
```

This is Chromium-only (Chrome/Edge). Safe to add — other browsers ignore it. The `conservative` eagerness only prefetches when the user hovers over a link.

---

## Step 8 — Fix known content issues

1. **`tokyo-in-film.html` line ~214** — Replace placeholder:
   ```html
   <!-- Change: -->
   <a href="https://example.com" style="color: inherit; text-decoration: underline;">Robert Ladd</a>
   <!-- To: -->
   <a href="https://chauesprinciple.github.io/ChauesProductions/" style="color: inherit; text-decoration: underline;">Robert Ladd</a>
   ```

2. **Corrupted emoji in `tokyo-in-film.html`** — Several emoji display as `?` or `??`. Review and restore:
   - CTA button: `📷 See Student Films & Projects`
   - Map key: `⭐`, `🎥`, `🍜`, `🌳`, `⛩️`, `🛍️`
   - Japanese partner text (line ~104): garbled UTF-8 — needs to be re-entered from source

3. **`glossary.html`** — `--accent-red` CSS variable is used but undefined in `style.css`. Either define it or replace with a concrete color value.

---

## Step 9 — Commit and push

```powershell
git add -A
git commit -m "Tokyo in Film: SEO/perf improvements — canonical, OG tags, JSON-LD, progress bar"
git push
```

---

## Priority order (if doing incrementally)

1. Steps 1–4 (canonical, preconnect, OG tags, decoding) — trivial, 30 min, high SEO impact
2. Step 8 (fix known content issues) — correctness fixes, 15 min
3. Step 5 (reading progress bar) — UX improvement, 20 min
4. Step 6 (JSON-LD) — SEO boost, 30 min
5. Step 7 (speculation rules) — performance, 5 min
