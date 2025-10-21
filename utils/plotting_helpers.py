# Helper functions for plotting results consistently

import matplotlib.pyplot as plt

def plot_comparison(x, true, pred, title='DE4 Surrogate Comparison'):
    plt.figure(figsize=(6,4))
    plt.plot(x, true, label='True')
    plt.plot(x, pred, label='Predicted', linestyle='--')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
