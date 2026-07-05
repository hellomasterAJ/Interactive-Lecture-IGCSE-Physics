---
title: Motion — Kinematics
topic: 1.2 Motion
level: IGCSE Physics 0625 — Extended
version: 1
---

## 📜 History

The study of motion, known as **kinematics**, began with ancient Greek philosophers.

**Aristotle (384–322 BCE)** believed that objects fell at speeds proportional to their weight — a heavier object falls faster than a lighter one. This idea was accepted for nearly 2,000 years because it seemed intuitive.

**Galileo Galilei (1564–1642)** challenged Aristotle's view. Through careful experiments using inclined planes and water clocks, he demonstrated that in the absence of air resistance, **all objects fall at the same rate regardless of mass**. Galileo's work laid the foundation for modern kinematics.

> **Myth vs Fact:** The story of Galileo dropping balls from the Leaning Tower of Pisa is a popular myth. In reality, he used inclined planes to slow down the motion so he could measure it more accurately with the primitive timing tools available.

**Sir Isaac Newton (1643–1727)** later formalised the laws of motion in his work *Philosophiæ Naturalis Principia Mathematica*, unifying terrestrial and celestial motion under the same mathematical framework.

## 🌍 Nature & Applications

Kinematics — the description of motion — is everywhere in our daily lives:

- **🚗 Cars & Transport**: Speedometers measure instantaneous speed. Sat-navs calculate average speed and time of arrival.
- **🏃 Sports**: Athletes analyse split times, acceleration off the starting block, and peak speed.
- **🛰️ Space Exploration**: Rocket launches require precise calculations of velocity and acceleration to reach orbit.
- **🚦 Safety**: Thinking distance and braking distance determine stopping distances for road safety.

**Key idea**: Motion is **relative** — we describe it from a chosen reference point (the observer's position).

## ⚛️ Theory

### Key Quantities

- **Distance (s)** — total path length travelled (scalar, SI unit: metre, m)
- **Displacement (s)** — straight-line distance from start to finish in a given direction (vector, m)
- **Speed (v)** — rate of change of distance: $v = \frac{\Delta s}{\Delta t}$ (scalar, m/s)
- **Velocity (v)** — rate of change of displacement: $v = \frac{\Delta s}{\Delta t}$ (vector, m/s)
- **Acceleration (a)** — rate of change of velocity: $a = \frac{\Delta v}{\Delta t}$ (vector, m/s²)

### Equations for Uniform Acceleration (SUVAT)

These equations apply only when acceleration is **constant**:

$$ v = u + at $$

$$ s = ut + \frac{1}{2}at^2 $$

$$ v^2 = u^2 + 2as $$

Where:
- $u$ = initial velocity (m/s)
- $v$ = final velocity (m/s)
- $a$ = acceleration (m/s²)
- $t$ = time (s)
- $s$ = displacement (m)

### Free Fall

When an object falls freely under gravity, **air resistance is negligible**, and the acceleration is constant at:

$$ g = 9.8 \, \text{m/s}^2 \, (\text{downward on Earth}) $$

The equations of motion become:

$$ v = u + gt $$

$$ s = ut + \frac{1}{2}gt^2 $$

**For a freely falling object dropped from rest** ($u = 0$):

$$ v = gt $$

$$ s = \frac{1}{2}gt^2 $$

### Graphs of Motion

| Graph Type | Y-axis | Gradient | Area Under |
|-----------|--------|----------|------------|
| Distance–Time | distance (m) | speed (m/s) | — |
| Speed–Time | speed (m/s) | acceleration (m/s²) | distance (m) |
| Acceleration–Time | acceleration (m/s²) | — | change in velocity (m/s) |

## 📊 Interactive Graphs

### Horizontal Motion

Experiment with different modes of motion — from rest, constant speed, acceleration, and deceleration.

```graph
type: horizontal-motion
mode: constant-speed
speed: 8
```

```graph
type: horizontal-motion
mode: increasing-speed
speed: 5
```

### Free Fall (Vertical Motion)

Observe the motion of a freely falling apple under different gravitational fields.

```graph
type: freefall
scenario: earth
```

```graph
type: freefall
scenario: moon
```

## ✍️ Worked Examples

### Example 1: Constant Acceleration

A car starts from rest and accelerates uniformly at $2.0 \, \text{m/s}^2$ for 10 seconds.

**(a)** What is its final velocity?
**(b)** How far does it travel?

**Solution (a):**
$$ v = u + at = 0 + (2.0)(10) = 20 \, \text{m/s} $$

**Solution (b):**
$$ s = ut + \frac{1}{2}at^2 = 0 + \frac{1}{2}(2.0)(10)^2 = 100 \, \text{m} $$

---

### Example 2: Free Fall

A ball is dropped from a height of 45 m. How long does it take to reach the ground? (Take $g = 10 \, \text{m/s}^2$)

**Solution:**
$$ s = \frac{1}{2}gt^2 $$
$$ 45 = \frac{1}{2}(10)t^2 $$
$$ t^2 = 9 $$
$$ t = 3.0 \, \text{s} $$

---

### Example 3: Thinking and Braking Distance

A car travels at $20 \, \text{m/s}$. The driver's reaction time is $0.5 \, \text{s}$. The braking deceleration is $4.0 \, \text{m/s}^2$.

**(a)** What is the thinking distance?
**(b)** What is the braking distance?
**(c)** What is the total stopping distance?

**Solution (a):**
Thinking distance = speed × reaction time
$$ = (20)(0.5) = 10 \, \text{m} $$

**Solution (b):**
Braking distance:
$$ v^2 = u^2 + 2as $$
$$ 0 = (20)^2 + 2(-4.0)s $$
$$ s = \frac{400}{8} = 50 \, \text{m} $$

**Solution (c):**
Total stopping distance = $10 + 50 = 60 \, \text{m}$