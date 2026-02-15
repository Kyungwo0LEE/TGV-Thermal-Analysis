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

## Material Consideration

The thermo-mechanical response in this study is strongly influenced by the material mismatch between copper vias and the glass substrate.

Copper exhibits:

- High thermal conductivity
- High coefficient of thermal expansion (CTE)

Glass exhibits:

- Low thermal conductivity
- Low CTE
- Brittle mechanical behavior

The significant CTE mismatch between copper and glass induces tensile principal stress at the via–glass interface under thermal loading.

Detailed material properties are provided in:
docs/material_properties.md

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

---

## 10. Results – Thermal and Structural Response

### 10.1 Maximum Temperature

| Via Count | Maximum Temperature (°C) |
|------------|--------------------------|
| 1 | 30.821 |
| 2 | 28.687 |
| 3 | 30.738 |
| 4 | 33.097 |
| 5 | 36.890 |

Temperature contour images are available in:

figures/phase1_temperature/

The temperature decreases when increasing redundancy from 1 to 2 vias.
However, beyond 2 vias, temperature rises again as via density increases within the confined 0.08 mm region.

This indicates that thermal interaction between adjacent vias begins to dominate beyond the dual configuration.

---

### 10.2 Maximum Principal Stress

| Via Count | Maximum Principal Stress (MPa) |
|------------|--------------------------------|
| 1 | 19.488 |
| 2 | 16.351 |
| 3 | 22.930 |
| 4 | 35.609 |
| 5 | 44.922 |

Stress contour images are available in:

figures/phase1_max_principal_stress/

Maximum principal stress was used as the primary evaluation metric, since glass is a brittle material and crack initiation is governed by tensile principal stress rather than von Mises equivalent stress.

---

### 10.3 Observed Trend

The results reveal a non-monotonic behavior:

- Increasing via count from 1 to 2 reduces both temperature and stress.
- Beyond 2 vias, both temperature and principal stress increase significantly.
- At 5 vias, principal stress increases by approximately 175% compared to 2 vias.

This behavior is attributed to:

- Increased redundancy density within the confined region
- Strong thermal interaction between closely spaced vias
- Mechanical constraint amplification in the glass substrate
- Localized stress concentration at via–glass interfaces

The 2-via configuration demonstrates the most favorable balance between thermal reduction and mechanical reliability under spatial confinement.

---

### 10.4 Engineering Interpretation

Although redundancy initially improves heat distribution, excessive via clustering within a fixed footprint leads to:

- Heat flux saturation
- Localized thermal accumulation
- Increased tensile stress in brittle glass

Therefore, optimal redundancy must consider density effects rather than simply increasing via count.

Under the imposed 0.08 mm spatial constraint, the dual-via configuration represents the optimal electro-thermal–mechanical balance.

---

### 10.5 Confinement-Induced Thermal Bottleneck

The increase in temperature and maximum principal stress beyond the dual-via configuration suggests the emergence of a confinement-induced thermal bottleneck.

Because all vias are restricted within the same 0.08 mm diameter region, increasing via count does not expand the heat dissipation footprint.
Instead, it increases redundancy density within a fixed thermal pathway.

As via density increases:

- Heat spreading inside the glass becomes spatially constrained
- Local thermal interaction between adjacent vias intensifies
- Effective heat dissipation paths become relatively limited
- Tensile principal stress in the brittle glass substrate is amplified

This behavior indicates that excessive redundancy within a confined footprint may degrade structural reliability despite initial improvements in heat distribution.

Therefore, optimal via redundancy must consider density-driven thermal bottleneck effects rather than simply increasing the number of vias.
