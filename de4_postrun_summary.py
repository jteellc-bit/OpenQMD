# Generates post-run summary plots and statistics

import pandas as pd
import matplotlib.pyplot as plt
from de4_surrogate_core import compute_surrogate_error, generate_test_data

def run_summary():
    df = generate_test_data()
    metrics = compute_surrogate_error(df['true_y'], df['pred_y'])
    print("Metrics:", metrics)

    plt.figure(figsize=(6, 4))
    plt.plot(df['x'], df['true_y'], label='True')
    plt.plot(df['x'], df['pred_y'], label='Surrogate', linestyle='--')
    plt.title('DE4 Surrogate Validation')
    plt.xlabel('x')
    plt.ylabel('Output')
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/de4_postrun_summary.png")
    df.to_csv("data/de4_fidelity_summary.csv", index=False)

if __name__ == "__main__":
    run_summary()
