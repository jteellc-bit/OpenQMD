# OpenQMD — 3×3 Coupled Phase Motor Prototype

## Overview
This module documents the experimental implementation of a DE4-based Quantum Motor Driver (QMD) using a 3×3 coupled-phase axial motor.
The system explores how Dynamic Equilibrium (DE4) field relationships manifest in real electromechanical hardware.

## Structure
- design/ — mechanical, electromagnetic, and PCB design files
- firmware/ — embedded control for stator and rotor inverters
- simulation/ — Python and Jupyter tools for DE4–QMD surrogate control
- results/ — validation data, fidelity metrics, and post-run visualizations

## Objectives
- Demonstrate DE4-derived control in a six-phase, ternary-state configuration
- Validate surrogate MPC performance under physical constraints
- Measure coupling factor (k), torque-per-amp, and constructive field stability

## Status
Preliminary surrogate validation complete (correlation 0.56–0.68 across observables).
Hardware construction underway. FEM and bench tests to follow.

## Repository
This prototype is part of the OpenQMD Project.
All data, models, and control software are released under an open license for collaborative research.
