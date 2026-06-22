import numpy as np

def phi_mix(a, b, ratio=0.5):
    A = np.fft.fft(a)
    B = np.fft.fft(b)
    M = (1 - ratio) * A + ratio * B
    return np.fft.ifft(M).real
