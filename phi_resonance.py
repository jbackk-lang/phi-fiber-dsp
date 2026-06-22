import numpy as np

def phi_resonance(x, beta=1.2):
    X = np.fft.fft(x)
    w = np.linspace(-1, 1, len(X))
    H = 1 + beta * (w**2)
    return np.fft.ifft(X * H).real
