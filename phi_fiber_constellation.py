import numpy as np
import matplotlib.pyplot as plt
from phi_fiber import phi_fiber_filter


def _normalize(x):
    x = x - np.min(x)
    return x / (np.max(x) + 1e-12)


def phi_constellation(i_samples, q_samples, mode="phi-mix", strength=1.0):
    """
    Analiza konstelacji QAM/PSK przez filtr φ.

    i_samples – próbki osi I (in-phase)
    q_samples – próbki osi Q (quadrature)
    """
    i = np.asarray(i_samples, dtype=np.float64)
    q = np.asarray(q_samples, dtype=np.float64)

    # filtrujemy osobno I i Q
    i_phi = phi_fiber_filter(i, mode=mode, strength=strength)
    q_phi = phi_fiber_filter(q, mode=mode, strength=strength)

    return i_phi, q_phi


def plot_constellation(i, q, title="Constellation"):
    """
    Rysuje konstelację sygnału.
    """
    plt.figure(figsize=(6, 6))
    plt.scatter(i, q, s=4, alpha=0.6)
    plt.axhline(0, color="gray", linewidth=0.5)
    plt.axvline(0, color="gray", linewidth=0.5)
    plt.title(title)
    plt.xlabel("I")
    plt.ylabel("Q")
    plt.grid(True, alpha=0.3)
    plt.show()
