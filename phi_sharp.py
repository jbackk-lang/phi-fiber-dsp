import numpy as np

def phi_sharp(x, alpha=0.2):
    dx = np.gradient(x)
    return x + alpha * dx
