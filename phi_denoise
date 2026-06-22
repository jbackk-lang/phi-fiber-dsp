import numpy as np

def phi_denoise(x, strength=0.1):
    X = np.fft.fft(x)
    mag = np.abs(X)
    threshold = strength * np.max(mag)
    X_filtered = np.where(mag > threshold, X, 0)
    return np.fft.ifft(X_filtered).real
