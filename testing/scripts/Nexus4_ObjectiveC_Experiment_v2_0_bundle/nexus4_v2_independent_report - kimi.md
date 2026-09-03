# Nexus 4 Objective C Deep-Time Detector Experiment v2.0 — Independent Run Report

**Run date:** 2026-09-03  
**Protocol version:** RUN_PROTOCOL_nexus4_leak_blindness_v2_0.md  
**Script version:** 2.0.0-merged-audited  
**Run status:** VALID

---

## 1. Execution Provenance

| Field | Value |
|---|---|
| OS | Linux 5.10.134-18.0.12.lifsea8.x86_64 |
| Architecture | x86_64 |
| CPU | N/A (containerized) |
| Python | 3.12.12 |
| NumPy | 2.2.5 |
| Script hash | `178f5bd650c832ac94172f3009a5189f1b40292f901bd97b4ec32e779a7492be` |
| Command | `python3 nexus4_leak_blindness_v2_0.py --years 1050 --seeds 40 --calib-seeds 200 --mdr-seeds 32 --horizon-seeds 40 --json my_run_v2.json` |
| Result JSON hash | `c6b8784324fa939a6cd211e650a0c3abab3adc4ffbea4a4b8c802d9d96099b66` |
| Run status | VALID |

The script hash matches the official hash exactly. No execution-breaking corruption was detected.

---

## 2. Self-Tests

All 8 self-tests passed:

| # | Test | Result |
|---|---|---|
| 1 | creep and instrument channel-1 streams are bit-identical | **PASS** |
| 2 | creep and instrument channel-2 streams differ | **PASS** |
| 3 | Green Sky returns exactly to original baseline | **PASS** |
| 4 | Green Sky reaches configured amplitude | **PASS** |
| 5 | green plateau is flat for 150 years | **PASS** |
| 6 | vectorized one-sided CUSUM matches sequential recurrence | **PASS** |
| 7 | vectorized two-sided CUSUM matches sequential recurrence | **PASS** |
| 8 | Gaussian-mixture e-process formula sanity check | **PASS** |

The run is valid. The identifiability construction (bit-identical channel-1 for creep vs instrument) is confirmed by construction.

---

## 3. Calibration

| Detector | Threshold Mode | h | Base-Horizon Null FA |
|---|---|---:|---:|
| Leaky abs-dev, λ=0.9 (τ=10) | empirical_fixed_horizon | 15.282149 | 0.050 |
| Leaky abs-dev, λ=0.99 (τ=100) | empirical_fixed_horizon | 97.03843 | 0.050 |
| Leaky abs-dev, λ=0.999 (τ=1000) | empirical_fixed_horizon | 839.39202 | 0.050 |
| Raw absolute-deviation sum | empirical_fixed_horizon | 10148.474 | 0.050 |
| Centered cumsum / √k [legacy] | empirical_fixed_horizon | 3.2250881 | 0.050 |
| One-sided CUSUM, ν=0.5 | empirical_fixed_horizon | 10.232037 | 0.050 |
| One-sided CUSUM, ν=0.1 | empirical_fixed_horizon | 42.731066 | 0.050 |
| One-sided CUSUM, ν=0.02 | empirical_fixed_horizon | 121.65711 | 0.050 |
| Two-sided CUSUM, ν=0.1 | empirical_fixed_horizon | 45.386569 | 0.050 |
| Fixed-reference EWMA [blue only] | empirical_fixed_horizon | 1.7506736 | 0.050 |
| Known-epoch EWMA bank [blue+green] | empirical_fixed_horizon | 1.7506736 | 0.050 |
| Cross-channel disagreement EWMA | empirical_fixed_horizon | 0.25513755 | 0.050 |
| Gaussian-mixture e-process, α=0.05 | analytic_anytime | 2.9957323 | 0.045 |

**Observations:**
- The e-process threshold is derived analytically (log(1/0.05) ≈ 2.996) and its empirical null FA (0.045) is consistent with the 0.05 target given 200 calibration seeds (quantization floor at 0.005).
- All empirical thresholds achieve exactly the allowed 0.050 calibration null FA, which is expected given the order-statistic calibration method.
- `ref_blue` and `ref_blue_green_known` share the same threshold because the distance-to-nearest-reference logic means adding a second reference point can only reduce or maintain the minimum distance; the calibration null traces happen to produce the same 95th-percentile maximum.

---

## 4. Scenario Results

### Post-onset detection rate by condition

| Detector | null | creep | instrument | greensky | shock | confound |
|---|---:|---:|---:|---:|---:|---:|
| Leaky λ=0.9 | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| Leaky λ=0.99 | 0.12 | 1.00 | 1.00 | 1.00 | 1.00 | 0.07 |
| Leaky λ=0.999 | 0.12 | 1.00 | 1.00 | 1.00 | 1.00 | 0.12 |
| raw_fixed | 0.10 | 1.00 | 1.00 | 1.00 | 1.00 | 0.10 |
| raw_sqrt | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| CUSUM ν=0.5 | 0.07 | 1.00 | 1.00 | 1.00 | 1.00 | 0.05 |
| CUSUM ν=0.1 | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| CUSUM ν=0.02 | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| CUSUM2 ν=0.1 | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| ref_blue | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| ref_blue_green_known | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| crosschannel | 0.05 | 0.00 | 1.00 | 0.00 | 0.00 | 1.00 |
| normal_mixture_e | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |

### Creep false alarms and detection delay

| Detector | Pre-onset FA | Post-onset Detection | Median Delay (years) |
|---|---:|---:|---:|
| Leaky λ=0.9 | 0.03 | 1.00 | 27.83 |
| Leaky λ=0.99 | 0.05 | 1.00 | 23.12 |
| Leaky λ=0.999 | 0.00 | 1.00 | 27.33 |
| raw_fixed | 0.00 | 1.00 | 147.08 |
| raw_sqrt | 0.05 | 1.00 | 33.04 |
| CUSUM ν=0.5 | 0.03 | 1.00 | 17.00 |
| CUSUM ν=0.1 | 0.00 | 1.00 | 14.67 |
| CUSUM ν=0.02 | 0.00 | 1.00 | 20.75 |
| CUSUM2 ν=0.1 | 0.00 | 1.00 | 15.33 |
| ref_blue | 0.05 | 1.00 | 62.92 |
| ref_blue_green_known | 0.05 | 1.00 | 62.92 |
| crosschannel | 0.05 | 0.00 | n/a |
| normal_mixture_e | 0.03 | 1.00 | 32.96 |

**Key observations:**
- Every single-channel detector achieves 100% post-onset detection on creep at this 6-sigma amplitude. The slow drift is not invisible; the question is sensitivity at smaller amplitudes (addressed in MDR50).
- `crosschannel` correctly reports 0% detection on creep because both channels move together (common-mode).
- `raw_fixed` has the worst delay (147 years) because it waits for the cumulative absolute deviation to cross a very high threshold.
- CUSUM variants have the best delays (14–20 years).
- The leaky detectors show a non-monotonic delay pattern with λ: λ=0.99 is fastest (23.1y), while λ=0.9 and λ=0.999 are slower (~28y). This suggests an intermediate memory is optimal for this particular ramp rate.

---

## 5. Green-Sky Reversal

| Detector | Green Plateau Alarm Fraction | Quiet After Return | Alarm After Return |
|---|---:|---:|---:|
| Leaky λ=0.9 | 1.00 | 1.00 | 0.00 |
| Leaky λ=0.99 | 1.00 | 0.90 | 0.10 |
| Leaky λ=0.999 | 1.00 | 0.00 | 1.00 |
| raw_fixed | 1.00 | 0.00 | 1.00 |
| raw_sqrt | 1.00 | 0.00 | 1.00 |
| CUSUM ν=0.5 | 1.00 | 0.00 | 1.00 |
| CUSUM ν=0.1 | 1.00 | 0.00 | 1.00 |
| CUSUM ν=0.02 | 1.00 | 0.00 | 1.00 |
| CUSUM2 ν=0.1 | 1.00 | 0.00 | 1.00 |
| ref_blue | 1.00 | 1.00 | 0.00 |
| ref_blue_green_known | 0.00 | 1.00 | 0.00 |
| crosschannel | 0.00 | 1.00 | 0.00 |
| normal_mixture_e | 1.00 | 0.00 | 1.00 |

**Key observations:**
- `ref_blue_green_known` is the only single-channel detector that correctly recognizes the green plateau as non-anomalous (0% alarm fraction), because green is already in its reference bank.
- `ref_blue` alarms through the entire plateau (100%) because green is foreign to its single reference.
- `crosschannel` stays quiet throughout because both channels track together during Green Sky.
- Most detectors (raw_sqrt, all CUSUMs, raw_fixed, normal_mixture_e) alarm after return to baseline. This is a **retrospective trigger problem**: the drift alarm fires after the world has already returned to blue. For a real cognitive system, this means the alarm arrives when the causal micro-events may already be consolidated.
- `leaky_l0.9` and `ref_blue` are the only detectors that stay quiet after return (100%). This is because their short memory (τ=10) forgets the excursion quickly.

---

## 6. MDR50 (Finite-Horizon Only)

| Detector | MDR50 (σ/year) | Years per 1σ displacement |
|---|---:|---:|
| Leaky λ=0.9 | 0.000624 | 1,603 |
| Leaky λ=0.99 | 0.000333 | 3,005 |
| Leaky λ=0.999 | 0.000233 | 4,289 |
| raw_fixed | 0.000190 | 5,259 |
| raw_sqrt | 0.0000576 | 17,359 |
| CUSUM ν=0.5 | 0.000172 | 5,819 |
| CUSUM ν=0.1 | 0.0000869 | 11,506 |
| CUSUM ν=0.02 | 0.0000331 | 30,190 |
| CUSUM2 ν=0.1 | 0.0000915 | 10,926 |
| ref_blue | 0.001668 | 600 |
| ref_blue_green_known | 0.001668 | 600 |
| crosschannel | n/a | n/a |
| normal_mixture_e | 0.0000589 | 16,967 |

**Explicitly labeled as finite-horizon only.** The final displacement at detection grows with horizon length, so lower MDR50 at 1050 years does not imply the same detector wins at 10,000 years.

**Ranking (best to worst):**
1. CUSUM ν=0.02: 3.31e-5 σ/year
2. raw_sqrt: 5.76e-5 σ/year
3. normal_mixture_e: 5.89e-5 σ/year
4. CUSUM2 ν=0.1: 9.15e-5 σ/year
5. CUSUM ν=0.1: 8.69e-5 σ/year
6. Leaky λ=0.999: 2.33e-4 σ/year
7. raw_fixed: 1.90e-4 σ/year
8. CUSUM ν=0.5: 1.72e-4 σ/year
9. Leaky λ=0.99: 3.33e-4 σ/year
10. Leaky λ=0.9: 6.24e-4 σ/year
11. ref_blue / ref_blue_green_known: 1.67e-3 σ/year

**Key observations:**
- The leaky detectors improve with larger λ but do not close the gap to CUSUM ν=0.02 or raw_sqrt. Best leaky (λ=0.999) is ~7× worse than CUSUM ν=0.02.
- P1 is confirmed: best leaky MDR50 (0.000233) vs raw_sqrt (0.0000576) = 4.0× ratio, exceeding the 3× threshold.
- P5 is confirmed FAIL: raw_sqrt is not the best; CUSUM ν=0.02 is ~1.7× better.
- The e-process is competitive with raw_sqrt (ratio 1.02), demonstrating that anytime-valid boundaries need not sacrifice much finite-horizon sensitivity under this null.
- Reference-based detectors (ref_blue, ref_blue_green_known) have the worst MDR50 because they measure distance to a fixed point, not accumulated deviation.

---

## 7. Horizon Robustness

Same threshold, longer null horizon. Seed resolution: 40 seeds → 0.025 per observation.

| Detector | x1 | x4 | x16 |
|---|---:|---:|---:|
| Leaky λ=0.9 | 0.025 | 0.175 | 0.425 |
| Leaky λ=0.99 | 0.050 | 0.350 | 0.725 |
| Leaky λ=0.999 | 0.050 | 0.200 | 0.950 |
| raw_fixed | 0.075 | 1.000 | 1.000 |
| raw_sqrt | 0.025 | 0.025 | 0.025 |
| CUSUM ν=0.5 | 0.100 | 0.425 | 0.775 |
| CUSUM ν=0.1 | 0.025 | 0.100 | 0.425 |
| CUSUM ν=0.02 | 0.025 | 0.275 | 0.850 |
| CUSUM2 ν=0.1 | 0.025 | 0.125 | 0.475 |
| ref_blue | 0.100 | 0.100 | 0.100 |
| ref_blue_green_known | 0.100 | 0.100 | 0.100 |
| crosschannel | 0.000 | 0.225 | 0.625 |
| normal_mixture_e | 0.025 | 0.025 | 0.025 |

**Key observations:**
- **raw_fixed** collapses completely by x4 (100% FA). This confirms R1.
- **raw_sqrt** is perfectly flat at x1/x4/x16 (0.025). This is because the √k denominator grows with horizon, self-normalizing. However, the protocol correctly notes this is **not** a proof of infinite-horizon safety (law of the iterated logarithm implies eventual crossing).
- **normal_mixture_e** is also flat (0.025), consistent with its analytic anytime-valid guarantee under the modeled null.
- **Leaky detectors** degrade with longer memory: λ=0.999 goes from 5% at x1 to 95% at x16. The longer the memory, the more the threshold calibrated at 1050 years is stressed by 16× more opportunities for rare excursions.
- **CUSUM** shows intermediate degradation: ν=0.02 degrades from 2.5% to 85% at x16; ν=0.5 degrades to 77.5%.
- **ref_blue / ref_blue_green_known** are flat at 10% across all horizons. This is because the EWMA distance to a fixed reference has a stationary distribution under the null, so the threshold is naturally horizon-robust.

---

## 8. Analytic Controls

### M4A — Constant-Severity Fixed Point

For q_{k+1} = λ q_k + s with threshold θ=1:

| λ | Crossing Floor s | q_∞ at 0.5× floor | q_∞ at 1.5× floor |
|---:|---:|---:|---:|
| 0.900 | 0.1 | 0.500 | 1.500 |
| 0.990 | 0.01 | 0.500 | 1.500 |
| 0.999 | 0.001 | 0.500 | 1.500 |

**Interpretation:** This is a mathematical property of the scalar recurrence. It shows that for constant input, there exists a severity floor below which the leaky accumulator never crosses threshold. In the Green-Sky scenario, the input is *not* constant (it ramps), so this control does not directly bound detection. It does, however, establish that a leaky accumulator with very long memory (λ→1) has a very low floor, making it sensitive to tiny constant biases—but also making it vulnerable to horizon degradation, as seen in the x16 results.

### M4B — Normalized Linear-EWMA Effective Memory

For m_k = λ m_{k-1} + (1-λ) x_k:

| λ | τ | N_eff | Stationary SD |
|---:|---:|---:|---:|
| 0.900 | 10.0 | 19.0 | 0.229416 |
| 0.990 | 100.0 | 199.0 | 0.070888 |
| 0.999 | 1000.0 | 1999.0 | 0.022366 |

**Interpretation:** N_eff ≈ 2τ for λ near 1, not τ. This is the mathematically correct effective sample size for a linear normalized EWMA. The experiment's leaky detectors are *not* normalized (they use q_{k+1} = λ q_k + |x-μ|), so this control does not directly describe them. It serves as a boundary check: if someone claims "τ=1000 samples are averaged," the correct statement for a normalized linear EWMA is N_eff ≈ 2000.

---

## 9. Historical P1–P8

| ID | Kind | Historical v1.1 | v2.0 Rerun | Statement |
|---|---|---|---|---|
| P1 | analytic | PASS | **PASS** | Leaky MDR ≥3× worse than raw_sqrt; gap does not close as λ→1. |
| P2 | empirical | PASS | **PASS** | Every detector fires on SHOCK. |
| P3 | analytic | FAIL | **FAIL** | raw_fixed cannot be calibrated. |
| P4 | empirical | FAIL | **FAIL** | CUSUM ν=0.5 blind to Green Sky drift (fire_rate < 0.5 on creep). |
| P5 | empirical | FAIL | **FAIL** | raw_sqrt has lowest finite-horizon MDR. |
| P6 | empirical | PASS | **PASS** | Fixed reference stays latched >50% of green plateau. |
| P7 | analytic | PASS | **PASS** | creep and instrument produce identical ch1; single-channel detectors give identical results. |
| P8 | empirical | PASS | **PASS** | crosschannel fires on instrument, NOT on creep. |

**History preserved.** P3/P4/P5 remain falsified. The v2.0 rerun reproduces all historical verdicts.

**Notable:** P4's historical failure is interesting. The original claim was that CUSUM ν=0.5 would be blind to the creep rate. In this run, CUSUM ν=0.5 detects 100% of post-onset creep. The historical failure was already noted in the protocol: "A slow ramp that eventually reaches +6 sigma can exceed ν=0.5 and then accumulate strongly." The v2.0 result confirms this correction.

---

## 10. Post-Pilot Replication Targets R1–R6

| ID | Class | Verdict | Evidence |
|---|---|---|---|
| R1 | post-pilot replication | **PASS** | raw_fixed x4 null FA = 1.000 ≥ 0.50 |
| R2 | post-pilot replication | **PASS** | CUSUM ν=0.5 creep post-onset detection = 1.00 ≥ 0.90 |
| R3 | post-pilot replication | **PASS** | raw_sqrt MDR50 = 5.76e-5; CUSUM ν=0.02 = 3.31e-5; ratio = 1.74 ≤ 2.0 |
| R4 | new control | **PASS** | e-process null FA at x1/x4/x16 = 0.025/0.025/0.025 ≤ 0.10 |
| R5 | post-pilot replication | **PASS** | crosschannel: creep=0.00 ≤ 0.10; instrument=1.00 ≥ 0.90; confound=1.00 ≥ 0.90 |
| R6 | reference semantics | **PASS** | ref_blue plateau alarm = 1.000; ref_blue_green_known = 0.000; difference = 1.000 ≥ 0.30 |

All R-targets pass in this environment.

---

## 11. Reference Comparison

**No reference JSON was provided in the upload.** The protocol mentions `nexus4_leak_blindness_v2_0_reference.json` and `nexus4_leak_blindness_v2_0_reference.md` as companion artifacts, but they were not included in the uploaded files.

Therefore, mechanical comparison against an official reference JSON cannot be performed. The following high-level expectations from the protocol are noted:

- All self-tests PASS ✓
- P1/P2/P6/P7/P8 reproduce PASS ✓
- P3/P4/P5 reproduce FAIL ✓
- R1–R6 PASS ✓

If a reference JSON becomes available, the following fields should be compared mechanically:
- `calibration.*.threshold` (absolute difference)
- `results.*.*.post_onset_detection_rate` (absolute difference, verdict-sensitive)
- `finite_horizon_mdr50.*` (relative difference where meaningful)
- `horizon_robustness.*.x4` and `.x16` (absolute difference, verdict-sensitive)
- `legacy_prediction_checks.*.verdict` (must match exactly)
- `post_pilot_target_checks.*.verdict` (must match exactly)

Given Python 3.12.12 / NumPy 2.2.5 vs the reference environment of Python 3.13.5 / NumPy 2.3.5, small numerical divergences in thresholds and MDR50 are expected due to different NumPy RNG implementations or floating-point behavior. The verdicts, however, should be stable.

---

## 12. Methodological Attacks

### Attack 1: Signal Model — The ramp is not a severity model
The `creep` signal is x_k = ramp(k) + noise, a state displacement. Real THDE `severity_k` may be a prediction error, a residual, a derivative, or a geometry-based quantity. The experiment does not establish that a state-displacement ramp is the correct operationalization of slow drift in Nexus. **This undermines transfer to M1–M3.**

**Repair:** After source inspection of THDE, construct a secondary experiment (S9) where the input is an actual THDE severity stream or a documented proxy.

### Attack 2: Null Model — iid Gaussian is unrealistically clean
The null is iid N(0,1). Real cognitive substrates have serial correlation, heavy tails, seasonality, and calibration drift. The e-process guarantee fails under even mild AR(1) correlation. **This undermines R4 and M7.**

**Repair:** Run S2 (AR(1) and heavy-tail nulls) and S3 (variance drift). Report e-process breakdown points.

### Attack 3: Calibration — Empirical threshold is horizon-dependent by construction
The empirical calibration method (order statistic of 200 null maxima) guarantees ≤5% FA *only* at the calibration horizon. It is not a surprise that detectors fail at x4/x16; it is a mathematical necessity for any non-anytime-valid boundary. The experiment treats this as a discovery, but it is mostly a tautology. **This undermines the framing of M3 as a stress test.**

**Repair:** Frame M3 as "measuring the rate of horizon degradation" rather than "discovering horizon fragility." Report the theoretical expected degradation for each detector class.

### Attack 4: MDR Metric — Final displacement scales with horizon
MDR50 measures the minimum ramp rate producing ≥50% detection. Because the signal is x_k = rate·k + noise, the final displacement at tick n is rate·n. A detector with better MDR50 at n=12600 may simply be better at detecting large displacements, not better at detecting slow drift per se. **This undermines P1 and P5 comparisons.**

**Repair:** Define a duration-independent metric: e.g., minimum detectable *displacement* at a fixed time, or minimum detectable rate at multiple horizons. Alternatively, fix the final displacement and vary the ramp duration.

### Attack 5: Horizon Test — x16 is not a proxy for infinity
The protocol correctly notes that surviving x16 ≠ infinite-horizon safety. However, the presentation of x16 results could still mislead readers into overconfidence. raw_sqrt's flat x1/x4/x16 is visually compelling but mathematically illusory (LIL guarantees eventual crossing). **This undermines any claim that raw_sqrt is "horizon-robust."**

**Repair:** Add a theoretical annotation to the M3 table: "raw_sqrt: flat empirically at x16, but provably unbounded under LIL." Add a secondary experiment (S1) sweeping to x64 or x256 to observe the eventual crossing.

### Attack 6: Identifiability Interpretation — Two channels may share failure modes
M5 demonstrates that single-channel detectors cannot distinguish creep from instrument drift. The crosschannel detector solves this *only* if the two channels are independent. In practice, shared calibration, shared training data, shared preprocessing, or shared physical substrate could make both channels drift together. The protocol mentions this in Q2 but the experiment does not test it. **This undermines P8's architectural generalization.**

**Repair:** Run S4 (correlated two-channel failures) and S5 (three-channel attribution with one faulty channel).

### Attack 7: Reference Semantics — `ref_blue_green_known` assumes what it should prove
The detector `ref_blue_green_known` assumes both blue and green epochs are already retained. This is a recurrence-recognition control, not a reference-authorization solution. The experiment does not test how a system *first* recognizes that green is a legitimate new epoch rather than an anomaly. **This undermines any claim that the reference-bank approach solves the Green-Sky problem.**

**Repair:** Run S6 (first-time reference authorization vs recurrence recognition) and S7 (repeated Green-Sky epochs with preserved history).

### Attack 8: Architectural Transfer — Scalar detectors may not generalize to high-dimensional state
All detectors here are scalar. Nexus state may be vector/tensor, manifold-valued, or ontology-dependent. A scalar detector winning on a scalar signal does not imply it wins on the real geometry. **This undermines every detector recommendation.**

**Repair:** Run S8 (high-dimensional/vector Green-Sky trajectory) and S9 (explicit THDE severity mapping after source inspection).

---

## 13. Repairs

For every attack above, a concrete repair is already proposed. Summarized:

| Attack | Repair |
|---|---|
| Signal model | S9: use actual THDE severity stream |
| Null model | S2: AR(1) + heavy-tail nulls; S3: variance drift |
| Calibration framing | Reframe M3 as "degradation rate measurement" |
| MDR metric | Fix final displacement, vary duration; or use rate-independent metric |
| Horizon test | Add LIL annotation; S1: sweep to x64/x256 |
| Identifiability | S4: correlated channels; S5: 3-channel attribution |
| Reference semantics | S6: first-time authorization; S7: repeated epochs |
| Architectural transfer | S8: high-dimensional trajectory; S9: THDE mapping |

Additionally:
- **Repair for P3 framing:** The historical P3 claim was "raw_fixed cannot be calibrated." The v1.1 correction and v2.0 result show it *can* be calibrated for a known finite horizon. The deeper problem is horizon dependence. The repair is to update the statement to: "raw_fixed can be calibrated for a known finite horizon, but its threshold scales linearly with horizon, making it useless for unknown or unbounded horizons."
- **Repair for P4 framing:** The historical P4 claim was "CUSUM ν=0.5 is blind to the creep rate." The correction is: "CUSUM ν=0.5 is not blind to large-amplitude ramps that eventually exceed ν; it is blind to ramps that remain below ν indefinitely." This is a more precise and defensible claim.

---

## 14. Answers to Q1–Q9

All claims tagged with epistemic vocabulary per protocol §8.

### Q1 — Transfer to real THDE
**UNRESOLVED.** The scalar analog uses |x-μ| as severity-like input. Real THDE is high-dimensional and coexists with rate-independent hysteresis. No source inspection of THDE implementation was performed. The experiment does not establish:
- What severity_k actually is
- Whether it is scalar/vector/tensor
- Whether it is signed or nonnegative
- Whether it is level-, residual-, derivative-, or geometry-based
- What role Preisach/PI/Bouc-Wen operators play

**Tag:** UNRESOLVED

### Q2 — Observation Independence
**UNRESOLVED / EXPERIMENTAL.** The experiment demonstrates that two independent channels can solve the identifiability problem (P8). It does not test whether real Nexus channels are independent. Shared failure modes (calibration, training data, clock, ontology, preprocessing, power, physical placement, causal model) could invalidate the crosschannel solution.

**Tag:** EXPERIMENTAL (for the demonstrated case); UNRESOLVED (for real Nexus)

### Q3 — Reference Authorization
**UNRESOLVED.** The experiment distinguishes `ref_blue` (single reference) from `ref_blue_green_known` (pre-known bank). It does not test:
- Who may add a new epoch reference
- How novelty is distinguished from anomaly
- How validation, promotion, supersession, or retirement work
- Whether reference migration shares machinery with constitutional evolution

**Tag:** UNRESOLVED

### Q4 — Review vs Resistance
**RESEARCH_HYPOTHESIS.** The experiment does not specify what posture a system should adopt during unresolved drift. Green Sky can be real. The detectors here only fire alarms; they do not specify whether the response should be mechanical resistance, cognitive review, increased retention, competing-hypothesis generation, or reference challenge.

**Tag:** RESEARCH_HYPOTHESIS

### Q5 — Retrospective Trigger Problem
**VERIFIED (as a problem).** The experiment confirms that cumulative detectors (raw_sqrt, CUSUM, e-process, raw_fixed, leaky λ=0.999) alarm *after* Green Sky has returned to baseline. This means the alarm arrives when causal micro-events may already be consolidated. The experiment does not specify what survives strongly enough to reconstruct the interval.

**Tag:** VERIFIED (problem exists); UNRESOLVED (what to retain)

### Q6 — Causal Hypothesis Collapse
**UNRESOLVED.** The experiment does not define a representation-stable trigger based on explanatory probability mass over hypothesis families. No quantity, update rule, threshold, computational cost, retention consequence, or false-trigger control is specified.

**Tag:** UNRESOLVED

### Q7 — CA Ownership
**UNRESOLVED.** The experiment does not determine whether slow-drift handling needs a CA-level regime policy or can remain below CA with resource allocation only after escalation. No discriminating test or source-based ownership argument is provided.

**Tag:** UNRESOLVED

### Q8 — Anytime-Validity Under Realistic Noise
**PARTIALLY_IMPLEMENTED / EXPERIMENTAL.** The e-process control demonstrates anytime-validity under iid Gaussian null. The protocol explicitly lists secondary tests (AR(1), Student-t, variance drift, seasonality, missing data, regime-switching, adversarial bursts, cross-channel correlated failures) that would determine robustness. None were run in the primary experiment.

**Tag:** PARTIALLY_IMPLEMENTED (Gaussian case); UNRESOLVED (realistic noise)

### Q9 — High-Dimensional State Geometry
**UNRESOLVED.** Green Sky is scalar. Actual Nexus state may require vector/tensor residuals, manifold distance, hypervector similarity, subspace drift, covariance change, ontology change, or hysteresis state. The experiment does not determine whether scalar conclusions survive under real geometry.

**Tag:** UNRESOLVED

---

## 15. Ownership Map

| Mechanism | Subsystem | Evidence/Source | Boundary Check |
|---|---|---|---|
| Slow-drift detection (scalar analog) | EXPERIMENTAL (not assigned to TMS/THDE/CA) | This script only | Not canonical; not source-inspected |
| Leaky recurrence q_{k+1}=λq_k+s | TMS (HVD 1.5 §16.2) | HVD 1.5 says TMS must preserve enough history for a future controller to compute *something such as* this | HVD 1.5 does NOT assert this is the implemented detector |
| Rate-independent hysteresis | THDE (separate spec) | Preisach / Prandtl-Ishlinskii / Bouc-Wen listed | Coexists with leaky form; role relative to scalar analog UNRESOLVED |
| Cross-channel disagreement | EXPERIMENTAL | This script only | Does not prove truth without independent reference |
| Reference bank (blue+green known) | EXPERIMENTAL | This script only | Does not implement authorization/migration |
| E-process anytime boundary | EXPERIMENTAL / MATH_CONTROL | Ville's inequality under iid Gaussian null | Model misspecification breaks guarantee |
| CUSUM detection | EXPERIMENTAL | This script only | Not asserted as canonical THDE representation |
| Calibration (empirical order statistic) | EXPERIMENTAL | This script only | Horizon-dependent by construction |

**No CA god-object is created.** The experiment deliberately does not assign detection to CA. The protocol's scope guardrails prevent this.

---

## 16. New Registered Predictions

**Date:** 2026-09-03  
**Context:** Formed AFTER running the experiment and reading the protocol, but BEFORE reading any reference JSON (which was not provided).

| ID | Prediction | Reason | Before/After |
|---|---|---|---|
| N1 | If AR(1) correlation ρ ≥ 0.3 is added to the null, the e-process empirical FA at x16 will exceed 0.10. | The e-process assumes iid; positive serial correlation inflates the effective variance of S_t, causing more frequent boundary crossings. | After seeing R4 pass under iid null |
| N2 | If the Green-Sky amplitude is reduced from 6σ to 2σ, CUSUM ν=0.5 post-onset detection will drop below 0.50, while CUSUM ν=0.02 will remain above 0.90. | ν=0.5 requires the signal to exceed 0.5 before accumulation; a 2σ ramp may never do so. ν=0.02 accumulates even tiny deviations. | After seeing P4 historical failure and current 100% detection at 6σ |
| N3 | A three-channel system with one faulty channel can be identified by majority-vote cross-channel disagreement, but only if the two truthful channels are independent. If all three share a hidden common mode, attribution fails. | This extends P8/M5 to the N=3 case. The confound construction generalizes. | After seeing P8 pass and Q2 unresolved |
| N4 | The `ref_blue_green_known` detector will fail to recognize a *third* epoch (e.g., "red sky") unless red is also pre-registered. Adding epochs one at a time without a governance mechanism will cause either false alarms or missed detections. | The detector only knows blue and green. Novelty outside the bank is treated as anomaly by construction. | After seeing R6 pass and Q3 unresolved |
| N5 | Under a Student-t null with ν=3 degrees of freedom, raw_sqrt's empirical FA at x16 will exceed 0.10, while the e-process will also degrade but more gracefully (FA < 0.20). | Heavy tails cause more extreme excursions. The e-process's martingale structure is robust to some misspecification but not unbounded variance. | After seeing raw_sqrt's flat horizon and e-process's analytic guarantee |

---

## 17. UNRESOLVED

The following items remain unresolved rather than filled optimistically:

1. **Real THDE severity mapping:** What is severity_k? Scalar or vector? Signed or nonnegative? Level-, residual-, derivative-, or geometry-based? How is it normalized? What resets its reference? (Q1)
2. **Observation independence in Nexus:** Do nominal channels share hidden common modes? (Q2)
3. **Reference authorization mechanism:** Who may add, validate, promote, supersede, or retire an epoch reference? (Q3)
4. **Response posture during unresolved drift:** Resistance, review, retention, hypothesis generation, or challenge? (Q4)
5. **Retrospective reconstruction:** What survives strongly enough to reconstruct the interval when a cumulative alarm fires late? (Q5)
6. **Causal hypothesis collapse metric:** No quantity, update rule, threshold, or cost specified. (Q6)
7. **CA ownership of slow-drift handling:** No discriminating test or source argument. (Q7)
8. **E-process under realistic noise:** AR(1), heavy tails, variance drift, seasonality, missing data, regime-switching, adversarial bursts, correlated failures — all untested. (Q8)
9. **High-dimensional state geometry:** Scalar conclusions may not survive under vector/tensor/manifold/hypervector state. (Q9)
10. **Preisach/PI/Bouc-Wen hysteresis role:** How do rate-independent operators interact with the leaky recurrence? No source inspection.
11. **Reference JSON comparison:** Could not be performed because the reference JSON was not provided.
12. **Numerical reproducibility across Python/NumPy versions:** This run used Python 3.12.12 / NumPy 2.2.5 vs reference 3.13.5 / 2.3.5. Small threshold differences are expected. Whether verdicts remain stable across versions is not formally proven.

---

## Appendix: Success Criterion Assessment

Per protocol §12, the experiment succeeds if it makes the next architectural question **narrower and better sourced**.

**Assessment:** The experiment succeeds at this criterion. It does not produce a preferred detector. Instead, it produces:
- A confirmed set of falsified historical predictions (P3, P4, P5) that refine the question space
- A clear demonstration that horizon robustness is a distinct property from finite-horizon performance and anytime validity
- A concrete identifiability result (P7/P8) that narrows the architectural question to "what independent information sources does Nexus actually possess?"
- A reference-semantics result (R6) that narrows the question to "how are new epochs authorized?"
- A retrospective-trigger result (Green-Sky after-return alarms) that narrows the question to "what survives for late reconstruction?"

The next narrower questions are:
1. What is the actual THDE severity_k after source inspection?
2. Are Nexus observation channels independent under realistic shared-failure-mode analysis?
3. What is the reference authorization protocol, and how does it differ from recurrence recognition?
4. What time-uniform evidence mechanism survives AR(1), heavy-tail, and variance-drift nulls?
5. What high-dimensional geometry does the real Nexus state use, and do scalar detector conclusions survive?

---

*End of report.*
