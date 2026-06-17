# phi-fiber-dsp  
Topologiczny filtr **φ** dla sygnałów światłowodowych (DSP), oparty na modelu **Λ–τ–ρ** z TRM‑Geometry‑Core.

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

## Instalacja

```bash
pip install -r requirements.txt
