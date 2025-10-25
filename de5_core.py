import numpy as np
def phi_operator(Lambda, Psi, f):
    return np.trapz(np.trapz(f(Lambda, Psi), Lambda), Psi)
