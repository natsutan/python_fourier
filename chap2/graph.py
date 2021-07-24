import numpy as np
import matplotlib.pyplot as plt

PI = np.pi


def partialsum(t, n):
    psum = PI / 2
    if n == 0:
        return psum
    for k in range(1, n+1):
        psum += -(4/PI) * np.cos((2*k-1)*t) / (2*k-1)**2
    return psum


t = np.linspace(-PI, PI, 10000)
x = np.abs(t)
s = partialsum(t, 1)

plt.plot(t, x)
plt.plot(t, s)
plt.savefig("graph.png")
