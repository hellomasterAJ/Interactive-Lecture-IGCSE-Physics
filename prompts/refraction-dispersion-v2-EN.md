# Prompt v2: Refraction & Dispersion — 2D Ray Tracing Suite
## For Fable 5.0 (Anthropic)
## HAUS Academy · IGCSE Physics 0625

---

## 0. Learning Goals

After using these simulations, students should understand:
- **Ray tracing** — the path of light as it travels through different media
- **Frequency is invariant** — when light enters a medium, its **frequency does not change**; only **speed and wavelength** change depending on the medium and the frequency
- **Dispersion** — different frequencies (colours) have slightly different refractive indices in the same medium, causing them to bend by different amounts, separating white light into its component colours

---

## Overview

Build **multiple separate interactive 2D Ray Tracing simulations** (single-file HTML + Canvas 2D each, NOT combined into one file) covering **Refraction and Dispersion of Light** through **various optical medium shapes**, following the IGCSE Physics 0625 curriculum.

### Medium Shapes (in priority order)

| # | Shape | Light sources | Sun Light | File |
|---|-------|--------------|-----------|------|
| 1 | 🔺 **Prism** (triangular) | Mono · Visible · Sun | ✅ Yes | `Wave_2_dispersion.html` |
| 2 | 🪟 **Parallel Glass Blocks** (1–2 blocks) | Mono · Visible | ❌ No | `Wave_3_glass_blocks.html` |
| 3 | 🔵 **Half Circular Block** | Mono · Visible | ❌ No | `Wave_4_half_circular.html` |
| 4 | 📐 **Right Triangle** | Mono · Visible | ❌ No | `Wave_5_right_triangle.html` |
| 5 | 💎 **Diamond Shape** | Mono · Visible | ❌ No | `Wave_6_diamond.html` |
| 6 | 💧 **Water Drop → Rainbow** | Mono · Visible (Sun optional) | TBD | `Wave_7_raindrop.html` |

### Core Principle
All simulations share the **Refraction + Dispersion** theme:
- **Monochromatic light** → pure refraction (Snell's Law, ray bending)
- **Visible Light (multi-colour)** → **dispersion** (different colours bend by different amounts)

### Main/Global Section (shared across all simulations)

All simulations share these global parameters:

**a) Light Source Selection:**
| Mode | Availability | Behaviour |
|------|-------------|-----------|
| 🔦 **Monochromatic** | All shapes | Single colour (ROYGBIV), 1 pill selectable |
| 🌈 **Visible Range** | All shapes | Multiple colours (ROYGBIV), multi-select pills |
| ☀️ **Sun Light** | **Prism only** | All visible + IR + UV, continuous spectrum bands |

**b) Ray Thickness (CRITICAL — FIX FROM V1):**
- **Ray line width: 1.3–1.5px (MAX 2px)**
- **DO NOT use thick rays** — V1 had rays that were too thick; when multiple colour rays overlapped, they became invisible
- In nature, the spectrum is a **continuous gradient**, not overlapping thick bands
- Each colour ray must be **thin and distinct** so all colours are visible even when they are close together
- Arrowhead at end of each ray (size proportional to ray width)
- **Sun Light mode:** Use wider semi-transparent **bands** (fills) for the continuous spectrum, with thin guide rays (1px) overlaid on top

**c) Standard Medium Colours & n Values (shared across ALL simulations):**
See the MEDIA array below. Every simulation must use the exact same MEDIA array.

---

## Section 1: Dispersion of Light — Prism
**File:** `Wave_2_dispersion.html`

### 1.1 Layout

Reference: `Wave_1_refraction_of_light.html` for exact layout patterns.

**Top Bar:**
- Title: "🌈 Dispersion of Light — Prism" + badge "v2.0.0"
- Theme selector (dropdown) — 6 themes
- HAUS Brand logo (top-right)

**Toolbar Row 1:**
| Control | Type | Details |
|---------|------|---------|
| Light Source | 3 pill buttons | 🔦 Mono · 🌈 Visible · ☀️ Sun |
| Colour pills | Circle swatches (ROYGBIV) | Mono = single select, Visible = multi-select |
| Prism medium | Dropdown | Crown Glass (BK7) · Flint Glass · Water · Perspex · Diamond |

**Toolbar Row 2:**
| Control | Type | Details |
|---------|------|---------|
| Apex angle | Slider + badge | 30°–80°, step 5°, **default 60°**, snap to prevent TIR |
| θ₁ | Slider + input | 0°–75°, step 0.5°, **default 45°** |
| ▶ Play / ⏸ Pause | Button | Pen-drawing animation |
| Speed | Pills | 0.5× · 1× · 2× |
| Show: Angles | Toggle | ∠ button |
| Show: Labels | Toggle | 🏷 button |
| Show: Normals | Toggle | ⊥ button |

**Canvas (Left, ~75%):**
- Dark background (`--graph-bg`)
- Triangular prism drawn in the centre
- Incident ray enters left face → disperses into colours → exits right face
- Animation: pen-drawing Type B (same as Refraction simulation)

**Side Panel (Right, ~25%):**
| Section | Content |
|---------|---------|
| 🎨 **Color Spectrum Table** | 7 rows (Red→Violet) + IR + UV (Sun only): Colour, λ (nm), f (THz), n, Deviation angle |
| 📐 **Formula** | Snell's Law + Dispersion: n(λ) = A + B/λ², live substitution |
| 📊 **Summary** | Angular spread Δθ between Red and Violet |
| 🧪 **Herschel's Thermometer** | Sun Light only: draggable thermometer, historical info |

### 1.2 Prism Geometry

```
        ╱╲
       ╱  ╲
      ╱    ╲
     ╱______╲
    ←──แสง───
```

- **Triangular prism** with apex at top, base at bottom
- Left face: incident light enters
- Right face: dispersed light exits
- Base at bottom
- Prism centred horizontally on Canvas
- Apex angle adjustable: 30°–80° (step 5°, default 60°)

**Prism drawing:**
- Semi-transparent fill using medium's fill colour (from MEDIA array)
- Edge lines with medium's edge colour
- Glass-like appearance (slight glow/transparency)
- Label: medium name below prism, apex angle above apex

### 1.3 Light Source (CRITICAL — get this right)

#### 3 Pill Buttons (mutually exclusive)

| Mode | Behaviour |
|------|-----------|
| 🔦 **Monochromatic** | User selects exactly **1 colour swatch** (ROYGBIV). Shows **single ray** in that colour. |
| 🌈 **Visible Light** | User selects **any number** of colour swatches (on/off each). Shows **multiple rays**, one per selected colour. Default: all 7 ON. |
| ☀️ **Sun Light** | **Only available with Prism medium.** Shows all 7 visible + IR + UV as **continuous spectrum bands**. User cannot toggle individual colours. |

#### Colour Swatches (cpills)
- 7 circular colour buttons (20×20 px, border-radius: 50%)
- Colours: Red (#FF3B30), Orange (#FF9500), Yellow (#FFCC00), Green (#34C759), Blue (#007AFF), Indigo (#5856D6), Violet (#AF52DE)
- **Mono mode:** exactly 1 active (clicking another deselects the previous)
- **Visible mode:** any number active (clicking toggles on/off, minimum 1 stays on)
- **Sun mode:** all forced on, swatches disabled/locked
- Active swatch: opacity 1.0, border-color: white
- Inactive swatch: opacity 0.35, border-color: transparent

#### Colour Data (for Side Panel)

Values chosen so **Δn between consecutive colours is approximately equal (~0.0030)** for Crown Glass.

| Colour | λ (nm) | f (THz) | n (BK7) | Hex |
|--------|:------:|:-------:|:-------:|:---:|
| 🔴 Red | 700 | 428 | 1.5132 | `#FF3B30` |
| 🟠 Orange | 610 | 492 | 1.5158 | `#FF9500` |
| 🟡 Yellow | 550 | 545 | 1.5185 | `#FFCC00` |
| 🟢 Green | 500 | 600 | 1.5214 | `#34C759` |
| 🔵 Blue | 460 | 652 | 1.5245 | `#007AFF` |
| 🟣 Indigo | 425 | 705 | 1.5278 | `#5856D6` |
| 🟣 Violet | 400 | 750 | 1.5309 | `#AF52DE` |

**IR & UV (Sun Light only):**
| Band | λ (nm) | Display colour | Opacity |
|------|:------:|:--------------:|:-------:|
| IR | 850 | Deep red (`#CC2200`) | ~30% of ray, band fill |
| UV | 360 | Deep violet (`#6600AA`) | ~30% of ray, band fill |

### 1.4 Media (Prism material)

```javascript
const MEDIA = [
  { name:"Crown Glass (BK7)", A:1.5046, B:0.00420, fill:"rgba(195,205,210,0.20)", edge:"rgba(200,215,225,0.85)" },
  { name:"Flint Glass (F2)",  A:1.5809, B:0.01426, fill:"rgba(205,195,225,0.22)", edge:"rgba(210,200,235,0.85)" },
  { name:"Water",             A:1.3242, B:0.00285, fill:"rgba(25,80,160,0.30)",  edge:"rgba(90,150,220,0.85)" },
  { name:"Perspex",           A:1.4840, B:0.00285, fill:"rgba(220,215,200,0.18)", edge:"rgba(225,220,205,0.8)" },
  { name:"Diamond",           A:2.3758, B:0.01188, fill:"rgba(200,225,235,0.22)", edge:"rgba(210,235,245,0.9)" }
];
```

**Refractive index function:** `n(λ) = A + B/λ²` where λ is in **nanometres** (convert to μm inside formula).

### 1.5 Physics (CRITICAL — precise math)

#### Prism Geometry
```
Apex: T = (320, 168)
Base left: BL = (320 - half, 442)
Base right: BR = (320 + half, 442)
where half = (442-168) * tan(apex/2)
```

#### Ray Tracing for One Colour
1. **Entry point E** on left face: `E = T + (BL - T) * S1.pos` (pos = 0.52 default, draggable)
2. **Inward normal** at left face: `ni = -nL`
3. **Incident ray direction:** rotate `ni` by `-θ₁`
4. **First refraction** (air → glass): `sin r₁ = sin θ₁ / n`
5. **Ray inside prism:** from E, direction = rotate `ni` by `-r₁`
6. **Intersection X** with right face (T→BR) or base (BL→BR)
7. **Angle of incidence at right face:** `r₂ = apex - r₁`
8. **Second refraction** (glass → air): `sin θₑ = n · sin r₂`
9. **Exit direction:** rotate `g.nR` (right face outward normal) by `θₑ`
10. **Deviation angle:** `δ = θ₁ + θₑ - apex`
11. **TIR check:** if `sin θₑ > 1` → TIR (should not happen — system prevents it)

#### TIR Prevention (CRITICAL)
System must **automatically prevent TIR** at all times:
- For the highest-n colour (Violet, or UV for Sun mode), calculate:
  - Critical angle inside glass: `θc = sin⁻¹(1/n)`
  - Maximum apex: `apex < 2·θc`
  - For given apex, minimum θ₁: `θ₁ ≥ sin⁻¹(n·sin(apex - θc))`
- If any parameter would cause TIR → **snap** to nearest safe value
- Show warning chip: "⚠ TIR prevented — angle adjusted"
- The simulation is about **Dispersion**, not TIR

#### Sun Light Mode (Continuous Spectrum)
- Calculate traces for: IR (850 nm), Red, Orange, Yellow, Green, Blue, Indigo, Violet, UV (360 nm)
- Draw **continuous coloured bands** (not individual lines):
  - Inside prism: fill the wedge between adjacent colour paths
  - Outside prism: fill the fan between adjacent exit rays
- Band opacity: ~34% for visible bands, ~16% for IR/UV bands
- Overlay **thin guide rays** for each colour edge
- **White incident ray** entering the prism
- Labels: "IR" (faint red), "Red", "Violet", "UV" (faint violet) — only at edges, not every colour

### Ray Drawing

**Ray thickness (CRITICAL — FIX FROM V1):**
- Line width: **1.3–1.5px** (MAX 2px)
- Arrowhead: small, proportional to ray width
- Shadow blur: 3–4px (not 6px — too thick)
- **Never use lineWidth > 2px for individual colour rays**

**Incident ray** (before medium):
- White/gold colour (`#f5f0dc`)
- Arrowhead only when animation completes

**Inside medium:**
- Coloured lines (or bands for Sun)
- Each colour bends at different angle

**Exit rays:**
- Coloured lines with arrowhead
- Labels: colour name

**Normal lines:**
- Dashed grey, at entry point and exit point
- Toggle: ⊥ button

**Angle arcs:**
- θ₁ at entry, θₑ at exit, θc shown if relevant
- Toggle: ∠ button

### 1.7 Herschel's Thermometer (Sun Light Mode only)

**CRITICAL — this must work correctly:**

- A small thermometer graphic appears on the Canvas when Sun mode is active
- User can **drag the thermometer** to any position along the spectrum
- Temperature reading updates based on position:
  - Violet end: ~22°C
  - Green/Blue: ~25°C
  - Red end: ~28°C
  - **Just beyond Red (IR peak): ~32°C — hottest**
  - Further beyond IR: drops back to ~22°C

**Temperature calculation:**
- Map thermometer position to the angular coordinate of the exit fan
- Calculate angle `a = atan2(p.y - Xc.y, p.x - Xc.x)` where `Xc` is midpoint of exit points
- Normalize between Violet angle (u=0) and Red angle (u=1)
- IR sits at u ≈ 1.15 (just beyond Red)
- Temperature baseline: 22 + 6·clamp(u, 0, 1) → 22°C at Violet, 28°C at Red
- Gaussian bump at IR position: +5°C → peak ~32°C
- Beyond IR: exponential decay to ambient

**Thermometer graphic:**
- Small vertical thermometer icon (~30×60 px)
- Liquid column fills proportionally to temperature (20°C = empty, 35°C = full)
- Display current temperature as a badge: "🌡️ 32°C"
- When thermometer is in IR region, show educational message in side panel:
  > "The thermometer reads highest just beyond the red end — this is **infrared radiation**. IR carries thermal energy. This is Herschel's famous experiment (1800)."

### 1.8 Side Panel

**Color Spectrum Table:**
- 7 rows (Red→Violet) + IR + UV (Sun only)
- Columns: Colour (with swatch), λ (nm), f (THz), n, Deviation angle (°)
- Values update live when parameters change
- When Sun is NOT active, IR/UV rows hidden

**Formula Box:**
- Top: Snell's Law: `n₁ sin θ₁ = n₂ sin θ₂`
- Bottom: Dispersion relation: `n(λ) = A + B/λ²` with current values
- KaTeX rendered

**Summary:**
- Angular spread: "Δθ (Red→Violet): X.X°"
- For Sun: "IR extends spectrum by +X.X°, UV by -Y.Y°"

**Herschel Info (Sun only):**
- Historical text
- Temperature reading from thermometer

---

## Section 2: Parallel Glass Blocks
**File:** `Wave_3_glass_blocks.html`

### 2.1 Layout

Same layout template as Section 1, but with different toolbar controls.

**Toolbar Row 1:**
| Control | Type | Details |
|---------|------|---------|
| Light Source | 3 pill buttons | 🔦 Mono · 🌈 Visible · ~~☀️ Sun~~ **(disabled)** |
| Colour pills | Swatches | Same as Section 1 |
| Block count | Pills | 1 · 2 |

**Toolbar Row 2:**
| Control | Type | Details |
|---------|------|---------|
| Block 1 medium | Dropdown | Crown Glass, Flint Glass, Water, Perspex, Diamond |
| Block 2 medium | Dropdown | (same, visible only when count=2) |
| θ₁ | Slider + input | 0°–75°, step 0.5°, default 40° |
| ▶ Play, Speed, Show | Same as Section 1 | |

### 2.2 Geometry

```
Light enters from TOP → passes through block(s) → exits at BOTTOM

Air (n=1)
┌───────────────────┐  ← Entry interface (always draw normal)
│   Block 1 (n₁)    │
└───────────────────┘  ← Interface 1 (draw normal if mono)
Air (if 1 block, or gap)
┌───────────────────┐  ← Interface 2 (draw normal if mono)
│   Block 2 (n₂)    │
└───────────────────┘  ← Exit interface (draw normal if mono)
Air (n=1)
```

- Rectangular blocks, full width of canvas
- Each block height: ~80px
- Gap between blocks: ~30px (if 2 blocks)
- Blocks centred vertically on canvas

### 2.3 Light Source Rules

| Mode | Allowed? | Behaviour |
|------|----------|-----------|
| 🔦 Monochromatic | ✅ Yes | Single ray, refraction at each interface, **TIR possible** between blocks |
| 🌈 Visible Light | ✅ Yes | Multiple colour rays, **dispersion** at each interface |
| ☀️ Sun Light | ❌ **Disabled** | Button greyed out with tooltip |

### 2.4 Normal Line Rules (CRITICAL)

| Condition | Draw Normal? |
|-----------|-------------|
| **Entry point** (first interface, air→block) | ✅ **Always** |
| Each interface, **Monochromatic mode** | ✅ **Always** |
| Each interface, **Visible Light (2+ colours)** | ❌ **Skip** — only at entry point |
| **Exit point** (last interface, block→air) | Follow same rule as above |

**Normal style:** Dashed grey line, length ~50px

### 2.5 Physics

#### Ray Tracing for One Colour
1. **Entry** (air → block): `sin r = sin θ₁ / n₁`
2. **Inside block:** straight line, direction = angle r from normal
3. **Exit** (block → air or block₂): `sin θ₂ = n₁ · sin r`
   - If no second block: exits to air, lateral displacement visible
   - If second block exists: enters block₂, refracts again
4. **TIR check:** If `n₁ > n₂` and the ray hits the interface at angle > θc → TIR occurs
   - Show TIR badge: "⚠ TIR at interface — ray reflected"
   - Draw reflected ray inside block back toward entry side

#### TIR Between Blocks
- When n₁ > n₂ (e.g., Crown Glass → Air)
- Critical angle: `θc = sin⁻¹(n₂/n₁)`
- If ray angle at interface > θc → **TIR**
- TIR ray reflects inside block 1 back toward entry face
- Show warning chip

#### Dispersion in Blocks
- When Visible Light with 2+ colours:
  - Each colour has slightly different n → different r at each interface
  - Colours gradually separate as they pass through blocks
  - Exit rays show lateral displacement + angular separation

### 2.6 Block Drawing

- Each block: filled rectangle with semi-transparent fill (medium colour)
- Outline: medium's edge colour, 2px stroke
- Label: medium name at centre of block
- If block is lifted/removed: not applicable (blocks stay visible)

### 2.7 Side Panel

**Current Values:**
- θ₁ (incident angle)
- For each interface: n₁, n₂, θ₁, θ₂, Status (Refraction / TIR)
- Total lateral displacement (mm)

**Formula:**
- Snell's Law at each interface
- For TIR: critical angle calculation

**Note:**
- "TIR occurs when light travels from a denser to a rarer medium at an angle greater than the critical angle."

---

## Section 3: Half Circular Glass Block
**File:** `Wave_4_half_circular.html`

### 3.1 Layout

**Toolbar Row 1:**
| Control | Type | Details |
|---------|------|---------|
| Light Source | 3 pill buttons | 🔦 Mono · 🌈 Visible · ~~☀️ Sun~~ **(disabled)** |
| Colour pills | Swatches | Same as Section 1 |
| Block medium | Dropdown | Crown Glass, Flint Glass, Water, Perspex, Diamond |

**Toolbar Row 2:**
| Control | Type | Details |
|---------|------|---------|
| Direction | Toggle button | ◀ from left / ▶ from right |
| θ₁ | Slider + input | 0°–89°, step 0.5°, default 30° |
| ▶ Play, Speed, Show | Same as Section 1 | |

### 3.2 Geometry

```
        ┌──────────────┐  ← Flat face (top)
        │              │
        │    Block     │
        │              │
        └──────────────┘
         ╲            ╱
          ╲          ╱   ← Curved face (bottom)
           ╲────────╱
                ↑
          Light enters from below
          (curved face → flat face → exits)
```

- D-shape block: **flat face on top, curved face on bottom**
- Light enters from **bottom → top** (from curved face)
- Light exits through **flat face** (top)
- Block centred horizontally, flat face at y ≈ 200, curved base at y ≈ 440

### 3.3 Light Source Rules

| Mode | Allowed? | Behaviour |
|------|----------|-----------|
| 🔦 Monochromatic | ✅ Yes | Shows **critical angle** — ray skims flat face when θ₁ = θc |
| 🌈 Visible Light | ✅ Yes | Ray tracing only — **no critical angle display** (too many colours) |
| ☀️ Sun Light | ❌ **Disabled** | Button greyed out |

### 3.4 Physics

#### Ray Tracing
1. Light enters from **below** (curved face)
2. Entry is along the **radius** of the curved face → **no refraction** at entry (normal to surface = radial direction, ray travels along radius)
3. Light travels in a straight line to the **flat face**
4. At the flat face: Snell's Law applies:
   - `sin θ₂ = n · sin θ₁` (block → air)
   - If `n · sin θ₁ > 1` → **TIR** (ray reflects back into block, exits through curved face)
5. **Critical angle:** `θc = sin⁻¹(1/n)`
   - When θ₁ = θc → ray **skims along** the flat face
   - When θ₁ < θc → normal refraction
   - When θ₁ > θc → TIR

#### Direction Control
- **"◀ from left" mode:** Light enters from left side of curved face → ray travels rightward toward flat face centre
- **"▶ from right" mode:** Light enters from right side of curved face → ray travels leftward
- Toggle button switches between the two

#### Monochromatic Mode (Critical Angle Display)
- Show **θc** value in side panel
- When θ₁ approaches θc, show status: "θ₁ = X.X° — approaching critical angle"
- When θ₁ = θc, show: "θ₁ = θc = X.X° — Critical Angle — ray skims surface"
- When θ₁ > θc, show: "θ₁ > θc — Total Internal Reflection"
- Draw reflected ray when TIR occurs

#### Visible Light Mode (Dispersion)
- Multiple colour rays, each with slightly different n
- Each colour has slightly different critical angle
- At a given θ₁, some colours may refract while others TIR
- Display ray tracing for each selected colour
- **No critical angle labels** (too cluttered)

### 3.5 Side Panel

**Current Values:**
- θ₁ (incident angle)
- θ₂ (refraction angle, or "TIR" if TIR)
- θc (critical angle, mono only)
- n (material)
- Status: Refraction / Critical / TIR

**Formula:**
- Snell's Law: `n₁ sin θ₁ = n₂ sin θ₂`
- Critical angle: `θc = sin⁻¹(n₂/n₁)`
- KaTeX rendered

**Note:**
- "Light entering along the radius of the curved face is not refracted. All refraction happens at the flat face — this is why semicircular blocks are used to measure the critical angle in IGCSE practicals."

---

## Shared Components (all 3 sections)

### Colour Data (same across all sections)

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
```

### MEDIA Array (same across all sections)

```javascript
const MEDIA = [
  { name:"Crown Glass (BK7)", A:1.5046, B:0.00420, fill:"rgba(195,205,210,0.20)", edge:"rgba(200,215,225,0.85)" },
  { name:"Flint Glass (F2)",  A:1.5809, B:0.01426, fill:"rgba(205,195,225,0.22)", edge:"rgba(210,200,235,0.85)" },
  { name:"Water",             A:1.3242, B:0.00285, fill:"rgba(25,80,160,0.30)",  edge:"rgba(90,150,220,0.85)" },
  { name:"Perspex",           A:1.4840, B:0.00285, fill:"rgba(220,215,200,0.18)", edge:"rgba(225,220,205,0.8)" },
  { name:"Diamond",           A:2.3758, B:0.01188, fill:"rgba(200,225,235,0.22)", edge:"rgba(210,235,245,0.9)" }
];
const nOf = (mi, wl) => MEDIA[mi].A + MEDIA[mi].B / Math.pow(wl/1000, 2);  // wl in nm, λ in μm
```

### Math Helpers (shared)

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
  if(k < 0) return null;  // TIR
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

### Canvas Setup

```javascript
function setupCanvas() {
  const dpr = window.devicePixelRatio || 1;
  const rect = cv.getBoundingClientRect();
  const px = Math.round(Math.max(64, (rect.width || W) * dpr));
  cv.width = px; cv.height = px;
  ctx.setTransform(px/W, 0, 0, px/W, 0, 0);
}
```

### Drawing Helpers

```javascript
function drawPath(pts, color, width, prog, opts = {}) {
  // Draw a polyline progressively (prog = 0..1)
  // If prog < 1, draw only the first fraction of the path
  // Arrowhead at end if opts.arrow !== false
  // Alpha = opts.alpha || 1
  // Shadow blur = 4-6px with same color
}
function drawNormal(pt, dir, len = 50) {
  // Dashed grey line, centered at pt, perpendicular to dir
  ctx.save();
  ctx.strokeStyle = C_GREY; ctx.setLineDash([6,5]); ctx.lineWidth = 1.2; ctx.globalAlpha = 0.6;
  ctx.beginPath();
  ctx.moveTo(pt.x - dir.x*len, pt.y - dir.y*len);
  ctx.lineTo(pt.x + dir.x*len, pt.y + dir.y*len);
  ctx.stroke();
  ctx.restore();
}
function arcAt(P, aFrom, aTo, r, color, label, labelR) {
  // Draw arc from aFrom to aTo + label at radius labelR
  // Auto-avoid label overlapping ray
}
function txt(t, x, y, color, size = 11, align = "center", weight = 600) {
  ctx.save();
  ctx.font = `${weight} ${size}px Inter, sans-serif`;
  ctx.fillStyle = color; ctx.textAlign = align; ctx.textBaseline = "middle";
  ctx.fillText(t, x, y);
  ctx.restore();
}
```

### Interactions

```javascript
// Drag near incident ray to adjust angle
cv.addEventListener("pointerdown", e => {
  const p = evtPt(e);
  cv.setPointerCapture(e.pointerId);
  // Check if near ray → start drag
  // Check if near draggable elements (thermometer, entry position dot)
  // Check if in zoom mode → pan
});

cv.addEventListener("pointermove", e => {
  // If dragging ray → update angle
  // If dragging thermometer → update position
  // If dragging entry dot → update position
  // If panning in zoom → update focus
});

cv.addEventListener("pointerup", () => { S.drag = null; });

// Double-click → toggle zoom
cv.addEventListener("dblclick", e => {
  const p = evtPt(e);
  if(!S.zoom) { S.focus = { ...p }; S.zoom = true; }
  else S.zoom = false;
  updateUI();
});

// Esc → exit zoom
window.addEventListener("keydown", e => {
  if(e.key === "Escape" && S.zoom) { S.zoom = false; updateUI(); }
  // Arrow keys → adjust θ₁
  if(!S.locked) {
    const step = e.shiftKey ? 5 : 1;
    if(e.key === "ArrowUp") { S.t1 = clamp(S.t1 + step, 0, 75); paramChanged(); }
    if(e.key === "ArrowDown") { S.t1 = clamp(S.t1 - step, 0, 75); paramChanged(); }
  }
});
```

### Animation Loop

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

### Theme System

Reuse the same theme system from `Wave_1_refraction_of_light.html`:
- 🌙 Classic Dark (default)
- ⌂ HAUS Night
- 🌃 Cyberpunk Neon
- ☀️ Classic Light
- ⌂ HAUS Day
- 🏺 Warm Clay

### Zoom

- Double-click → zoom into focus point (2.5×)
- Drag to pan when zoomed
- Esc or double-click → zoom out
- Zoom chip indicator: "🔍 2.5× — drag = pan · dbl-click/Esc = exit"

---

## File Requirements

| File | Section |
|------|---------|
| `Wave_2_dispersion.html` | Section 1: Dispersion (Prism) |
| `Wave_3_glass_blocks.html` | Section 2: Parallel Glass Blocks |
| `Wave_4_half_circular.html` | Section 3: Half Circular Block |
| `Wave_5_right_triangle.html` | Section 4: Right Triangle |
| `Wave_6_diamond.html` | Section 5: Diamond Shape |
| `Wave_7_raindrop.html` | Section 6: Water Drop → Rainbow |

**Specifications:**
- **Separate single HTML files** (DO NOT combine into one file)
- External dependencies: Google Fonts + KaTeX CDN only
- Reference layout: `Wave_1_refraction_of_light.html` (toolbar, side panel, theme system)
- Language: English
- All IGCSE Physics 0625 conventions followed
- Real refractive index values (Cauchy equation)
- **NO TIR in Prism section** (auto-prevent)
- **TIR allowed in Glass Blocks, Half Circle, Right Triangle, Diamond** (part of the physics)

### Viewport Rules (CRITICAL — FIX FROM V1)
- **The entire simulation must fit in ONE browser window** — NO vertical scrolling
- V1 had content going out of bounds (experiment was clipped off-screen)
- Layout calculation:
  - Top bar: ~40px
  - Section tabs (if any): ~40px  
  - Toolbar (2 rows): ~80px
  - Main grid: remaining viewport height
  - Side panel: 25–30% of width
  - Canvas: 70–75% of width, height = remaining viewport minus toolbar
- All content — labels, rays, controls, chips — must be **fully visible** within the Canvas
- **Test by rendering headless** and checking that every element is within bounds
- If a medium shape is too large for the Canvas, **scale it down** — never clip it

---

## Feature Checklist

### Global (shared across all simulations)
- [x] Learning Goals stated (ray tracing, frequency invariant, dispersion)
- [x] 3 Light Sources: Mono (1 pill) / Visible (multi-pill) / Sun (Prism only, continuous bands)
- [x] 7 colour swatches (circle pills, ROYGBIV)
- [x] **Ray thickness: 1.3–1.5px** (thin, distinct, not overlapping)
- [x] Standard MEDIA array with Cauchy n(λ) = A + B/λ²
- [x] Shared medium colours and n values across all files
- [x] Viewport-fit: **entire sim in ONE browser window** (no scroll)
- [x] Pen-drawing animation (Type B)
- [x] 6 themes (Classic Dark, HAUS Night, Neon, Classic Light, HAUS Day, Warm Clay)
- [x] Zoom (double-click)
- [x] Separate files per section

### Section 1: Dispersion (Prism)
- [x] Triangular prism with adjustable apex (30°–80°, default 60°)
- [x] Sun Light: all colours + IR + UV as continuous spectrum bands
- [x] Snell's Law + Cauchy dispersion — NO TIR allowed (auto-prevent)
- [x] Incidence angle 0°–75°, step 0.5°, default 45°
- [x] Ray position on prism face: draggable
- [x] 5 prism materials (Crown/Flint/Water/Perspex/Diamond)
- [x] Herschel's Thermometer: draggable, IR peak ~32°C
- [x] Side Panel: Color Spectrum Table + Formula + Summary + Herschel info

### Section 2: Parallel Glass Blocks
- [x] 1 or 2 blocks (selectable), each with independent refractive index
- [x] Light enters top → exits bottom
- [x] Normal: always at entry, mono=every interface, 2+ colours=entry only
- [x] TIR between blocks when n₁ > n₂ and angle exceeds θc
- [x] Dispersion when Visible Light with 2+ colours
- [x] Sun Light NOT available
- [x] Side Panel: Current Values + Interface Angles table + Formula

### Section 3: Half Circular Block
- [x] D-shape face up, light enters from bottom curved face
- [x] Adjustable direction (left/right)
- [x] Incident angle 0°–89°, step 0.5°, default 30°
- [x] Light enters along radius → no refraction at curved face
- [x] Monochromatic: shows critical angle + TIR
- [x] Visible Light: ray tracing only (dispersion)
- [x] Sun Light NOT available
- [x] Side Panel: Current Values + Formula + IGCSE note

### Section 4: Right Triangle
- [x] Right-angled triangular prism (45°–45°–90° or adjustable)
- [x] Light enters one face → reflects/refracts → exits another face
- [x] Common IGCSE exam shape for ray tracing
- [x] Monochromatic: full Snell's Law + TIR
- [x] Visible Light: dispersion
- [x] Sun Light NOT available

### Section 5: Diamond Shape
- [x] Rhombus/diamond cross-section
- [x] Light enters top face → multiple internal reflections → exits
- [x] High dispersion (Flint Glass recommended)
- [x] Monochromatic: ray tracing + TIR
- [x] Visible Light: dispersion

### Section 6: Water Drop → Rainbow
- [x] Circular/spherical water drop
- [x] Light enters → refracts → reflects inside → exits
- [x] White light → **rainbow** effect (dispersion + reflection)
- [x] Simple ray tracing (not full Mie scattering)
- [x] Sun Light option TBD