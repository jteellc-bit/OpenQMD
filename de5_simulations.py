import numpy as np
from de5_fractal_operator import fractal_transform
def simulate_quantum_to_macro(n=100):
    Lambda = np.linspace(0, 10, n)
    Psi = np.linspace(0, 10, n)
    data = fractal_transform(Lambda[:, None], Psi[None, :], scale_factor=0.5)
    return Lambda, Psi, data
