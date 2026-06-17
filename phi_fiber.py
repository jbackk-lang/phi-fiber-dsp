import numpy as np
from scipy.signal import hilbert, butter, filtfilt


def _normalize(x):
    x = x.astype(np.float64)
    x = x - x.min()
    return x / (x.max() + 1e-12)


def _lambda_component(signal, lowcut=0.0, highcut=0.1):
    """
    Λ – część stabilna (niskie częstotliwości / nośna).
    Zakładamy sygnał znormalizowany w dziedzinie czasu [0,1].
    """
    # prosty filtr dolnoprzepustowy
    b, a = butter(4, highcut, btype="lowpass")
    return filtfilt(b, a, signal)


def _tau_component(signal, lowcut=0.1, highcut=0.5):
    """
    τ – część przejściowa (modulacja / średnie częstotliwości).
    """
    b, a = butter(4, [lowcut, highcut], btype="bandpass")
    return filtfilt(b, a, signal)


def _rho_component(signal, highcut=0.5):
    """
    ρ – defekty / zakłócenia (wysokie częstotliwości, szum).
    """
    b, a = butter(4, highcut, btype="highpass")
    return filtfilt(b, a, signal)


def phi_fiber_filter(signal, mode="phi-mix", strength=1.0):
    """
    Topologiczny filtr φ dla sygnału 1D (światłowód / fotodioda).

    mode:
        - "lambda"  – zwraca Λ
        - "tau"     – zwraca τ
        - "rho"     – zwraca ρ
        - "phi"     – φ = Λ + τ – ρ
        - "phi-mix" – φ z dodatkowym wzmocnieniem τ
    """
    signal = np.asarray(signal, dtype=np.float64)
    signal = signal - np.mean(signal)

    L = _lambda_component(signal)
    T = _tau_component(signal)
    R = _rho_component(signal)

    if mode == "lambda":
        out = L
    elif mode == "tau":
        out = T
    elif mode == "rho":
        out = R
    else:
        phi = L + T - R
        if mode == "phi-mix":
            phi = phi + strength * T
        out = phi

    return out
