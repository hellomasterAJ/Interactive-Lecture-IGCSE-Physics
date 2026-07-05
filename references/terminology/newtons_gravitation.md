---
title: Newton's Law of Universal Gravitation
field: Mechanics / Gravitation
type: terminology
version: 1
tags: [gravity, gravitation, universal gravitation, g, inverse square law, orbital motion]
related_lectures: [topic15_forces]
related_terminology: [newtons_laws, dynamics, terminal_velocity]
aliases: [Law of Gravitation, Universal Gravitation, Inverse Square Law]
---

# Newton's Law of Universal Gravitation

## 📖 Etymology

**Gravitation** comes from the Latin **"gravitas"** meaning "weight, heaviness" — from **"gravis"** (heavy, serious). The same root gives us **gravity**, **grave** (serious), **grief**, and **gravamen** (the burden of a complaint).

Newton's Law of Universal Gravitation was the **first physical law to be truly "universal"** — it applied to objects on Earth AND to the planets and stars. Before Newton, earthly and celestial phenomena were thought to obey **different rules**.

---

## 📜 Historical Timeline

### 🏛️ Ancient Ideas

- **Aristotle** (350 BCE): heavy objects fall toward the centre of the Earth because that is their "natural place." The heavens were made of a different substance (aether) with different rules
- **Copernicus** (1543): placed the Sun at the centre, but had no mechanism for why planets orbit — he simply assumed circular motion

### 🔭 Before Newton — Kepler's Laws (1609–1619)

**Johannes Kepler** (1571–1630) analysed Tycho Brahe's precise planetary observations and derived **three laws of planetary motion**:

| Law | Statement |
|-----|-----------|
| **1st** (1609) | Planets orbit the Sun in **ellipses**, with the Sun at one focus |
| **2nd** (1609) | A planet sweeps out **equal areas in equal times** |
| **3rd** (1619) | $T^2 \propto r^3$ — the square of the orbital period is proportional to the cube of the semi-major axis |

Kepler described *how* planets move, but had no explanation for *why*. That required Newton.

### 🍎 Newton's Apple (c. 1666)

The famous (possibly apocryphal) story: Newton saw an apple fall and wondered if the same force that pulled the apple to Earth extended to the Moon. He calculated:

- Acceleration of the apple at Earth's surface: $g = 9.8 \, \text{m/s}^2$
- Acceleration of the Moon toward Earth: $a_m = \frac{v^2}{r} \approx 0.0027 \, \text{m/s}^2$
- Ratio: $g / a_m \approx 3600$
- Distance ratio: $(R_{\text{Earth}} / r_{\text{Moon}})^2 = (6370 / 384{,}400)^2 \approx 1/3600$

The force follows an **inverse square law**! This was the breakthrough moment.

### 🧠 Newton's Published Work (1687)

In the *Principia*, Newton published the Law of Universal Gravitation:

> *"Every particle of matter in the universe attracts every other particle with a force that is directly proportional to the product of their masses and inversely proportional to the square of the distance between them."*

He used this law to:
- Derive **Kepler's Laws** from first principles
- Explain **tides** as the Moon's gravitational pull
- Predict the **precession of the equinoxes**
- Calculate the **mass of the Earth** and other planets

### ⚡ 18th–19th Century — Triumphs

| Discovery | Scientist | Date | How it Confirmed Newton |
|-----------|-----------|------|------------------------|
| **Prediction of Neptune** | Le Verrier & Adams | 1846 | Anomalies in Uranus's orbit predicted Neptune's existence and position |
| **Cavendish experiment** | Henry Cavendish | 1798 | Measured $G$ directly using a torsion balance — "weighing the Earth" |
| **Orbit of Halley's Comet** | Edmond Halley | 1705 | Showed comets obey the same gravitational laws as planets |

### 🌌 20th Century — Einstein's Refinement (1915)

Einstein's **General Theory of Relativity** showed that Newton's Law is an **approximation** for weak gravitational fields:

| Situation | Newton | Einstein (GR) |
|-----------|--------|--------------|
| Force carrier | Instantaneous action-at-a-distance | Curved spacetime, gravitational waves |
| Speed of propagation | Infinite (instantaneous) | Speed of light ($c$) |
| Mercury's orbit | Slight discrepancy (43 arcseconds/century) | Perfectly explained |
| Strong gravity | Inaccurate | Accurate (black holes, neutron stars) |

Despite this, Newton's Law is **still used** for most practical calculations (satellite orbits, projectile motion, planetary dynamics) because it is simpler and accurate enough for weak fields.

---

## 📐 The Law

### Mathematical Statement

$$ \boxed{F = G\frac{m_1 m_2}{r^2}} $$

| Symbol | Meaning | Value / Unit |
|--------|---------|--------------|
| $F$ | Gravitational force between two masses | $\text{N}$ |
| $G$ | Universal gravitational constant | $6.674 \times 10^{-11} \, \text{N·m}^2/\text{kg}^2$ |
| $m_1, m_2$ | Masses of the two objects | $\text{kg}$ |
| $r$ | Distance between the **centres** of the masses | $\text{m}$ |

### Key Properties

| Property | Meaning |
|----------|---------|
| **Inverse square** | Double $r$ → force becomes $\frac{1}{4}$ |
| **Always attractive** | Gravity only pulls — it never repels |
| **Universal** | Every mass attracts every other mass |
| **Acts through any medium** | No shielding — gravity passes through everything |
| **Weakest of the four forces** | $10^{38}$ times weaker than the strong nuclear force |

### Gravitational Field Strength ($g$)

The gravitational field strength at a distance $r$ from a mass $M$ is:

$$ \boxed{g = \frac{F}{m} = \frac{GM}{r^2}} $$

At Earth's surface: $g = 9.81 \, \text{N/kg} = 9.81 \, \text{m/s}^2$

| Location | $g$ (m/s²) |
|----------|:---------:|
| Earth's surface | 9.81 |
| Moon's surface | 1.62 |
| Mars' surface | 3.72 |
| Jupiter's surface | 24.8 |
| International Space Station (400 km altitude) | 8.7 |
| Deep space | ≈ 0 |

> 💡 **Common question**: Why do astronauts on the ISS float if $g = 8.7 \, \text{m/s}^2$? Because they are in **free fall** — the ISS and astronauts are both falling toward Earth at the same rate (orbital motion). They are not "weightless" due to zero gravity — they are weightless because they are falling.

### Weight vs Mass

| Quantity | Definition | Depends on $g$? | Unit |
|----------|-----------|:---:|:---:|
| **Mass** ($m$) | Amount of matter | ❌ No | kg |
| **Weight** ($W = mg$) | Gravitational force on an object | ✅ Yes | N |

Mass is the same everywhere. Weight changes with location.

---

## 🧪 Key Experiments

### 1. Cavendish Experiment (1798) — Measuring $G$

Henry Cavendish used a **torsion balance** — a horizontal rod with two lead balls suspended by a thin fibre. Large lead balls were placed near the small balls. The tiny gravitational attraction twisted the fibre. By measuring the twist angle, Cavendish calculated $G$ to within 1% of the modern value.

> *Cavendish's experiment was called "weighing the Earth" because knowing $G$ allowed the mass of the Earth to be calculated.*

### 2. Orbital Motion — Kepler's Third Law Verified

From Newton's Law and circular motion:

$$ F = \frac{GMm}{r^2} = \frac{mv^2}{r} = m\omega^2 r = \frac{4\pi^2 mr}{T^2} $$

This gives:

$$ T^2 = \frac{4\pi^2}{GM}r^3 $$

This is **Kepler's Third Law** — now derived from first principles. Measuring orbital periods and distances of moons or planets allows us to calculate the mass of the central body.

### 3. The Falling Apple (Demonstration)
A simple classroom demonstration: an apple and a feather are dropped in a vacuum chamber. **Both fall at the same rate** ($g$), confirming that gravitational acceleration is independent of mass — exactly as Newton's Law predicts because $F \propto m$ cancels in $a = F/m$.

---

## 🌍 Real-World Applications

| Application | How Gravitation Matters |
|------------|------------------------|
| 🛰️ **Satellites in orbit** | $GMm/r^2 = mv^2/r$ determines orbital speed and period. Geostationary orbits require $r \approx 42{,}000$ km from Earth's centre |
| 🚀 **Escape velocity** | Minimum speed to escape Earth's gravity: $v_{\text{esc}} = \sqrt{2GM/R} \approx 11.2 \, \text{km/s}$ |
| 🌊 **Tides** | The Moon's gravity pulls on Earth's oceans, creating tidal bulges. The Sun also contributes |
| 🌍 **Weight variation** | Your weight changes slightly depending on latitude (Earth is not a perfect sphere) and altitude |
| 🪐 **Planetary exploration** | Gravitational **slingshots** use a planet's gravity to accelerate spacecraft |
| 🕳️ **Black holes** | When a mass is compressed below its Schwarzschild radius ($r_s = 2GM/c^2$), gravity is so strong that not even light can escape |

---

## 💡 Common Misconceptions

| Misconception | Truth |
|--------------|-------|
| "There is no gravity in space" | ❌ Gravity exists everywhere. Astronauts on the ISS float because they are in **free fall**, not because gravity is absent ($g \approx 8.7 \, \text{m/s}^2$ at the ISS) |
| "The Earth's gravity pulls more on heavier objects" | ✅ True — but heavier objects also have more **inertia**. The two effects cancel, giving all objects the same acceleration $g$ |
| "Gravity is caused by the Earth's atmosphere" | ❌ Gravity is a fundamental force of nature, independent of the atmosphere. A vacuum chamber doesn't remove gravity |
| "The Moon has no gravity" | ❌ The Moon's gravity is $g = 1.62 \, \text{m/s}^2$ — about 1/6 of Earth's |
| "Gravity is a force that pulls instantly at any distance" | ❌ According to General Relativity, changes in gravity propagate at the **speed of light** as gravitational waves |
| "$G$ and $g$ are the same thing" | ❌ $G$ is the **universal constant** ($6.67 \times 10^{-11}$). $g$ is the **gravitational field strength** at a specific location (≈ 9.81 at Earth's surface) |

---

## 📊 Gravitational Force Comparison Table

| Pair of Objects | Masses | Distance | Force (N) |
|----------------|--------|----------|:---------:|
| You and Earth | 70 kg × $6.0 \times 10^{24}$ kg | $6.37 \times 10^6$ m | ≈ 690 N (your weight) |
| Earth and Moon | $6.0 \times 10^{24} \times 7.3 \times 10^{22}$ kg | $3.8 \times 10^8$ m | $2.0 \times 10^{20}$ N |
| Two 1 kg masses | 1 kg × 1 kg | 1 m apart | $6.67 \times 10^{-11}$ N (tiny!) |
| Sun and Earth | $2.0 \times 10^{30} \times 6.0 \times 10^{24}$ kg | $1.5 \times 10^{11}$ m | $3.5 \times 10^{22}$ N |

---

## 🔗 Related Terminology & Lectures

- [Newton's Laws of Motion (Complete)](newtons_laws.md) — the broader framework
- [Terminology: Dynamics](dynamics.md) — forces and motion
- [Terminology: Terminal Velocity](terminal_velocity.md) — free fall under gravity with air resistance
- [Topic 1.5 Forces](../lectures/topic15_forces.md) — IGCSE lecture on forces, weight, and gravity

---

*This reference is part of the Terminology Archive. Last updated: July 2026.*