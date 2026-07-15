# Prompt: Dispersion of Light — 2D Ray Tracing Simulation
## For Fable 5.0 (Anthropic)

---

## 1. Overview

Build an **interactive 2D Ray Tracing Simulation** (single-file HTML + Canvas 2D) for **Dispersion of White Light** through a prism, following the **IGCSE Physics 0625** curriculum.

The simulation covers:
- White light dispersion into ROYGBIV spectrum via a triangular prism
- Monochromatic light (selectable single colour)
- Sun Light mode (Visible + IR + UV) with Herschel's thermometer experiment
- Adjustable prism apex angle, incident angle, and ray position

---

## 2. Layout (Ref: `Wave_1_refraction_of_light.html`)

### Top Bar
- Title: "🌈 Dispersion of Light" + badge "v1.0.0"
- Mode: (No Practice/Quiz — Simulate only)
- Theme Selector (dropdown) — reuse the same 6+ theme system
- HAUS Brand Logo (top-right, yellow background)

### Toolbar (2 rows)

**Row 1:**
| Control | Type | Options |
|---------|------|---------|
| Light Source | 3 Buttons (pill) | Monochromatic · Visible Light · Sun Light |
| Prism Medium | Dropdown | Crown Glass (BK7) · Flint Glass · Water |
| Apex Angle | Slider + Input | 30°–80°, step 5°, default **60°** |
| Direction Badge | Auto chip | Shows "Fast → Slow" or "Slow → Fast" based on n₁ vs n₂ |

**Row 2:**
| Control | Type | Options |
|---------|------|---------|
| Colour Picker | Pills | Red · Orange · Yellow · Green · Blue · Indigo · Violet |
| | Behavior | **Monochromatic:** select only 1 pill. **Visible Light:** select multiple pills (on/off per colour). **Sun Light:** all pills forced on + IR/UV |
| Incident Angle θ₁ | Slider + Input | 0°–75°, step 0.5°, default **45°** |
| Play/Pause | Button | ▶ Play / ⏸ Pause |
| Speed | Pills | 0.5× · 1× · 2× |
| Show Toggles | Buttons | Angles (∠) · Labels · Wavefront |

### Main Grid (65% Canvas : 35% Side Panel)

**Canvas (Left):**
- Dark background
- Triangular prism drawn in the centre (apex angle adjustable)
- White light ray enters left face → disperses into colours → exits right face
- Each colour ray shown as a separate line with arrowhead
- Animation: pen-drawing (Type B) — same as Refraction simulation

**Side Panel (Right):**
| Section | Content |
|---------|---------|
| 🎨 **Color Spectrum** | Table: 7 rows (Red → Violet) + IR + UV columns: Colour, λ (nm), f (THz), n, θ₂, Deviation angle |
| 📐 **Formula** | Snell's Law + Dispersion: n(λ) = A + B/λ² |
| 📊 **Summary** | Total deviation angle per colour, Δθ between consecutive colours |
| 🧪 **IR Thermometer** (Sun Light only) | Draggable thermometer, shows temperature at each colour position |

---

## 3. Light Source System

### Mode Selection (3 pill buttons, mutually exclusive)

| Mode | Behaviour |
|------|-----------|
| 🔦 **Monochromatic** | Select exactly **1 colour pill** (ROYGBIV). Single ray shown in that colour. |
| 🌈 **Visible Light** | Select **any number of colour pills** (on/off each). Each selected colour shown as a separate ray. Default: all 7 ON. |
| ☀️ **Sun Light** | Only available when **Prism** is selected as medium. Shows **all 7 visible + IR + UV** as a **continuous spectrum**-style display. IR & UV added automatically. |

### Sun Light — Ray Display
- Rays are drawn as **continuous spectrum bands** (not individual thin lines)
- **Infrared (IR):** Faint red/ deep red band, width ~same as visible bands. λ > 750 nm.
- **Ultraviolet (UV):** Faint violet band. λ < 380 nm.
- Visible colours are drawn as before but blended into a continuous gradient band (prism-like spectrum).
- When using **Parallel Glass Block** or other media (future phases), Sun Light falls back to individual IR/UV labels.

---

## 4. Prism (Dispersion Medium)

### Geometry
- Triangular prism drawn on Canvas with adjustable apex angle
- Light enters the **left face** → refracts → disperses → exits the **right face**
- Prism drawn with semi-transparent fill (colour based on medium)
- Prism material: **Crown Glass (BK7)** as default

### Adjustable Parameters
| Parameter | Range | Step | Default |
|-----------|-------|------|---------|
| Apex angle | 30°–80° | 5° | **60°** |
| Incident angle θ₁ | 0°–75° | 0.5° | **45°** |
| Ray position on prism face | Drag on canvas | — | Centre |

### Constraint: NO Total Internal Reflection (TIR)
- System must automatically limit angles to **prevent TIR**
- If user adjusts any parameter that would cause TIR → snap to nearest safe value
- Show warning chip: "⚠ TIR prevented — angle adjusted"
- The entire simulation is about **Dispersion**, not TIR

### Prism Medium Options (Dropdown)
| Medium | Dispersion | n range (400–700 nm) | Notes |
|--------|-----------|---------------------|-------|
| Crown Glass (BK7) | Moderate | 1.513–1.531 | Default, IGCSE standard |
| Flint Glass (F2) | High | 1.610–1.670 | Stronger dispersion, wider spectrum |
| Water | Low | 1.330–1.342 | Weak dispersion |
| Perspex | Moderate-low | 1.490–1.502 | |

---

## 5. Colour Data (Wavelength, Frequency, Refractive Index)

Values chosen so that **Δn (change in refractive index between consecutive colours) is approximately equal (~0.0030 ± 0.0003)** — this ensures the spectrum spacing looks even on screen.

### Crown Glass (BK7) — Cauchy equation: n(λ) = 1.5046 + 0.00420/λ² (λ in μm)

| Colour | λ (nm) | f (THz) | n (BK7) | Δn | Hex colour |
|--------|:------:|:-------:|:-------:|:--:|:----------:|
| 🔴 Red | 700 | 428 | 1.5132 | — | `#FF3B30` |
| 🟠 Orange | 610 | 492 | 1.5158 | +0.0026 | `#FF9500` |
| 🟡 Yellow | 550 | 545 | 1.5185 | +0.0027 | `#FFCC00` |
| 🟢 Green | 500 | 600 | 1.5214 | +0.0029 | `#34C759` |
| 🔵 Blue | 460 | 652 | 1.5245 | +0.0031 | `#007AFF` |
| 🟣 Indigo | 425 | 705 | 1.5278 | +0.0033 | `#5856D6` |
| 🟣 Violet | 400 | 750 | 1.5309 | +0.0031 | `#AF52DE` |

### Flint Glass (F2) — for comparison (approximate)
Use Cauchy: n(λ) = A + B/λ² where A ≈ 1.585, B ≈ 0.00800 μm²
- Red (700 nm): n ≈ 1.601
- Violet (400 nm): n ≈ 1.635
- Stronger dispersion → wider separation on screen

### Water
Use Cauchy: n(λ) = 1.321 + 0.00310/λ² (λ in μm)
- Red (700 nm): n ≈ 1.327
- Violet (400 nm): n ≈ 1.340

### Beyond Visible (for Sun Light mode)

| Band | λ range (nm) | f range (THz) | Display colour |
|------|:-----------:|:------------:|:--------------:|
| ☀️ Infrared (IR) | 780–2500 | 120–385 | Faint red/dark red band |
| 🌈 Visible | 400–750 | 400–750 | Standard ROYGBIV |
| ☀️ Ultraviolet (UV) | 100–400 | 750–3000 | Faint violet band |

---

## 6. Canvas Drawing

### Canvas Layout
```
┌──────────────────────────────────┐
│                                  │
│    ← White Light  ╱╲             │
│    ← enters     ╱  ╲  Dispersion │
│    left face   ╱    ╲  exits     │
│               ╱______╲  right    │
│              Prism     face      │
│    🔴🟠🟡🟢🔵🟣              │
│                                  │
└──────────────────────────────────┘
```

### Ray Drawing Rules
1. **Incident ray:** Thick white/gold line entering left face of prism
2. **Inside prism:** White ray enters → bends according to Snell's Law → different colours diverge inside
3. **Exiting rays:** Each colour exits right face at a different angle
4. **Ray thickness:** Monochromatic/Visible mode = same thickness (~3px). Sun Light mode = continuous spectrum band style
5. **Arrowheads** at the end of each outgoing ray
6. **Labels:** Colour name on/near each ray (just the name — λ, f, n in side panel)
7. **Animation:** Pen-drawing (Type B) — same progressive draw as Refraction simulation

### IR & UV Drawing (Sun Light mode only)
- **IR:** Faint red band (#FF3B30 with ~30% opacity), drawn beyond Red (λ > 750 nm)
- **UV:** Faint violet band (#AF52DE with ~30% opacity), drawn beyond Violet (λ < 400 nm)
- Width of band approximately the same as a visible colour band
- IR band shown as continuous, not a single line

---

## 7. Interaction

### Drag Ray on Canvas
- User can **drag** the incident ray **left/right** along the prism's left face
- This changes both the incident angle θ₁ and the point of incidence
- Same pointer-drag pattern as Refraction simulation (hit-test near ray)

### Slider Controls (Toolbar)
- **Apex angle slider:** Adjusts prism geometry (redraws prism)
- **θ₁ slider:** Adjusts incident angle (fine control)
- **θ₁ input:** Direct number entry

### Zoom
- **Double-click** on canvas → zoom in (magnified view around incident point)
- **Esc** or **double-click again** → zoom out
- Same pattern as Refraction simulation

---

## 8. IR Thermometer Experiment (Sun Light mode only)

### Historical Context (for Info Box / side panel)
> **Sir William Herschel** discovered infrared radiation in 1800. He passed sunlight through a prism and placed thermometers at different positions in the spectrum. He found that the temperature **increased** from violet to red, and was **highest just beyond the red end** — in what we now call the infrared region. This proved that there is invisible radiation beyond the visible spectrum that carries heat energy.
>
> This experiment appears in **IGCSE Physics 0625** exams.

### Interactive Thermometer
- A small **thermometer icon/graphic** appears in the scene when Sun Light mode is active
- User can **drag the thermometer** to any position along the spectrum (after the prism)
- **Temperature reading** changes based on position:
  | Position | Temperature | Explanation |
  |----------|-------------|-------------|
  | Violet end | ~22°C (coolest) | Least heating |
  | Green/Blue | ~25°C | Moderate |
  | Red end | ~28°C | Warmer |
  | **Just beyond Red (IR)** | **~32°C (hottest)** | **IR carries most heat** |
  | Beyond IR (further out) | ~28°C (drops) | No radiation → returns to ambient |
- Thermometer has a visible **liquid column** that rises/falls with temperature
- A **badge** shows the current temperature: "🌡️ 32°C at IR peak"

### Educational Message (shown when thermometer is in IR region)
> "The thermometer reads highest just beyond the red end — this is **infrared radiation**. IR carries thermal energy, which is why warm objects emit IR. This is Herschel's famous experiment!"

---

## 9. Side Panel Details

### 🎨 Color Spectrum Table
| Colour | λ (nm) | f (THz) | n | θ₂ | ΔDeviation |
|--------|:------:|:-------:|:-:|:--:|:----------:|
| 🔴 Red | 700 | 428 | 1.5132 | 22.1° | — |
| 🟠 Orange | 610 | 492 | 1.5158 | 21.8° | -0.3° |
| ... | ... | ... | ... | ... | ... |
| 🟣 Violet | 400 | 750 | 1.5309 | 19.5° | -2.6° |

### 📐 Formula Box
- Snell's Law: n₁ sin θ₁ = n₂ sin θ₂
- Dispersion relation: n(λ) = A + B/λ² (Cauchy equation)
- Live substitution showing calculated values for each colour
- KaTeX rendered (same as Refraction simulation)

### 📊 Summary
- Total deviation angle per colour (from original white light direction)
- Angular spread: Δθ between Red and Violet
- For Sun Light: "IR extends Δθ by +X°, UV by -Y°"

### 🧪 Herschel's Experiment (Sun Light only)
- Brief text: "Sir William Herschel discovered IR in 1800..."
- Draggable thermometer with live readout

---

## 10. Visual & Theme

### Theme System
Reuse the same 6+ themes from existing simulations (Classic Dark, HAUS Night, Neon, Classic Light, HAUS Day, Warm Clay).

### Canvas Aesthetics
- Dark background (default)
- Prism drawn with semi-transparent fill (medium colour)
- Glass-like effects: slight glow on prism edges
- Rays drawn with shadow/blur for a luminous effect
- Normal line (dashed) at each refraction point
- Angle arcs between ray and normal

### Fonts
- Inter (UI), JetBrains Mono (values/formulas), KaTeX (equations)

---

## 11. File Requirements

- **Single HTML file** (standalone, no external dependencies except Google Fonts + KaTeX CDN)
- Place at: `~/InteractiveLecture/simulations/Wave_2_dispersion_of_light.html`
- Reference layout: `Wave_1_refraction_of_light.html` (toolbar, grid, side panel patterns)
- Default theme: Classic Dark
- Language: English (default)

---

## 12. Feature Checklist

- [x] Triangular prism (adjustable apex angle 30°–80°, default 60°)
- [x] 3 Light Source modes (Monochromatic / Visible Light / Sun Light)
- [x] 7 Colour pills (ROYGBIV) — single select (mono) / multi-select (visible)
- [x] Sun Light: all colours + IR (faint red) + UV (faint violet) — continuous spectrum band
- [x] Snell's Law + Dispersion (n varies with λ) — NO TIR allowed
- [x] Incident angle θ₁: 0°–75°, step 0.5°, default 45°
- [x] Ray position on prism face: draggable on canvas
- [x] Zoom: double-click to magnify
- [x] Pen-drawing animation (Type B)
- [x] 4 prism materials (Crown Glass / Flint Glass / Water / Perspex)
- [x] Side panel: Color Spectrum Table + Formula + Summary
- [x] Herschel's IR Experiment: draggable thermometer, highest temp in IR
- [x] IGCSE historical context: Herschel discovered IR in 1800
- [x] 6+ themes (same as existing sims)
- [x] Simulate mode only (no Practice/Quiz in this phase)