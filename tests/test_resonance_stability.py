import numpy as np
from phi_fiber_filter import phi_filter

def test_resonance():
    x = np.random.normal(0, 1, 4096)
    y = phi_filter(x)
    assert np.sum(y**2) > 0
