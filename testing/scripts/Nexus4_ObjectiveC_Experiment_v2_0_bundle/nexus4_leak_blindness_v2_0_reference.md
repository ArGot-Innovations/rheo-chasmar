# Nexus 4 -- Objective C Deep-Time Detector Experiment v2.0

- script version: `2.0.0-merged-audited`
- script sha256: `178f5bd650c832ac94172f3009a5189f1b40292f901bd97b4ec32e779a7492be`
- python: `3.13.5`
- numpy: `2.3.5`
- primary horizon: 1050 years = 12600 ticks
- evaluation seeds: 40
- calibration seeds: 200
- MDR seeds: 32
- horizon seeds: 40
- target null false-alarm probability: 0.050

## Scope guardrails

- RESEARCH artifact, not canon or specification.
- The leaky absolute-deviation detector is a scalar analog, not the complete THDE runtime.
- The finite-horizon ramp MDR is not an asymptotic leak-blindness proof.
- `raw_sqrt` is not anytime-valid despite strong finite tested horizons.
- The Gaussian-mixture e-process is an anytime-valid control only under its iid Gaussian null assumptions.
- Cross-channel disagreement does not identify truth without independent reference/provenance.
- `ref_blue_green_known` assumes both epochs already exist; it does not implement reference authorization/migration.

## Self-tests

- PASS creep and instrument channel-1 streams are bit-identical
- PASS creep and instrument channel-2 streams differ
- PASS Green Sky returns exactly to original baseline
- PASS Green Sky reaches configured amplitude
- PASS green plateau is flat for 150 years
- PASS vectorized one-sided CUSUM matches sequential recurrence
- PASS vectorized two-sided CUSUM matches sequential recurrence
- PASS Gaussian-mixture e-process formula sanity check

## Calibration

| detector | threshold mode | h | base-horizon null FA |
|---|---|---:|---:|
| Leaky absolute-deviation accumulator, lambda=0.9 (tau=10) | empirical_fixed_horizon | 15.282149 | 0.050 |
| Leaky absolute-deviation accumulator, lambda=0.99 (tau=100) | empirical_fixed_horizon | 97.03843 | 0.050 |
| Leaky absolute-deviation accumulator, lambda=0.999 (tau=1000) | empirical_fixed_horizon | 839.39202 | 0.050 |
| Raw absolute-deviation sum, fixed threshold | empirical_fixed_horizon | 10148.474 | 0.050 |
| Centered cumulative sum / sqrt(k) [legacy] | empirical_fixed_horizon | 3.2250881 | 0.050 |
| One-sided CUSUM, nu=0.5 | empirical_fixed_horizon | 10.232037 | 0.050 |
| One-sided CUSUM, nu=0.1 | empirical_fixed_horizon | 42.731066 | 0.050 |
| One-sided CUSUM, nu=0.02 | empirical_fixed_horizon | 121.65711 | 0.050 |
| Two-sided scalar CUSUM, nu=0.1 | empirical_fixed_horizon | 45.386569 | 0.050 |
| Fixed-reference EWMA distance [blue only] | empirical_fixed_horizon | 1.7506736 | 0.050 |
| Known-epoch EWMA bank [blue+green already retained] | empirical_fixed_horizon | 1.7506736 | 0.050 |
| Cross-channel disagreement EWMA | empirical_fixed_horizon | 0.25513755 | 0.050 |
| Gaussian-mixture e-process, alpha=0.05 | analytic_anytime | 2.9957323 | 0.045 |

## Post-onset detection rate by condition

Null column is any-alarm rate because there is no onset.

| detector | null | creep | instrument | greensky | shock | confound |
|---|---:|---:|---:|---:|---:|---:|
| Leaky absolute-deviation accumulator, lambda=0.9 (tau=10) | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| Leaky absolute-deviation accumulator, lambda=0.99 (tau=100) | 0.12 | 1.00 | 1.00 | 1.00 | 1.00 | 0.07 |
| Leaky absolute-deviation accumulator, lambda=0.999 (tau=1000) | 0.12 | 1.00 | 1.00 | 1.00 | 1.00 | 0.12 |
| Raw absolute-deviation sum, fixed threshold | 0.10 | 1.00 | 1.00 | 1.00 | 1.00 | 0.10 |
| Centered cumulative sum / sqrt(k) [legacy] | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| One-sided CUSUM, nu=0.5 | 0.07 | 1.00 | 1.00 | 1.00 | 1.00 | 0.05 |
| One-sided CUSUM, nu=0.1 | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| One-sided CUSUM, nu=0.02 | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| Two-sided scalar CUSUM, nu=0.1 | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| Fixed-reference EWMA distance [blue only] | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| Known-epoch EWMA bank [blue+green already retained] | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| Cross-channel disagreement EWMA | 0.05 | 0.00 | 1.00 | 0.00 | 0.00 | 1.00 |
| Gaussian-mixture e-process, alpha=0.05 | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |

## Creep false alarms and detection delay

| detector | pre-onset FA | post-onset detection | median delay years |
|---|---:|---:|---:|
| Leaky absolute-deviation accumulator, lambda=0.9 (tau=10) | 0.03 | 1.00 | 27.83 |
| Leaky absolute-deviation accumulator, lambda=0.99 (tau=100) | 0.05 | 1.00 | 23.12 |
| Leaky absolute-deviation accumulator, lambda=0.999 (tau=1000) | 0.00 | 1.00 | 27.33 |
| Raw absolute-deviation sum, fixed threshold | 0.00 | 1.00 | 147.08 |
| Centered cumulative sum / sqrt(k) [legacy] | 0.05 | 1.00 | 33.04 |
| One-sided CUSUM, nu=0.5 | 0.03 | 1.00 | 17.00 |
| One-sided CUSUM, nu=0.1 | 0.00 | 1.00 | 14.67 |
| One-sided CUSUM, nu=0.02 | 0.00 | 1.00 | 20.75 |
| Two-sided scalar CUSUM, nu=0.1 | 0.00 | 1.00 | 15.33 |
| Fixed-reference EWMA distance [blue only] | 0.05 | 1.00 | 62.92 |
| Known-epoch EWMA bank [blue+green already retained] | 0.05 | 1.00 | 62.92 |
| Cross-channel disagreement EWMA | 0.05 | 0.00 | n/a |
| Gaussian-mixture e-process, alpha=0.05 | 0.03 | 1.00 | 32.96 |

## Green Sky reversal behavior

| detector | green plateau alarm fraction | quiet after return | alarm after return |
|---|---:|---:|---:|
| Leaky absolute-deviation accumulator, lambda=0.9 (tau=10) | 1.00 | 1.00 | 0.00 |
| Leaky absolute-deviation accumulator, lambda=0.99 (tau=100) | 1.00 | 0.90 | 0.10 |
| Leaky absolute-deviation accumulator, lambda=0.999 (tau=1000) | 1.00 | 0.00 | 1.00 |
| Raw absolute-deviation sum, fixed threshold | 1.00 | 0.00 | 1.00 |
| Centered cumulative sum / sqrt(k) [legacy] | 1.00 | 0.00 | 1.00 |
| One-sided CUSUM, nu=0.5 | 1.00 | 0.00 | 1.00 |
| One-sided CUSUM, nu=0.1 | 1.00 | 0.00 | 1.00 |
| One-sided CUSUM, nu=0.02 | 1.00 | 0.00 | 1.00 |
| Two-sided scalar CUSUM, nu=0.1 | 1.00 | 0.00 | 1.00 |
| Fixed-reference EWMA distance [blue only] | 1.00 | 1.00 | 0.00 |
| Known-epoch EWMA bank [blue+green already retained] | 0.00 | 1.00 | 0.00 |
| Cross-channel disagreement EWMA | 0.00 | 1.00 | 0.00 |
| Gaussian-mixture e-process, alpha=0.05 | 1.00 | 0.00 | 1.00 |

## Finite-horizon minimum detectable linear-ramp rate (MDR50)

Lower is better for THIS configured finite horizon only.

| detector | MDR50 sigma/year | years per 1-sigma displacement |
|---|---:|---:|
| Leaky absolute-deviation accumulator, lambda=0.9 (tau=10) | 0.00062387698 | 1603 |
| Leaky absolute-deviation accumulator, lambda=0.99 (tau=100) | 0.00033280423 | 3005 |
| Leaky absolute-deviation accumulator, lambda=0.999 (tau=1000) | 0.00023315452 | 4289 |
| Raw absolute-deviation sum, fixed threshold | 0.00019016567 | 5259 |
| Centered cumulative sum / sqrt(k) [legacy] | 5.7608291e-05 | 17359 |
| One-sided CUSUM, nu=0.5 | 0.00017185992 | 5819 |
| One-sided CUSUM, nu=0.1 | 8.6908986e-05 | 11506 |
| One-sided CUSUM, nu=0.02 | 3.3123492e-05 | 30190 |
| Two-sided scalar CUSUM, nu=0.1 | 9.1528431e-05 | 10926 |
| Fixed-reference EWMA distance [blue only] | 0.0016678656 | 600 |
| Known-epoch EWMA bank [blue+green already retained] | 0.0016678656 | 600 |
| Cross-channel disagreement EWMA | n/a | n/a |
| Gaussian-mixture e-process, alpha=0.05 | 5.8938696e-05 | 16967 |

## Horizon robustness: same threshold, longer null horizon

This is a finite stress test at x1/x4/x16, not proof of infinite-horizon validity.

| detector | x1 | x4 | x16 |
|---|---:|---:|---:|
| Leaky absolute-deviation accumulator, lambda=0.9 (tau=10) | 0.03 | 0.17 | 0.42 |
| Leaky absolute-deviation accumulator, lambda=0.99 (tau=100) | 0.05 | 0.35 | 0.72 |
| Leaky absolute-deviation accumulator, lambda=0.999 (tau=1000) | 0.05 | 0.20 | 0.95 |
| Raw absolute-deviation sum, fixed threshold | 0.07 | 1.00 | 1.00 |
| Centered cumulative sum / sqrt(k) [legacy] | 0.03 | 0.03 | 0.03 |
| One-sided CUSUM, nu=0.5 | 0.10 | 0.42 | 0.78 |
| One-sided CUSUM, nu=0.1 | 0.03 | 0.10 | 0.42 |
| One-sided CUSUM, nu=0.02 | 0.03 | 0.28 | 0.85 |
| Two-sided scalar CUSUM, nu=0.1 | 0.03 | 0.12 | 0.47 |
| Fixed-reference EWMA distance [blue only] | 0.10 | 0.10 | 0.10 |
| Known-epoch EWMA bank [blue+green already retained] | 0.10 | 0.10 | 0.10 |
| Cross-channel disagreement EWMA | 0.00 | 0.23 | 0.62 |
| Gaussian-mixture e-process, alpha=0.05 | 0.03 | 0.03 | 0.03 |

## Exact leaky-memory analytic controls

### Constant-severity recurrence

| lambda | threshold | exact severity floor | q_inf at 0.5x floor | q_inf at 1.5x floor |
|---:|---:|---:|---:|---:|
| 0.900 | 1.0 | 0.1 | 0.500 | 1.500 |
| 0.990 | 1.0 | 0.01 | 0.500 | 1.500 |
| 0.999 | 1.0 | 0.001 | 0.500 | 1.500 |

### Normalized linear-EWMA effective memory

| lambda | tau=1/(1-lambda) | N_eff=(1+lambda)/(1-lambda) | stationary SD |
|---:|---:|---:|---:|
| 0.900 | 10.0 | 19.0 | 0.229416 |
| 0.990 | 100.0 | 199.0 | 0.070888 |
| 0.999 | 1000.0 | 1999.0 | 0.022366 |

## Historical pre-pilot predictions P1-P8

P3/P4/P5 are intentionally preserved even though earlier pilots falsified them.

| id | kind | historical v1.1 verdict | v2.0 rerun verdict | statement |
|---|---|---|---|---|
| P1 | analytic | **PASS** | **PASS** | Leaky detectors have a minimum-detectable-rate at least 3x worse than raw_sqrt, and it does NOT improve as lambda->1 fast enough to close the gap. |
| P2 | empirical | **PASS** | **PASS** | Every detector fires on the SHOCK condition. Fast shocks are not the problem. |
| P3 | analytic | **FAIL** | **FAIL** | raw_fixed cannot be calibrated: it either alarms on the null or never alarms at all. It measures elapsed time, not departure. |
| P4 | empirical | **FAIL** | **FAIL** | CUSUM with nu=0.5 is blind to the Green Sky drift rate (fire_rate < 0.5 on 'creep'). CUSUM does not automatically fix slow drift; nu is a floor. |
| P5 | empirical | **FAIL** | **FAIL** | raw_sqrt has the lowest minimum-detectable-rate of all single-channel detectors tested. |
| P6 | empirical | **PASS** | **PASS** | With a FIXED reference, at least one detector stays latched for >50% of the green plateau -- i.e. it spends 150 years reporting that a genuinely green sky is anomalous. |
| P7 | analytic | **PASS** | **PASS** | Conditions 'creep' and 'instrument' produce identical channel-1 streams, so every single-channel detector gives identical results on both. Integral tracking alone cannot solve the instrument problem. |
| P8 | empirical | **PASS** | **PASS** | The cross-channel detector fires on 'instrument' and NOT on 'creep', separating world change from instrument change. |

## Post-pilot independent-replication targets R1-R6

These were registered after observing v1.1, so they are replication targets, not pre-pilot discoveries.

| id | class | verdict | target |
|---|---|---|---|
| R1 | post-pilot replication | **PASS** | raw_fixed loses fixed-horizon calibration badly by x4 (null FA >= 0.50). |
| R2 | post-pilot replication | **PASS** | CUSUM nu=0.5 detects the configured 6-sigma creep excursion (post-onset detection >= 0.90). |
| R3 | post-pilot replication | **PASS** | raw_sqrt and CUSUM nu=0.02 have finite-horizon MDR50 values within a factor of 2. |
| R4 | new control | **PASS** | The Gaussian-mixture e-process remains <=10% empirical null FA at every tested horizon x1/x4/x16. |
| R5 | post-pilot replication | **PASS** | Cross-channel disagreement is low on common-mode creep (<=0.10) and high on instrument drift and confound (>=0.90 each). |
| R6 | reference semantics | **PASS** | The blue-only reference alarms for most of the green plateau, while the pre-known blue+green bank alarms for substantially less of that plateau. |

## Interpretation guardrails

- A finite-horizon detector win does not make that detector canonical Nexus machinery.
- A fixed threshold that survives x16 has not been proven safe for an unbounded horizon.
- The e-process has a time-uniform bound only under the modeled iid Gaussian null; model misspecification still matters.
- `creep` is a growing state displacement, not a direct model of THDE severity_k.
- The exact q fixed-point control and linear-EWMA variance control are mathematics of simplified recurrences, not evidence about Nexus implementation.
- The known blue+green reference bank demonstrates retained-epoch recognition only; it does not solve who authorizes a new reference.
- Cross-channel disagreement establishes identifiability limits and disagreement detection, not absolute truth.

JSON written to /mnt/data/nexus4_leak_blindness_v2_0_reference.json
