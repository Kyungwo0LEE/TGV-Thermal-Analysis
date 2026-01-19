# Figures

This directory contains figures generated during the TGV thermal analysis, with a focus on the mesh convergence behavior of the maximum temperature.

The figures summarize numerical results obtained from ANSYS simulations and subsequent post-processing using Python, including nonlinear regression–based extrapolation to estimate mesh-independent solutions.


## Structure

- `mesh_convergence/`  
  Final figures related to the mesh convergence study, including convergence plots that illustrate the extrapolated converged temperature \( T_\infty \) obtained from nonlinear regression analysis.

  - `archive/`  
    Contains figures generated during the early stage of the study using a limited mesh dataset or preliminary convergence criteria.
    These figures are retained for reference and to document the development of the analysis methodology.


## Notes

Only the finalized figures are intended to represent the final results of the study.
Archived figures are preserved to provide traceability of the analysis workflow, from preliminary exploration to the finalized mesh convergence assessment.
