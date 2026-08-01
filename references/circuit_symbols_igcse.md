# Circuit Symbols Reference — IGCSE Physics 0625 (UK / BS 3939 / IEC 60617)
## For HAUS Academy Circuit Lab Simulation

> **Source:** Cambridge IGCSE Physics 0625 Syllabus (2026–2028), Appendix: Electrical Symbols
> **Standard:** British Standard BS 3939 / IEC 60617 (NOT US ANSI)
> **Key UK vs US difference:** UK uses **rectangle** for resistor; US uses **zigzag**

---

## 1. Power Sources

| # | Symbol | Description | UK/IGCSE Shape | Notes |
|:-:|--------|-------------|----------------|-------|
| 1 | **Cell** | ![cell](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Cell_symbol.svg/40px-Cell_symbol.svg.png) | Long thin line (+) + short thick line (−) | Single cell = 1.5 V |
| 2 | **Battery of Cells** | ![battery](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Battery_symbol.svg/60px-Battery_symbol.svg.png) | Multiple cell symbols stacked | Represents multiple cells |
| 3 | **DC Power Supply** | `+ —○— −` | Circle with + and − terminals | Regulated DC supply |
| 4 | **AC Power Supply** | `○ ~` | Circle with sine wave (~) inside | Mains supply |
| 5 | **Earth / Ground** | `─ ─ ─` | Descending horizontal lines: `─ ┬ ┴ ┴` | Protective earth |

---

## 2. Output / Load Devices

| # | Symbol | Description | UK/IGCSE Shape | Notes |
|:-:|--------|-------------|----------------|-------|
| 6 | **Lamp (Bulb)** | ![lamp](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Lamp_symbol.svg/40px-Lamp_symbol.svg.png) | **Circle with × (cross) inside** | ⚠️ UK = X inside circle. US = loop (filament) inside circle |
| 7 | **Fixed Resistor** | `—[ ]—` | **Rectangle** | ⚠️ **KEY UK vs US difference:** UK = rectangle, US = zigzag (`—\/\/\/—`) |
| 8 | **Variable Resistor** | `—[✓]—` | Rectangle with **arrow diagonally through** | Rheostat or potentiometer |
| 9 | **Heater** | `—[ ]—` | Rectangle (same as resistor) | Heating element |
| 10 | **Fuse** | `—[ ]—` | Rectangle with line through | Or small rectangle |
| 11 | **Motor** | `○ M` | Circle with **M** inside | Converts electrical → kinetic |
| 12 | **Generator** | `○ G` | Circle with **G** inside | Converts kinetic → electrical |
| 13 | **Bell** | `○ M` or bell shape | Circle with **M** or bell symbol | Electric bell |
| 14 | **Potential Divider** | `—[†]—` | Rectangle with **arrow pointing to middle** | Also called potentiometer |

---

## 3. Input / Control / Sensor Devices

| # | Symbol | Description | UK/IGCSE Shape | Notes |
|:-:|--------|-------------|----------------|-------|
| 15 | **Switch (open)** | `—o / o—` | Break in line with a lever | No current flows |
| 16 | **Switch (closed)** | `—o/ o—` | Lever making contact | Current flows |
| 17 | **Diode** | `—▶|—` | **Triangle** pointing to a **vertical line** | Allows current ONE direction only |
| 18 | **Light-Emitting Diode (LED)** | `—▶|— ↖ ↗` | Diode symbol + **two outward arrows** | Emits light when forward biased |
| 19 | **Thermistor** | `—[—]—` | Rectangle with **diagonal line through** | R decreases as T increases (NTC) |
| 20 | **Light-Dependent Resistor (LDR)** | `—[ ]— ↖ ↗` | Rectangle with **two arrows pointing at it** | R decreases as light increases |
| 21 | **Relay Coil** | `—□□□—` | Coil / solenoid symbol | Electromagnetic switch |
| 22 | **Magnetising Coil** | `—□□□—` | Coil / solenoid symbol | For electromagnets |

---

## 4. Measuring Instruments

| # | Symbol | Description | UK/IGCSE Shape | Notes |
|:-:|--------|-------------|----------------|-------|
| 23 | **Ammeter** | `○ A` | Circle with **A** inside | Connected in **series** |
| 24 | **Voltmeter** | `○ V` | Circle with **V** inside | Connected in **parallel** |
| 25 | **Galvanometer** | `○ G` | Circle with **G** inside | Sensitive current detector |

---

## 5. Electromagnetic / Transformers

| # | Symbol | Description | UK/IGCSE Shape | Notes |
|:-:|--------|-------------|----------------|-------|
| 26 | **Transformer** | ![transformer](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Transformer_symbol.svg/60px-Transformer_symbol.svg.png) | Two **coils** separated by **vertical lines** (iron core) | No electrical connection between coils |
| 27 | **Inductor / Coil** | `—□□□—` | Series of **loops / semicircles** | Air-core or iron-core |

---

## 6. Wires and Connections

| # | Symbol | Description | UK/IGCSE Shape | Notes |
|:-:|--------|-------------|----------------|-------|
| 28 | **Wire (conductor)** | `────────` | Straight line | Connecting components |
| 29 | **Junction of Conductors** | `─┬─` | **Dot** (●) where wires cross and connect | ⚠️ UK uses **dot** at junction. Absence of dot = no connection |
| 30 | **Crossing Wires (no connection)** | `─┼─` | Crossing lines **without dot** | Wires cross but not connected |

---

## ⚠️ Critical UK vs US Differences for the Simulation

| Component | **UK/IGCSE (BS 3939 / IEC)** | **US (ANSI)** |
|-----------|------------------------------|---------------|
| Fixed Resistor | **Rectangle** `—[—]—` | **Zigzag** `—\/\/\/—` |
| Lamp | Circle with **× (cross)** | Circle with **loop (filament)** |
| Cell/Battery | Long thin + short thick | Same (no difference) |
| Junction | **Dot** (●) where wires join | Dot (same) |
| Earth | Descending lines `─ ┬ ┴ ┴` | Same |
| Variable Resistor | Rectangle + arrow through | Zigzag + arrow through |
| Fuse | Rectangle with line | Semicircle with line |

---

## SVG Drawing Specifications (for Canvas implementation)

All symbols should be drawn using Canvas 2D API. Sizes relative to a **40px × 40px** grid cell:

### Power Sources
- **Cell:** Line 5px thick (short, −) and 2px thick (long, +), separated by 4px
- **Battery:** 3 cell symbols stacked vertically
- **DC Supply:** Circle r=14px, + and − inside
- **AC Supply:** Circle r=14px, ~ wave inside
- **Earth:** 3 descending horizontal lines: 16px, 12px, 8px wide

### Resistors (UK Rectangle)
- **Fixed:** Rectangle 24px × 10px
- **Variable:** Rectangle 24px × 10px + diagonal arrow 45°
- **Thermistor:** Rectangle 24px × 10px + diagonal line
- **LDR:** Rectangle 24px × 10px + 2 arrows from top-left
- **Potential Divider:** Rectangle 24px × 10px + arrow to midpoint

### Semiconductor
- **Diode:** Triangle (base 12px, height 10px) + vertical line 16px
- **LED:** Same as diode + 2 outward arrows at 45°

### Lamp (UK)
- **Circle** r=12px + **×** (lines from top-left→bottom-right and top-right→bottom-left)

### Measuring
- **Ammeter/Voltmeter:** Circle r=14px, text A or V inside, font bold 14px

### Switches
- **Open:** Line from left to right, gap 8px, lever at 45° from right terminal
- **Closed:** Straight line across

### Junctions
- **Connected:** Filled circle r=3px at intersection
- **Not connected:** Crossing lines, no dot

---

## Colour Scheme (for Simulation)

| Component | Default Colour | Notes |
|-----------|---------------|-------|
| Wire | `#888` (grey) | Thickness 2px |
| Wire (selected) | `#e3b341` (gold) | When hovered/active |
| Component body | `#444` (dark grey) | On dark theme |
| Component fill | `#2a2a2a` | |
| Positive | `#ff4444` (red) | + terminal |
| Negative | `#4444ff` (blue) | − terminal |
| Junction dot | `#e3b341` (gold) | |
| Meter display | `#00ff88` (green) | Digital readout |
| Switch ON | `#00cc44` | |
| Switch OFF | `#cc4444` | |

---

## Component API (for JavaScript Simulation)

```javascript
// Each component type
const COMPONENTS = {
  cell:           { type: 'source',     symbol: 'cell',           label: 'Cell',          pins: 2, value: '1.5V' },
  battery:        { type: 'source',     symbol: 'battery',        label: 'Battery',       pins: 2, value: '3.0V / 4.5V / 6.0V / 9.0V' },
  dcSupply:       { type: 'source',     symbol: 'dcSupply',       label: 'DC Supply',     pins: 2, value: '0-12V' },
  acSupply:       { type: 'source',     symbol: 'acSupply',       label: 'AC Supply',     pins: 2, value: '230V' },
  earth:          { type: 'source',     symbol: 'earth',          label: 'Earth',         pins: 1 },
  switch:         { type: 'control',    symbol: 'switch',         label: 'Switch',        pins: 2, state: false },
  lamp:           { type: 'output',     symbol: 'lamp',           label: 'Lamp',          pins: 2, resistance: 10 },
  fixedResistor:  { type: 'passive',    symbol: 'fixedResistor',  label: 'Fixed Resistor', pins: 2, resistance: 100 },
  variableResistor:{type: 'passive',    symbol: 'variableResistor',label: 'Variable Resistor', pins: 3, resistance: [0, 1000] },
  fuse:           { type: 'protective', symbol: 'fuse',           label: 'Fuse',          pins: 2, rating: 5 },
  heater:         { type: 'output',     symbol: 'heater',         label: 'Heater',        pins: 2, resistance: 50 },
  motor:          { type: 'output',     symbol: 'motor',          label: 'Motor',         pins: 2, resistance: 20 },
  diode:          { type: 'semiconductor', symbol: 'diode',       label: 'Diode',         pins: 2, forwardVoltage: 0.7 },
  led:            { type: 'semiconductor', symbol: 'led',         label: 'LED',           pins: 2, forwardVoltage: 2.0 },
  thermistor:     { type: 'sensor',     symbol: 'thermistor',     label: 'Thermistor',    pins: 2, resistanceAt25C: 1000 },
  ldr:            { type: 'sensor',     symbol: 'ldr',            label: 'LDR',           pins: 2, resistanceAtBright: 100 },
  ammeter:        { type: 'meter',      symbol: 'ammeter',        label: 'Ammeter',       pins: 2, unit: 'A' },
  voltmeter:      { type: 'meter',      symbol: 'voltmeter',      label: 'Voltmeter',     pins: 2, unit: 'V' },
  transformer:    { type: 'passive',    symbol: 'transformer',    label: 'Transformer',   pins: 4, ratio: 1 },
  relay:          { type: 'control',    symbol: 'relay',          label: 'Relay Coil',    pins: 2 },
  magnetisingCoil:{ type: 'output',     symbol: 'magnetisingCoil',label: 'Magnetising Coil', pins: 2 },
  bell:           { type: 'output',     symbol: 'bell',           label: 'Electric Bell', pins: 2 },
  potentialDivider:{type: 'passive',    symbol: 'potentialDivider',label: 'Potential Divider', pins: 3 },
};
```

---

## Notes for Simulation Implementation

1. **Wire connections:** Every component has 2 pins (or 3/4 for special). Pins are connection points where wires attach.
2. **Junction dots:** Automatically shown when ≥3 wires connect at the same point.
3. **Orientation:** Components can be rotated 0° / 90° / 180° / 270°.
4. **Labels:** Each component shows its label and value when the "🏷 Labels" toggle is ON.
5. **UK Standard only:** The simulation uses ONLY UK/IGCSE symbols — no US zigzag resistors.
6. **Colour coding:** Use standard IGCSE colour conventions for wires (red = positive, black = negative/return).