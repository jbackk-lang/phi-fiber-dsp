import numpy as np

def phi_stability(x, gamma=0.05):
    mean = np.mean(x)
    return (1 - gamma) * x + gamma * mean
