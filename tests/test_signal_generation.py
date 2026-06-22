import numpy as np

def test_signal_generation():
    t = np.linspace(0, 1, 48000)
    assert len(t) == 48000
