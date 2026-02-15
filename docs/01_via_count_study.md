# Phase 1 – Spatially Confined Via Redundancy Optimization
(Literature-Grounded Electro-Thermal Modeling Under 1 W RF Excitation)

---

## 1. Research Objective

This phase investigates thermo-mechanical stability of a glass interposer with varying numbers of copper Through-Glass Vias (TGVs) under 1 W RF excitation conditions.

The objective is to determine the optimal via redundancy within a spatially confined footprint that minimizes thermally induced stress.

Unlike conventional redundancy expansion approaches, all vias are restricted within a fixed circular region, allowing controlled evaluation of redundancy density effects.

---

## 2. Spatial Confinement Constraint (Primary Differentiator)

All via configurations (1–5 vias) satisfy:

- Every via lies inside a circular region of 0.08 mm diameter
- The circle is centered at the origin (0, 0)
- Via diameter: 0.02 mm
- Glass substrate: 0.4 mm × 0.4 mm × 0.2 mm
- Units: millimeters (mm)

Increasing via count does NOT increase occupied footprint.
Instead, it increases redundancy density within the same confined region.

This isolates density-driven thermal interaction and mechanical constraint amplification effects, rather than footprint expansion effects.

---

## 3. Literature-Based Heat Source Derivation (1 W Condition)

Heat source values were derived from:

L. Chen et al.,
“Electro-thermal Co-Design and Verification of TGV Transmission Structures for High-Power High-Frequency Applications,” TechRxiv, 2025.

The referenced work reports interface heat flux values under 1 W @ 18 GHz excitation.

Reported maximum interface heat flux:

| Via Count | Interface Heat Flux q″ (W/m²) |
|------------|--------------------------------|
| 1 (Single) | 3.51 × 10⁵ |
| 2 (Dual)   | 1.91 × 10⁵ |
| 3 (Triple) | 1.87 × 10⁵ |
| 4 (Quad)   | 1.87 × 10⁵ |
| 5 (Penta)  | 1.87 × 10⁵ |

These values were used to back-calculate the dissipated thermal power per via.

---

## 4. Conversion to Volumetric Heat Generation

Via geometry:

- Radius: 0.01 mm (1 × 10⁻⁵ m)
- Height: 0.2 mm (2 × 10⁻⁴ m)

Via volume:

V = π r² h  
V = 6.283 × 10⁻¹⁴ m³

Derived dissipated power per via:

| Via Count | Heat per Via (W) |
|------------|-------------------|
| 1 | 4.41 × 10⁻³ |
| 2 | 2.40 × 10⁻³ |
| 3 | 2.35 × 10⁻³ |
| 4 | 2.35 × 10⁻³ |
| 5 | 2.35 × 10⁻³ |

Volumetric heat generation applied in ANSYS:

q‴ = Q / V

| Via Count | q‴ (W/m³) |
|------------|------------|
| 1 | 7.02 × 10¹⁰ |
| 2 | 3.82 × 10¹⁰ |
| 3 | 3.74 × 10¹⁰ |
| 4 | 3.74 × 10¹⁰ |
| 5 | 3.74 × 10¹⁰ |

These volumetric heat sources were applied uniformly within each copper via.

---

## 5. Modeling Assumptions

This model assumes:

- RF excitation = 1 W (as reported in literature)
- Reported interface heat flux represents EM-to-thermal conversion
- Dissipated power is fully converted into heat inside copper vias
- Heat generation is uniformly distributed within each via
- Radiation and secondary EM losses are not explicitly modeled
- Higher-order electro-thermal coupling effects are neglected

This controlled simplification enables direct comparison of redundancy density effects under identical excitation conditions.

---

## 6. Mesh Strategy

To ensure accurate stress prediction near critical interfaces, a structured mesh strategy was adopted.

### Local Refinement

- Fine mesh applied at copper–glass interfaces
- Increased mesh density within the 0.08 mm confined region
- Gradual mesh coarsening away from the via cluster

### Convergence Validation

Mesh independence was verified through:

- Element size variation study
- Monitoring maximum principal stress convergence
- Ensuring peak stress stabilization

Convergence data is available in:

data/mesh_convergence/

Mesh screenshots for each configuration are stored in:

ansys/mesh/

Final mesh density was selected based on stress convergence stability rather than temperature alone.

---

## 7. Boundary Conditions

- Volumetric heat generation applied only to copper vias
- Convection boundary condition applied to external surfaces
- Coupled thermal–structural analysis performed
- Identical boundary conditions used for all via counts

This ensures that performance differences arise solely from redundancy density variations.

---

## 8. Engineering Insight

Because all vias are confined within the same 0.08 mm diameter region, increasing via count increases redundancy density rather than expanding thermal footprint.

Literature data shows exponential saturation of interface heat flux beyond N = 2.

This indicates:

- Strong thermal interaction between adjacent vias
- Local heat concentration saturation
- Mechanical constraint amplification in glass
- Non-monotonic stress reduction behavior

The 2-via configuration provides the most balanced redundancy density under spatial confinement.

---

## 9. Significance

This study demonstrates that optimal via redundancy must be evaluated under spatial confinement constraints.

It provides a literature-grounded, controlled electro-thermal modeling framework
for analyzing clustered TGV architectures
in advanced glass interposer systems.
