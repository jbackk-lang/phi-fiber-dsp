import numpy as np
import matplotlib.pyplot as plt
from phi_fiber import phi_fiber_filter

t = np.linspace(0, 1, 4096)
signal = np.sin(2*np.pi*50*t) + 0.3*np.sin(2*np.pi*400*t)

phi = phi_fiber_filter(signal, mode="phi-mix", strength=1.0)

plt.plot(t, signal, label="wejście")
plt.plot(t, phi, label="φ-mix")
plt.legend()
plt.show()
