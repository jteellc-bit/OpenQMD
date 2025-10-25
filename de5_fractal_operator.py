import numpy as np
def fractal_transform(Lambda, Psi, scale_factor=1.0):
    return np.sin(scale_factor * Lambda) * np.cos(scale_factor * Psi)
