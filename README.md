# Thermal and Thermo-Mechanical Analysis of TGV Glass Substrate
ANSYS-based thermal analysis of Through-Glass Via (TGV) glass substrates with a focus on mesh strategy and parametric studies.

## Overview
This repository documents a two-month undergraduate research project focused on the thermal and thermo-mechanical behavior of Through-Glass Via (TGV) glass substrates with redundant via structures.

The study is simulation-based and conducted using ANSYS Mechanical.
It aims to investigate the trade-off between enhanced thermal performance and increased thermo-mechanical stress caused by thermal expansion mismatch between copper vias and glass substrates.

## Research Background
Redundant TGV structures, in which multiple vias are connected to a single metal pad, are widely adopted to reduce electrical loss and increase effective conductivity due to enlarged conductive cross-sectional area.

From a thermal perspective, increasing the number of vias can improve heat conduction and increase effective thermal conductivity (k_eff).
However, the coefficient of thermal expansion (CTE) mismatch between copper and glass induces significant thermal stress at the Cu–glass interfaces, potentially leading to crack initiation.

Therefore, continuously increasing the number of redundant vias may introduce structural reliability issues despite thermal benefits.

## Research Objectives
The objectives of this study are:
- To model glass substrates with varying numbers of redundant TGVs connected to a single metal pad
- To evaluate heat spreading behavior and effective thermal conductivity as the number of vias increases
- To analyze thermal stress and stress concentration caused by CTE mismatch between copper and glass
- To identify structural limitations on the maximum allowable number of vias per pad from a thermo-mechanical reliability perspective
- To predict potential crack initiation locations based on hotspot temperature and maximum thermal stress

## Methodology
- 3D modeling of glass substrates with 1, 2, and 4 vias per pad
- Local mesh refinement at Cu–glass interfaces to capture stress concentration
- Steady-state thermal analysis to evaluate temperature distribution
- Calculation of effective thermal conductivity (k_eff) for each configuration
- Sequential thermo-mechanical analysis using thermal results as input
- Identification of hotspot regions and maximum von Mises stress locations

## Tools & Environment
- ANSYS Workbench / Mechanical
- ANSYS SpaceClaim
- Python (post-processing and data visualization)

## Project Scope
This study focuses on identifying physical trends and reliability limits
rather than optimizing a final industrial design.
Simplified geometries are intentionally used to isolate the effects of
redundant TGV configurations on thermal performance and structural stability.

## Repository Structure
- `geometry/` : CAD and SpaceClaim geometry files
- `mesh/` : Mesh strategies and convergence studies
- `simulation/`
  - `thermal/` : Steady-state thermal analyses
  - `structural/` : Thermo-mechanical stress analyses
- `parametric_study/` : Via count and geometric variation cases
- `results/`
  - `temperature_distribution/`
  - `effective_conductivity/`
  - `thermal_stress/`
- `docs/` : Research notes and literature review
- `logbook/` : Weekly research records

## Expected Contributions
- Quantitative evaluation of the trade-off between thermal performance
  and thermo-mechanical reliability in redundant TGV structures
- Identification of critical stress locations associated with
  via multiplicity
- Design guidelines for determining an upper bound on the number of
  vias per pad considering both thermal and structural constraints

## Author
Kyungwoo Lee  
Undergraduate Student, Mechanical Engineering
