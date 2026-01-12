# Mesh Convergence Data

This directory contains numerical data used for the mesh convergence study of the TGV thermal analysis.

## Files

- `mesh_convergence_data.csv`  
  Final mesh convergence dataset used for nonlinear regression analysis.
  This file includes:
  - element size (m)
  - maximum temperature obtained from ANSYS simulations
  - fitted maximum temperature predicted by the regression model

- `mesh_convergence_params.csv`  
  Parameters obtained from the nonlinear regression analysis, including:
  - estimated converged maximum temperature
  - regression coefficients
  - reference converged temperature based on the finest mesh result

## Notes

Preliminary datasets generated during early mesh studies have been moved to
the `archive/` directory and are retained for reference and reproducibility.
