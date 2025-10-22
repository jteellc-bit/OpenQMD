# Single-Coil Module (OpenQMD)

This folder contains a self-contained single-coil surrogate demo for OpenQMD.
Files:
- Notebooks/OpenQMD_SingleCoil_Surrogate.ipynb : interactive demo
- Scripts/singlecoil_surrogate_core.py : model definition + helper
- Scripts/singlecoil_mpc_controller.py : simple MPC driver
- Data/singlecoil_synthetic_seed.csv : example synthetic seed data
- Results/* : example outputs, plots, and small saved model

To run:
1. Open the notebook in Notebooks/ and run all cells.
2. Optional: replace Data/seed CSV with your measured dataset and re-run.
