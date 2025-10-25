import matplotlib.pyplot as plt
import numpy as np
def visualize_coherence(Lambda, Psi, data):
    plt.figure(figsize=(6,5))
    plt.contourf(Lambda, Psi, data, cmap='viridis')
    plt.xlabel("Λ (System Parameters)")
    plt.ylabel("Ψ (State Space)")
    plt.colorbar(label="Φ(Λ,Ψ) Magnitude")
    plt.title("Fractal Coherence Mapping")
    plt.show()
