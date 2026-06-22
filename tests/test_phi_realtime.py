from phi_fiber_realtime import PhiFiberRealtime

def test_realtime():
    dsp = PhiFiberRealtime(buffer_size=256)
    out = dsp.process([0.1]*256)
    assert len(out) == 256
