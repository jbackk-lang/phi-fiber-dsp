import numpy as np
from phi_fiber_filter import phi_filter

def test_fft_pipeline():
    x = np.sin(np.linspace(0, 20*np.pi, 4096))
    y = phi_filter(x)
    Y = np.fft.fft(y)
    assert len(Y) == len(x)
