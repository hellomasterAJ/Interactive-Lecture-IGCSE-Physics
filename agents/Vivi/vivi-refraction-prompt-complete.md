# Prompt: Refraction of Light — 2D Interactive Simulation

> **Author:** Vivi (Science Content Agent, HAUS Academy)
> **Date:** 2026-07-11
> **Level:** IGCSE Physics 0625
> **UI Language:** English only
> **Target:** standalone HTML+Canvas file, single-file, no external deps (except Google Fonts)

---

## INSTRUCTION

You must create a **2D Physics Simulation** — Refraction of Light — as a **single standalone HTML file** (HTML + CSS + JS all in one file). It demonstrates Snell's Law and Total Internal Reflection at the boundary between two optical media.

### Reference layout for the UI structure
Study this file for the toolbar, top bar, main-grid layout (canvas left + side panel right), mode tabs, theme selector, badges, cards, and general UI patterns:

📄 `~/InteractiveLecture/simulations/Mathematics_1_vector_addition.html`

Adapt the same structural approach (top bar → toolbar 2 rows → main grid) but with refraction-specific content.

---

## 1. Scope

| What's included | What's NOT included |
|----------------|-------------------|
| ✅ Refraction at boundary between 2 media | ❌ Dispersion / Prism (separate sim) |
| ✅ Snell's Law via refractive index n | ❌ Lens (convex/concave) (separate sim) |
| ✅ TIR + Critical angle (Case 2 only) | ❌ Real & Apparent depth |
| ✅ Case 1: Fast→Slow (e.g. air→water) | ❌ Applied examples (fibre optics, mirage) |
| ✅ Case 2: Slow→Fast (e.g. water→air) | |

**IGCSE convention:** n of air = 1 always. The formula is written as:
- Case 1 (Fast→Slow): `n = sin i / sin r`
- Case 2 (Slow→Fast): `n = sin r / sin i`

---

## 2. Physics Logic

### 2.1 Six Media

| # | Medium | n (IGCSE) | Fill Color |
|---|--------|-----------|------------|
| 1 | Air | 1.00 | `#000000` (black — because white rays) |
| 2 | Water | 1.33 | `rgba(25, 80, 160, 0.38)` Deep blue |
| 3 | Ice | 1.31 | `rgba(180, 215, 235, 0.3)` Frost blue |
| 4 | Perspex | 1.49 | `rgba(220, 215, 200, 0.22)` Warm clear |
| 5 | Crown Glass | 1.52 | `rgba(195, 205, 210, 0.22)` Neutral glass |
| 6 | Diamond | 2.42 | `rgba(200, 210, 220, 0.18)` Cool white |

- **n of air = 1** (IGCSE standard)
- User selects 2 media from dropdowns (Medium 1 Top, Medium 2 Bottom)
- When n₁ = n₂ → straight ray (no refraction), allowed as-is

### 2.2 Case Direction (auto-calculated)

| Condition | Case | Light travels | Ray bends | TIR? |
|-----------|------|--------------|-----------|------|
| n₁ < n₂ | **Fast→Slow** | Top → Bottom | **toward** normal (θ₂ < θ₁) | ❌ No |
| n₁ > n₂ | **Slow→Fast** | Bottom → Top | **away** from normal (θ₂ > θ₁) | ✅ Yes |

### 2.3 Snell's Law

```
n₁ · sin θ₁ = n₂ · sin θ₂
```

**IGCSE shorthand:**
- Case 1 (Fast→Slow): `n = sin i / sin r`
- Case 2 (Slow→Fast): `n = sin r / sin i`

### 2.4 Critical Angle & TIR (Case 2 only)

```
θc = sin⁻¹(n₂ / n₁)   where n₁ > n₂
```

Three conditions:
1. **Normal** — θ₁ < θc → refraction as usual
2. **Critical Angle** — θ₁ ≈ θc → θ₂ = 90° (ray skims boundary)
3. **TIR** — θ₁ > θc → **no refracted ray**, full reflection

---

## 3. Layout

### 3.1 Overall Structure

```
┌────────────────────────────────────────────────────┐
│  Top Bar: Title · Mode Tabs · Theme Select · Brand│
├────────────────────────────────────────────────────┤
│  Toolbar Row 1: Medium 1│Medium 2│Direction        │
│  Toolbar Row 2: Angle│Play│Toggles                │
├────────────────────────┬───────────────────────────┤
│                        │                           │
│   Canvas (Ray Tracing) │  Side Panel (~1/4 width)  │
│   ~3/4 width           │  Changes per mode:        │
│   Square aspect ratio  │  - Simulate: Readouts +   │
│                        │    Formula Panel          │
│   Medium 1 ▓▓▓▓▓      │  - Practice: Inputs +     │
│   ─── Boundary ─────  │    Worked Solution        │
│   Medium 2 ░░░░░      │  - Quiz: Questions +      │
│                        │    Results Table          │
└────────────────────────┴───────────────────────────┘
```

### 3.2 Top Bar
- Title: `🌗 Refraction of Light`
- Mode tabs: **Simulate** | **Practice** | **Quiz**
- Theme selector dropdown (same 11 themes as Vector Addition)
- HAUS brand logo (yellow rounded rect, top-right)

### 3.3 Toolbar (Fixed 2 Rows — zero layout shift)

**Row 1:**
- Medium 1 dropdown (6 media)
- Medium 2 dropdown (6 media)
- Direction badge (auto: "Fast→Slow" / "Slow→Fast" / "n₁=n₂ (straight)")

**Row 2:**
- Incident Angle slider (0°–89°) + numeric input
- Play/Pause button ▶/⏸
- Toggles:
  - `Show Reflected` (OFF default, auto-ON in TIR)
  - `Show Wavefront` (OFF default)
  - `Show Angles` (ON default)

### 3.4 Main Grid
```css
.main-grid {
  display: grid;
  grid-template-columns: 3fr 1fr;
  gap: 12px;
}
```

### 3.5 Canvas Area
- **Responsive** — fills ~75% of viewport width, **square aspect ratio**
- **Boundary line** at exact center (50:50 — Top medium 50%, Bottom medium 50%)
- Chip overlays: status, zoom hint

### 3.6 Side Panel (~25%)

Switches content entirely when mode changes:

**Simulate Mode:** Readout badges + Formula Panel
- Badges: `θ₁`, `θ₂`, `n₁`, `n₂`, `θc`, `Status`
- Formula panel: Snell's Law + live substitution

**Practice Mode:** Practice inputs + Worked Solution
- Input fields for answer, Check button, Score
- On Check: shows full step-by-step + summary

**Quiz Mode:** 5 questions, Submit, Stars, Results table

---

## 4. Canvas Rendering

### 4.1 Medium Display
- Top half (50%): Medium 1 background fill
- Bottom half (50%): Medium 2 background fill
- Boundary line: solid horizontal, `#8b949e`, 1.5px
- Normal line: dashed vertical at boundary midpoint, `#8b949e`, opacity 0.5

### 4.2 Ray System

| Element | Color | Default | Notes |
|---------|-------|---------|-------|
| Incident Ray | Gold `#e3b341` | ON | Draggable; adjustable via slider/input |
| Refracted Ray | Blue `#58a6ff` | ON | Calculated from Snell's Law |
| Reflected Ray | Orange `#f0883e` | OFF toggle | Available in ALL cases; auto-ON in TIR |
| Reflected Angle θᵣ | Orange | ON with ray | Arc + label `θᵣ = XX.X°` |
| Normal Line | Grey `#8b949e` dashed | ON | Vertical at boundary midpoint |
| Boundary Line | Grey `#8b949e` solid | ON | Horizontal at center |

**TIR special rules:**
- No refracted ray shown
- Reflected ray auto-shown (overrides toggle)
- Reflected angle = incident angle (θᵣ = θ₁)
- Ray thickness/color unchanged

### 4.3 Ray Drawing
- Each ray is a **thick line** (2.5–3.5px) with an **arrowhead** at the tip
- Arrowhead: small filled triangle, ~12px length
- Incident ray: from canvas edge → boundary point (midpoint)
- Refracted ray: from boundary point → opposite canvas edge
- Reflected ray: from boundary point → same-side canvas edge (shown above boundary)

### 4.4 Angle Arcs & Labels
- Draw small circular arcs between ray and normal
- Labels: `θ₁ = XX.X°`, `θ₂ = XX.X°`, `θᵣ = XX.X°` (if reflected ray shown)
- Arc radius: ~25px
- **Labels must NOT overlap rays** — place outward from the arc
- Font: `11px Inter, sans-serif`, color matching the ray

### 4.5 Critical Angle Status (displayed on canvas corner or in side panel)
- `θ₁ < θc  —  Normal Refraction`
- `θ₁ = θc  —  Critical Angle`
- `θ₁ > θc  —  Total Internal Reflection`

### 4.6 Animation: Line draws gradually (Type B)
- On Play: the ray path draws progressively from source → boundary → destination
- On parameter change: reset animation immediately
- requestAnimationFrame-based, dt constant
- Speed adjustable via slider
- Press Play/Pause to toggle

### 4.7 Wavefront (Toggle — OFF by default)
- Shows wavelength change + bending direction simultaneously
- **Animated** — wavefront lines move along the ray path
- Play/Pause control (same as ray animation, or linked toggle)
- **Auto-adjust density** based on wavelength (λ₁/λ₂ = n₂/n₁)
- Wavefront spacing = λ in each medium: closer in slower (higher n) medium
- Drawn as lines perpendicular to ray direction
- Color: `rgba(56, 178, 255, 0.3)`

---

## 5. Interaction

### 5.1 Adjust Incident Ray
**Mouse Drag:** Click near the tip of the incident ray → drag to rotate. The angle updates in real-time (0°–89°).

```javascript
// Pointer events (works on touch too)
cv.addEventListener("pointerdown", e => {
  if (S.locked) return;
  // hit test: distance from click to incident ray tip < 20px
  if (hitTip) { dragging = true; }
});
cv.addEventListener("pointermove", e => {
  if (!dragging) return;
  // calculate new angle from boundary midpoint
  S.incidentAngle = clamp(Math.atan2(...), 0, 89);
  updateSimulation();
});
```

**Slider/Input:** Range 0°–89°, step 0.5°

**Keyboard:**
- ↑/↓ = ±1°, Shift+↑/↓ = ±5°
- Esc = exit zoom

### 5.2 Double-click Zoom
- Double-click empty canvas → zoom into boundary area (2.5×)
- Esc → exit zoom
- While zoomed: drag empty space = pan view

---

## 6. Three Modes

### 6.1 Simulate Mode
- **locked = false, reveal = true**
- Free exploration: change media, adjust angle, toggle rays/wavefront
- All values visible instantly

### 6.2 Practice Mode
- **locked = true, reveal = false → true on Check**
- Randomize medium pair + incident angle
- Student enters: `θ₂ = ?` (or asks for n, or θc depending on case)
- ✓ Check → reveals full worked solution:

```
Step 1: n₁ sin θ₁ = n₂ sin θ₂
Step 2: 1.00 × sin(30.0°) = 1.33 × sin(θ₂)
Step 3: sin(θ₂) = 0.500 / 1.33 = 0.376
Step 4: θ₂ = sin⁻¹(0.376) = 22.1°
→ θ₂ = 22.1°  (your answer: 23.0°, error: 0.9°)
```

- Tolerance: |student - correct| < 0.5° → ✓

### 6.3 Quiz Mode
- **locked = true, reveal = false**
- 5 pre-generated questions (randomized media + angles)
- No hints during quiz
- Submit → star rating: 5/5 → ★★★, 4/5 → ★★, 3/5 → ★
- Results table: `{Q#, target, your answer, correct?}`
- Step-by-step solutions revealed after submission

---

## 7. State Object

```javascript
const S = {
  // Media
  medium1: { name: 'Air', n: 1.00, fill: '#000000' },
  medium2: { name: 'Water', n: 1.33, fill: 'rgba(25,80,160,0.38)' },

  // Angles (degrees)
  incidentAngle: 30.0,     // θ₁, range 0–89
  refractedAngle: 0,        // θ₂, calculated
  criticalAngle: 0,         // θc, calculated (Case 2 only)

  // Toggles
  showReflected: false,
  showWavefront: false,
  showAngles: true,

  // Animation
  animating: false,
  animProgress: 0,          // 0→1
  animSpeed: 1.0,

  // Mode
  mode: 'simulate',         // 'simulate' | 'practice' | 'quiz'
  locked: false,
  reveal: true,

  // Zoom
  zoom: false,
};
```

---

## 8. HAUS Design Tokens

```css
:root {
  --bg: #0d1117; --card: #161b22; --card2: #1c2430; --border: #30363d;
  --text: #e6edf3; --dim: #8b949e; --text-muted: #64748b;
  --accent: #e3b341;  /* gold — incident ray, primary values */
  --blue: #58a6ff;    /* refracted ray */
  --orange: #f0883e;  /* reflected ray */
  --green: #3fb950;
  --red: #f85149;
  --amber: #fbbf24;
}
```

### 11 Themes
Same as Vector Addition: `dark` (default), `hausnight`, `vintage`, `neon`, `cosmic`, `onedark`, `light`, `haus`, `clay`, `sage`, `mist`

---

## 9. Validation Checklist

- [ ] Snell's Law round-trip: θ₁ → θ₂ → θ₁ (exhaustive, all media pairs)
- [ ] θ₁ = 0° → straight ray, no bending
- [ ] θ₁ = 89° → near-grazing incidence
- [ ] Case 1 (Fast→Slow): bends toward normal, θ₂ < θ₁, no TIR
- [ ] Case 2 (Slow→Fast): bends away from normal, θ₂ > θ₁
- [ ] TIR threshold: θ₁ = θc → θ₂ = 90° exactly
- [ ] TIR region: θ₁ > θc → no refracted ray, reflected ray auto-ON
- [ ] n₁ = n₂ (same medium) → straight ray
- [ ] Case direction swaps correctly when media swapped
- [ ] Animation resets on any parameter change
- [ ] Wavefront density auto-adjusts with n
- [ ] Angle labels don't overlap rays
- [ ] Reflected ray available in ALL cases (not just TIR)
- [ ] Screenshot every mode + every condition

---

## 10. File

Save to:
```
~/InteractiveLecture/simulations/Wave_1_refraction_of_light.html
```

Commit message: `feat: add refraction of light simulation (Snell's Law + TIR)`