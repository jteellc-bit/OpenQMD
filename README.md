# OpenQMD — Simulation Suite  
**Directory:** `/OpenQMD/simulations/`  
**Purpose:** Numerical exploration of efficiency and collective response behaviors under varying λₗ (Lambda-collective) and dynamic load conditions.

## Contents
| File | Description |
|------|--------------|
| `singlecoil_lambda_scan.py` | Single-coil reference model for baseline Λₗ efficiency mapping. |
| `triplegrid_lambda_scan.py` | Three-grid interaction model with coherence analysis. |
| `ff_turbine_simulation.py` | ferrofluid turbine surrogate model testing multi-stage response. |

## Run Commands
```bash
python3 singlecoil_lambda_scan.py
python3 triplegrid_lambda_scan.py
python3 ff_turbine_simulation.py
```

## Output Files
| Script | Output CSV | Columns |
|--------|-------------|----------|
| `singlecoil_lambda_scan.py` | `singlecoil_summary_table.csv` | lambda_L, mean_efficiency, std_efficiency, torque_rms |
| `triplegrid_lambda_scan.py` | `triplegrid_summary.csv` | lambda_L, mean_eff, std_eff, mean_coherence |
| `ff_turbine_simulation.py` | `ff_turbine_summary.csv` | lambda_L, rpm, stages, efficiency, elec_output |

© OpenQMD Research Group — Simulation Infrastructure (Deliverable 1, DE2 → DE4 → QMD Series)
