# Prompt v2: Ray Tracing Through Different Mediums & Dispersion
## For Fable 5.0 (Anthropic)
## HAUS Academy · IGCSE Physics 0625

---

## 0. Learning Goals

After using this simulation, students should understand:
- **Ray tracing** — the path of light as it travels through different medium shapes
- **Frequency is invariant** — when light enters a medium, its **frequency does not change**; only **speed and wavelength** change depending on the medium
- **Dispersion** — different frequencies (colours) have slightly different refractive indices, causing them to bend by different amounts

**⚠️ IMPORTANT: This simulation is about the PATH of light, NOT calculations.**
- The primary educational value is visual: students see how rays bend through different shapes
- Calculations and formulas should be **available but NOT prominent**
- Advanced equations beyond IGCSE curriculum must be **hidden by default** (with a toggle to show)
- The focus is **Ray Tracing**, not math

---

## 1. Overview

Build a **single interactive 2D Ray Tracing simulation** (single-file HTML + Canvas 2D) covering **6 different medium shapes**. The user selects which shape to use via section tabs at the top.

| # | Tab | Shape | Sun Light | Medium |
|---|-----|-------|-----------|--------|
| 1 | 🔺 **Prism** | Triangular prism, adjustable apex | ✅ Yes | Crown Glass only |
| 2 | 🪟 **Glass Blocks** | 1–2 parallel rectangular blocks | ❌ No | All 6 media |
| 3 | 🔵 **Half Circle** | D-shape block, flat face on top | ❌ No | All 6 media |
| 4 | 📐 **Right Triangle** | Right-angled triangular block | ❌ No | All 6 media |
| 5 | 💎 **Diamond** | Rhombus/diamond cross-section | ❌ No | Diamond only |
| 6 | 💧 **Rainbow** | Spherical water drop → rainbow | ✅ Optional | Water only |

### Core Principle
- **Monochromatic light** → pure refraction (Snell's Law, ray bending)
- **Visible Light (multi-colour)** → **dispersion** (colours separate)
- **Sun Light** → **Prism only** (all colours + IR + UV as continuous spectrum)

---

## 2. Layout (NEW — Full-width, no side panel)

**Reference:** `Measurement_1_vernier_caliper.html` for layout pattern (full-width canvas, data below).

### 2.1 Viewport Rules (CRITICAL — FIX FROM V1)
- **The entire simulation must fit in ONE browser window** — NO vertical scrolling
- Layout height: **10% taller than `Measurement_1_vernier_caliper.html`** (more vertical space for the canvas)
- Layout calculation:
  - Top bar: ~40px
  - Section tabs: ~44px (6 tabs)
  - Toolbar (2 rows): ~80px
  - **Canvas: remaining viewport height, full width** (taller than Vernier by ~10%)
  - Below-canvas panels: scrollable within their section if needed
- All content — labels, rays, controls, chips — must be **fully visible** within the Canvas
- If a medium shape is too large, **scale it down** — never clip it

### 2.2 Canvas Division (5 equal parts horizontally)

The canvas is divided into **5 equal segments** for positioning:

```
   1/5        2/5        3/5        4/5        5/5
   │           │           │           │           │
   │← ray end  │           │  Prism    │ ray start→│
   │  (arrow)  │           │  (25%)    │  (source)  │
   │           │           │           │           │
```

- **Light travels from RIGHT to LEFT** (enters from the right side)
- **Ray start (source):** at ~4/5 of canvas width (right side)
- **Ray end (arrow tip):** at ~1/5 of canvas width (left side)
- **Prism width:** ~25% of canvas width, centred horizontally
- This applies to all shapes unless otherwise specified — the light source is always on the right, ray travels leftward

### 2.3 Layout Structure

```
┌──────────────────────────────────────────────────┐
│ Top Bar: Title + Theme selector + Brand          │
├──────────────────────────────────────────────────┤
│ Section Tabs: 🔺 🪟 🔵 📐 💎 💧                  │
├──────────────────────────────────────────────────┤
│ Toolbar Row 1: Light Source + Colour swatches    │
│ Toolbar Row 2: Section-specific controls + θ₁    │
│                  + Play + Speed + Show toggles   │
├──────────────────────────────────────────────────┤
│                                                  │
│              Canvas (Full width)                 │
│              Ray tracing area                    │
│              Chips + hints overlay               │
│                                                  │
├──────────────────────────────────────────────────┤
│ Color Spectrum Table (ALWAYS VISIBLE)            │
│ [Colour] [λ nm] [f THz] [n] [θ₂] [Deviation °]  │
├──────────────────────────────────────────────────┤
│ Summary (ALWAYS VISIBLE — written in detail)     │
│ "The angular spread between Red and Violet is    │
│  X.X°. This means..." (full sentences)           │
├──────────────────────────────────────────────────┤
│ 📐 Equation (HIDDEN by default — toggle to show) │
│   Snell's Law + basic IGCSE formulas             │
│   Advanced equations (Cauchy) — 2nd toggle       │
├──────────────────────────────────────────────────┤
│ 💡 Info / Educational notes (always visible)     │
└──────────────────────────────────────────────────┘
```

### 2.4 Top Bar
- Title: "🌈 Ray Tracing — Refraction & Dispersion" + badge "v2.0.0"
- HAUS Brand logo (top-right)
- Theme selector: 6 themes dropdown

### 2.5 Section Tabs
```
[ 🔺 Prism ] [ 🪟 Glass Blocks ] [ 🔵 Half Circle ] [ 📐 Right Triangle ] [ 💎 Diamond ] [ 💧 Rainbow ]
```
- Active tab highlighted (accent colour)
- Switching tabs resets animation and updates toolbar controls

### 2.6 Toolbar

**Row 1 — Light Source & Colour:**
| Control | Type | Details |
|---------|------|---------|
| Light Source | 3 pill buttons | 🔦 Mono · 🌈 Visible · ☀️ Sun (Sun: Prism only) |
| Colour swatches | Circle pills (ROYGBIV) | Mono = single select, Visible = multi-select |

**Row 2 — Section-specific controls + Shared:**
| Control | Type | Details |
|---------|------|---------|
| [Section-specific] | Various | Apex angle, block count, direction, etc. |
| θ₁ | Slider + input | 0°–75° (or 0°–89° for Half Circle), step 0.5° |
| ▶ Play / ⏸ Pause | Button | Pen-drawing animation |
| Speed | Pills | 0.5× · 1× · 2× |
| Show: Angles | Toggle | ∠ |
| Show: Labels | Toggle | 🏷 |
| Show: Normals | Toggle | ⊥ |
| Show: Deviation | Toggle | ⸻ (Prism only — undeviated dashed line) |
| Show: Equations | Toggle (hidden by default) | 📐 |
| ↺ **Global Reset** | Button | **Reset ALL parameters to defaults** (shape, source, angle, medium, zoom — everything) |

### 2.7 Canvas (Full width, no side panel)
- Dark background (`--graph-bg`)
- Medium shape drawn in the centre
- Incident ray enters from the right → refracts/disperses → exits to the left
- Animation: pen-drawing Type B
- All rays, labels, and angles must be fully visible within canvas bounds
- **Chips** overlay on canvas for status info (same as Refraction simulation)

### 2.8 Below-Canvas Panels (in order)

#### Color Spectrum Table (ALWAYS VISIBLE — never hidden)
A table showing the current colour data. This must be shown at all times, regardless of equation toggle state.

| Colour | λ (nm) | f (THz) | n | θ₂ (°) | Deviation (°) |
|--------|:------:|:-------:|:-:|:------:|:-------------:|
| 🔴 Red | 700 | 428 | 1.5132 | 22.1 | 7.1 |
| 🟠 Orange | 610 | 492 | 1.5158 | 21.8 | 6.8 |
| ... | ... | ... | ... | ... | ... |
| 🟣 Violet | 400 | 750 | 1.5309 | 19.5 | 4.5 |

- Only shows colours that are currently active (selected pills + Sun Light includes IR/UV)
- IR and UV rows shown only when Sun Light mode is active
- Rows have a small colour swatch before the colour name

#### Summary (ALWAYS VISIBLE — written in DETAIL)
This section must explain the results in **full sentences**, not just show numbers. Examples:

**For Prism (Monochromatic - 1 colour):**
> "The light ray enters the prism at an angle of incidence θ₁ = 45.0°. Inside the Crown Glass prism (n = 1.52), the ray bends toward the normal at an angle of r₁ = 27.7°. The ray then strikes the right face of the prism and exits at an angle of θₑ = 52.3° relative to the normal. The total deviation from the original path is δ = 37.3°."

**For Prism (Visible Light - all 7 colours):**
> "White light entering the prism is dispersed into its component colours. The angular spread between Red (λ = 700 nm, deviation = 37.1°) and Violet (λ = 400 nm, deviation = 34.5°) is Δθ = 2.6°. This is because the refractive index of Crown Glass varies slightly with wavelength — from n = 1.5132 for Red to n = 1.5309 for Violet. Higher frequency light (Violet) slows down more and bends more, while lower frequency light (Red) slows down less and bends less."

**For Glass Blocks (1 block, Monochromatic):**
> "The light ray enters the glass block at θ₁ = 40.0° and refracts to θ₂ = 25.0° inside the block (n = 1.52). The ray travels straight through the block and exits at the bottom, emerging parallel to the incident ray but with a lateral displacement of 8.2 mm. This lateral shift is a key characteristic of refraction through a parallel-sided medium — the ray direction is restored, but the position is shifted."

**For Half Circle (Monochromatic, at critical angle):**
> "The light enters the curved face of the block along the radius, so it is not refracted at the entry surface. At the flat face, the ray hits at θ₁ = 41.1° which equals the critical angle for Crown Glass (θc = 41.1°). The refracted ray skims along the boundary at θ₂ = 90.0°. This is the critical angle — the angle beyond which Total Internal Reflection (TIR) would occur."

**For Rainbow (Visible Light):**
> "White light enters the spherical water droplet and refracts at the surface. Inside the droplet, the light travels to the back surface where it undergoes one internal reflection. When the light exits the droplet, the different colours have separated, forming a rainbow. The primary rainbow is formed by one internal reflection, with Red appearing on the outer edge and Violet on the inner edge."

#### Equation Section (HIDDEN by default — toggle to show)
- When the "📐 Equations" toggle is OFF, this entire section is hidden
- When ON, shows basic IGCSE-level equations:
  - Snell's Law: n₁ sin θ₁ = n₂ sin θ₂
  - n = sin i / sin r (IGCSE form)
  - θc = sin⁻¹(n₂/n₁) (critical angle formula)
- **Advanced equations (Cauchy dispersion: n(λ) = A + B/λ²) are beyond IGCSE** — hidden by default with a separate smaller toggle "Show advanced equations"
- Default state: **equations OFF**

#### Info / Educational Notes (always visible)
- Shape-specific educational text
- For Prism: Herschel's experiment info (Sun mode)
- For Half Circle: explanation of why light enters along radius without refraction
- For Glass Blocks: explanation of lateral displacement
- For Rainbow: how rainbows form

---

## 3. Ray Thickness & Labels (CRITICAL — FIX FROM V1)

### 3.1 Ray Thickness

| Property | Value |
|----------|-------|
| **Line width (Monochromatic)** | **1.6px** |
| **Line width (Visible Light)** | **1px** |
| **Line width (Sun Light guide rays)** | **1px** |
| Arrowhead size | Proportional to ray width (smaller for 1px rays) |
| Shadow blur | 3–4px |
| **Rule** | **Mono = 2px (thicker, single ray). Visible/Sun = 1px (thinner, multiple rays side by side)** |

**Why?**
- V1 had thick rays (3px+) that overlapped and became invisible when multiple colours were close together
- **Mono mode (1.6px):** Only 1 ray → thicker is fine, easy to see
- **Visible mode (1px):** Multiple colour rays side by side → must be thin so each colour is distinct and visible
- **Sun Light mode:** Use wider semi-transparent **bands** (fills) for the continuous spectrum, with thin guide rays (1px) overlaid

### 3.2 Colour Labels on Canvas (abbreviated — keeps canvas clean)

On the canvas, only **5 key spectral positions** are labelled to avoid clutter. The full set of colours is shown in the Color Spectrum Table below the canvas.

| Colour | Label | Visible in mode |
|--------|:-----:|:---------------:|
| 🔴 Infrared | **IR** | Sun Light only |
| 🔴 Red | **R** | Mono · Visible · Sun |
| 🟢 Green | **G** | Mono · Visible · Sun |
| 🔵 Blue | **B** | Mono · Visible · Sun |
| 🟣 Violet | **V** | Mono · Visible · Sun |
| 🟣 Ultraviolet | **UV** | Sun Light only |
| ⚪ White | **W** | Incident ray (not a colour label) |

- Only labels: **IR, R, G, B, V, UV** — not all 7 colours (avoids clutter)
- Label font size: 10–11px, colour matching the ray
- **Toggle:** 🏷 Labels button in toolbar to show/hide all labels

---

## 4. Colour Data (shared across ALL shapes)

```javascript
const COLORS = [
  { name:"Red",    wl:700, f:428, hex:"#FF3B30" },
  { name:"Orange", wl:610, f:492, hex:"#FF9500" },
  { name:"Yellow", wl:550, f:545, hex:"#FFCC00" },
  { name:"Green",  wl:500, f:600, hex:"#34C759" },
  { name:"Blue",   wl:460, f:652, hex:"#007AFF" },
  { name:"Indigo", wl:425, f:705, hex:"#5856D6" },
  { name:"Violet", wl:400, f:750, hex:"#AF52DE" }
];
const IR = { name:"IR", wl:850, hex:"#FF3B30" };
const UV = { name:"UV", wl:360, hex:"#AF52DE" };
```

## 5. Media Array (shared across ALL shapes)

**IMPORTANT:** These values are taken from the reference file `Wave_1_refraction_of_light.html` (fill colours) and extended with Cauchy coefficients for dispersion.

### Simple n values (at 550 nm — same as `Wave_1_refraction_of_light.html`)

```javascript
const MEDIA_SIMPLE = [
  { name:"Air",         n:1.00, fill:null },
  { name:"Water",       n:1.33, fill:"rgba(25,80,160,0.38)" },
  { name:"Ice",         n:1.31, fill:"rgba(180,215,235,0.3)" },
  { name:"Perspex",     n:1.49, fill:"rgba(220,215,200,0.22)" },
  { name:"Crown Glass", n:1.52, fill:"rgba(195,205,210,0.22)" },
  { name:"Diamond",     n:2.42, fill:"rgba(200,210,220,0.18)" }
];
```

### Cauchy coefficients (for dispersion — n(λ) = A + B/λ², λ in μm)

```javascript
const MEDIA = [
  { name:"Crown Glass (BK7)", A:1.5046, B:0.00420, fill:"rgba(195,205,210,0.20)", edge:"rgba(200,215,225,0.85)" },
  { name:"Flint Glass (F2)",  A:1.5809, B:0.01426, fill:"rgba(215,190,165,0.24)", edge:"rgba(225,200,175,0.85)" },
  { name:"Water",             A:1.3242, B:0.00285, fill:"rgba(25,80,160,0.30)",  edge:"rgba(90,150,220,0.85)" },
  { name:"Ice",               A:1.3050, B:0.00150, fill:"rgba(180,215,235,0.30)", edge:"rgba(200,225,245,0.85)" },
  { name:"Perspex",           A:1.4840, B:0.00285, fill:"rgba(220,215,200,0.18)", edge:"rgba(225,220,205,0.8)" },
  { name:"Diamond",           A:2.3758, B:0.01188, fill:"rgba(200,225,235,0.22)", edge:"rgba(210,235,245,0.9)" }
];
const nOf = (mi, wl) => MEDIA[mi].A + MEDIA[mi].B / Math.pow(wl/1000, 2);  // wl in nm
```

### Media Availability per Shape

| Shape | Available Media | Light Source |
|-------|----------------|--------------|
| 🔺 **Prism** | **Crown Glass only** | Mono · Visible · Sun |
| 🪟 **Glass Blocks** | All 6 media | Mono · Visible |
| 🔵 **Half Circle** | All 6 media | Mono · Visible |
| 📐 **Right Triangle** | All 6 media | **Mono only** |
| 💎 **Diamond** | **Diamond only** | **Mono only** |
| 💧 **Rainbow** | **Water only** (sky blue fill) | Mono · Visible |

---

## 6. Section Details

### 6.1 🔺 Prism

**Controls (Row 2):**
| Control | Type | Details |
|---------|------|---------|
| Apex angle | Slider + badge | **45°–75°, step 1°, default 45°** |
| θ₁ | Slider + input | **0°–75°, step 0.5°, default 50°** |
| Entry position | Drag on prism face | Vertical position along left/right face |

**Prism orientation:**
- **Light enters from the RIGHT face** (not the left face — this is different from V1)
- **Light exits from the LEFT face**
- Prism centred horizontally, occupying ~25% of canvas width
- Apex at top, base at bottom

**Physics:**
- Light enters right face → refracts inside → disperses → exits left face
- **NO TIR** — auto-prevent (snap parameters)
  - `s1Enforce()` function checks the highest-n colour (Violet for visible, UV for Sun)
  - If TIR would occur, snap apex and/or θ₁ to nearest safe value
  - Show warning chip: "⚠ TIR prevented — angle adjusted"
- Entry point E on prism face: **draggable vertically**
**Prism-specific feature — Undeviated dashed line (Deviation angle):**
- A **dashed white line** extends the incident ray's direction in a straight line through the prism (as if no refraction occurred)
- At the exit side, the **deviation angle δ** is shown as an arc between the undeviated line and the actual exit ray
- **Toggle button:** `⸻ Deviation` in toolbar — shows/hides the dashed line and deviation angle arc
- The deviation angle `δ = θ₁ + θₑ − apex` is calculated and displayed
- This helps students visualise how much the prism bends the light
- Only available in Prism section (not relevant for other shapes)

**Herschel Thermometer (Sun mode):**
- Draggable thermometer on canvas
- Temperature peaks at IR (~32°C)
- Educational message when dragged to IR region

### 6.2 🪟 Glass Blocks

**Controls (Row 2):**
| Control | Type | Details |
|---------|------|---------|
| Block count | Pills | 1 · 2 |
| Block 1 medium | Dropdown | All 6 media |
| Block 2 medium | Dropdown | All 6 media (visible only when count=2) |
| θ₁ | Slider + input | **0°–90°, step 0.5°, default 40°** |

**Geometry:**
- Light enters from **top → bottom** (right to left in canvas)
- **1 Block:** vertical height = **1/4** of canvas, horizontal width = **2/3** of canvas
- **2 Blocks:** total vertical height = **2/3** of canvas (each block ~1/3), horizontal width = **2/3** of canvas
- Gap between blocks: ~15px

**Educational descriptions (shown in Summary panel):**

| θ₁ value | Description |
|----------|-------------|
| **θ₁ = 0°** | "The ray enters the block at 0° — it is perpendicular to the surface. No direction change occurs. The frequency of light does not change, but the speed decreases and the wavelength shortens inside the medium." |
| **0° < θ₁ < 90°** | **1 block:** Uses IGCSE formula `n = sin i / sin r` (KaTeX rendered). **2 blocks:** Uses Snell's Law `n₁ sin θ₁ = n₂ sin θ₂` at each interface (KaTeX rendered). |
| **θ₁ ≈ 90°** | "The ray is almost parallel to the surface. The angle of refraction approaches the critical angle of this medium (θc = X.X°). For a parallel-sided block, the emergent ray is parallel to the incident ray but laterally displaced." |

**Physics:**
- Normal rules: always at entry, mono=every interface, 2+ colours=entry only
- TIR possible between blocks when n₁ > n₂ and angle exceeds θc
- Dispersion visible with multiple colours
- For 1 block: emergent ray is **parallel to incident ray** but with **lateral displacement**

### 6.3 🔵 Half Circle

**Controls (Row 2):**
| Control | Type | Details |
|---------|------|---------|
| Block medium | Dropdown | All 6 media |
| Direction | Toggle | ◀ from left / ▶ from right |
| θ₁ | Slider + input | 0°–89°, step 0.5°, default 30° |

**Geometry:**
- Size: **~2/5 of Canvas** (diameter = 2/5 canvas width)
- D-shape face up, flat face on top, curved face on bottom
- Light enters from **bottom curved face** → travels along radius → **no refraction at entry**
- All refraction happens at the **flat face** (top)

**Physics (CRITICAL — must be physically accurate):**
- Light enters along the **radius of the curved face** → normal to surface → no bending
- Ray travels straight to the **flat face**
- Snell's Law applies at the flat face: `n₁ sin θ₁ = n₂ sin θ₂`
- **Direction rule:**
  - If incident ray enters from **bottom-left** of curved face → refracted ray exits to **top-right** of flat face
  - If incident ray enters from **bottom-right** of curved face → refracted ray exits to **top-left** of flat face
- Monochromatic: shows critical angle + TIR clearly
- Visible Light: ray tracing only (dispersion, no critical angle display)

**Entry position:** **Draggable** along the curved face (user can slide the entry point left/right)

### 6.4 📐 Right Triangle

**Controls (Row 2):**
| Control | Type | Details |
|---------|------|---------|
| Block medium | Dropdown | All 6 media |
| Triangle angles | Dropdown | 45-45-90 · 30-60-90 · adjustable |
| θ₁ | Slider + input | 0°–89°, step 0.5°, default 45° |
| Entry position | Drag on entry face | Slide up/down along left face |

**Light source:** **Monochromatic only** (Visible Light NOT available)

**Geometry:**
- Size: **~2/5 of Canvas**
- Right-angled triangle (one side is perpendicular)
- Light enters from **left face only** → travels **left→right**
- Reference: Screenshot 2 (45-45-90 triangle with ray tracing)

**Physics (CRITICAL — must be physically accurate):**
- Light enters the vertical left face → refracts
- Inside the triangle, the ray travels toward the hypotenuse
- At the hypotenuse: may refract out OR undergo TIR depending on angle
  - If TIR occurs → ray reflects toward the base → exits through the base
  - If no TIR → ray exits through the hypotenuse
- Common IGCSE exam shape — questions often test ray tracing through right triangles
- TIR possible at internal faces when angle exceeds θc
- **Entry position:** **Draggable** along the left face (up/down)
- **Triangle configuration:**
  - Right angle at **C** (bottom-left)
  - **Angle A** (top vertex) is **adjustable** — slider or dropdown
  - Angle B = 90° − Angle A (calculated automatically)
  - Side **AC is vertical** (left face) — light enters here
  - Side **CB is horizontal** (base)
  - Side **AB is the hypotenuse** (sloping)
  - Presets: 30°–60°–90°, 45°–45°–90°, or custom slider for angle A of **20°–70°**, default **45°**
- Light enters from **left side only** (one entry face)

### 6.5 💎 Diamond

**Controls (Row 2):**
| Control | Type | Details |
|---------|------|---------|
| Medium | — | **Diamond only** (locked) |
| θ₁ | Slider + input | 0°–89°, step 0.5°, default 30° |
| Entry position | Drag on top face | Slide left/right along top facet |

**Light source:** **Monochromatic only** (Visible Light NOT available)

**Geometry:**
- Size: **~2/5 of Canvas**, centred
- **Realistic diamond shape** (like Screenshot 1) — not a simple rhombus
- Classic faceted outline:
  - Flat **top facet** (horizontal, where light enters)
  - Flat **bottom facet** (horizontal, pointed tip)
  - **Left and right pointed tips** (at the widest point)
  - **Multiple sloping facets** on each side (crown above, pavilion below)
  - Proportional dimensions matching a real diamond's cross-section
- Light enters from **top face only** → travels **top→bottom**
- Reference: Screenshot 1 (diamond TIR diagram)

**Physics (CRITICAL — must be physically accurate):**
- Light enters the top facet → refracts into the diamond
- Inside the diamond, the ray hits the lower-left facet → **Total Internal Reflection** (n_diamond ≈ 2.42, θc ≈ 24.4°)
- Reflected ray travels toward the right side → may hit another facet → TIR again
- Multiple internal reflections possible (zigzag path) — this is what gives diamonds their "sparkle"
- Ray eventually exits through a facet where the angle of incidence is less than θc
- **Entry position:** **Draggable** along the top face (left/right)
- Must be physically accurate — direction of TIR must follow physics (angle of incidence = angle of reflection)

### 6.6 💧 Rainbow (Water Drop)

**Controls (Row 2):**
| Control | Type | Details |
|---------|------|---------|
| Medium | — | **Water only** (locked) |
| Rainbow type | Pills | Single Rainbow · Double Rainbow (if possible) |

**Light source:** **Monochromatic or Visible Light only** (Sun Light NOT available)

**Geometry:**
- Size: **~2/5 of Canvas**
- **Position:** Offset **upward** (more space below the droplet for the rainbow to appear)
- Circular/spherical water drop
- Reference: Screenshot 3 (raindrop rainbow diagram)

**Physics (CRITICAL — must be physically accurate):**
- Light enters the top of the droplet → refracts at the air-water interface
- Inside the droplet, light travels to the back surface → **one internal reflection** (primary rainbow)
- **Cannot select entry position** — the incident ray position is fixed by physics (optimal position for rainbow formation)
- The incident ray enters at the top of the droplet and exits at the bottom-left
- **Single Rainbow:** 1 internal reflection → colours appear in order: Violet (top), Indigo, Blue, Green, Yellow, Orange, Red (bottom)
- **Double Rainbow (if possible):** 2 internal reflections → colours appear in reverse order
- Visible Light mode: shows 7 colour rays separating
- Monochromatic mode: shows a single ray path through the droplet
- Use sky blue fill (`rgba(100,180,230,0.20)`) for the droplet — lighter than standard Water for ray visibility

---

## 7. Math Helpers (shared)

```javascript
const D2R = Math.PI/180, R2D = 180/Math.PI;
const clamp = (v,a,b) => Math.max(a, Math.min(b, v));
const vsub = (a,b) => ({x:a.x-b.x, y:a.y-b.y});
const vadd = (a,b) => ({x:a.x+b.x, y:a.y+b.y});
const vmul = (a,k) => ({x:a.x*k, y:a.y*k});
const vlen = a => Math.hypot(a.x, a.y);
const vnorm = a => { const L = vlen(a) || 1; return {x:a.x/L, y:a.y/L}; };
const vdot = (a,b) => a.x*b.x + a.y*b.y;
const rotV = (v, deg) => { const a = deg*D2R, c = Math.cos(a), s = Math.sin(a);
  return { x: v.x*c - v.y*s, y: v.x*s + v.y*c }; };
function refractV(d, n, n1, n2) {
  const cosi = -vdot(d, n), eta = n1/n2;
  const k = 1 - eta*eta*(1 - cosi*cosi);
  if(k < 0) return null;
  return vnorm({ x: eta*d.x + (eta*cosi - Math.sqrt(k))*n.x,
                 y: eta*d.y + (eta*cosi - Math.sqrt(k))*n.y });
}
const reflectV = (d, n) => { const dn = 2*vdot(d,n); return vnorm({x:d.x-dn*n.x, y:d.y-dn*n.y}); };
function raySeg(o, d, a, b) {
  const rx = b.x-a.x, ry = b.y-a.y;
  const den = d.x*ry - d.y*rx;
  if(Math.abs(den) < 1e-12) return null;
  const t = ((a.x-o.x)*ry - (a.y-o.y)*rx) / den;
  const u = Math.abs(rx) > Math.abs(ry) ? (o.x + t*d.x - a.x)/rx : (o.y + t*d.y - a.y)/ry;
  if(t < 1e-7 || u < -1e-9 || u > 1+1e-9) return null;
  return { t, u: clamp(u,0,1), pt: { x:o.x+t*d.x, y:o.y+t*d.y } };
}
```

## 8. Drawing Helpers

```javascript
function drawPath(pts, color, width, prog, opts = {}) {
  // Progressive polyline (prog = 0..1)
  // width: 2px for mono, 1px for visible/sun
  // Arrowhead at end if opts.arrow !== false
  // Alpha = opts.alpha || 1
  // Shadow blur: 3–4px
}
function drawNormal(pt, dir, len = 48) {
  // Dashed grey line, centered at pt
}
function arcAt(P, aFrom, aTo, r, color, label, labelR) {
  // Angle arc + label
}
function txt(t, x, y, color, size = 11, align = "center", weight = 600) {
  ctx.font = `${weight} ${size}px Inter, sans-serif`;
  ctx.fillStyle = color; ctx.textAlign = align; ctx.textBaseline = "middle";
  ctx.fillText(t, x, y);
}
```

## 9. Interactions

| Action | Result |
|--------|--------|
| **Drag ray** | Adjust θ₁ (hit-test near ray) |
| **Drag entry dot** (Prism) | Move entry point along face |
| **Drag thermometer** (Prism Sun) | Move Herschel thermometer |
| **Double-click** | Zoom in (2.5×) |
| **Esc / double-click** | Zoom out |
| **Arrow keys** | Adjust θ₁ (±1° or ±5° with Shift) |
| **↺ Global Reset** | Reset ALL to defaults: Section 0 (Prism), θ₁=50°, Apex=45°, Mono+Red, Dark theme, zoom off, animation stopped |

## 10. Animation

```javascript
function tick(t) {
  if(lastT === null) lastT = t;
  const dt = (t - lastT)/1000; lastT = t;
  if(S.playing) {
    if(S.prog < 1) S.prog = Math.min(1, S.prog + dt*S.speed/1.4);
    draw();
    rafId = requestAnimationFrame(tick);
  } else { lastT = null; rafId = null; }
}
function paramChanged() { S.prog = S.playing ? 0 : 1; updateUI(); }
```

## 11. Themes

Reuse the same theme system from `Wave_1_refraction_of_light.html`:
- 🌙 Classic Dark (default)
- ⌂ HAUS Night
- 🌃 Cyberpunk Neon
- ☀️ Classic Light
- ⌂ HAUS Day
- 🏺 Warm Clay

## 12. Equation Toggle System

```javascript
const S = {
  // ... other state
  showEquations: false,   // DEFAULT: false (hidden)
  showAdvanced: false     // DEFAULT: false (Cauchy hidden)
};

// Toolbar button: "📐 Equations" toggle
// When OFF: No equation section visible below canvas
// When ON: Show IGCSE-level equations (Snell's Law, n = sin i / sin r)
//          Advanced equations (Cauchy) need a SECOND toggle below

// Below-canvas sections:
// - Color Spectrum Table: ALWAYS visible (toggle has no effect)
// - Summary: ALWAYS visible (toggle has no effect)
// - 📐 Equation: ONLY visible when showEquations = true
//   - Within equation section: "Show advanced equations" small toggle
//   - When advanced ON: show Cauchy dispersion formula
// - 💡 Info: ALWAYS visible
```

## 13. File Requirements

- **Single HTML file** (standalone, all 6 shapes in ONE file with section tabs)
- Filename: `Wave_2_ray_tracing.html`
- External dependencies: Google Fonts + KaTeX CDN only
- **Layout reference:** `Measurement_1_vernier_caliper.html` (full-width canvas, data below)
- **Physics reference:** `Wave_1_refraction_of_light.html` (ray tracing, Snell's Law, MEDIA values)
- Language: English
- All IGCSE Physics 0625 conventions followed
- Real refractive index values (Cauchy equation)
- **Color Spectrum Table: ALWAYS visible**
- **Summary: ALWAYS visible** (written in detail, full sentences)
- **Equations: HIDDEN by default** — toggle to show basic IGCSE equations
- **Advanced equations (Cauchy): HIDDEN** — separate toggle within equation section

## Feature Checklist

### Layout
- [x] Full-width canvas (no side panel) — like Vernier Caliper
- [x] Color Spectrum Table: ALWAYS visible below canvas
- [x] Summary: ALWAYS visible below canvas (written in detail, not abbreviated)
- [x] Equations: HIDDEN by default, toggle to show
- [x] Advanced equations (Cauchy): HIDDEN, separate toggle
- [x] Viewport-fit: entire sim in ONE browser window
- [x] 6 themes

### Global
- [x] Single file with 6 section tabs (Prism, Glass Blocks, Half Circle, Right Triangle, Diamond, Rainbow)
- [x] Learning Goals stated
- [x] Ray thickness: 1.3–1.5px (thin, distinct)
- [x] Primary focus: Ray Tracing, not calculations
- [x] 3 Light Sources: Mono / Visible / Sun (Prism only)
- [x] 7 colour swatches (circle pills, ROYGBIV)
- [x] Standard MEDIA array from `Wave_1_refraction_of_light.html`
- [x] Pen-drawing animation (Type B)
- [x] Zoom (double-click)

### Per-Shape
- [x] Prism: adjustable apex, NO TIR, Sun Light, Herschel thermometer
- [x] Glass Blocks: 1–2 blocks, TIR, Dispersion
- [x] Half Circle: critical angle + TIR (mono), ray tracing (visible)
- [x] Right Triangle: IGCSE exam shape, TIR, Dispersion
- [x] Diamond: internal reflections, high dispersion
- [x] Rainbow: water drop, 1 internal reflection, rainbow effect