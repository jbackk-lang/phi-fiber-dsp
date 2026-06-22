import numpy as np

def phi_compress(x, k=0.8):
    return np.sign(x) * (np.abs(x) ** k)
