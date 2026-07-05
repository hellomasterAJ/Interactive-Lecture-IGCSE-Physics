---
title: Torque
field: Mechanics
type: terminology
version: 1
tags: [torque, rotational dynamics, angular acceleration, moment, couple, power]
related_lectures: [topic16_effects_of_forces]
related_terminology: [moment]
---

# Torque

## 📖 Etymology

**Torque** comes from the Latin **"torquēre"** meaning "to twist, turn, wring, distort." It entered English through French (*torque*) in the 19th century.

The term was first introduced into physics by **James Clerk Maxwell** (1831–1879), who used it in his 1873 work *A Treatise on Electricity and Magnetism* to describe the twisting force in electromagnetic systems. Before Maxwell, physicists used "moment of a force" or simply "moment" for the same quantity.

> **Note:** In IGCSE Physics, the term **turning effect** or **moment of a force** is the standard. At A-Level, **torque** becomes more common — especially in the context of a **couple**, where A-Level syllabuses use the phrase **torque of a couple**.

---

## 📜 Historical Timeline

### 🏛️ Archimedes (287–212 BCE)

The principle of the lever — turning force at a distance — was fully understood by Archimedes, though he called it by a different name. The *mathematical* treatment of torque begins here.

### ⚙️ James Clerk Maxwell (1873)

Maxwell introduced the word **"torque"** in *A Treatise on Electricity and Magnetism*:

> *"A torsion balance measures torque by the angle of twist of a fibre."*

He needed a distinct term for rotational effects in electromagnetic systems and chose *torque* from Latin "twist."

### 🚗 20th Century — Engineering & Automotive

Torque became a central concept in:
- **Internal combustion engines**: torque curves define engine performance
- **Electric motors**: torque determines starting power and hill-climbing ability
- **Robotics**: servo torque determines lifting capacity
- **Power transmission**: gearboxes multiply torque while reducing speed ($P = \tau \omega$)

---

## 📐 Modern Definition

### Torque

> **Torque** ($\tau$) is the rotational analogue of force — it measures the tendency of a force to cause an object to **rotate about an axis**.

$$ \boxed{\tau = F \cdot r \cdot \sin\theta} $$

| Symbol | Meaning | Unit |
|--------|---------|------|
| $\tau$ | Torque | $\text{N·m}$ |
| $F$ | Applied force | $\text{N}$ |
| $r$ | Distance from axis to point of force | $\text{m}$ |
| $\theta$ | Angle between $F$ and $r$ | degrees or radians |

When the force is perpendicular ($\theta = 90^\circ$), this simplifies to:

$$ \tau = F \cdot r $$

### Torque as a Vector

Torque is a **vector** quantity. Its direction is given by the **right-hand rule**: curl fingers in the direction of rotation, and the thumb points along the axis in the direction of the torque vector.

### Rotational Dynamics — Newton's Second Law for Rotation

$$ \boxed{\tau_{\text{net}} = I \alpha} $$

| Symbol | Meaning | Unit | Analogue |
|--------|---------|------|----------|
| $\tau$ | Net torque | $\text{N·m}$ | $F$ (force) |
| $I$ | Moment of inertia | $\text{kg·m}^2$ | $m$ (mass) |
| $\alpha$ | Angular acceleration | $\text{rad/s}^2$ | $a$ (acceleration) |

### Power and Torque

$$ \boxed{P = \tau \cdot \omega} $$

where $\omega$ is the angular velocity (rad/s). This is a fundamental equation in engine design and vehicle dynamics.

### Torque vs Moment of a Force

| Aspect | Moment of a Force | Torque |
|--------|-----------------|--------|
| **Context** | Static equilibrium, beams, levers | Rotating shafts, engines, dynamics |
| **Typical use** | IGCSE / A-Level Physics | Engineering, mechanics, motors |
| **Quantity** | Scalar (in 2D problems) | Vector (3D axis) |
| **Focus** | Balancing forces around a pivot | Rotational acceleration & power |

**Physically they are the same quantity** — the difference is mainly contextual and pedagogical.

### Torque of a Couple (A-Level)

At **A-Level Physics**, the term **torque of a couple** is used for the moment produced by a pair of equal, parallel, and opposite forces acting on a body but not along the same line.

$$ \boxed{\text{Torque of a couple} = F \times d} $$

where:
- $F$ = magnitude of one of the forces (N)
- $d$ = **perpendicular distance between the two forces** (m)

Key properties of a couple:
- Produces **pure rotation** — no net force, so no translation
- The torque is the **same about any pivot point** (unlike a single force, whose moment depends on the pivot)
- Examples: turning a steering wheel, opening a jar lid, the forces on a compass needle in a magnetic field

> 💡 **IGCSE → A-Level progression**: At IGCSE, students learn the **turning effect of a single force** about a pivot. At A-Level, this extends to the **torque of a couple** — two forces working together to produce rotation without sideways movement.

---

## 🧪 Key Experiments

### 1. Torque Wrench Calibration
A torque wrench is used to apply a known torque to a bolt. A spring balance at a known distance verifies the reading. This demonstrates $\tau = F \cdot r$ in a practical calibration setup.

### 2. Rotational Dynamics Apparatus
A disc or pulley is mounted on a frictionless axle. A string is wound around it and a hanging mass provides a constant torque. The angular acceleration $\alpha$ is measured, and $\tau = I\alpha$ is verified.

### 3. Engine Dynamometer (Dyno Test)
An engine is connected to a dynamometer that measures torque output at different RPM. The resulting **torque curve** shows at which RPM the engine produces peak torque — critical for vehicle performance analysis.

---

## 🌍 Real-World Applications

| Application | How Torque Matters |
|------------|-------------------|
| 🚗 **Car engines** | Torque determines acceleration and towing power. High torque at low RPM = good for trucks |
| 🔩 **Torque wrench** | Ensures bolts are tightened to exactly the right torque — too loose = failure, too tight = stripped thread |
| 🚲 **Bicycle gears** | Changing gear ratio multiplies torque at the wheel (lower gear = more torque, less speed) |
| 🏗️ **Electric screwdrivers** | Torque setting prevents over-tightening |
| 🚁 **Helicopter rotor** | The engine must produce enough torque to spin the rotor blades and overcome air resistance |
| 🦾 **Robotic arm** | Each joint has a torque rating — the maximum twisting force it can apply before stalling |

### Engine Torque Curves

A typical internal combustion engine produces:
- **Low RPM**: torque builds up as the engine breathes efficiently
- **Peak torque**: at mid-RPM — the sweet spot for acceleration
- **High RPM**: torque drops off as friction and intake limitations dominate

Electric motors, by contrast, produce **maximum torque from zero RPM** — which is why electric vehicles accelerate so quickly off the line.

---

## 💡 Common Misconceptions

| Misconception | Truth |
|--------------|-------|
| "Torque and horsepower are the same thing" | ❌ Torque is the twisting force; horsepower is **power** ($P = \tau \omega$). You can have high torque at low RPM but low power |
| "More torque always means a faster car" | ❌ Acceleration depends on power-to-weight ratio. A lightweight car with less torque but higher RPM can accelerate faster |
| "Torque is a scalar" | ❌ Torque is a **vector** — it has direction (along the axis of rotation, given by the right-hand rule) |
| "Torque and moment are completely different quantities" | ❌ Same physical quantity ($F \cdot d$), different contexts. Moment is used in statics, torque in dynamics |
| "A longer wrench always gives more torque" | ✅ Correct — for the same applied force, a longer lever arm produces more torque |

---

## 🔗 Related Terminology & Lectures

- [Terminology: Moment of a Force](moment.md) — the static equilibrium counterpart
- [Topic 1.6 Effects of Forces](../lectures/topic16_effects_of_forces.md) — turning effects, centre of mass

---

*This reference is part of the Terminology Archive. Last updated: July 2026.*