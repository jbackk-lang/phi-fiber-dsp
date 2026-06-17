import numpy as np
from collections import deque
from phi_fiber import phi_fiber_filter


class PhiFiberRealtime:
    """
    Realtime topological φ filter for fiber‑optic DSP.
    Works on streaming samples (e.g. ADC, photodiode, SDR).
    """

    def __init__(self, window=1024, mode="phi-mix", strength=1.0):
        self.window = window
        self.mode = mode
        self.strength = strength
        self.buffer = deque(maxlen=window)

    def push(self, sample):
        """
        Add one sample to the buffer.
        Returns None until buffer is full.
        """
        self.buffer.append(sample)
        if len(self.buffer) < self.window:
            return None

        arr = np.array(self.buffer, dtype=np.float64)
        out = phi_fiber_filter(arr, mode=self.mode, strength=self.strength)
        return out[-1]  # last filtered sample

    def process_block(self, block):
        """
        Process a block of samples (e.g. from audio/fiber ADC).
        """
        output = []
        for s in block:
            y = self.push(s)
            if y is not None:
                output.append(y)
        return np.array(output)
