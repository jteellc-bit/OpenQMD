# QMD Global Efficiency v2

This package contains:
- The latest dissipative retrained QMD model (3-output: torque, loss, utility)
- System-scale simulation of global adoption scenarios
- Energy, supply, and CO₂ impact data
- Configs, logs, and reproducibility scripts

## Scenarios
| Scenario   | Years | Installed Fraction | Energy Saved (TWh) | Repurposed Supply (TWh) | CO₂ Avoided (Mt) |
|-------------|--------|--------------------|--------------------|--------------------------|------------------|
| SlowAdopt   | 15     | 0.3667             | 2149.64            | 1289.79                  | 859.86           |
| MedAdopt    | 15     | 0.7941             | 5373.12            | 3223.87                  | 2149.25          |
| FastAdopt   | 15     | 0.9648             | 7622.61            | 4573.57                  | 3049.04          |

All outputs derived from trained QMD v2 dissipative model.
