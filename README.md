# phi-fiber-dsp  
Topologiczny filtr **φ** dla sygnałów światłowodowych (DSP), oparty na modelu **Λ–τ–ρ** z TRM‑Geometry‑Core.
### Podwójne przejście (double-pass)

Filtr φ działa w dwóch przejściach:

1. **Pierwsze przejście (Λ → τ)**  
   Obraz jest analizowany pod kątem kierunku przepływu i lokalnych zmian.  
   To wyciąga komponent τ (transformacja).

2. **Drugie przejście (τ → Λ)**  
   Ten sam obraz przechodzi ponownie przez filtr, ale w kierunku stabilizacji.  
   To wyciąga komponent Λ (struktura).

Różnica między tymi przejściami ujawnia defekt:



\[
\rho = \Lambda - \tau
\]



A finalny operator:



\[
\phi = \Lambda + \tau - \rho
\]



działa tylko wtedy, gdy wykonane są **oba przejścia**.  
Bez podwójnego przejścia filtr nie pokazuje struktury światła, tylko zwykły gradient.

## Idea

Zamiast filtrować tylko amplitudę, filtr φ traktuje sygnał jak projekcję:

- **Λ** – część stabilna (składowa „nośna”),
- **τ** – część przejściowa (zmiany, modulacja),
- **ρ** – defekty propagacji (dyspersja, zakłócenia).

Operator:



\[
\phi = \Lambda + \tau - \rho
\]



działa tu jako **equalizer topologiczny**: wzmacnia strukturę, odejmuje defekty.

## Realtime DSP (phi_fiber_realtime.py)

Repo zawiera moduł `phi_fiber_realtime.py`, który umożliwia działanie filtra φ
na strumieniu danych w czasie rzeczywistym.

Przykład:

```python
from phi_fiber_realtime import PhiFiberRealtime

rt = PhiFiberRealtime(window=2048, mode="phi-mix", strength=1.0)

for sample in stream:  # np. dane z fotodiody / ADC
    y = rt.push(sample)
    if y is not None:
        print("filtered:", y)


## Instalacja

```bash
pip install -r requirements.txt


## Analiza konstelacji (QAM/PSK)

Repo zawiera moduł `phi_fiber_constellation.py`, który umożliwia analizę
konstelacji modulacji światłowodowych przez filtr φ.

Przykład:

```python
from phi_fiber_constellation import phi_constellation, plot_constellation

# przykładowe dane I/Q
i = [...]
q = [...]

i_phi, q_phi = phi_constellation(i, q, mode="phi-mix", strength=1.0)

plot_constellation(i, q, "Wejście")
plot_constellation(i_phi, q_phi, "Po filtrze φ")
