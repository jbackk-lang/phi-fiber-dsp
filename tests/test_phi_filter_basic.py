import numpy as np
from phi_fiber_filter import phi_filter

def test_phi_basic():
    x = np.sin(np.linspace(0, 10*np.pi, 2048))
    y = phi_filter(x)
    assert len(y) == len(x)
