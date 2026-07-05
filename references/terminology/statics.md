---
title: Statics
field: Mechanics
type: terminology
version: 1
tags: [statics, equilibrium, forces, resultant, centre of mass, stability]
related_lectures: [topic16_effects_of_forces]
related_terminology: [dynamics, moment, torque]
---

# Statics

## 📖 Etymology

**Statics** comes from the Greek word **"στατικός"** (*statikos*) meaning "causing to stand, skilled in weighing" — from **"ἵστημι"** (*histēmi*) "to stand, set, place, weigh."

The term entered English through Latin (*staticus*) and French (*statique*). The first use in a mechanical context is attributed to **Archimedes** (287–212 BCE), who founded the science of statics with his work on **levers, centres of gravity, and floating bodies**.

The word "statics" contrasts directly with **"dynamics"** — while dynamics is about *motion and change* (from Greek *dynamis* "power"), statics is about *rest and balance* (from Greek *statikos* "standing still").

---

## 📜 Historical Timeline

### 🏛️ Archimedes of Syracuse (287–212 BCE) — The Father of Statics

Archimedes is considered the **founder of statics**. His major contributions:

- **Law of the Lever** (c. 260 BCE): *"Magnitudes are in equilibrium at distances reciprocally proportional to their weights."* This is the first mathematical statement of static equilibrium.
- **Centre of Gravity**: Archimedes determined the centre of gravity of various plane figures, including triangles, parallelograms, and parabolas.
- **Principle of Buoyancy** (Archimedes' Principle): *"A body immersed in a fluid experiences an upthrust equal to the weight of the fluid displaced."* This is a cornerstone of **fluid statics**.
- **The Archimedes Screw**: a practical device for raising water, demonstrating static force transmission.

> 🏺 *The Eureka story*: According to Vitruvius, Archimedes discovered his principle of buoyancy while getting into a bath, noticing the water displaced. He ran naked through the streets shouting **"Εὕρηκα!"** (Eureka! — "I have found it!").

### ⚖️ Hero of Alexandria (c. 10–70 CE)

Hero (Heron) extended Archimedes' work in *Mechanics* and *Pneumatics*, analysing the **parallelogram of forces** and the **balance of forces** in simple machines.

### 📐 Simon Stevin (1548–1620)

The Flemish mathematician **Simon Stevin** is known as the **second founder of statics**. His key contributions:

- **Parallelogram of forces**: Stevin showed that forces can be resolved into components and combined vectorially
- **Principle of the inclined plane**: he derived the mechanical advantage of an inclined plane using static equilibrium
- **Hydrostatic paradox**: the pressure at the bottom of a vessel depends only on the height of the liquid, not the shape of the vessel

Stevin's work *De Beghinselen der Weegconst* (Principles of the Art of Weighing, 1586) is a landmark in the history of statics.

### 🔧 Galileo Galilei (1599–1638)

Galileo's *Le Meccaniche* (On Mechanics) and *Discorsi* (Two New Sciences) extended statics to include:
- **Strength of materials**: the breaking strength of beams and columns
- **The lever and the balance**: analysed in terms of virtual work
- **Hydrostatic balance**: weighing objects in water to determine density

### 🧠 Pierre Varignon (1687)

Varignon formalised the **Principle of Moments** (Varignon's Theorem): the moment of a force about a point equals the sum of the moments of its components. This is central to the analysis of static equilibrium.

### 🏗️ 19th–20th Century — Engineering Statics

Statics became the foundation of **civil and mechanical engineering**:
- **Structural analysis**: trusses, beams, bridges, arches
- **Soil mechanics**: static equilibrium of earth and foundations
- **Fluid statics**: dams, hydraulic systems, atmospheric pressure
- **Navier, Cauchy, and Saint-Venant**: developed the theory of **elasticity** and **stress analysis**

---

## 📐 Modern Definition

### Statics

> **Statics** is the branch of mechanics that deals with **bodies at rest** (or in uniform motion) — i.e., bodies in **equilibrium**. The fundamental condition is that the **net force** and **net moment** on the body are both zero.

### Conditions for Equilibrium

For a body to be in **static equilibrium**, two conditions must be satisfied:

**1. Translational Equilibrium** — net force is zero:
$$ \boxed{\sum \vec{F} = 0} $$

$$ \sum F_x = 0, \quad \sum F_y = 0, \quad \sum F_z = 0 $$

**2. Rotational Equilibrium** — net moment is zero:
$$ \boxed{\sum \vec{M} = 0} $$

$$ \sum M_{\text{cw}} = \sum M_{\text{acw}} $$

### Free Body Diagram (FBD)

A **free body diagram** is a sketch showing all forces acting on a single object. Every statics problem begins with a correctly drawn FBD. Common forces to include:

| Force | Direction | Symbol |
|-------|-----------|--------|
| Weight | Vertically downward | $W = mg$ |
| Normal reaction | Perpendicular to surface | $N$ or $R$ |
| Friction | Parallel to surface, opposing motion | $F_f$ |
| Tension | Along the string/cable | $T$ |
| Thrust/Compression | Along the member | $F$ |
| Upthrust (fluid) | Vertically upward | $U$ |

### Types of Equilibrium

| Type | If Disturbed... | Example |
|------|----------------|---------|
| **Stable** | Returns to original position | A pendulum, a cone on its base |
| **Unstable** | Moves further away from original position | A pencil balanced on its tip |
| **Neutral** | Stays in the new position | A sphere on a flat surface, a cone on its side |

### The Line of Action and Stability

An object is stable if the **line of action of its weight** falls **within the base of support**. This is why:
- A wide-legged stance is more stable than standing with feet together
- A low centre of mass (e.g. a racing car) is more stable than a high one
- The Leaning Tower of Pisa still stands — its centre of mass is still inside its base

---

## 🧪 Key Experiments

### 1. The Spring Balance — Verifying Equilibrium
A mass is suspended from a spring balance. The reading equals the weight. Adding a second spring balance at an angle shows how forces resolve — the vector sum of the tensions equals the weight.

### 2. Force Table
A ring is centred on a force table by three or more strings attached to pulleys with hanging masses. The angles and masses are adjusted until the ring is centred (equilibrium). The vector sum of all forces should be zero.

### 3. Principle of Moments — Metre Ruler
A metre ruler is balanced on a pivot. Masses are hung at various distances. The condition $\sum M_{\text{cw}} = \sum M_{\text{acw}}$ is verified. This can be extended to find the **weight of the ruler itself** (whose centre of mass is at the 50 cm mark).

### 4. Centre of Mass — Irregular Lamina
An irregularly shaped card is suspended from a pin. A plumb line is drawn from the suspension point. Repeating from 2–3 different points, the centre of mass is where the lines intersect. When the card is pinned at this point, it balances perfectly.

### 5. Toppling — Stability Demonstration
A block on a tiltable platform. As the platform is tilted, the line of action of the weight moves. When it passes outside the base, the block topples. The **critical angle** depends on the width of the base and the height of the centre of mass.

---

## 🌍 Real-World Applications

| Application | How Statics Matters |
|------------|--------------------|
| 🌉 **Bridges** | Trusses and beams must be in static equilibrium under their own weight and traffic loads |
| 🏢 **Buildings** | Structural engineers calculate forces in columns, beams, and foundations so nothing moves |
| 🚛 **Cranes** | Counterweights provide an opposing moment to balance the load — static equilibrium prevents tipping |
| 🪑 **Furniture** | A chair must be stable — centre of mass inside the base, legs strong enough to support the load |
| 🚗 **Car jack** | A car jack is a static equilibrium problem — a small force at the handle produces a large lifting force |
| 🎪 **Tents / Cables** | Tension in guy ropes and poles must be in equilibrium to keep the structure standing |
| 🏗️ **Retaining walls** | Must resist the **turning moment** from soil pressure behind them — otherwise they topple |

---

## 💡 Common Misconceptions

| Misconception | Truth |
|--------------|-------|
| "Statics is just dynamics with no motion" | ❌ Statics is a **distinct branch** with its own principles (equilibrium, stability, free body diagrams). It is not simply "dynamics with $a=0$" |
| "If an object is not moving, no forces act on it" | ❌ A book on a table is not moving, but it experiences **weight** (down) and **normal reaction** (up) — they cancel to give zero net force |
| "The centre of mass must be inside the object" | ❌ The centre of mass can be **outside** the object — e.g. a ring, a boomerang, a hollow sphere |
| "A wider base always means more stability" | ✅ Generally true — but a **low centre of mass** is equally important. A tall object with a wide base can still topple if the centre of mass is too high |
| "Equilibrium means the object is at rest" | ❌ Equilibrium means **zero net force and zero net moment** — the object could be moving at constant velocity (dynamic equilibrium) |

---

## 🔗 Related Terminology & Lectures

- [Terminology: Dynamics](dynamics.md) — the study of forces causing motion (the complement of statics)
- [Terminology: Moment of a Force](moment.md) — turning effects, Principle of Moments
- [Terminology: Torque](torque.md) — rotational equilibrium, couple
- [Topic 1.6 Effects of Forces](../lectures/topic16_effects_of_forces.md) — turning effects, centre of mass, pressure, stability

---

*This reference is part of the Terminology Archive. Last updated: July 2026.*