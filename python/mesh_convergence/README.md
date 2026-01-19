# Mesh Convergence Analysis (Python)

This directory contains the finalized Python implementation for the mesh convergence analysis of the TGV thermal model.

The analysis evaluates the convergence behavior of the maximum temperature with respect to mesh size and applies nonlinear regression to estimate the mesh-independent solution by extrapolation to vanishing element size.


## Overview

The mesh convergence study is based on numerical results obtained from ANSYS thermal simulations.
For each mesh configuration, the maximum temperature of the model is extracted as the quantity of interest, since peak values are generally the most sensitive to mesh resolution in thermal analyses.

A nonlinear regression model is used to describe the convergence trend and to estimate the asymptotic maximum temperature as the mesh size approaches zero.


## Methodology

- A mesh size sweep is performed, and the maximum temperature is recorded for each element size.
- The convergence behavior is modeled using a nonlinear exponential function of the form:

  \[
  T_{\max}(h) = T_\infty + A \exp\left(-\frac{B}{h}\right),
  \]

  where \( h \) is the characteristic element size, and \( T_\infty \) represents the extrapolated mesh-independent temperature.

- Model parameters are estimated using the Levenberg–Marquardt algorithm implemented in `scipy.optimize.curve_fit`.
- The converged temperature \( T_\infty \) is obtained by extrapolating the fitted model to the limit \( h \to 0 \) and is visualized as a horizontal reference line in the convergence plot.


## Files

- `mesh_convergence.py`  
  Final Python script performing the mesh convergence analysis.
  The script:
  - fits the nonlinear regression model,
  - generates the mesh convergence figure,
  - exports raw mesh convergence data and regression parameters to CSV files.

- `requirements.txt`  
  Python dependencies required to run the analysis.


## Output

Running the script generates the following outputs in the same directory:

- **Figure**
  - `mesh_convergence.png`  
    Mesh convergence plot showing FEM simulation data, the nonlinear regression curve, and the extrapolated converged temperature \( T_\infty \).

- **Data**
  - `mesh_convergence_data.csv`  
    Raw mesh convergence data containing element size and maximum temperature.
  - `mesh_convergence_params.csv`  
    Estimated regression parameters, including the extrapolated converged temperature \( T_\infty \).


## Remarks

The extrapolated converged temperature provides a quantitative and mesh-independent reference value, allowing the final mesh resolution to be selected based on numerical accuracy rather than visual inspection alone. 
This approach ensures reliable thermal predictions while avoiding unnecessary computational cost.
