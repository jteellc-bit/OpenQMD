# Core DE4 Surrogate vs True Model comparison module

import numpy as np
import pandas as pd

def compute_surrogate_error(true_values, pred_values):
    mse = np.mean((true_values - pred_values)**2)
    mae = np.mean(np.abs(true_values - pred_values))
    corr = np.corrcoef(true_values, pred_values)[0, 1]
    return {"mse": mse, "mae": mae, "corr": corr}

def generate_test_data(n=100):
    x = np.linspace(-1, 1, n)
    true_y = np.sin(np.pi * x)
    pred_y = true_y + np.random.normal(0, 0.05, n)
    return pd.DataFrame({"x": x, "true_y": true_y, "pred_y": pred_y})
