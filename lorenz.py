import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def lorenz(state, t, sigma, beta, rho):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

sigma = 10.0
beta = 8 / 3
rho = 28.0
state0 = [1.0, 1.0, 1.0]
t = np.linspace(0, 100, 10000)
solution = odeint(lorenz, state0, t, args=(sigma, beta, rho))

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution[:, 0], solution[:, 1], solution[:, 2], lw=0.5, color='blue')
ax.set_title('Atrator de Lorenz')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

