---
title: Terminal Velocity
field: Mechanics
type: terminology
version: 1
tags: [terminal velocity, drag, air resistance, free fall, skydiving]
related_lectures: [topic15_forces]
related_graphs: [kinematics_terminal_velocity_v1]
---

# Terminal Velocity

## 📖 Etymology

**Terminal** comes from the Latin **"terminalis"** — "of or relating to the end, boundary, or limit" (from *terminus* "end, boundary"). **Velocity** from Latin *vēlōcitās* ("swiftness, speed").

The phrase **"terminal velocity"** first appeared in physics literature in the mid-19th century, describing the **maximum constant speed** reached by a falling object when the drag force equals the weight — the *terminal* (final, limiting) speed of the motion.

---

## 📜 Historical Timeline

### 🏛️ Aristotle (384–322 BCE)

Aristotle believed that all falling objects have a natural speed proportional to their weight and inversely proportional to the resistance of the medium. He argued that in a vacuum, objects would fall infinitely fast — a view that was later proven wrong but shows an early intuition that the medium (air, water) affects falling speed.

### 🔭 Galileo Galilei (1564–1642)

Galileo demonstrated that in the absence of air resistance, all objects fall at the same rate ($g = 9.8 \, \text{m/s}^2$). He acknowledged that air resistance creates a **limit** on falling speed, but did not mathematically model it.

### 🧠 Isaac Newton (1687)

In *Principia*, Newton analysed **fluid resistance** (drag) mathematically. He proposed that drag force is proportional to:
- The **density** of the fluid
- The **cross-sectional area** of the object
- The **square of the velocity** ($F_d \propto v^2$)

This directly leads to the concept of terminal velocity: when $F_d = mg$, acceleration stops and velocity becomes constant.

### ⚙️ George Gabriel Stokes (1851)

Stokes derived the drag force for **small spherical objects** moving through a viscous fluid at low speeds:

$$ F_d = 6\pi\eta r v $$

where $\eta$ is the fluid viscosity and $r$ is the sphere's radius. This is known as **Stokes' Law** and applies to the **laminar flow** regime (low Reynolds number).

### 🪂 20th Century — Skydiving & Aerodynamics

- **Skydiving**: terminal velocity for a human in a belly-to-earth position is ~53 m/s (190 km/h, 120 mph). Heads-down position can reach ~90 m/s (320 km/h).
- **Aerodynamics**: the study of drag reduction, streamlining, and parachute design became a practical science during the aviation boom.
- **Felix Baumgartner (2012)**: broke the sound barrier in a free fall from 39 km altitude (stratosphere). Because air density is extremely low at that height, he reached ~1,357 km/h (Mach 1.25) — **no terminal velocity** in the conventional sense until he hit denser air.

---

## 📐 Modern Definition

### Terminal Velocity

> **Terminal velocity** is the constant maximum speed reached by a falling object when the upward **drag force** equals the downward **weight**, resulting in **zero net force** and therefore **zero acceleration**.

$$ \boxed{mg = \frac{1}{2} \rho C_d A v_t^2} $$

Solving for terminal velocity:

$$ \boxed{v_t = \sqrt{\frac{2mg}{\rho C_d A}}} $$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $v_t$ | Terminal velocity | $\text{m/s}$ |
| $m$ | Mass of object | $\text{kg}$ |
| $g$ | Gravitational acceleration | $\text{m/s}^2$ |
| $\rho$ | Density of fluid (air) | $\text{kg/m}^3$ |
| $C_d$ | Drag coefficient (shape-dependent) | dimensionless |
| $A$ | Cross-sectional area | $\text{m}^2$ |

### The Two Drag Regimes

| Regime | Drag Force | Flow Type | Example |
|--------|-----------|-----------|---------|
| **Low speed** (Stokes) | $F_d = 6\pi\eta r v$ | Laminar | Small dust particles, tiny droplets |
| **High speed** (Newton) | $F_d = \frac{1}{2}\rho C_d A v^2$ | Turbulent | Skydiver, car, plane |

### Velocity–Time Profile for a Falling Object

An object falling from rest under gravity with drag follows a **tanh** (hyperbolic tangent) curve:

$$ v(t) = v_t \tanh\left(\frac{gt}{v_t}\right) $$

- **Initial stage** ($t$ small): $v \approx gt$ — nearly free fall, drag negligible
- **Transition**: drag builds up proportional to $v^2$, acceleration decreases
- **Steady stage** ($t$ large): $v \to v_t$ — acceleration approaches zero

---

## 🧪 Key Experiments

### 1. Coffee Filter Drop
Stacked coffee filters are dropped from a height. Each filter has the same area but different mass. Measuring terminal velocity shows that $v_t \propto \sqrt{m}$ — a classic classroom experiment.

### 2. Ball Drop in Viscous Fluid
Metal balls of different sizes are dropped into a tall cylinder of glycerol or golden syrup. The balls quickly reach terminal velocity, and Stokes' Law can be verified by measuring the constant speed.

### 3. Wind Tunnel Testing
A model or object is placed in a wind tunnel. The drag force is measured at various airspeeds to determine $C_d$ and predict terminal velocity.

### 4. Skydiving with Sensors
Modern skydivers wear GPS and accelerometer loggers. The recorded v–t graph shows the characteristic tanh curve: acceleration from 0 → terminal velocity, then constant speed, then a sharp deceleration when the parachute opens.

---

## 🌍 Real-World Applications

| Application | How Terminal Velocity Matters |
|------------|-----------------------------|
| 🪂 **Parachute design** | Parachute increases $A$ → reduces $v_t$ to safe landing speed (~5–7 m/s) |
| 🚗 **Car aerodynamics** | Reducing $C_d$ (drag coefficient) increases top speed and fuel efficiency |
| 🏗️ **Base jumping / free fall** | Body position changes $A$ → changes $v_t$ (belly: 190 km/h, head-down: 320 km/h) |
| ☔ **Raindrops** | Typical raindrop $v_t \approx 9 \, \text{m/s}$ — small enough not to hurt, large enough to fall |
| 🪐 **Planetary entry** | Spacecraft entering Mars or Earth's atmosphere must survive extreme heating at terminal velocity |
| ⚗️ **Industrial settling** | Particles in a fluid settle at terminal velocity — used in centrifugation and sedimentation |

---

## 💡 Common Misconceptions

| Misconception | Truth |
|--------------|-------|
| "Terminal velocity means you stop accelerating immediately" | ❌ No — acceleration gradually decreases to zero as drag builds up. The object still accelerates, just less and less until $a=0$ |
| "Heavier objects always have a higher terminal velocity" | ✅ Generally true — $v_t \propto \sqrt{m}$, so heavier objects fall faster at terminal velocity |
| "Terminal velocity is the same for all objects of the same shape" | ❌ Mass also matters — a heavier object with the same shape and size has a higher $v_t$ |
| "In a vacuum, there is no terminal velocity" | ✅ Correct — no air resistance means no drag, so objects accelerate indefinitely ($v = gt$) |
| "Terminal velocity is reached instantly" | ❌ It takes time to reach $v_t$ — typically 10–15 seconds for a skydiver (~400–500 m of fall) |

---

## 🔗 Related Lectures & Graphs

- [Topic 1.5 Forces](../lectures/topic15_forces.md) — drag forces and equilibrium
- [Terminal Velocity V–T Graph](../graphs/kinematics_terminal_velocity_v1.html) — Interactive simulation with tanh profile, parachute deployment, and 4 presets
- [Terminology: Free Fall](kinematics.md) — companion term for idealised $g$ motion

---

*This reference is part of the Terminology Archive. Last updated: July 2026.*