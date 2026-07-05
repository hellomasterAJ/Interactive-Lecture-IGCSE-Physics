---
title: Moment of a Force
field: Mechanics
type: terminology
version: 1
tags: [moment, torque, turning effect, pivot, lever, equilibrium]
related_lectures: [topic16_effects_of_forces]
---

# Moment of a Force

## 📖 Etymology

**Moment** comes from the Latin **"mōmentum"** meaning "movement, moving power, a cause of motion" — from **"movēre"** ("to move"). In Latin, *mōmentum* also meant "an instant" (a decisive point in time) and "a weight, importance" — all related to the idea of a *small cause producing a large effect*.

The term **"moment of a force"** was introduced in mechanics in the 17th–18th century by **Archimedes** (indirectly through his work on levers) and formalised mathematically by **Leonhard Euler** and **Johann Bernoulli**. The alternative name **"torque"** comes from the Latin **"torquēre"** ("to twist"), introduced later in electrical engineering contexts by **James Clerk Maxwell** (19th century).

---

## 📜 Historical Timeline

### 🏛️ Archimedes of Syracuse (287–212 BCE) — The Father of Levers

Archimedes laid the foundation for the concept of moment without naming it. In his work *On the Equilibrium of Planes*, he stated the **Law of the Lever**:

> *"Magnitudes are in equilibrium at distances reciprocally proportional to their weights."*

He famously declared:

> *"Δῶς μοι πᾶ στῶ καὶ τὰν γᾶν κινάσω"* (Give me a place to stand, and I shall move the Earth.)

Archimedes understood that the **turning effect** depends on both the **force** and the **distance from the pivot** — the essence of moment.

### ⚖️ Stevinus & the Early Modern Period (1586)

**Simon Stevin** (1548–1620) extended Archimedes' work on equilibrium, developing the **parallelogram of forces** and analysing levers and pulleys. His work *De Beghinselen der Weegconst* ("Principles of the Art of Weighing") formalised the conditions for rotational equilibrium.

### 🔧 Galileo Galilei (1599)

In *Le Meccaniche* (On Mechanics), Galileo analysed the lever, the screw, and the pulley, showing that the **principle of virtual work** could explain all simple machines. He understood that mechanical advantage depends on the ratio of distances from the pivot.

### 📐 Pierre Varignon (1687)

The French mathematician **Pierre Varignon** (1654–1722) gave the **first clear, modern formulation** of the moment of a force:

$$ M = F \times d $$

where $d$ is the perpendicular distance from the pivot to the line of action of the force. This is now known as **Varignon's Theorem**: the moment of a force about a point equals the sum of the moments of its components.

### 🧠 Leonhard Euler (1750)

Euler extended the concept of moment into **rotational dynamics**, establishing the rotational analogue of Newton's Second Law:

$$ \tau = I \alpha $$

where $\tau$ is torque (moment of force), $I$ is the moment of inertia, and $\alpha$ is angular acceleration. Euler is credited with giving torque its modern mathematical treatment.

### ⚡ James Clerk Maxwell (19th Century)

Maxwell introduced the term **"torque"** (from Latin *torquēre* — to twist) in the context of electromagnetism and mechanical systems. The word gained popularity in English-speaking engineering contexts over the 20th century.

---

## 📐 Modern Definition

### Moment of a Force (Torque)

> The **moment of a force** (also called **torque**) is the **turning effect** produced by a force acting at a distance from a pivot. It is a **vector quantity**.

$$ \boxed{M = F \cdot d} $$

where:
- $M$ = moment / torque (N·m)
- $F$ = applied force (N)
- $d$ = perpendicular distance from pivot to line of action of force (m)

### Principle of Moments

> For a body in **rotational equilibrium**:
> $$ \text{Sum of clockwise moments} = \text{Sum of anticlockwise moments} $$
> $$ \sum M_{\text{cw}} = \sum M_{\text{acw}} $$

### Types of Moment

| Type | Description | Example |
|------|------------|---------|
| **Clockwise moment** | Turns the body clockwise | Seesaw with a heavier person on the right |
| **Anticlockwise moment** | Turns the body anticlockwise | Seesaw with a heavier person on the left |

### Moment vs Torque

| Term | Typically Used For |
|------|-------------------|
| **Moment of a force** | Static equilibrium, levers, beams (IGCSE/A-Level) |
| **Torque** | Rotating shafts, engines, motors, dynamics |

In IGCSE Physics, **moment** is the standard term. In engineering, **torque** is more common. Physically they are the same quantity.

### 📚 Curriculum Notes

#### IGCSE Physics (0625) — "Turning Effect"

In the IGCSE Physics 0625 syllabus, the term **Turning Effect** is used as the simpler, more intuitive name for the moment of a force. This is to help students build conceptual understanding before introducing formal terminology.

| Syllabus Level | Preferred Term | Formula |
|---------------|---------------|---------|
| **IGCSE** (Year 10–11) | **Turning Effect** | $F \times d$ |
| **A-Level** (Year 12–13) | **Moment of a force** | $F \times d$ |
| **Engineering** | **Torque** | $\tau = F \cdot r$ |

At IGCSE, students learn:
- A force can cause a **turning effect** about a pivot
- The size of the turning effect depends on **force** and **distance from pivot**
- The **Principle of Moments** for equilibrium
- Applications: levers, seesaws, spanners, balancing

The formal term **"moment of a force"** is introduced later at A-Level, alongside the vector treatment and rotational dynamics.

### Couple

A **couple** is a pair of equal and opposite forces acting on a body but not along the same line. The total moment of a couple is:

$$ M = F \times d $$

where $d$ is the **perpendicular distance between the two forces**. A couple produces pure rotation with no net force.

**Examples**: turning a steering wheel, using a screwdriver, twisting a lid off a jar.

### Centre of Mass and Stability

The stability of an object depends on:
- **Position of the centre of mass** — lower = more stable
- **Width of the base** — wider = more stable
- **Line of action of weight**: if it falls **inside** the base → stable; **outside** → topples

---

## 🧪 Key Experiments

### 1. The Seesaw (Balancing Act)
A metre rule is balanced on a pivot. Weights are hung at different distances. Students verify the **principle of moments**: $F_1 d_1 = F_2 d_2$.

### 2. Hanging Mass on a Ruler
A metre rule is clamped at one end. Masses are hung at various positions. The moment at the clamp is calculated as $F \cdot d$. A spring balance at the other end measures the reaction force.

### 3. Finding the Centre of Mass
An irregularly shaped card (lamina) is suspended from a pin. A plumb line is hung from the same pin. The line is drawn on the card. The process is repeated from 2–3 different suspension points. The **centre of mass** is where the lines intersect.

### 4. Balancing a Toy (Stability Test)
A toy is placed on a tilted platform. The angle at which it topples is measured. Adding mass to the base (lowering centre of mass) increases stability. This demonstrates $M = Fd$ in reverse — the weight's moment about the pivot point determines tipping.

---

## 🌍 Real-World Applications

| Application | How Moment Matters |
|------------|-------------------|
| 🔧 **Spanner / Wrench** | Longer handle = larger $d$ = more turning force with same effort |
| 🚪 **Door handle** | Placed far from hinge → small force produces large moment |
| ⚖️ **See-saw / Balance** | Light person sits farther from pivot to balance a heavier person |
| 🚜 **Crane counterweight** | Counterweight at large $d$ balances heavy load at small $d$ |
| 🔩 **Screwdriver** | Wider handle = larger radius = more torque to turn the screw |
| 🏗️ **Leaning Tower of Pisa** | Centre of mass still inside the base — that's why it hasn't fallen |
| 🚗 **Wheel lug nut** | Long breaker bar = more torque to loosen a tight nut |

---

## 💡 Common Misconceptions

| Misconception | Truth |
|--------------|-------|
| "Moment and force are the same thing" | ❌ A moment is **force × distance** — the same force produces different moments at different distances |
| "A larger force always produces a larger moment" | ❌ A small force far from the pivot can produce a larger moment than a large force near the pivot |
| "If the net force is zero, the object must be in equilibrium" | ❌ Net force zero ≠ equilibrium — a **couple** produces rotation even with zero net force |
| "The pivot must be at the centre of the object" | ❌ The pivot can be anywhere — the principle of moments works for any pivot point |
| "Torque and work have the same unit (N·m), so they're the same" | ❌ Both have N·m as units, but torque is a **vector** (turning effect) and work is a **scalar** (energy transfer) — fundamentally different quantities |

---

## 🔗 Related Lectures

- [Topic 1.6 Effects of Forces](../lectures/topic16_effects_of_forces.md) — turning effects, centre of mass, pressure
- [Terminology: Inertia](inertia.md) — resistance to change in motion

---

*This reference is part of the Terminology Archive. Last updated: July 2026.*