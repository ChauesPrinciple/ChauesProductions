---
description: Edit, debug, or extend interactive canvas-based visualization pages. Invoke when asked to work on closure_axiom(1).html, filter_test.html, or any standalone HTML file that uses the Canvas API, requestAnimationFrame, and inline JS for mathematical or spatial visualization with no external framework dependencies.
---

# Interactive Visualization Skill

## File Inventory

| File | Subject | Tech |
|---|---|---|
| `closure_axiom(1).html` | Sacred geometry — S³, Dante's cosmos, qibla, spherical trig | Canvas 2D, rAF loop, inline CSS/JS |
| `filter_test.html` | Filter/color test (dev/experimental) | Canvas 2D |

---

## closure_axiom Architecture

Single-file, zero dependencies. All CSS and JS inline. 6 canvas panels:

| Panel | Canvas ID | Content | Animated? |
|---|---|---|---|
| 1 | `cLadder` | Dimensional ladder S⁰→S³, button-toggle | Yes (S¹/S² rotation) |
| 2 | `cRope` | World-line threading S² slices, ψ slider | No (responds to slider) |
| 3 | `cCoord` | ψ/θ/φ coordinate sliders generating S³ point | No (responds to sliders) |
| 4 | `cDante` | Dante's nested spheres, depth slider | No (responds to slider) |
| 5 | `cFull` | Complete S³ cross-section, world-line, **own ψ slider** | No (responds to slider) |
| 6 | `cSphere` + `cQS3` | Qibla — rotating globe + S³ projection | Yes (globe spins) |
| 7 | `cTriangle` | Spherical law of sines live ratio | No (responds to qibla inputs) |

---

## Global State Variables

```js
let dim = 2;              // Active dimension on Ladder panel (0-3)
let psi = Math.PI / 2;    // Rope panel slice depth
let fullPsi = Math.PI/2;  // Full panel slice depth (independent)
let danteAngle = Math.PI/2;
let coordPsi, coordTheta, coordPhi;  // Coordinate panel sliders
let obsLat, obsLon, qPsiVal;         // Qibla panel inputs
let t = 0;                           // Animation time counter
```

All panel-specific state is stored as module-level `let` variables. There is no state object or class.

---

## Canvas Sizing

```js
function initCanvases() {
  const dpr = window.devicePixelRatio || 2;
  // ...
  cv.width  = parentWidth * dpr;
  cv.height = Math.round(cssH * dpr);
  cv.style.height = cssH + 'px';  // locks CSS display height
}
```

**Critical:** `cv.style.height` is set explicitly so the canvas renders at the CSS size while the buffer is `dpr` times larger. All drawing coordinates are in buffer space (already scaled). Do not remove `cv.style.height` assignment.

`initCanvases()` is also bound to `window.addEventListener('resize', initCanvases)`.

---

## Mathematical Correctness Reference

These are verified correct — do not change without understanding the geometry:

**S³ parameterization** (Panel 3):
```
x₀ = cos ψ
x₁ = sin ψ · cos θ
x₂ = sin ψ · sin θ · cos φ
x₃ = sin ψ · sin θ · sin φ
→ x₀² + x₁² + x₂² + x₃² = 1 ✓
```

**Qibla bearing** (`computeQibla`):
Standard forward bearing via `atan2(sin Δλ · cos φ₂, cos φ₁ · sin φ₂ − sin φ₁ · cos φ₂ · cos Δλ)` — correct.

**Haversine distance** (`computeQibla`): Clamped correctly with `Math.max(0, Math.min(1, a))` before `asin`. Correct.

**SLERP great-circle arcs** (`gcArc`): 3-vector linear interpolation with `sin((1-t)ω)/sinω` weighting. Correct.

**Spherical law of sines** (`drawTriangle`): `sin(a)/sin(Q)` where `a` = great-circle distance, `Q` = qibla bearing (interior angle at observer in North–Observer–Mecca triangle). Correct.

**findCrossings**: Sign-change detection (`d0 * d1 < 0`) over `range = Math.PI * 10`. Correct and consistent with `drawFull` world-line range.

---

## Known Design Choices (not bugs)

- `knotPoint()` is labeled "Knot parameterization" but is a parametric oscillating path, not a mathematical knot. Intentional — it produces visually compelling world-line crossings.
- `drawQS3` qibla geodesic uses a Bézier curve driven by bearing fraction — schematic illustration, not geometrically precise S³ projection. Intentional.
- All 8 canvases redraw every `rAF` frame even though only 2 animate. Acceptable for a single-page tool.

---

## Procedure for Edits

### Adding a new panel
1. Add canvas element to HTML with a unique `id` and `height` attribute
2. Add `[id, cssH]` entry to `specs` array in `initCanvases()`
3. Write `drawPanelName()` function following the pattern: `const c = CTX['id']; if (!c) return;`
4. Call `drawPanelName()` from `loop()`
5. Add any new global state variables and UI callbacks

### Editing a slider
- Each slider: `<input type="range" id="..." min="..." max="..." value="..." oninput="onFnName(this.value)">`
- Corresponding JS: `function onFnName(v) { globalVar = (v / 100) * Math.PI; ... }`
- Display label: `gc('labelId').textContent = formattedValue`

### Adding a UI callback (button, slider)
- Keep callback functions named `on[Panel][Control]` for consistency
- Update display labels within the callback — don't rely on loop() to update text

### Changing math
- Run all four affected panel draws after changing a shared variable
- Verify the `vnorm` readout stays at 1.000 after coordinate changes (S³ normalization check)
- For qibla: verify bearing changes when dragging lat/lon sliders

---

## Theoretical Context (closure_axiom)

This file visualizes *The Closure Axiom* — the argument that sacred geometry across cultures (Vedic fire altars, Islamic qibla, Dante's Commedia, Wheeler's single electron) is the same mathematical structure: successive closed manifolds S⁰→S¹→S²→S³, driven by the theological constraint that "the sacred cannot leak."

The S³ is Dante's cosmos: ψ=0 is Earth (punto), ψ=π is God (punto), ψ=π/2 is the Primum Mobile (maximum S² equator). The three angular coordinates ψ,θ,φ are the Trinity as dimensionality. The world-line threading all S² slices is Wheeler's single electron.

Understanding this context matters when writing panel labels, axis labels, or tooltip text. The language should be precise and consistent with the theory.
