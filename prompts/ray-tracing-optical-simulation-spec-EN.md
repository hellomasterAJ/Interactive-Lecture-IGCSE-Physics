# Prompt: Ray Tracing Optical Simulation — Complete Suite
## For Fable 5.0 (Anthropic)
## HAUS Academy · IGCSE Physics 0625

---

## Overview

Build a series of **interactive 2D Ray Tracing Simulations** (single-file HTML + Canvas 2D) covering **Refraction, Dispersion, and Optical Phenomena** following the IGCSE Physics 0625 curriculum.

### Sections (in priority order)

| # | Topic | Medium/Setup | Light Sources | Sun Light |
|---|-------|-------------|---------------|-----------|
| 1 | 🌈 **Dispersion of Light** | Prism (adjustable apex) | Mono / Visible / Sun | ✅ Yes |
| 2a | 🪟 **Parallel Glass Blocks** | 1–2 rectangular blocks | Mono / Visible | ❌ No |
| 2b | 🔵 **Half Circular Glass Block** | D-shape block | Mono / Visible | ❌ No |
| 2c | 🔦 **Optical Fiber** | Core + Cladding + Bend + Damage | Mono / Visible | ❌ No |
| 3 | 📌 **IGCSE Pin Experiment** | Rectangular block + 4 pins | White light only | ❌ No |
| 4 | 👁️ **Real & Apparent Depth** | Container + liquid + coin | White light only | ❌ No |

### Shared Layout (Ref: `Wave_1_refraction_of_light.html`)

All sections share the same layout template:

```
┌──────────────────────────────────────────────┐
│ Top Bar: Title + Mode tabs + Theme + Brand   │
├──────────────────────────────────────────────┤
│ Toolbar Row 1 (Section-specific controls)     │
│ Toolbar Row 2 (Angle, Play, Show toggles)     │
├──────────────────────┬───────────────────────┤
│                      │                       │
│   Canvas (65%)       │   Side Panel (35%)    │
│   - Ray Tracing      │   - Current Values    │
│   - Interactive      │   - Equation/Formula  │
│   - Drag + Zoom      │   - Educational Info  │
│                      │                       │
└──────────────────────┴───────────────────────┘
```

**Canvas:** 640×640 logical pixels, DPR-aware, dark background  
**Side Panel:** Color Spectrum Table (for dispersion) · Current Values · Formula Box · Summary  
**Themes:** 6+ themes (Classic Dark, HAUS Night, Neon, Classic Light, HAUS Day, Warm Clay)  
**Fonts:** Inter (UI), JetBrains Mono (values), KaTeX (equations)  
**Animation:** Pen-drawing Type B (same as Refraction simulation)  
**Zoom:** Double-click to magnify, Esc to exit  

---

# SECTION 1: Dispersion of Light (Prism)

## 1.1 Light Source System

3 mutually exclusive pill buttons in toolbar:

| Mode | Behaviour |
|------|-----------|
| 🔦 **Monochromatic** | Select exactly **1 colour pill** (ROYGBIV). Single ray shown. |
| 🌈 **Visible Light** | Select **any number of colour pills** (on/off each). Multiple rays shown. |
| ☀️ **Sun Light** | Only available with **Prism**. Shows all visible + IR + UV as continuous spectrum band. |

**Sun Light Restrictions:**
- Only available with Prism (Section 1)
- NOT available for Parallel Glass Blocks, Half Circular Block, Optical Fiber, Pin Experiment, or Real & Apparent Depth

## 1.2 Prism

### Geometry
- Triangular prism drawn on Canvas, apex angle adjustable
- **IGCSE standard orientation:** Light enters **left face** → disperses → exits **right face**
- Prism drawn with semi-transparent fill (medium colour)

### Parameters
| Parameter | Range | Step | Default |
|-----------|-------|------|---------|
| Apex angle | 30°–80° | 5° | **60°** |
| Incident angle θ₁ | 0°–75° | 0.5° | **45°** |
| Ray position on prism face | Drag on canvas | — | Centre |

### Constraint: NO TIR
- System automatically limits angles to prevent TIR
- If user adjusts any parameter that would cause TIR → snap to nearest safe value
- Show warning chip: "⚠ TIR prevented — angle adjusted"
- This entire section is about **Dispersion**, not TIR

### Prism Medium Options (Dropdown)
| Medium | Dispersion | n range (400–700 nm) | Notes |
|--------|-----------|---------------------|-------|
| Crown Glass (BK7) | Moderate | 1.513–1.531 | Default, IGCSE standard |
| Flint Glass (F2) | High | 1.610–1.670 | Stronger dispersion |
| Water | Low | 1.330–1.342 | Weak dispersion |
| Perspex | Moderate-low | 1.490–1.502 | |
| Diamond | Very high | 2.40–2.45 | |

**Colour fill for each medium:** Use the same MEDIA array and fill colours from `Wave_1_refraction_of_light.html`:
```javascript
const MEDIA = [
  { name:"Air",         n:1.00, fill:null },
  { name:"Water",       n:1.33, fill:"rgba(25,80,160,0.38)" },
  { name:"Ice",         n:1.31, fill:"rgba(180,215,235,0.3)" },
  { name:"Perspex",     n:1.49, fill:"rgba(220,215,200,0.22)" },
  { name:"Crown Glass", n:1.52, fill:"rgba(195,205,210,0.22)" },
  { name:"Diamond",     n:2.42, fill:"rgba(200,210,220,0.18)" }
];
```

## 1.3 Colour Data (Wavelength, Frequency, Refractive Index)

Values chosen so that **Δn between consecutive colours is approximately equal (~0.0030 ± 0.0003)** for Crown Glass — ensures even spectrum spacing on screen.

### Crown Glass (BK7) — Cauchy: n(λ) = 1.5046 + 0.00420/λ² (λ in μm)

| Colour | λ (nm) | f (THz) | n (BK7) | Δn | Hex colour |
|--------|:------:|:-------:|:-------:|:--:|:----------:|
| 🔴 Red | 700 | 428 | 1.5132 | — | `#FF3B30` |
| 🟠 Orange | 610 | 492 | 1.5158 | +0.0026 | `#FF9500` |
| 🟡 Yellow | 550 | 545 | 1.5185 | +0.0027 | `#FFCC00` |
| 🟢 Green | 500 | 600 | 1.5214 | +0.0029 | `#34C759` |
| 🔵 Blue | 460 | 652 | 1.5245 | +0.0031 | `#007AFF` |
| 🟣 Indigo | 425 | 705 | 1.5278 | +0.0033 | `#5856D6` |
| 🟣 Violet | 400 | 750 | 1.5309 | +0.0031 | `#AF52DE` |

### IR & UV (Sun Light mode only)
| Band | λ range | Display |
|------|---------|---------|
| ☀️ IR | 780–2500 nm | Faint red band (`#FF3B30` ~30% opacity) |
| ☀️ UV | 100–400 nm | Faint violet band (`#AF52DE` ~30% opacity) |

## 1.4 Ray Display Rules

**Monochromatic / Visible Light mode:**
- All rays same thickness (~3px)
- Each colour shown as a separate line with arrowhead
- Colour pill controls: mono = single select, visible = multi-select

**Sun Light mode:**
- Rays drawn as **continuous spectrum bands** (not individual thin lines)
- **IR:** Faint red band, width ~same as visible bands
- **UV:** Faint violet band
- Visible colours blended into a continuous gradient band

**Labels on Canvas:** Colour name only (λ, f, n values in Side Panel)

## 1.5 Side Panel

| Section | Content |
|---------|---------|
| 🎨 **Color Spectrum Table** | 7 rows (Red→Violet) + IR + UV: Colour, λ (nm), f (THz), n, θ₂, Deviation angle |
| 📐 **Formula** | Snell's Law + Dispersion: n(λ) = A + B/λ² (Cauchy), live substitution for each colour |
| 📊 **Summary** | Total deviation angle per colour, angular spread (Δθ between Red and Violet) |
| 🧪 **IR Thermometer** | Draggable thermometer. Temperature: Violet~22°C → Red~28°C → **IR peak ~32°C** |

## 1.6 Herschel's IR Thermometer Experiment (Sun Light mode)

### Historical Context (Side Panel Info)
> **Sir William Herschel** discovered infrared radiation in 1800. He passed sunlight through a prism and placed thermometers at different positions in the spectrum. He found the temperature was **highest just beyond the red end** — in what we now call the infrared region. This proved invisible radiation beyond visible spectrum carries heat energy. This experiment appears in **IGCSE Physics 0625** exams.

### Interactive Thermometer
- Draggable thermometer icon on Canvas (Sun Light mode only)
- User drags thermometer to any position along the spectrum
- **Temperature reading** changes:
  | Position | Temp | Reason |
  |----------|------|--------|
  | Violet | ~22°C | Least heating |
  | Green/Blue | ~25°C | Moderate |
  | Red | ~28°C | Warmer |
  | **Beyond Red (IR)** | **~32°C** | **IR carries most heat** |
  | Further out | ~28°C | Returns to ambient |

### Educational Message (when thermometer in IR region)
> "The thermometer reads highest just beyond the red end — this is **infrared radiation**. IR carries thermal energy, which is why warm objects emit IR. This is Herschel's famous experiment!"

---

# SECTION 2a: Parallel Glass Blocks (1–2 Blocks)

## 2a.1 Setup

- **1 or 2 rectangular glass blocks** (user selects count via dropdown/toggle)
- Blocks stacked vertically (ray enters top → passes through block(s) → exits bottom)
- Each block can have a **different refractive index** (dropdown per block)
- The blocks **do not have colour fills** — just outlined with label showing n value and colour name

### Block Material Options
Reuse the same `MEDIA` array from Section 1. Each block has its own dropdown.

## 2a.2 Light Source

| Mode | Allowed? |
|------|----------|
| 🔦 Monochromatic | ✅ Yes |
| 🌈 Visible Light | ✅ Yes (colour pills, multi-select) |
| ☀️ Sun Light | ❌ **NOT allowed** |

## 2a.3 Direction

- Light enters from **top → bottom** (source at top, blocks below)
- Single incident ray (or multiple colour rays for visible light)

## 2a.4 Normal Line Rules

| Condition | Draw Normal? |
|-----------|-------------|
| 🎯 Entry point (first surface) | ✅ **Always** |
| 🔦 Monochromatic (1 colour) | ✅ **Every refraction point** |
| 🌈 Visible Light (2+ colours) | ❌ **Skip** (except entry point) — avoids clutter |

**Normal style:** Dashed gray line, same as in Refraction simulation

## 2a.5 TIR Between Blocks

- When light passes from block 1 → block 2 (or block → air)
- If n₁ > n₂ and θ₁ > θc → **TIR occurs** (light reflects back into block)
- Show warning chip: "⚠ TIR at interface — ray reflected"

## 2a.6 Dispersion in Blocks

- When Visible Light mode is active with 2+ colour pills
- Each colour refracts at a different angle at each interface → **dispersion occurs**
- Colours separate as they pass through blocks (similar to prism but with parallel faces)
- Exit rays show lateral displacement + angular separation between colours

---

# SECTION 2b: Half Circular Glass Block

## 2b.1 Setup

- **D-shape** block (half circle), **flat face on top, curved face on bottom**
- Light enters from **bottom → top** (from curved face)
- Light exits through **flat face** (top)

## 2b.2 Parameters

| Parameter | Range | Interaction |
|-----------|-------|-------------|
| Entry position on curved face | Full arc | **Drag ray** along curved face |
| Incident angle | ~0–90° | Adjustable via slider or drag |
| Direction (left/right) | Switchable | Toggle or drag to either side |

## 2b.3 Light Source

| Mode | Allowed? | Behaviour |
|------|----------|-----------|
| 🔦 Monochromatic | ✅ Yes | Shows **critical angle** — ray skims flat face when θ₁ = θc |
| 🌈 Visible Light | ✅ Yes | Ray tracing only (no critical angle display) |
| ☀️ Sun Light | ❌ **NOT allowed** | |

## 2b.4 Physics

- Light enters curved face → **no refraction** (normal to surface = radial direction)
- Light travels straight to flat face → **refracts** at flat face
- At flat face: Snell's Law applies (n₁ sin θ₁ = n₂ sin θ₂)
- **Critical angle** can be observed when ray inside block hits flat face at θc → ray skims along surface
- Beyond θc: TIR occurs (ray reflects back into block → out through curved face)

---

# SECTION 2c: Optical Fiber

## 2c.1 Setup

- **Core** (high n, e.g., Crown Glass 1.52) + **Cladding** (low n, e.g., Perspex 1.49)
- Fiber drawn as horizontal tube with core (thick) + cladding (thin outer layer)
- Light enters at **left end** → travels via **TIR** → exits at **right end**

## 2c.2 Parameters

| Feature | Interaction |
|---------|-------------|
| Entry position | **Drag** along left end face (up/down) |
| Entry angle θ₁ | **Slider** or **drag ray** |
| **1 Bend point** | **Drag** a control point on the fiber to bend it |
| **Cladding damage** | **Drag to scrape** — drag mouse along cladding to remove it |

**When cladding is damaged:**
- At the damaged point, light escapes (no TIR possible there)
- Show escaping ray(s) — visible as faint glow/ray leaving the fiber
- Damaged region shown as missing cladding (transparent patch)

## 2c.3 Light Source

| Mode | Allowed? | Behaviour |
|------|----------|-----------|
| 🔦 Monochromatic | ✅ Yes | Single ray, TIR at correct angle |
| 🌈 Visible Light | ✅ Yes | Multiple colour rays — **each colour has different θc** → some colours may leak while others still TIR |
| ☀️ Sun Light | ❌ **NOT allowed** | |

**Educational effect (Visible Light):**
- Different colours have different critical angles (due to n varying with λ)
- For a given bend/damage, some colours may **leak** while others **continue via TIR**
- This creates a beautiful visual effect where the fiber output changes colour depending on bend/damage severity

## 2c.4 Physics

- **TIR condition:** θ₁ > θc where θc = sin⁻¹(n_cladding / n_core)
- For Crown Glass core (1.52) / Perspex cladding (1.49): θc ≈ sin⁻¹(1.49/1.52) ≈ 78.5°
- Different colours have slightly different θc (by ~0.5° across spectrum)
- **Bend:** Changes the angle at which light hits the core-cladding interface → tighter bend = larger angle → may exceed θc → leak
- **Damage:** Missing cladding → n_outside = air (1.00) → critical angle drops → light escapes even at shallow angles

---

# SECTION 3: IGCSE Pin Experiment (Rectangular Glass Block)

## 3.1 Setup

- **Rectangular glass block** placed on a paper/workspace background
- User **drags 4 pins** into position:
  - **Pin 1 & 2:** Placed above the block (incident ray side)
  - **Pin 3 & 4:** Placed below the block (refracted ray side)
- Pins are shown as small circle/cross marks on canvas

## 3.2 Workflow

```
1. Place 4 pins around block
2. Remove block (button: "Lift Block" → block fades/disappears)
3. Press "Auto Draw Lines" → lines drawn connecting opposite pins
4. Draw block outline back (optional)
5. Normal lines auto-drawn at entry and exit points
6. User measures angles i (incidence) and r (refraction) from canvas
7. User enters i and r values → system calculates n = sin i / sin r
```

## 3.3 Key Features

| Feature | Detail |
|---------|--------|
| **4 Pins** | User drags to place. Visual: crosshair/circle marker. Labelled P₁, P₂, P₃, P₄ |
| **Lift Block** | Button to remove block from view (simulates real experiment) |
| **Auto Draw Lines** | Button → connects P₁→P₂ (incident ray), P₃→P₄ (refracted ray), extends through block area |
| **Draw Block Outline** | Toggle to show/hide block outline |
| **Auto Normal Lines** | ✅ Dashed gray normal at entry and exit points (always drawn when lines visible) |
| **Angle Measurement** | User reads i and r from canvas (protractor lines or angle display) |
| **Calculate n** | User inputs i and r → system computes n = sin i / sin r |
| **Light Source** | White light only (no colour pills) |

## 3.4 Educational Explanation (shown when "Auto Draw Lines" is pressed)

> **Why use 4 pins?**
> 1. Pins P₁ and P₂ define the **incident ray** (straight line through air)
> 2. Pins P₃ and P₄ define the **emergent ray** (straight line through air after block)
> 3. Removing the block and connecting the lines lets us trace the **path of light through the block**
> 4. The **lateral shift** between incident ray (P₁P₂) and emergent ray (P₃P₄) shows that light changes direction inside the block
> 5. Measuring angles **i** (at entry) and **r** (inside block) allows us to calculate the **refractive index** n = sin i / sin r
>
> This is a **standard IGCSE practical** — allow students to understand how Snell's Law was discovered and verified through simple experiments.

---

# SECTION 4: Real & Apparent Depth

## 4.1 Setup

- **Container (beaker/glass)** filled with liquid, viewed from above
- **Coin** at the bottom of the container
- User looks from **above the liquid surface**
- Due to refraction, the coin **appears shallower** than its actual depth

## 4.2 Parameters

| Parameter | Range | Control |
|-----------|-------|---------|
| Real depth | 5–30 cm | Slider (step 1 cm, default 15 cm) |
| Viewing angle | 0°–60° | Slider (step 1°, default 30°) |
| **Liquid type** | Dropdown | Water (n=1.33), Oil (n=1.47), Glycerin (n=1.47) |

## 4.3 Visual Display

- **2 ray paths** from coin to eye:
  1. Ray from coin → refracts at surface → reaches eye
  2. Second ray at slightly different angle → helps determine apparent position
- **Dashed line** shows where the coin **appears to be** (apparent depth)
- **Solid line** shows where the coin **actually is** (real depth)
- Both depths labelled clearly on canvas
- **Scuba/underwater visual effect** — slight blue tint in water layer

## 4.4 Side Panel

| Field | Content |
|-------|---------|
| 📏 Real depth | [value] cm |
| 👁️ Viewing angle | [value]° |
| 🌊 Liquid | [name] n = [value] |
| 📐 Apparent depth | [value] cm (calculated) |
| 📝 Formula | Apparent depth = Real depth / n |
| | And: Apparent depth = Real depth × cos(i) / cos(r) × 1/n (for angled viewing) |

## 4.5 Modes

| Mode | Behaviour |
|------|-----------|
| 🎮 **Simulate** | All values visible. User can adjust parameters freely. |
| 🎯 **Practice** | Apparent depth hidden. User must calculate from given real depth and n. |
| ❌ **Quiz** | Not included |

## 4.6 IGCSE Explanation (Side Panel)

> **Why does the coin appear shallower?**
> - Light from the coin travels from **water→air**, which is **slow→fast** (n₁ > n₂)
> - Light bends **away from the normal** at the surface
> - Our brain assumes light travels in straight lines, so it **projects the ray backward** in a straight line
> - This creates a **virtual image** above the real position — the coin looks like it's closer to the surface
>
> **Formula:** Apparent depth = Real depth / n  
> Example: Coin at 15 cm in water (n = 1.33) → Apparent depth = 15 / 1.33 = **11.3 cm**

---

# Shared Controls & Interactions

## Toolbar Structure (all sections)

**Row 1 (Section-specific):**
- Light Source: 3 pill buttons (Mono / Visible / Sun — where applicable)
- Colour pills: ROYGBIV (multi-select for Visible, single for Mono)
- Medium/Block selection: Dropdowns for media, block count, etc.

**Row 2 (Shared):**
- θ₁ slider + input: 0°–75° (or appropriate range per section), step 0.5°
- ▶ Play / ⏸ Pause
- Speed: 0.5× / 1× / 2×
- Show toggles: Angles (∠) / Labels / Wavefront (where applicable)

## Canvas Interactions

| Action | Result |
|--------|--------|
| **Drag ray** | Adjust incident angle (hit-test near ray) |
| **Double-click** | Zoom in at point |
| **Esc / double-click** | Zoom out |
| **Drag objects** | Move pins (Pin Experiment), move thermometer (Sun Light), scrape cladding (Fiber) |

## Themes

Reuse the same theme system from `Wave_1_refraction_of_light.html`:
- 🌙 Classic Dark (default)
- ⌂ HAUS Night
- 🌃 Cyberpunk Neon
- ☀️ Classic Light
- ⌂ HAUS Day
- 🏺 Warm Clay

---

# File Structure

Each section should be a **separate single HTML file**:

| File | Section |
|------|---------|
| `Wave_2_dispersion_of_light.html` | Section 1: Dispersion (Prism) |
| `Wave_3_parallel_glass_blocks.html` | Section 2a: Parallel Glass Blocks |
| `Wave_4_half_circular_block.html` | Section 2b: Half Circular Block |
| `Wave_5_optical_fiber.html` | Section 2c: Optical Fiber |
| `Wave_6_pin_experiment.html` | Section 3: IGCSE Pin Experiment |
| `Wave_7_real_apparent_depth.html` | Section 4: Real & Apparent Depth |

**Specifications:**
- Single HTML file per section (standalone)
- External dependencies: Google Fonts + KaTeX CDN (same as Refraction)
- Reference layout: `Wave_1_refraction_of_light.html`
- Language: English (default)
- All IGCSE Physics 0625 conventions followed
- Real refractive index values used throughout

---

# Feature Checklist

### Section 1: Dispersion (Prism)
- [x] Triangular prism (adjustable apex 30°–80°, default 60°)
- [x] 3 Light Sources (Mono / Visible / Sun)
- [x] 7 colour pills (ROYGBIV) — single/multi-select
- [x] Sun Light: all colours + IR (faint red) + UV (faint violet) as continuous band
- [x] Snell's Law + Dispersion — NO TIR allowed
- [x] Incident angle 0°–75°, step 0.5°, default 45°
- [x] Ray position draggable on prism face
- [x] 5 prism materials (reuse MEDIA array from Refraction)
- [x] Side Panel: Color Spectrum Table + Formula + Summary
- [x] Herschel's IR Thermometer (draggable, highest temp in IR)
- [x] IGCSE historical context: Herschel discovered IR in 1800
- [x] 6 themes

### Section 2a: Parallel Glass Blocks
- [x] 1 or 2 blocks (selectable)
- [x] Each block has independent refractive index (dropdown)
- [x] Light enters top → exits bottom
- [x] Normal: always at entry point, mono=every point, 2+ colours=skip
- [x] TIR between blocks when n₁ > n₂ and angle exceeds θc
- [x] Dispersion when Visible Light with 2+ colours
- [x] Sun Light NOT allowed

### Section 2b: Half Circular Block
- [x] D-shape face up, light enters from bottom curved face
- [x] Adjustable entry position (drag along curved face)
- [x] Incident angle ~0–90°
- [x] Left/right direction adjustable
- [x] Monochromatic: shows critical angle
- [x] Visible Light: ray tracing only
- [x] Sun Light NOT allowed

### Section 2c: Optical Fiber
- [x] Core (high n) + Cladding (low n)
- [x] Entry position + entry angle adjustable
- [x] 1 bend point (drag to bend)
- [x] Cladding damage: drag to scrape
- [x] TIR physics with different θc per colour
- [x] Visible Light: each colour may leak independently
- [x] Sun Light NOT allowed

### Section 3: Pin Experiment
- [x] 4 draggable pins
- [x] Lift Block button
- [x] Auto Draw Lines button (with educational explanation)
- [x] Auto Normal Lines (dashed gray)
- [x] User measures i and r → calculates n = sin i / sin r
- [x] White light only

### Section 4: Real & Apparent Depth
- [x] Container + liquid + coin
- [x] Real depth slider (5–30 cm)
- [x] Viewing angle (0°–60°)
- [x] Liquid selection (Water/Oil/Glycerin)
- [x] Ray tracing from coin to eye
- [x] Apparent depth formula: d_app = d_real / n
- [x] Simulate + Practice modes
- [x] IGCSE explanation

---

# Reference Implementation

See `Wave_1_refraction_of_light.html` for:
- Canvas rendering (DPR, coordinate transforms, Ray drawing)
- Toolbar pattern (pills, tgroup, tbtn, dropdowns)
- Side panel (val-grid, eq-box, KaTeX rendering)
- Animation loop (pen-drawing Type B)
- Zoom (double-click, focus point, pan)
- Theme system (CSS variables, setTheme())
- Media array (n values, fill colours)
- Snell's Law physics (sinT2, critical angle, TIR detection)