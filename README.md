<img width="936" height="1436" alt="paper  5 graphic" src="https://github.com/user-attachments/assets/7c15ad1c-1bd1-43db-aa4d-d57c76b6ecb5" />
<img width="1536" height="1024" alt="hybrid paper image" src="https://github.com/user-attachments/assets/4d0cb991-d31e-40b8-be9f-ad40b37d379c" />
<img width="1536" height="1024" alt="paper 4 graphic" src="https://github.com/user-attachments/assets/3da6ac73-5ce3-49cb-86b4-d84fd10d47ef" />
<img width="5035" height="2184" alt="image" src="https://github.com/user-attachments/assets/efdaf70c-975e-4b49-b41a-3d4b1b5d753e" />
QMD v1.1 — “OpenESC Minimal”
Purpose:
A lightweight, open-source–friendly analytic efficiency model derived from early DE-class formulations. Designed for embedded controllers and educational use.
Characteristics:
    • Closed-form η(τ) curve using a simplified 3-parameter kernel
    • Float-only microcontroller variant (no math.h)
    • Symmetric response around τ = 1
    • Stable for lookup tables and fast simulation
    • Intended as a “gift” model for OpenMESC, Plug’n’Play FOC, and hobby ESC tooling
When to use v1.1:
    • You need speed over accuracy
    • You are running on small MCUs (F0/F1-class, ESP32)
    • You need something easy to integrate into an open-source repo
    • You do not need DE-level predictive performance

QMD v2.0 — “High-Fidelity Engineering Model”
Purpose:
A formally corrected and calibrated version of the QMD kernel designed for engineering-grade prediction. Based on a refined DE5-inspired structure with correction terms for real motor behavior.
Characteristics:
    • Fully corrected analytic structure (post-DE5 reconciliation)
    • Accurate across wide voltage and loading regimes
    • Includes forward (τ → η) and inverse (η → τ) mappings
    • Stable derivatives for optimization and MPC
    • Supports “dominance map” analysis and sensitivity sweeps
    • Produces trustworthy efficiency predictions for practical motors
When to use v2.0:
    • Hardware design
    • Motor tuning and optimization
    • High-accuracy simulations
    • Cross-validation against real dyno or telemetry data
Status:
v2.0 is considered the first mature release of the QMD series.

QMD v3.0 — “Dual-Kernel DE5-Class Model (A/B)”
Purpose:
A next-generation, dual-track model combining:
    • Kernel A: Algebraic DE5 polynomial
    • Kernel B: Physics-weighted DE5 response
This allows direct A/B evaluation, cross-consistency testing, and hybridized efficiency predictions.
Characteristics:
    • Two kernels (A: algebraic, B: physically calibrated) evaluated side-by-side
    • Stability-checked across 10 tests (1–7 essential, 8–10 optional academic completeness)
    • Supports τ sweeps, q sweeps, PWM sweeps, cross-sensitivity maps, curvature analysis
    • Fully MCU-capable via polynomial reciprocal implementation
    • Version 3.0 introduces the first truly robust η(τ) ↔ τ(η) dual-mapping
    • Fully self-contained (no dependencies, analytic-only)
When to use v3.0:
    • High-end ESC design
    • Research-grade modeling
    • Comparative studies with DE5 or other physics kernels
    • Any application requiring maximal accuracy and stability
Status:
v3.0 is the current flagship model, superseding v2.0 in accuracy and structure while retaining backward compatibility.
