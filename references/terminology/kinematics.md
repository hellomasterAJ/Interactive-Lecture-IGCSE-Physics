---
title: Kinematics
field: Mechanics
type: terminology
version: 1
tags: [motion, velocity, acceleration, displacement]
related_lectures: [topic12_motion]
---

# Kinematics

## 📖 Etymology

**Kinematics** derives from the Greek word **κίνημα** (*kinēma* — "motion, movement"), from **κινεῖν** (*kinein* — "to move"). The term was introduced into physics by:

> **André-Marie Ampère** (1775–1836) — in his *Essai sur la philosophie des sciences* (1834), Ampère divided mechanics into two branches:
> - **Kinematics** — the *geometry* of motion (description without regard to forces)
> - **Dynamics** — the study of forces and their effect on motion

The adjective **kinematic** first appeared in English around the 1840s.

---

## 📜 Historical Timeline

### 🏛️ Antiquity — Aristotle (384–322 BCE)

Aristotle classified motion into two types:
- **Natural motion** — objects seeking their "natural place" (e.g. a stone falling downward)
- **Violent motion** — motion caused by an external push or pull

He believed heavier objects fall faster, and that a moving object requires a continuous force to keep moving — both incorrect, but dominant for ~2,000 years.

### 🔭 The Breakthrough — Galileo Galilei (1564–1642)

Galileo is considered the **father of kinematics**. His key contributions:

- **Inclined plane experiments** (~1604): rolled balls down grooves in a tilted wooden plank, using a water clock to measure time. He discovered:
  - Distance ∝ time² ($s \propto t^2$) for uniform acceleration
  - In the absence of air resistance, **all objects fall at the same rate** regardless of mass

- **Law of falling bodies**: $v \propto t$ and $s \propto t^2$ for free fall

- **Concept of acceleration**: Galileo was the first to treat acceleration as a quantitative variable — the rate of change of velocity.

> 🧪 *Key experiment*: The inclined plane "diluted" gravity, allowing Galileo to measure times accurately with primitive water clocks. This was a masterful example of experimental design.

### 🧠 The Formalisation — Isaac Newton (1643–1727)

Newton published **Philosophiæ Naturalis Principia Mathematica** (1687), where he:
- Formalised the three laws of motion
- Defined **velocity** and **acceleration** as vector quantities
- Showed that kinematics under constant acceleration leads to the **SUVAT equations**
- Unified terrestrial and celestial motion under the same kinematic framework

### ⚙️ The Modern Era (18th–19th Century)

- **Leonhard Euler** (1707–1783): developed the mathematical formalism of kinematics, introducing the concept of **angular velocity** and rigid-body kinematics
- **Jean le Rond d'Alembert** (1717–1783): formulated **d'Alembert's principle**, linking kinematics to dynamics
- **André-Marie Ampère** (1834): officially coined "kinematics" as a distinct branch of mechanics

### 🔬 20th Century & Beyond

- **Albert Einstein** (1905): Special Relativity redefined the kinematics of objects at speeds approaching $c$, showing that time and space are relative
- **Quantum kinematics**: at the atomic scale, position and momentum obey the **Heisenberg uncertainty principle** — a fundamentally different kinematic framework

---

## 📐 Modern Definition

### Kinematics

> **Kinematics** is the branch of classical mechanics that describes the motion of points, bodies, and systems of bodies **without considering the forces that cause them**.

The fundamental quantities of kinematics are:

| Quantity | Symbol | Unit | Scalar/Vector | Definition |
|----------|--------|------|---------------|------------|
| Position | $x$ | m | — | Location relative to a reference point |
| Displacement | $s$ | m | ✅ Vector | Change in position in a given direction |
| Distance | $d$ | m | ❌ Scalar | Total path length travelled |
| Speed | $v$ | m/s | ❌ Scalar | Rate of change of distance |
| Velocity | $v$ | m/s | ✅ Vector | Rate of change of displacement |
| Acceleration | $a$ | m/s² | ✅ Vector | Rate of change of velocity |
| Time | $t$ | s | ❌ Scalar | Duration of motion |

### The SUVAT Equations (for constant acceleration)

$$ v = u + at $$
$$ s = ut + \frac{1}{2}at^2 $$
$$ s = \frac{1}{2}(u + v)t $$
$$ v^2 = u^2 + 2as $$

---

## 🧪 Key Experiments in Kinematics

### 1. Galileo's Inclined Plane (~1604)
Measured distances and times for balls rolling down a slope. Established $s \propto t^2$ for uniformly accelerated motion.

### 2. Atwood Machine (1784, George Atwood)
Two masses connected by a string over a pulley. Slows down free fall so acceleration can be measured directly. Used to verify Newton's laws of motion.

### 3. Modern Photogate Experiments
Using light gates and electronic timers to measure instantaneous velocity and acceleration with high precision — standard in school laboratories today.

### 4. High-Speed Video Analysis
Modern smartphones and tracking software (e.g. Tracker, Logger Pro) record motion frame-by-frame to plot displacement–time and velocity–time graphs directly.

---

## 💡 Common Misconceptions

| Misconception | Truth |
|--------------|-------|
| "If velocity is zero, acceleration must be zero" | ❌ No — an object at the top of its trajectory (e.g. thrown upward) has $v=0$ but $a = g \neq 0$ |
| "Acceleration always means speeding up" | ❌ Acceleration can be negative (deceleration) — slowing down is also acceleration |
| "Heavier objects fall faster" | ❌ In the absence of air resistance, all objects fall at $g = 9.8\,\text{m/s}^2$ regardless of mass |
| "Distance and displacement are the same thing" | ❌ Distance is scalar (total path), displacement is vector (straight line from start to finish) |
| "A constant speed means zero acceleration" | ✅ Correct — but only if direction also doesn't change. Circular motion at constant speed still has centripetal acceleration |

---

## 🔗 Related Lectures

- [Topic 1.2 Motion](../lectures/topic12_motion.md) — IGCSE Physics lecture on kinematics
- [Free Fall](../graphs/kinematics_freefall_v1.html) — Interactive graph
- [V-T Graphs](../graphs/kinematics_vt_graph_v1.html) — Velocity–time graph simulations

---

*This reference is part of the Terminology Archive. Last updated: July 2026.*