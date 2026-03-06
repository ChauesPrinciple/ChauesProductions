# Frontend Patterns Reference
*Parsed and saved Mar 2026 — for use across Chaues Productions projects*

---

## 1. SVG Sprite Systems

### Pattern A — External SVG File + XHR Injection (SmugMug / chrisburkard.com)
Fetch an external `.svg` file and inject it at the top of `<body>`. Then reference icons
anywhere with `<use href="#icon-name">`. Works cross-origin if served from same domain.

```js
var getSVG = function(path) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', path, true);
    xhr.responseType = 'document';
    xhr.onload = function() {
        try {
            if (this.status >= 200 && (this.status < 300 || this.status === 304)) {
                xhr.responseXML && document.body.insertBefore(
                    xhr.responseXML.documentElement,
                    document.body.childNodes[0]
                );
            }
        } catch(e) {}
    };
    xhr.send();
};

getSVG('/img/icons-large.svg');
getSVG('/img/icons-small.svg');
```

The external SVG file structure:
```xml
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
    <symbol id="instagram" viewBox="0 0 16 16">
        <path d="..."/>
    </symbol>
    <symbol id="menu" viewBox="0 0 24 24">
        <path d="..."/>
    </symbol>
</svg>
```

Usage in HTML (after injection):
```html
<svg width="20" height="20" fill="currentColor">
    <use href="#instagram"/>
</svg>
```

### Pattern B — CSS mask-image Data URI (Tokyo in Film implementation)
Icon defined once in CSS, zero HTML markup needed. Best for single repeated icons.

```css
.ig-icon::before {
    content: '';
    display: block;
    width: 20px;
    height: 20px;
    background-color: currentColor;
    -webkit-mask-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='...'/%3E%3C/svg%3E");
    mask-image: url("data:image/svg+xml,...");
    -webkit-mask-size: contain;
    mask-size: contain;
    -webkit-mask-repeat: no-repeat;
    mask-repeat: no-repeat;
}
```

**When to use which:**
- Pattern A → multiple different icons reused throughout a site
- Pattern B → one or two icons that only appear in one context

---

## 2. Retina / HiDPI Images

### Retina Logo Pattern (SmugMug)
Store both 1× and 2× versions, serve via JS or CSS:

```json
{
    "imageUrl":   "logo-100x46.png",
    "retinaUrl":  "logo-200x92.png"
}
```

```html
<!-- HTML srcset approach (preferred) -->
<img
    src="logo-100x46.png"
    srcset="logo-100x46.png 1x, logo-200x92.png 2x"
    width="100"
    height="46"
    alt="Logo"
/>
```

### SmugMug Image Size Naming Convention
Pre-generated at upload time — reference for naming your own size variants:

| Key  | Dimensions     | Use case              |
|------|----------------|-----------------------|
| Ti   | 100×100        | Tiny thumbnail        |
| Th   | 150×150        | Thumbnail             |
| S    | 400×267        | Small                 |
| M    | 600×400        | Medium                |
| L    | 800×533        | Large (card)          |
| XL   | 1024×683       | Extra large           |
| X2   | 1280×853       | Retina medium         |
| X3   | 1600×1067      | Retina large          |
| X4   | 2048×1365      | Cold (rarely served)  |
| X5   | 2560×1707      | Cold                  |
| 4K   | 3840×2560      | Cold                  |
| O    | Original       | Download only         |

```html
<!-- srcset using SmugMug-style sizing -->
<img
    src="photo-M.jpg"
    srcset="photo-S.jpg 400w, photo-M.jpg 600w, photo-L.jpg 800w, photo-XL.jpg 1024w, photo-X2.jpg 1280w"
    sizes="(max-width: 600px) 400px, (max-width: 1024px) 800px, 1280px"
    alt="Description"
    loading="lazy"
/>
```

---

## 3. Video Background with Image Fallback

### Pattern (SmugMug / chrisburkard.com)
Multiple video resolutions + HLS stream + static image fallback:

```json
{
    "BackgroundType": "video",
    "Loop": true,
    "VideoKey": "MNzLz88",
    "FallbackImageKey": "qfpXq3L",
    "VideoSizes": {
        "1280": "video-1280.mp4",
        "1920": "video-1920.mp4",
        "HLS":  "master.m3u8"
    }
}
```

```html
<video autoplay muted loop playsinline poster="fallback.jpg">
    <source src="video-1920.mp4" type="video/mp4" media="(min-width: 1280px)">
    <source src="video-1280.mp4" type="video/mp4">
    <!-- Fallback for no-video support -->
    <img src="fallback.jpg" alt="Background">
</video>
```

**CSS background fallback pattern:**
```css
.hero {
    background-image: url('fallback.jpg');
    background-size: cover;
    background-position: center;
}
.hero video {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

---

## 4. Scroll Animation — Locomotive Scroll v5 Data API

### Source: Locomotive Scroll v5 Astro demo

**Core data attributes:**

```html
<!-- Marks element for scroll observation -->
<div data-scroll>...</div>

<!-- Parallax speed: negative = slower, positive = faster, 0 = normal -->
<div data-scroll data-scroll-speed="-0.1">Slow</div>
<div data-scroll data-scroll-speed="0.5">Fast</div>

<!-- Add CSS class when element enters viewport -->
<div style="opacity:0;" data-scroll data-scroll-class="is-visible" data-scroll-offset="10%, 10%">
    Fades in
</div>

<!-- CSS class toggles on EVERY scroll in/out (not just once) -->
<div data-scroll data-scroll-repeat data-scroll-class="is-visible">
    Repeats
</div>

<!-- Expose scroll progress as CSS variable --progress (0→1) -->
<div style="opacity: var(--progress);" data-scroll data-scroll-css-progress>
    Gets more opaque as you scroll
</div>

<!-- Fire a named custom JS event with progress data -->
<div data-scroll data-scroll-event-progress="myProgressEvent" data-scroll-offset="10%, 10%">
</div>

<!-- Control which edge of element triggers: start | middle | end -->
<div data-scroll-position="start,end" data-scroll data-scroll-event-progress="myEvent">
</div>

<!-- Fire a named event on enter/leave -->
<div data-scroll data-scroll-call="myScrollEvent" data-scroll-repeat>
</div>

<!-- Smooth scroll to target -->
<button data-scroll-to data-scroll-to-href="#section-id">Go to section</button>

<!-- Enable parallax speed on touch devices -->
<div data-scroll data-scroll-speed="-0.1" data-scroll-enable-touch-speed>
</div>
```

### Vanilla JS Equivalent (no library — IntersectionObserver)
For simple "reveal on scroll" without a library:

```js
const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
        e.target.classList.toggle('is-visible', e.isIntersecting);
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -10% 0px'
});

document.querySelectorAll('[data-scroll]').forEach(el => observer.observe(el));
```

```css
[data-scroll] {
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.6s ease, transform 0.6s ease;
}
[data-scroll].is-visible {
    opacity: 1;
    transform: translateY(0);
}
```

### CSS-Only Progress Variable (no library)
The `--progress` pattern from Locomotive Scroll — native CSS scroll-driven animations (Chrome 115+):

```css
@keyframes fade-in {
    from { opacity: 0; }
    to   { opacity: 1; }
}

.element {
    animation: fade-in linear;
    animation-timeline: view();
    animation-range: entry 0% entry 100%;
}
```

---

## 5. Progressive Enhancement Pattern (Teatr Lalka site)

Add `no-js` class to `<html>`, remove it immediately with JS:

```html
<html class="no-js">
<script>document.documentElement.classList.replace('no-js', 'js');</script>
```

Add `is-not-ready` to `<body>`, remove after init:
```js
document.body.classList.remove('is-not-ready');
```

CSS targets:
```css
/* Shown only without JS */
.no-js .js-required { display: none; }

/* Prevents FOUC during JS init */
.is-not-ready .animated-element { visibility: hidden; }
```

---

## 6. Cache-Busting with Version Strings

### File-level (query string) — used in Tokyo in Film
```html
<link rel="stylesheet" href="style.css?v=6">
<script src="js/glossary.js?v=4"></script>
```

### Build-level (content hash) — used by Webflow/Astro
```html
<!-- Hash changes only when file content changes -->
<link rel="stylesheet" href="/demo/_astro/horizontal.Cu5fLzAL.css">
<script src="/demo/_astro/hoisted.BN0EKy7u.js"></script>
```

### Asset-level with timestamp (SmugMug)
```
icons-small-defs-40fc07a1e299d0a2e8772a59b52f97b5.svg
```
MD5 hash of content appended to filename. Infinite cache TTL safe.

---

## 7. Schema.org Structured Data

### Person schema on `<html>` element (chrisburkard.com)
```html
<html itemscope itemtype="https://schema.org/Person">
<head>
    <meta itemprop="name"        content="Chris Burkard">
    <meta itemprop="description" content="Photographer...">
    <meta itemprop="image"       content="https://...jpg">
    <meta itemprop="url"         content="https://www.chrisburkard.com">
</head>
```

### JSON-LD approach (preferred — easier to maintain)
```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Robert Ladd",
    "url": "https://chauesprinciple.github.io/ChauesProductions/",
    "sameAs": [
        "https://www.instagram.com/chaues/"
    ]
}
</script>
```

---

## 8. Browser UA Detection via HTML Classes (SmugMug)

Server-side UA detection written to `<html>` at render time:
```html
<html class="sm-ua-gecko sm-browser-firefox sm-browser-firefox-148 sm-platform-windows">
```

Client-side equivalent (JS, run early):
```js
(function() {
    var html = document.documentElement;
    var ua = navigator.userAgent;
    if (/Firefox/.test(ua))  html.classList.add('browser-firefox');
    if (/Chrome/.test(ua))   html.classList.add('browser-chrome');
    if (/Safari/.test(ua) && !/Chrome/.test(ua)) html.classList.add('browser-safari');
    if (/Mobi/.test(ua))     html.classList.add('platform-mobile');
})();
```

Then in CSS:
```css
.browser-firefox .some-element { /* Firefox-specific fix */ }
.platform-mobile .desktop-only { display: none; }
```

---

## 9. JS Component Init Pattern (data-comp / data-options)

From Teatr Lalka — initialize JS components via HTML attributes:

```html
<div
    data-comp="Slider"
    data-options='{"autoplay": true, "speed": 400, "loop": true}'
>
    <!-- slider markup -->
</div>
```

```js
document.querySelectorAll('[data-comp]').forEach(el => {
    const name    = el.dataset.comp;
    const options = JSON.parse(el.dataset.options || '{}');
    if (window.Components && window.Components[name]) {
        new window.Components[name](el, options);
    }
});
```

---

## Sources
| Source | URL / Context | Date Parsed |
|--------|---------------|-------------|
| Teatr Lalka | External HTML shared in chat (Polish theater site) | Mar 2026 |
| Locomotive Scroll v5 | Astro demo page HTML | Mar 2026 |
| chrisburkard.com | SmugMug Pro portfolio page source | Mar 2026 |
| Webflow Designer | App shell (gallery names only — no impl code) | Mar 2026 |
