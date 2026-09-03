# Nexus 4 — Objective C Deep-Time Detector Experiment v2.0
## Independent panel-member response

Blind-replication rule followed as specified: only `nexus4_leak_blindness_v2_0.py` and
`RUN_PROTOCOL_nexus4_leak_blindness_v2_0.md` were provided with this task.
`nexus4_leak_blindness_v2_0_reference.json` / `_reference.md` were **not** included, so no
reference artifact existed to read early or late — Section 11 below is a genuine gap, not a
withheld comparison.

---

## 1. Execution provenance

```
OS:              Ubuntu 24.04.4 LTS
architecture:    x86_64
CPU:             Intel(R) Xeon(R) Processor @ 2.10GHz
Python:          3.12.3
NumPy:           2.4.4
script hash:     178f5bd650c832ac94172f3009a5189f1b40292f901bd97b4ec32e779a7492be
                 (matches the protocol's stated official hash exactly — no corruption)
command:         python3 nexus4_leak_blindness_v2_0.py --years 1050 --seeds 40 \
                 --calib-seeds 200 --mdr-seeds 32 --horizon-seeds 40 --json my_run_v2.json
result JSON hash: 85786f35f819d79534082db8a4e16664159a8d06ab4b5f57cf1c0f3a08f0ebe6
run status:      VALID
```

No whitespace normalization, line-ending changes, parameter edits, or patches were applied.
Reference environment (per protocol §7) was Python 3.13.5 / NumPy 2.3.5; this run used
Python 3.12.3 / NumPy 2.4.4. Both satisfy the stated `Python >= 3.10` + NumPy requirement.

## 2. Self-tests

All 8 declared self-tests passed; none failed:

- PASS creep and instrument channel-1 streams are bit-identical
- PASS creep and instrument channel-2 streams differ
- PASS Green Sky returns exactly to original baseline
- PASS Green Sky reaches configured amplitude
- PASS green plateau is flat for 150 years
- PASS vectorized one-sided CUSUM matches sequential recurrence
- PASS vectorized two-sided CUSUM matches sequential recurrence
- PASS Gaussian-mixture e-process formula sanity check

Run status is VALID under the protocol's own rule ("a self-test failure invalidates the run").

## 3. Calibration

| detector | mode | h | base-horizon null FA |
|---|---|---:|---:|
| leaky λ=0.9 (τ=10) | empirical | 15.282149 | 0.050 |
| leaky λ=0.99 (τ=100) | empirical | 97.03843 | 0.050 |
| leaky λ=0.999 (τ=1000) | empirical | 839.39202 | 0.050 |
| raw_fixed | empirical | 10148.474 | 0.050 |
| raw_sqrt | empirical | 3.2250881 | 0.050 |
| cusum1 ν=0.5 | empirical | 10.232037 | 0.050 |
| cusum1 ν=0.1 | empirical | 42.731066 | 0.050 |
| cusum1 ν=0.02 | empirical | 121.65711 | 0.050 |
| cusum2 ν=0.1 | empirical | 45.386569 | 0.050 |
| ref_blue | empirical | 1.7506736 | 0.050 |
| ref_blue_green_known | empirical | 1.7506736 | 0.050 |
| crosschannel | empirical | 0.25513755 | 0.050 |
| normal_mixture_e (α=0.05) | analytic_anytime | 2.9957323 | 0.045 |

13 detectors calibrated; 12 by empirical order-statistic on 200 null runs, 1 (the e-process) by
closed-form `log(1/α)`.

## 4. Scenario results

Post-onset detection rate (null column = any-alarm rate, no onset exists):

| detector | null | creep | instrument | greensky | shock | confound |
|---|---:|---:|---:|---:|---:|---:|
| leaky λ=0.9 | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| leaky λ=0.99 | 0.12 | 1.00 | 1.00 | 1.00 | 1.00 | 0.07 |
| leaky λ=0.999 | 0.12 | 1.00 | 1.00 | 1.00 | 1.00 | 0.12 |
| raw_fixed | 0.10 | 1.00 | 1.00 | 1.00 | 1.00 | 0.10 |
| raw_sqrt | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| cusum1 ν=0.5 | 0.07 | 1.00 | 1.00 | 1.00 | 1.00 | 0.05 |
| cusum1 ν=0.1 | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| cusum1 ν=0.02 | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| cusum2 ν=0.1 | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.03 |
| ref_blue | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| ref_blue_green_known | 0.05 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |
| crosschannel | 0.05 | 0.00 | 1.00 | 0.00 | 0.00 | 1.00 |
| normal_mixture_e | 0.03 | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 |

Creep pre-onset false alarms / post-onset detection / median delay:

| detector | pre-onset FA | post-onset detection | median delay (yrs) |
|---|---:|---:|---:|
| leaky λ=0.9 | 0.03 | 1.00 | 27.83 |
| leaky λ=0.99 | 0.05 | 1.00 | 23.12 |
| leaky λ=0.999 | 0.00 | 1.00 | 27.33 |
| raw_fixed | 0.00 | 1.00 | 147.08 |
| raw_sqrt | 0.05 | 1.00 | 33.04 |
| cusum1 ν=0.5 | 0.03 | 1.00 | 17.00 |
| cusum1 ν=0.1 | 0.00 | 1.00 | 14.67 |
| cusum1 ν=0.02 | 0.00 | 1.00 | 20.75 |
| cusum2 ν=0.1 | 0.00 | 1.00 | 15.33 |
| ref_blue | 0.05 | 1.00 | 62.92 |
| ref_blue_green_known | 0.05 | 1.00 | 62.92 |
| crosschannel | 0.05 | 0.00 | n/a |
| normal_mixture_e | 0.03 | 1.00 | 32.96 |

No detector receives false credit for a pre-onset alarm; the script scores post-onset detection
and pre-onset false alarms as separate fields, so an early false alarm cannot masquerade as fast
detection here.

## 5. Green-Sky reversal

| detector | plateau alarm frac. | quiet after return | alarm after return |
|---|---:|---:|---:|
| leaky λ=0.9 | 1.00 | 1.00 | 0.00 |
| leaky λ=0.99 | 1.00 | 0.90 | 0.10 |
| leaky λ=0.999 | 1.00 | 0.00 | 1.00 |
| raw_fixed | 1.00 | 0.00 | 1.00 |
| raw_sqrt | 1.00 | 0.00 | 1.00 |
| cusum1 ν=0.5 | 1.00 | 0.00 | 1.00 |
| cusum1 ν=0.1 | 1.00 | 0.00 | 1.00 |
| cusum1 ν=0.02 | 1.00 | 0.00 | 1.00 |
| cusum2 ν=0.1 | 1.00 | 0.00 | 1.00 |
| ref_blue | 1.00 | 1.00 | 0.00 |
| ref_blue_green_known | 0.00 | 1.00 | 0.00 |
| crosschannel | 0.00 | 1.00 | 0.00 |
| normal_mixture_e | 1.00 | 0.00 | 1.00 |

Every detector alarms through most or all of the 150-year green plateau. Whether it goes quiet
again after the return to baseline splits sharply along memory type: short/medium-leak and
fixed-reference detectors quiet down; long-leak (λ=0.999), raw/CUSUM/e-process detectors stay
latched. This split is itself the most decision-relevant finding in the whole run (see §12/§13).

## 6. Finite-horizon MDR50 (**finite-horizon only — not an asymptotic floor**)

| detector | MDR50 (σ/yr) | yrs per 1σ displacement |
|---|---:|---:|
| leaky λ=0.9 | 6.239e-4 | 1603 |
| leaky λ=0.99 | 3.328e-4 | 3005 |
| leaky λ=0.999 | 2.332e-4 | 4289 |
| raw_fixed | 1.902e-4 | 5259 |
| raw_sqrt | 5.761e-5 | 17359 |
| cusum1 ν=0.5 | 1.719e-4 | 5819 |
| cusum1 ν=0.1 | 8.691e-5 | 11506 |
| cusum1 ν=0.02 | 3.312e-5 | 30190 |
| cusum2 ν=0.1 | 9.153e-5 | 10926 |
| ref_blue | 1.668e-3 | 600 |
| ref_blue_green_known | 1.668e-3 | 600 |
| crosschannel | n/a | n/a |
| normal_mixture_e | 5.894e-5 | 16967 |

These are ranked comparisons at the 1050-year configured horizon only, per protocol §4/M2 — not
a duration-independent sensitivity claim.

## 7. Horizon robustness (same threshold, longer null; finite stress test only)

| detector | x1 | x4 | x16 |
|---|---:|---:|---:|
| leaky λ=0.9 | 0.03 | 0.17 | 0.42 |
| leaky λ=0.99 | 0.05 | 0.35 | 0.72 |
| leaky λ=0.999 | 0.05 | 0.20 | 0.95 |
| raw_fixed | 0.07 | 1.00 | 1.00 |
| raw_sqrt | 0.03 | 0.03 | 0.03 |
| cusum1 ν=0.5 | 0.10 | 0.42 | 0.78 |
| cusum1 ν=0.1 | 0.03 | 0.10 | 0.42 |
| cusum1 ν=0.02 | 0.03 | 0.28 | 0.85 |
| cusum2 ν=0.1 | 0.03 | 0.12 | 0.47 |
| ref_blue | 0.10 | 0.10 | 0.10 |
| ref_blue_green_known | 0.10 | 0.10 | 0.10 |
| crosschannel | 0.00 | 0.23 | 0.62 |
| normal_mixture_e | 0.03 | 0.03 | 0.03 |

At `--horizon-seeds 40`, one run = 0.025 of empirical rate (the raw JSON stores e.g.
`0.025/0.025/0.025` for `normal_mixture_e`, displayed above rounded to `0.03/0.03/0.03`) —
differences smaller than that are not distinguishable from seed noise at this seed count.
`raw_fixed` and long-leak/CUSUM detectors degrade sharply by x16; `raw_sqrt` and the e-process
hold flat — expected, since both were built specifically to be horizon-insensitive in different
ways (law-of-iterated-logarithm normalization vs. an explicit anytime-valid martingale bound).

## 8. Analytic controls (M4A/M4B — mathematics of a simplified recurrence, not simulation output)

**M4A — constant-severity fixed point**, `q[k+1] = λq[k] + s`, fixed point `q_∞ = s/(1-λ)`:

| λ | θ | exact severity floor `(1-λ)θ` | q∞ at 0.5×floor | q∞ at 1.5×floor |
|---:|---:|---:|---:|---:|
| 0.900 | 1.0 | 0.1 | 0.500 | 1.500 |
| 0.990 | 1.0 | 0.01 | 0.500 | 1.500 |
| 0.999 | 1.0 | 0.001 | 0.500 | 1.500 |

I recomputed this independently rather than trusting the printout: `q∞/θ` at `s = c·floor` reduces
algebraically to exactly `c`, independent of λ. That's why every row reads 0.500 / 1.500 regardless
of λ — this is exact closed-form arithmetic, not a Monte Carlo result, and it checks out.

**M4B — normalized linear-EWMA effective memory**, `m[k] = λm[k-1] + (1-λ)x[k]`,
`Var(m∞) = σ²(1-λ)/(1+λ)`, `N_eff = (1+λ)/(1-λ)`:

| λ | τ=1/(1-λ) | N_eff | stationary SD |
|---:|---:|---:|---:|
| 0.900 | 10.0 | 19.0 | 0.229416 |
| 0.990 | 100.0 | 199.0 | 0.070888 |
| 0.999 | 1000.0 | 1999.0 | 0.022366 |

Hand-check: `sqrt((1-0.999)/(1+0.999)) = sqrt(0.001/1.999) = 0.022366` ✓ (and similarly for the
other two rows). Both control tables are exact-formula outputs, correctly computed; neither is
evidence about how real Nexus `severity_k` is generated (per protocol §4/M4).

## 9. Historical P1–P8 (history preserved, not overwritten)

| id | v1.1 historical | v2.0 rerun | statement |
|---|---|---|---|
| P1 | **PASS** | **PASS** | Leaky MDR ≥3× worse than raw_sqrt, gap doesn't close as λ→1. |
| P2 | **PASS** | **PASS** | Every detector fires on SHOCK. |
| P3 | **FAIL** | **FAIL** | raw_fixed can't be calibrated (measures elapsed time, not departure). |
| P4 | **FAIL** | **FAIL** | CUSUM ν=0.5 is blind to Green-Sky drift rate. |
| P5 | **FAIL** | **FAIL** | raw_sqrt has the best finite-horizon MDR. |
| P6 | **PASS** | **PASS** | ≥1 fixed-reference detector stays latched >50% of the green plateau. |
| P7 | **PASS** | **PASS** | creep/instrument give every single-channel detector identical results. |
| P8 | **PASS** | **PASS** | crosschannel fires on instrument, not on creep. |

Every verdict reproduced exactly; none flipped. I independently re-derived each verdict from the
raw tables above rather than only reading the script's own printed verdict — e.g. P1's "≥3×"
claim checks out at 10.83×/5.78×/4.05× for λ=0.9/0.99/0.999 respectively, all above the 3× bar and
shrinking (but not closing) as λ→1.

Note on reading P3–P5 correctly: "FAIL" here means *the original prediction was falsified*, not
that the detector performed badly — e.g. P4's original claim was "CUSUM ν=0.5 can't detect this
drift," and it's marked FAIL because CUSUM ν=0.5 actually detects it perfectly (rate 1.00) once
the ramp gets large enough to overcome the ν slack. I flag this because it's easy to misread the
FAIL/PASS column as a performance grade rather than a claim-truth grade.

## 10. R1–R6 (independently re-verified against raw numbers, not just the script's self-report)

| id | verdict | independent check |
|---|---|---|
| R1 | **PASS** | raw_fixed x4 null FA = 1.00 ≥ 0.50 ✓ |
| R2 | **PASS** | cusum1 ν=0.5 creep post-onset detection = 1.00 ≥ 0.90 ✓ |
| R3 | **PASS** | raw_sqrt / cusum1 ν=0.02 MDR50 ratio = 5.761e-5 / 3.312e-5 ≈ 1.74×, within factor of 2 ✓ |
| R4 | **PASS** | e-process empirical null FA = 0.025 at x1/x4/x16, all ≤ 0.10 ✓ |
| R5 | **PASS** | crosschannel: creep = 0.00 (≤0.10), instrument = 1.00, confound = 1.00 (both ≥0.90) ✓ |
| R6 | **PASS** | ref_blue plateau alarm = 1.00 vs ref_blue_green_known = 0.00 — substantial gap ✓ |

All six replication targets independently confirmed from the underlying tables.

## 11. Reference comparison

**Not performed — the reference artifacts were not part of this upload.** Only the script and
the run protocol were provided; `nexus4_leak_blindness_v2_0_reference.json` and
`_reference.md` are absent from `/mnt/user-data/uploads`. Per the blind-replication rule this
is actually the correct order of operations (independent run first), but there is nothing to
open at step 7 in this session. If you share the reference JSON, I can do a mechanical field-by-
field diff (absolute/relative difference, verdict-flip check, environment deltas) in a follow-up.

## 12. Methodological attacks

- **Signal model** — Pre/post-onset scoring uses the *true, exactly-known* onset tick to split
  the record. A real detector never has ground-truth onset; a fair test would force onset
  estimation (e.g. blind changepoint detection) rather than handing the evaluator the answer.
- **Null model** — Everything is calibrated and stress-tested under iid N(0,1) noise only. Real
  telemetry is essentially never iid; positive autocorrelation alone would likely widen the true
  null distribution of every cumulative-sum-type statistic well beyond what these thresholds
  assume (this is explicitly Q8/S2, but it's still an open attack on every number in §3–§7).
- **Calibration** — Thresholds are the ~10th-smallest of 200 null maxima (5% floor on 200 seeds).
  No confidence interval is reported on `h` itself, so we don't know how much a different-but-
  equally-valid seed draw would move each threshold — the M3 "horizon robustness failure" is
  partly a mechanical consequence of calibrating threshold-per-fixed-horizon in the first place.
- **MDR metric** — Because `x_k = rate·k + noise` grows without bound, MDR50 at a fixed horizon
  conflates *rate sensitivity* with *how much time the horizon gives a slow ramp to accumulate*.
  A detector could look MDR-competitive here purely because the horizon is long, independent of
  whether it would still look competitive at a different horizon (the protocol's own §4/M2 flags
  this; it's real and worth restating independently rather than only citing the built-in caveat).
- **Horizon test** — M3 only lengthens the *same* iid-Gaussian null; it doesn't test a null that
  contains occasional legitimate transients unrelated to genuine drift, nor does the degradation
  finding (CUSUM/leaky thresholds inflate by x16) come as a surprise given these are exactly the
  running-max statistics whose LIL blowup `raw_sqrt`'s own docstring already warns about.
- **Identifiability (M5)** — The creep/instrument tie is a proof *by construction* that such a
  pair can exist, not a proof that world-drift and instrument-drift are *generally*
  indistinguishable on one channel. Real drift and real instrument bias could well differ in
  autocorrelation or response to a calibration ping, which a richer single-channel detector might
  exploit — the "requires a second information source" conclusion is correct for this
  construction, not automatically for every real case.
- **Reference semantics (M6)** — `ref_blue_green_known` is a static two-point prior fixed at
  t=0, mathematically just a wider acceptance region from the start. It says nothing about how a
  system would *safely learn* a second reference at runtime, or how it would resist an adversary
  trying to get a bad state accepted as a spuriously "known-good" epoch.
- **Architectural transfer** — Every detector here uses leaky/CUSUM-style memory that forgets
  exponentially or resets. Protocol §3 states real THDE coexists with rate-independent hysteresis
  (Preisach/Prandtl-Ishlinskii/Bouc-Wen), which by design *retains* a high-water-mark rather than
  forgetting. The Green-Sky "quiet after return" split in §5 is exactly the scenario where leaky
  and hysteretic memory would diverge most — this experiment cannot say which behavior real THDE
  would show, because no hysteretic control is in the harness at all.

## 13. Repairs

- **Signal model** → Add a blind-onset variant: don't tell the scorer the true onset tick; require
  it to be estimated from the data, and score detection delay relative to the *estimated*, not
  true, onset.
- **Null model** → Add an AR(1) null (φ ∈ {0.1, 0.3, 0.5}) and rerun §3/§7 under it; report the
  "correlation tax" as the multiplicative inflation of empirical FA at the iid-calibrated
  threshold (this is S2 in the protocol's own follow-up list — worth prioritizing first).
- **Calibration** → Bootstrap the 200 calibration null-maxima (e.g. 1,000 resamples) and report a
  confidence interval on each `h`, not just a point estimate.
- **MDR metric** → Report MDR50 as a curve across ≥3 horizon lengths instead of one number at one
  horizon, so rate-sensitivity and horizon-length stop being conflated.
- **Horizon test** → Add a null variant containing occasional legitimate transients (a rare,
  short, non-recurring bump) and check whether thresholds calibrated on purely quiet nulls
  over- or under-alarm on it.
- **Identifiability** → Construct a creep/instrument pair that also differs in a second
  single-channel statistic (e.g. response to an injected calibration ping, or autocorrelation
  decay) and test whether a higher-order single-channel detector partially separates them — this
  would bound how strong the "single channel is blind" claim really is.
- **Reference semantics** → Build an actual candidate-epoch pipeline: detect novelty → hold
  candidate under an explicit validation policy (e.g. N consecutive stable years plus a second
  corroborating signal) → promote to the reference bank — turning the current static demo into a
  real test of the authorization question in Q3.
- **Architectural transfer** → Add one hysteretic control (a minimal two-state Preisach relay or
  Bouc-Wen operator) into the same M1/M3 harness and specifically compare it against the leaky
  family on the Green-Sky reversal scenario, since that's where the two memory types should
  diverge most visibly.

## 14. Answers to Q1–Q9

- **Q1 (transfer to real THDE):** UNRESOLVED. No THDE source or spec was provided in this task,
  so `severity_k`'s scalar/vector form, sign, normalization, and reset behavior cannot be
  determined here. The `|x-μ|` proxy used throughout is EXPERIMENTAL only.
- **Q2 (observation independence):** The general principle "shared failure modes defeat
  two-channel identifiability" is VERIFIED within this simulation (via `confound`). Whether real
  Nexus channels actually share calibration/clock/ontology/etc. is UNRESOLVED — that's an
  inventory question about the real system, not something this script can answer.
- **Q3 (reference authorization):** UNRESOLVED. Nothing in the script performs detection,
  retention, validation, or promotion of a new epoch; `ref_blue_green_known` is a static prior
  (DESIGN_TARGET/EXPERIMENTAL at best), not a governance mechanism.
- **Q4 (review vs. resistance):** UNRESOLVED / RESEARCH_HYPOTHESIS. No policy choice between
  mechanical resistance, cognitive review, or increased retention is encoded anywhere in this
  code; any answer here would be speculation, not a finding.
- **Q5 (retrospective trigger problem):** The delay numbers in §4 (15–150+ years depending on
  detector) are VERIFIED evidence of *how late* detection can be, which motivates Q5, but the
  script implements no retention/replay mechanism — what should be retained to reconstruct the
  interval remains UNRESOLVED.
- **Q6 (causal hypothesis collapse):** UNRESOLVED. No hypothesis-family probability-mass
  mechanism exists in this script; entirely out of scope for this experiment.
- **Q7 (CA ownership):** UNRESOLVED. No CA source material was available to discriminate.
- **Q8 (anytime-validity under realistic noise):** The Gaussian-mixture e-process formula and its
  ≤10% empirical FA at x1/x4/x16 are VERIFIED, but strictly under its own iid-Gaussian null. None
  of the eight listed realistic-noise conditions (AR(1), heavy tails, variance drift, etc.) were
  tested here — UNRESOLVED, and flagged in the protocol itself as future work (S2/S10).
- **Q9 (high-dimensional geometry):** UNRESOLVED. Every signal and detector here is scalar by
  construction; nothing tests vector/tensor residuals, manifold distance, or hypervector
  similarity, so whether these scalar conclusions survive real Nexus geometry is untested.

## 15. Ownership map

| mechanism | subsystem claimed | evidence/source | boundary check |
|---|---|---|---|
| Leaky abs-deviation accumulator | candidate THDE-style analog | this script's M1–M4 only | NOT verified against real THDE source; explicitly barred from being "the leaky THDE form" (protocol §3) |
| One/two-sided CUSUM | generic statistical control | this script only | protocol §3 explicitly prohibits "CUSUM should replace THDE" |
| Gaussian-mixture e-process | generic anytime-valid control | self-test + M7 | prohibited from being called canonical Nexus (§3) |
| Cross-channel disagreement | M5/Q2 identifiability demo | confound/instrument results | "does not identify absolute truth by itself" — not extending that claim here |
| ref_blue / ref_blue_green_known | candidate HIGC-adjacent analog | Green-Sky table | explicitly NOT reference authorization/migration (M6) |
| HTCE / TMS / HVD / HIGC / THDE / QMT / HDF5 (real named subsystems) | — | **none inspected in this task** | no source for these was provided; any mapping beyond generic conceptual analogy would violate §3's prohibited-claims list |

This map is deliberately thin: this task tested generic statistical candidates against synthetic
data, not the real Nexus/HVD codebase, which was not part of this submission.

## 16. New registered predictions

Both formed **2026-09-03, after** seeing this run's results — not pre-registered, not eligible to
be scored as pre-pilot discoveries:

- **NP1:** A hysteretic control detector (Preisach/Bouc-Wen-style) added to this harness will
  *not* return to "quiet" after the Green-Sky reversal as readily as the short/medium-leak and
  fixed-reference detectors do in §5, because hysteretic memory is built to retain a high-water
  mark rather than exponentially forget.
- **NP2:** Under an AR(1) null with even modest positive autocorrelation (φ≈0.3), empirical FA at
  the current thresholds will exceed the nominal 5% by a margin comparable to or larger than the
  x4 horizon-robustness degradation already seen in §7, since positive autocorrelation reduces
  the calibration window's effective sample size in a directionally similar way to lengthening it.

## 17. UNRESOLVED

- Reference-JSON comparison (§11) — files not provided.
- Q1, Q3, Q4, Q6, Q7, Q9 — no source material or in-script mechanism exists to resolve these.
- Real THDE `severity_k`'s exact mathematical form — unknown absent source inspection.
- Robustness under non-Gaussian/correlated/adversarial noise (Q8's list) — none of S1–S10 were
  run in this task.
- Whether any scalar finding here survives high-dimensional/hysteretic real geometry (Q9) —
  untested; NP1 is a prediction about this, not a finding.
- Governance of reference authorization/promotion (Q3) — no mechanism was tested, only a static
  two-point prior.
