# Project Objective
Compare **TraceWin** GAP-models and Field-Map-models with **PyOrbit**.

# Plan for Comparison
- We compare the first elements of these sections: **MEBT, DTL, SPOKE, High-Beta**.
- If you agree, I'll provide the initial distribution for each section. (Or whatever you prefer, Benjamin)
- **0 current** to begin with.
- What exactly do we want to compare?
---

## MEBT

- [ ] **Objective**: We are considering the *first cavity* in the MEBT line. *(GAP vs FIELD)*
- [x] **Distribution File from TW**: Please see the file located in `MEBT/distribution`.

---

## DTL

- [ ] **Objective**: We want to check *DTL1*, the first drift tube linac section. *(GAP vs FIELD)*
- [ ] **Additional Comment**: If possible, when using the *GAP model*, analyze only *the first gap* in DTL1.  
      *(It might not be possible to do this with the field-model.)*
- [ ] **Distribution File from TW**: 

---

## SPK

- [ ] **Objective**: We will check the *first cavity*. *(GAP vs FIELD)*
- [ ] **Distribution File from TW**: 

---


# Beam Parameters MEBT

| **Parameter**                  | **X**       | **Y**       | **Z**       |
|--------------------------------|-------------|-------------|-------------|
| **Twiss Alpha** \(\alpha_{x,x'}\) / \(\alpha_{y,y'}\) / \(\alpha_z\) | -0.14280953     | -0.23746869     | -0.19102336   |
| **Twiss Beta** \(\beta_{x,x'}\) / \(\beta_{y,y'}\) / \(\beta_z\)     | 0.15035595  | 0.26458384     | 0.46179172     |
| **Sigma** \(\sigma_x\), \(\sigma_{x'}\), \(\sigma_y\), \(\sigma_{y'}\), \(\sigma_\phi\), \(\sigma_w\) | (value) | (value) | (value) |
| **\(\phi\)** (Phase)           | (value)     | (value)     | (value)     |
| **\(w\)** (Energy Spread)      | (value)     | (value)     | (value)     |
| **Particles** (\(N\))          | (value)     | (value)     | (value)     |
| **Current** (\(I\))            | (value)     | (value)     | (value)     |
| **Energy** (\(E\))             | (value)     | (value)     | (value)     |
| **Phase** (\(\theta\))         | (value)     | (value)     | (value)     |
| **Frequency** (\(f\))          | (value)     | (value)     | (value)     |
| **\(M_0\)**                    | (value)     | (value)     | (value)     |
| **Norm. RMS Emittance** \(\varepsilon_{n,x,x'}\) / \(\varepsilon_{n,y,y'}\) / \(\varepsilon_{n,z}\) | (value) | (value) | (value) |

> **Notes**:
> - The **Parameter** column lists the items you requested: Twiss \(\alpha\), Twiss \(\beta\), \(\sigma\), \(\phi\), \(w\), particles, current, energy, phase, frequency, \(M_0\), and normalized RMS emittances.
> - Columns **X**, **Y**, and **Z** let you place specific values for each plane (transverse \(x\), transverse \(y\), and longitudinal \(z\)).
> - For \(\sigma\)-values (beam size in position and angle), you can split them out more explicitly (e.g., \(\sigma_x\), \(\sigma_{x'}\), etc.) if you prefer separate table rows or additional columns.
> - Replace **(value)** with the actual numeric data (e.g., “2.0 mm” or “-1.2 deg,” etc.).



## High-Beta

- [ ] **Objective**: We are looking at **the first elliptical cavity** in the high-beta section. *(GAP vs FIELD)*
- [ ] **Distribution File from TW**: 
