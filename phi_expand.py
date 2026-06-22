import numpy as np

def phi_expand(x, k=1.2):
    return np.sign(x) * (np.abs(x) ** k)
