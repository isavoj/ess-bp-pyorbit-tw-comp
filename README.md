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

## High-Beta

- [ ] **Objective**: We are looking at **the first elliptical cavity** in the high-beta section. *(GAP vs FIELD)*
- [ ] **Distribution File from TW**: 

# Beam Parameters MEBT

| **Parameter**                           | **X**        | **Y**        | **Z**        | **w/ \$\theta$ / Global**     |
|-----------------------------------------|------------:|------------:|------------:|---------------:|
| **Twiss Alpha** \($\alpha_{x,x'}$, $\alpha_{y,y'}$, $\alpha_{z,z'}$\) | -0.14280953 | -0.23746869 | -0.19102336 |      -         |
| **Twiss Beta (mm/n.mrad) and (deg/n.MeV)** \($\beta_{x,x'}$, $\beta_{y,y'}$, $\beta_{z,z'}$, $\beta_{\phi,w}$\)     |  0.15035595 |  0.26458384 |  0.46179172 |      305.9117        |
| **Sigma (mm) and (deg)** \($\sigma_x$, $\sigma_y$, $\sigma_z$ , $\sigma_\phi$\)          |  0.5437     |  0.7268     |  1.5324     |      7.3970         |
| **Sigma (mrad) and (keV)** \($\sigma_{x'}$, $\sigma_{y'}$, $\sigma_{z'}$ , $\sigma_w$\)  |  3.6527     |  2.8235     |  3.3783     |      24.6174         |
| **Norm. RMS Emittance(pi.mm.mrad), and (pi.deg.MeV)** \($\varepsilon_{x,x'}$, $\varepsilon_{y,y'}$, $\varepsilon_{z,z'}$, $\varepsilon_{\phi,w}$\) |  0.1729169   |  0.1756221   |  0.4507168   |  0.1788611             |
| **Energy Spread (MeV)** \($\delta w$\)                                         |     -       |     -       |     -       |  0      |
| **Phase (deg)** \($\delta \theta$\)                                            |     -       |     -       |     -       | -63.314        |
| **Particles (Nbr)** \($N$\)                                       |     -       |     -       |     -       |  8660          |
| **Current** \($I$\)                                               |     -       |     -       |     -       |  0             |
| **Kinetic Energy (MeV)** \($E$\)                                  |     -       |     -       |     -       |  3.6224112     |
| **Realtivistic Beta** \($B$\)                                  |     -       |     -       |     -       |  0.0876     |
| **Frequency (MHz)** \($f$\)                                       |     -       |     -       |     -       |  352.21        |
| **$M_0$ (MeV)**                                                   |     -       |     -       |     -       |  938.276       |

```math
\begin{bmatrix}
(m) 2.955900 \times 10^{-7} & 2.807543 \times 10^{-7} & 0 & 0 & 0 & 0 \\
(rad) 2.807543 \times 10^{-7} & 1.334187 \times 10^{-5} & 0 & 0 & 0 & 0 \\
(m) 0 & 0 & 5.282922 \times 10^{-7} & 4.741517 \times 10^{-7} & 0 & 0 \\
 (rad)0 & 0 & 4.741517 \times 10^{-7} & 7.972095 \times 10^{-6} & 0 & 0 \\
 (m)0 & 0 & 0 & 0 & 2.348198 \times 10^{-6} & 9.788631 \times 10^{-7} \\
\Delta_P / P 0 & 0 & 0 & 0 & 9.788631 \times 10^{-7} & 1.159048 \times 10^{-5}
\end{bmatrix}
