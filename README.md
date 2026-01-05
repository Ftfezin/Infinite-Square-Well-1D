# Particle in a 1D Infinite Square Well 


This is a simple Python simulation of a **particle in a 1D infinite square well**, also known as the **particle in a box problem** from quantum mechanics.  

##  What’s This About?

In quantum mechanics, a particle confined to a box of width `a` can only occupy certain **allowed energy levels**. The particle's **wavefunction (ψ)** describes the probability of finding it at different positions inside the box.  

Mathematically, the wavefunction and energy levels can be derived from the **time-independent Schrödinger equation**, which I’ve also solved in my **handwritten notes** for better understanding.

---

##  About the Code

This Python code:

1. Calculates the **wavefunction** for a given energy level `n`.
2. Plots **ψ(x)** along the box.
3. Prints the **allowed energy** for that level.

Example:  

- Width of the box: `a = 1e-9 m`  
- Energy level: `n = 3`  

The code uses **NumPy** for calculations and **Matplotlib** for plotting.

---

##  How to Run

1. Make sure you have Python installed (3.8+).  
2. Install dependencies:

```bash
pip install numpy matplotlib scipy
