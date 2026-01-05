import numpy as  np
import matplotlib.pyplot as  plt
from scipy.constants import hbar,m_e


a = 1e-9 
n = 3
x = np.linspace(0,a,1000)
A = np.sqrt(2/a)
theta = (n * np.pi/a) * x
psi = A * np.sin(theta)

energy = (n**2 * np.pi**2 * hbar**2) / (2*m_e * a**2)

print("allowed energy levels: ", energy)

plt.plot(psi)
plt.xlabel("X")
plt.ylabel("psi(x)")
plt.title("Infinite Square Well 1D")
plt.grid()
plt.show()