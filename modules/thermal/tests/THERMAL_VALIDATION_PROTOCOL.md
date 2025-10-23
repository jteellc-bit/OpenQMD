# OpenQMD Thermal Validation Protocol
Version 1.0.0 — October 2025

## Purpose
Defines empirical and simulation validation framework for the OpenQMD Thermal Integration Module.
Evaluates QMD control algorithms when augmented with real-time thermal imaging and point-sensor data fusion.

## Objectives
1. Validate temperature feedback accuracy and latency.
2. Correlate thermal imaging data with electromagnetic loss estimates.
3. Quantify energy savings from thermally adaptive control.
4. Establish baseline protocols for replication.

## Test Architecture
### Hardware Setup
- Motor/Generator: BLDC or PMSM motor under variable load.
- Sensors: IR camera (≥60 Hz) + thermistors (stator, rotor, bearings).
- Controller: QMD DE4/DE5 recursive algorithm.
- Logging: 1 kHz electrical data, 10 Hz thermal overlay.

### Software
- Simulation: OpenQMD/SimPy or PyTorch DE5 recursion.
- Control: Adaptive feedback logic.
- Data Fusion: Kalman or Gaussian process regression.

## Procedure
1. Calibration: Align timestamps, record baseline.
2. Operation: Run tests at 20–100% torque; record P_in, P_out, T_field, Ξ_coherent.
3. Adaptive Control: Enable thermal feedback, measure efficiency/stability.
4. Data Analysis: Cross-correlate heat variance and EM losses.

## Metrics
| Metric | Symbol | Target | Description |
|---------|---------|---------|-------------|
| Thermal Delay | δt | <100 ms | Response time |
| Efficiency Gain | Δη | ≥10% | vs static control |
| ΔT Reduction | ΔT_max | −15% | Peak temperature drop |
| Stability | S_i | ≥0.9 | Coherence–temperature correlation |

## Reporting
Export `.csv`, `.mp4`, and `.json` to `/data/thermal_validation/YYYYMMDD_runXX/`.

## Extensions
- ML-based predictive control.
- Optical flow modeling.
- Multi-motor comparative studies.
