import numpy as  np
import matplotlib.pyplot as  plt
from scipy.constants import hbar,m_e


a = 1e-9 
# n = 2
# x = np.linspace(0,a,1000)
# A = np.sqrt(2/a)
# theta = (n * np.pi/a) * x
# psi = A * np.sin(theta)

# energy = (n**2 * np.pi**2 * hbar**2) / (2*m_e * a**2)

# print("allowed energy levels: ", energy)

# plt.plot(psi)
# plt.xlabel("X")
# plt.ylabel("psi(x)")
# plt.title("Infinite Square Well 1D")
# plt.grid()
# plt.show()

# plt.close()

def PlotPsi(n):
    x = np.linspace(0,a,1000)
    A = np.sqrt(2/a)
    theta = (n * np.pi/a) * x
    psi = A * np.sin(theta)
    
    plt.plot(x, psi, label=f"n={n}")
    plt.ylabel("psi(x)")
    plt.xlabel("x")
    plt.title("Infinite Square Well 1D " + "n=" + str(n))
    plt.grid(True)
    plt.show()

def EnergyLevel(n):
    energy = (n**2 * np.pi**2 * hbar**2) / (2*m_e * a**2)
    return energy

def PlotEneryLevels(n):
    levels = [EnergyLevel(i) for i in range(1, n+1)]
    plt.figure()
    # plt.stem(range(1, n+1), levels, use_line_collection=True)
    plt.stem(range(1, n+1), levels)
    plt.xlabel("Quantum Number n")
    plt.ylabel("Energy Levels (Joules)")
    plt.title("Energy Levels in Infinite Square Well")
    plt.grid(True)
    plt.show()

def PlotEnergryForWellWidth(a, n=1):
    """
    Calculate energy level for given well width a and quantum number n.
    """
    n = 1
    energy = (n**2 * np.pi**2 * hbar**2) / (2*m_e * a**2)
    return energy

def PlotEnergyForWellWidth(aMin=0.5e-9, aMax=5e-9, n=1, numberOfPoints=10):
    """
    Plot energy level as a function of well width varying from aMin to aMax for given quantum number n.
    n: Quantum number (default is 1)
    numberOfPoints: Number of points to calculate between aMin and aMax (default is 10)

    """
    a_values = np.linspace(aMin, aMax, numberOfPoints)
    energies = [PlotEnergryForWellWidth(a_val, n=n) for a_val in a_values]
    
    plt.figure()
    plt.plot(a_values*1e9, energies)
    plt.xlabel("Well Width a (nm)")
    plt.ylabel("Energy Level (Joules)")
    plt.title("Energy Level vs Well Width in Infinite Square Well")
    plt.grid(True)
    plt.show()

def orthogonality(n1,n2):
    x = np.linspace(0,a,1000)
    dx = x[1] - x[0]
    A = np.sqrt(2/a)
    theta1 = (n1 * np.pi/a) * x
    theta2 = (n2 * np.pi/a) * x
    psi1 = A * np.sin(theta1)
    psi2 = A * np.sin(theta2)
    
    orthogonal = psi1 * psi2 
    result = np.sum(orthogonal) * dx
    print(result)
    

# Example usage:
# PlotEnergyEvels as well width changes
# PlotEnergyForWellWidth(1e-9, 5e-9, n=1, numberOfPoints=10)
# PlotPsi(3)
# PlotEneryLevels(5)
# orthogonality(1,2)

plt.ion()


