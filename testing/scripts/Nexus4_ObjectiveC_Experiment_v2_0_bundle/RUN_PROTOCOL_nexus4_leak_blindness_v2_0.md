# RUN PROTOCOL — Nexus 4 Objective C Deep-Time Detector Experiment v2.0

**Artifact status:** RESEARCH / EXPERIMENTAL  
**Not canon. Not a Nexus specification.**

Companion artifacts:

- `nexus4_leak_blindness_v2_0.py`
- `nexus4_leak_blindness_v2_0_reference.json`
- `nexus4_leak_blindness_v2_0_reference.md`

Official script SHA-256:

```text
178f5bd650c832ac94172f3009a5189f1b40292f901bd97b4ec32e779a7492be
```

Official reference JSON SHA-256:

```text
ce3f4aab70c54c5dffabe0c861c8ef34634fe1f9ac7101eee82a36eec39f68bd
```

---

## 0. Why v2.0 exists

This experiment is the merged successor to three earlier lines:

1. the original scalar leak-blindness / Green-Sky experiment;
2. the vectorized v1.1 experiment that added horizon robustness and preserved the original P1–P8 preregistration;
3. the audited v1.2 experiment that corrected source hierarchy, detector semantics, pre/post-onset accounting, and the overclaim that a finite state-displacement ramp proves an asymptotic THDE sensitivity floor.

The merge deliberately preserves **falsified history** rather than rewriting it.

The v1.1 pilot falsified P3, P4, and P5. Those statements remain in the script verbatim with their historical verdicts. v2.0 separately reports whether a new run reproduces or diverges from those outcomes.

The v1.1 pilot also exposed a new question that was not preregistered before that run:

> **How does a detector calibrated at one horizon behave if the cognitive system lives far beyond that horizon?**

v2.0 therefore treats horizon robustness as a first-class measurement while also correcting a second overreach:

> Surviving x16 does **not** make `S_k/sqrt(k)` infinite-horizon safe.

A fixed `sqrt(k)` boundary is not anytime-valid. v2.0 adds a Gaussian-mixture e-process control with a genuine time-uniform false-alarm guarantee **under its modeled iid Gaussian null assumptions**.

This means the experiment now distinguishes:

```text
finite-horizon performance
!=
finite tested horizon robustness
!=
time-uniform statistical validity
!=
Nexus architectural suitability
```

---

# 1. Blind-replication rule

If you are one member of a multi-model panel, perform your run **before reading the reference JSON or reference Markdown**.

You may be given all files together for convenience, but the reference result is a holdback artifact.

Required order:

```text
1. hash the script
2. inspect the script for execution-breaking corruption only
3. run the official command unchanged
4. save your JSON
5. hash your JSON
6. write your independent interpretation
7. only then compare to the reference JSON
```

Do not optimize for agreement with another model.

Do not ask what Claude, ChatGPT, Gemini, Grok, DeepSeek, Copilot, or another reviewer obtained.

A divergence is useful if it is real.

---

# 2. Official execution command

Run exactly:

```bash
python3 nexus4_leak_blindness_v2_0.py \
  --years 1050 \
  --seeds 40 \
  --calib-seeds 200 \
  --mdr-seeds 32 \
  --horizon-seeds 40 \
  --json my_run_v2.json
```

Dependencies:

```text
Python >= 3.10
NumPy
```

No network, SciPy, plotting library, Jupyter-specific feature, or external dataset is required.

Record:

```text
OS
architecture
CPU if available
Python version
NumPy version
script SHA-256
result JSON SHA-256
```

If the script hash differs from the official hash, report the difference before interpreting the results.

Do **not** silently normalize whitespace, change line endings, alter parameters, or patch the code.

---

# 3. What is canonical and what is not

The experiment is not allowed to redefine Project Nexus.

The relevant source hierarchy must remain explicit.

Direct source inspection has established the following boundaries in current Nexus/HVD architecture:

- **CA:** high-level cognitive orchestration, prediction, learning, and system-level cognitive behavior; not storage engine or object resolver.
- **HTCE:** owns the active cognitive field, including ephemeral HVD generation, active thought-space population, coalition membership, resonance, activation/decay, field expansion/collapse, and candidate release.
- **TMS:** mandatory live substrate; owns active realization, trajectory, history, working memory, structural sharing/COW state, WAL, Memtables, SSTables, compaction/reconsolidation, and physical state movement.
- **HVD:** complete cognitive database semantics: collections, records, stable logical identity, mutation, exact/associative retrieval, HTLA/HTNLA representation, indexing, cross-HVD references, durability/distribution contracts.
- **HIGC:** constitutional/admissibility boundary.
- **THDE:** bounded state evolution and hysteretic intervention.
- **QMT:** continuity across transformation.
- **HDF5:** durable long-term/permanent persistence, not merely snapshot storage.

Source hierarchy caveat:

- HVD 1.5 §16.2 says TMS must preserve enough historical information for a **future controller to compute something such as** `q_(k+1)=lambda*q_k+severity_k`.
- That section is **not proof that this scalar recurrence is the implemented THDE detector**.
- The deterministic N-dimensional architecture separately specifies the leaky THDE form and also lists Preisach / Prandtl-Ishlinskii / Bouc-Wen hysteresis with **rate-independent memory**.

Therefore the following claims are prohibited unless independently source-inspected:

```text
"all Nexus barriers are leaky"
"all Nexus barriers are derivative-based"
"THDE is exactly d_leaky_abs()"
"CUSUM should replace THDE"
"raw_sqrt should replace THDE"
"the e-process is canonical Nexus"
```

The code contains candidate analogs and controls, not canonical subsystem replacements.

---

# 4. Experiment modules

v2.0 has seven logically distinct modules. Do not collapse them into one conclusion.

## M0 — Generator and implementation invariants

Built-in self-tests must establish:

```text
creep channel 1 == instrument channel 1 bit-for-bit
creep channel 2 != instrument channel 2
Green Sky reaches +6 sigma
Green Sky has a flat 150-year plateau
Green Sky returns exactly to baseline
vectorized one-sided CUSUM == sequential recurrence
vectorized two-sided CUSUM == sequential recurrence
Gaussian-mixture e-process formula sanity check passes
```

A self-test failure invalidates the run.

---

## M1 — Scenario stress test

Six observation conditions:

```text
null
creep
instrument
greensky
shock
confound
```

`creep` is a **linearly increasing state displacement relative to the original reference**.

It is **not** a direct implementation of THDE `severity_k`, and it is not derivative-only input.

That distinction is mandatory.

The scenario test reports:

```text
pre-onset false alarm
post-onset detection
post-onset delay
Green-Sky plateau alarm fraction
quiet/alarming after return
```

A detector that false-alarms before onset must not receive credit for that alarm as successful post-onset detection.

---

## M2 — Finite-horizon ramp sensitivity

The experiment searches for an MDR50:

```text
minimum linear ramp rate producing >= 50% detection
```

at the configured 1050-year horizon.

This metric is intentionally retained for continuity with v1.1.

But its interpretation is narrower than the old headline claim.

Because:

```text
x_k = rate*k + noise
```

the final displacement grows with observation length.

Therefore:

> **MDR50 on this ramp does not by itself establish a duration-independent leak-blindness floor.**

Use it only as a finite-horizon comparison of candidate detector behavior under this particular signal construction.

---

## M3 — Horizon robustness

Every detector keeps the same threshold it received at the 1050-year base horizon.

It is then exposed to null data for:

```text
1x
4x
16x
```

the base horizon.

This asks:

> If I tune this detector today and do not know how long the individual will continue operating, does the nominal false-alarm behavior deteriorate as observation opportunities accumulate?

Important:

```text
survives x16
!=
proved safe forever
```

The experiment is finite.

At `--horizon-seeds 40`, one observed run corresponds to 0.025 in the empirical rate. Treat small rate differences accordingly.

---

## M4 — Exact leaky-memory controls

Two mathematical controls are separate from the Green-Sky simulation.

### M4A — Constant-severity fixed point

For:

```math
q_{k+1} = lambda q_k + s
```

with `0 <= lambda < 1`:

```math
q_infinity = s / (1-lambda)
```

For threshold `theta`, constant input below:

```math
s < (1-lambda) theta
```

cannot cross `theta` in the idealized recurrence.

This establishes a property of the recurrence.

It does **not** establish that real Nexus `severity_k` is constant, scalar, derivative-like, Gaussian, signed, or generated from the Green-Sky observable this way.

### M4B — Normalized linear-EWMA effective memory

For the control:

```math
m_k = lambda m_{k-1} + (1-lambda)x_k
```

with iid input variance `sigma^2`:

```math
Var(m_infinity) = sigma^2 (1-lambda)/(1+lambda)
```

and therefore:

```math
N_eff = (1+lambda)/(1-lambda)
```

This is the mathematically correct finite-effective-memory statement for a **linear normalized leaky estimator**.

It is more precise than casually saying `tau=1/(1-lambda)` samples are averaged. For lambda near one, `N_eff` is approximately `2/(1-lambda)`, while `tau=1/(1-lambda)` remains the recurrence time constant.

Again: this is a mathematical control, not a claim about the complete THDE measurement mapping.

---

## M5 — Single-channel identifiability

`creep` and `instrument` are deliberately constructed to have identical channel-1 observations.

Therefore no deterministic or stochastic algorithm that receives **only that same observation stream and no additional information** can infer which latent causal construction produced it better than whatever prior assumptions it already carries.

That is a construction-level identifiability result, not merely an empirical detector failure.

The required architectural conclusion is narrower than:

```text
"Nexus must have exactly two physical sensors"
```

What follows is:

> **Causal attribution between observationally equivalent world-change and instrument-change hypotheses requires an additional independent information source.**

That source could be:

```text
an independent sensor
an external metrological reference
instrument lineage/calibration evidence
an intervention
an independently grounded physical model
another causally informative channel
```

The `crosschannel` detector is only one minimal demonstration.

It detects disagreement; it does not identify absolute truth by itself.

---

## M6 — Reference and recurrence semantics

Two reference comparators are deliberately separated:

```text
ref_blue
    knows only the original blue epoch

ref_blue_green_known
    assumes blue AND green are already retained references
```

The second detector is a **recurrence-recognition control**.

It is not allowed to support any claim that the system knows how to:

```text
authorize a first-time new epoch
promote a reference
migrate a reference
retire a reference
establish that green is true
```

It answers only:

> What changes if a previously accepted epoch is already in the reference set?

That distinction matters because "clearing by forgetting" and "clearing by recognizing a retained epoch" are architecturally different capabilities.

---

## M7 — Anytime-valid control

`normal_mixture_e` is included because the pilot overinterpreted `S_k/sqrt(k)`.

Under iid Gaussian observations with known mean and variance under the null:

```math
M_t = sqrt(rho/(rho+t)) exp(S_t^2 / (2(rho+t)))
```

is a nonnegative martingale.

Thresholding at:

```math
M_t >= 1/alpha
```

provides a time-uniform false-alarm bound via Ville's inequality under those assumptions.

This detector is included to demonstrate the conceptual class:

```text
fixed-horizon empirical threshold
vs
finite tested horizon survival
vs
anytime-valid boundary
```

It is not a proposed canonical Nexus detector.

Its guarantee can fail under model misspecification such as:

```text
serial correlation
heavy tails
unknown/changing variance
nonstationary null
adversarial dependence
incorrect reference mean
```

Those are explicit secondary-test targets.

---

# 5. Historical preregistration P1–P8

These statements are immutable historical records from before the first pilot.

Do not edit them to make the experiment look better.

Historical v1.1 results:

```text
P1 PASS
P2 PASS
P3 FAIL
P4 FAIL
P5 FAIL
P6 PASS
P7 PASS
P8 PASS
```

The failures matter:

### P3

Original claim:

> `raw_fixed` cannot be calibrated.

Correction:

It **can** be calibrated for a known finite horizon. The deeper problem observed later is horizon dependence: its fixed threshold becomes useless when the run greatly exceeds the calibration horizon.

### P4

Original claim:

> CUSUM `nu` is a floor on detectable drift rate.

Correction:

For the implemented Page CUSUM, `nu` is a reference/slack on the monitored location/mean-shift statistic. A slow ramp that eventually reaches +6 sigma can exceed `nu=0.5` and then accumulate strongly.

### P5

Original claim:

> `raw_sqrt` has the best finite-horizon MDR.

Correction:

The pilot found CUSUM `nu=0.02` slightly better. v2.0 uses more MDR seeds because that comparison is close and noisy.

The correct scientific behavior is to preserve the failed prediction and refine the question, not rewrite the prediction.

---

# 6. Post-pilot replication targets R1–R6

These were registered **after** seeing v1.1.

They are valid independent-replication targets, but they are not pre-pilot discoveries.

```text
R1 raw_fixed should lose calibration badly by x4.
R2 CUSUM nu=0.5 should detect the configured 6-sigma creep excursion.
R3 raw_sqrt and CUSUM nu=0.02 finite-horizon MDR50 should be within a factor of 2.
R4 Gaussian-mixture e-process empirical null FA should remain <=0.10 at x1/x4/x16.
R5 crosschannel should stay low on common-mode creep and high on instrument/confound.
R6 blue-only reference should alarm through green while a pre-known blue+green bank should alarm much less on the plateau.
```

A failed R-target remains a result.

Do not rerun until it passes.

---

# 7. Reference run

The official reference was generated with:

```text
Python: 3.13.5
NumPy: 2.3.5
--years 1050
--seeds 40
--calib-seeds 200
--mdr-seeds 32
--horizon-seeds 40
```

Do **not** read the detailed reference results before your independent run.

After your run is saved, compare JSON fields mechanically.

Expected high-level reference outcomes are intentionally limited here to bookkeeping:

```text
all self-tests PASS
historical P1/P2/P6/P7/P8 reproduce PASS
historical P3/P4/P5 reproduce FAIL
post-pilot R1-R6 PASS in the reference environment
```

Numerical disagreement is not automatically failure. Report:

```text
absolute difference
relative difference where meaningful
whether verdict changes
Python/NumPy/environment differences
```

---

# 8. Rules for multi-model reviewers

1. **Run before interpreting.**
2. **Do not cite this protocol as evidence that a Nexus architectural claim is true.**
3. **Any claim about actual Nexus architecture must cite an exact inspected source section or be UNRESOLVED.**
4. **Do not use derived audio transcripts to establish CANONICAL or IMPLEMENTED status.**
5. **A detector in this script is EXPERIMENTAL unless source inspection independently says otherwise.**
6. **Do not promote a finite-horizon result into a 10,000-year guarantee.**
7. **Do not promote an iid-Gaussian anytime guarantee into robustness under arbitrary real-world noise.**
8. **Do not equate cross-channel disagreement with truth.**
9. **Do not equate a pre-known reference bank with reference migration or governance.**
10. **Do not treat a scalar signed detector as automatically meaningful for high-dimensional or non-scalar Nexus state.**
11. **Attack before agreeing.** Name at least one discriminating failure test for every proposed architectural conclusion.
12. **Every objection must include a concrete repair or alternative.**
13. **Preserve negative results.** Never edit P1–P8 after the fact.

Use epistemic tags for substantive architectural claims:

```text
CANONICAL
IMPLEMENTED
VERIFIED
PARTIALLY_IMPLEMENTED
PROPOSED
DESIGN_TARGET
EXPERIMENTAL
RESEARCH_HYPOTHESIS
INFERRED
TESTIMONY
DERIVED
HISTORICAL_SUPERSEDED
UNRESOLVED
```

---

# 9. Open questions the experiment does not settle

## Q1 — Transfer to real THDE

The scalar analog uses:

```text
severity-like input = |x-mu|
```

Real THDE is high-dimensional and coexists with rate-independent hysteresis operators.

Inspect the implementation/specification and answer:

```text
What exactly is severity_k?
Is it scalar or vector/tensor derived?
Is it signed or nonnegative?
Is it level-, residual-, derivative-, prediction-error-, or geometry-based?
How is it normalized?
What resets or changes its reference?
What role do Preisach/PI/Bouc-Wen operators play relative to the leaky recurrence?
```

Until inspected, transfer from this experiment to production THDE is **UNRESOLVED**.

---

## Q2 — Observation independence

What independent information sources does Nexus actually possess?

Do not merely count sensors.

Identify shared failure modes:

```text
shared calibration
shared training data
shared clock
shared ontology
shared preprocessing
shared power/substrate
shared physical placement
shared causal model
```

Two nominal channels with one common failure mode may not solve M5.

---

## Q3 — Reference authorization

Who may add a new epoch reference?

Separate:

```text
detect novelty
retain candidate epoch
validate evidence
promote reference
supersede reference
recognize recurrence
```

Detection must not silently perform promotion.

Does reference migration share machinery with constitutional/contract evolution, or merely share abstract continuity requirements?

---

## Q4 — Review vs resistance

Green Sky can be real.

Should persistent drift cause:

```text
mechanical resistance
cognitive review
increased retention
competing-hypothesis generation
reference challenge
some combination
```

What is the interim posture while review is unresolved?

---

## Q5 — Retrospective trigger problem

A cumulative drift alarm may fire decades after the causal micro-events have been consolidated.

Specify what survives strongly enough to reconstruct that interval:

```text
predictions
anomalies
testimony
calibration events
ontology changes
interventions
constitutional/identity events
reference changes
```

A proposal that says "retain more once drift is detected" is incomplete because detection is late.

---

## Q6 — Causal hypothesis collapse

Define a representation-stable trigger based on explanatory probability mass over hypothesis families rather than hypothesis count.

Specify:

```text
quantity
update rule
threshold
computational cost
retention consequence
false-trigger control
```

---

## Q7 — CA ownership

Does slow-drift handling need a CA-level regime policy, or can observation/detection remain below CA with CA only allocating resources after escalation?

Do not answer by architecture taste.

Give a discriminating test or source-based ownership argument.

---

## Q8 — Anytime-validity under realistic noise

The e-process control assumes iid Gaussian noise with known sigma.

Run secondary tests under:

```text
AR(1) correlation
Student-t heavy tails
variance drift
seasonality
missing data
regime-switching null
adversarial bursts
cross-channel correlated failures
```

The objective is not to defend the e-process. It is to determine what kind of time-uniform evidence mechanism survives realistic Nexus conditions.

---

## Q9 — High-dimensional state geometry

Green Sky is represented here as one scalar coordinate.

Actual Nexus state may require:

```text
vector/tensor residuals
manifold distance
hypervector similarity/dissimilarity
subspace drift
covariance change
ontology change
hysteresis state
```

Determine whether the scalar conclusions survive under the real geometry.

---

# 10. Secondary experiments encouraged after the primary run

Do not modify the official primary run.

Create a separately named artifact for every extension.

Priority secondary experiments:

```text
S1 sweep horizon factors and estimate rate confidence intervals
S2 AR(1) and heavy-tail nulls for horizon robustness
S3 variance drift / calibration drift
S4 correlated two-channel failures
S5 three-or-more-channel attribution with one faulty channel
S6 first-time reference authorization vs recurrence recognition
S7 repeated Green-Sky epochs with preserved epoch history
S8 high-dimensional/vector Green-Sky trajectory
S9 explicit candidate mappings from real THDE severity_k after source inspection
S10 anytime-valid detectors robust to non-Gaussian/dependent noise
```

---

# 11. Required response format for panel members

Return exactly these sections:

## 1. Execution provenance

```text
OS:
architecture:
CPU:
Python:
NumPy:
script hash:
command:
result JSON hash:
run status: VALID / INVALID / INCOMPLETE
```

## 2. Self-tests

Report every self-test.

## 3. Calibration

Full detector threshold table.

## 4. Scenario results

Report post-onset detection, pre-onset false alarms, and delays.

## 5. Green-Sky reversal

Report plateau alarm and after-return behavior.

## 6. MDR50

Report the finite-horizon values and explicitly label them finite-horizon.

## 7. Horizon robustness

Report x1/x4/x16 and state the seed resolution.

## 8. Analytic controls

Explain M4A and M4B separately from the simulation.

## 9. Historical P1–P8

Report both:

```text
historical v1.1 verdict
current rerun verdict
```

Do not overwrite history if they differ.

## 10. R1–R6 replication targets

PASS / FAIL / INDETERMINATE with evidence.

## 11. Reference comparison

Only now open the reference JSON.

Report meaningful numerical divergences.

## 12. Methodological attacks

At least one serious attack on:

```text
signal model
null model
calibration
MDR metric
horizon test
identifiability interpretation
reference semantics
architectural transfer
```

## 13. Repairs

Concrete alternative for every attack.

## 14. Answers to Q1–Q9

Every substantive claim tagged with the epistemic vocabulary.

## 15. Ownership map

```text
mechanism -> subsystem -> evidence/source -> boundary check
```

Do not recreate a CA god-object.

## 16. New registered predictions

Give date, reason, and whether the prediction was formed before or after seeing any relevant result.

## 17. UNRESOLVED

State unresolved items rather than filling them optimistically.

---

# 12. Success criterion

The experiment succeeds if it makes the next architectural question **narrower and better sourced**.

It does not succeed by producing a preferred detector.

A valid outcome can be:

```text
an old prediction remains falsified
an apparent horizon-robust detector fails under correlated noise
a supposed independent channel proves correlated
a source inspection shows real THDE severity is unlike the scalar analog
a candidate repair creates unacceptable false alarms
```

Those are discoveries, not failures of the exercise.
