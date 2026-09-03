# Nexus 4 Objective C Deep-Time Detector Experiment v2.0
## Experiment Overview, Rationale, Reading Guide, and Interpretation Supplement

**Artifact status:** RESEARCH SUPPLEMENT  
**Purpose:** Explain the scope, origin, design, interpretation, and limits of the Nexus 4 Objective C deep-time detector experiment.  
**Companion artifacts:**  
- `nexus4_leak_blindness_v2_0.py`
- `RUN_PROTOCOL_nexus4_leak_blindness_v2_0.md`
- `nexus4_leak_blindness_v2_0_reference.json`
- `nexus4_leak_blindness_v2_0_reference.md`

**This document supplements those artifacts. It does not replace them.**

---

# 1. Why this document exists

The experiment bundle contains a Python research harness, a replication protocol, a machine-readable reference result, and a human-readable reference result. Those files are useful for execution and comparison, but by themselves they do not preserve enough of the intellectual context that caused the experiment to exist.

A future reader encountering only a table such as:

```text
CUSUM nu=0.02: x1 = 0.03, x4 = 0.28, x16 = 0.85
```

would have no reliable way to know:

- why CUSUM was tested in the first place;
- what "x16" means;
- what problem the experiment was intended to distinguish;
- why Green Sky returns to blue;
- why `creep` and `instrument` deliberately share an identical observation channel;
- why a reference bank appears next to cumulative detectors;
- why several historically preregistered predictions are intentionally preserved even after being falsified;
- why a Gaussian-mixture e-process was added later;
- or, most importantly, what any of this does and does not say about the actual Nexus 4 architecture.

This supplement preserves that missing scope.

---

# 2. Executive summary

The Objective C experiment grew out of a Project Nexus 4 deep-time architecture review asking a deceptively simple question:

> **Can a long-lived cognitive system notice meaningful change that occurs so slowly that no individual step looks exceptional?**

The question arose from the **Green Sky** thought experiment. In simplified form, a Nexus individual experiences approximately:

```text
500 years: sky is blue
150 years: the world gradually changes until the sky is genuinely green
150 years: sky remains genuinely and stably green
150 years: the world gradually returns toward blue
100 years: sky is blue again
```

The challenge is not merely to detect that something changed. A deep-time cognitive system must distinguish several different problems:

1. **Slow-change detection** — can gradual displacement be noticed at all?
2. **Long-horizon calibration** — does a detector that behaves well over 1,000 years remain statistically sane if the system continues for 4,000, 16,000, or longer?
3. **World-versus-instrument attribution** — did reality change, or did the measuring apparatus drift?
4. **Regime recognition** — is the current state novel, or is it a return to a previously known epoch?
5. **Reference governance** — who or what is allowed to declare that a newly observed regime has become an accepted reference?
6. **Historical retention** — how does the system remember that blue, green, and blue-again were three historically meaningful regimes without averaging them into a fictitious timeless state?
7. **Architectural ownership** — which part of Nexus should detect, interpret, retain, authorize, or act on these conditions?

The experiment does **not** solve all seven problems. It deliberately isolates smaller mathematical and epistemic subproblems so that they can be measured instead of argued about.

The central lesson of v2.0 is that there is no single scalar question called "slow-drift blindness." Several distinct mechanisms can fail for different reasons:

```text
leaky memory
fixed-horizon calibration
single-channel non-identifiability
fixed-reference latching
failure to recognize recurrence
model misspecification
```

Those failures must not be collapsed into one detector choice.

---

# 3. Origin of the experiment

## 3.1 The architectural dispute

During an adversarial review of Nexus 4, multiple language models were asked whether the architecture could miss arbitrarily slow environmental or cognitive drift.

The review produced apparent agreement, but the evidentiary basis was weak. Some responses treated assertions in the research prompt as if they were already established architectural facts. Others generalized simplified THDE equations into claims about the whole Nexus stability architecture.

That created two separate problems:

```text
A. The technical question was still unresolved.

B. The review process itself was capable of manufacturing consensus
   without independent measurement.
```

The experiment was created to remove as much of Objective C as possible from the language-model deliberation layer.

Instead of asking:

> "Do you think Nexus is blind to slow drift?"

the project could now ask:

> "Under explicitly defined stochastic conditions, how do several classes of sequential detector actually behave?"

That is a narrower question, but it is measurable.

---

# 4. The Green Sky problem

The Green Sky scenario is not simply a change-detection benchmark.

Its deeper purpose is to expose how a long-lived cognitive system can corrupt history if it treats truth as a timeless average or as a single overwriteable value.

The bad outcomes are easy to state.

## 4.1 Averaging failure

If centuries of blue and centuries of green are collapsed into one aggregate representation, the system can produce a fictitious "average sky" that was never actually observed.

Conceptually:

```text
BLUE epoch
   +
GREEN epoch
   +
BLUE-again epoch
   ↓
timeless average
   ↓
CYAN-like representation that never existed
```

This destroys historical truth.

## 4.2 Overwrite failure

If the system simply replaces old belief with new belief:

```text
sky = blue
↓
sky = green
↓
sky = blue
```

then the final state may be correct while the history of the green epoch disappears.

That is catastrophic forgetting of epistemic history.

## 4.3 Deep-time requirement

A correct system needs something closer to:

```text
epoch A:
    world state
    available evidence
    belief
    confidence
    reference state

epoch B:
    changed world state
    changed evidence
    changed belief
    relationship to epoch A

epoch C:
    return or partial return
    relationship to A and B
```

The experiment does not implement the entire historical architecture. It tests several lower-level mechanisms that such an architecture would depend on.

---

# 5. What Objective C is actually testing

Objective C is best understood as a **deep-time sequential detection and epistemic identifiability experiment**.

It asks five primary experimental questions.

## Q1 — What does leakage do to persistent evidence?

A simplified leaky recurrence has the form:

```math
q_{k+1} = \lambda q_k + s_k,
\qquad 0 \le \lambda < 1.
```

For constant severity \(s\),

```math
q_\infty = \frac{s}{1-\lambda}.
```

Therefore a fixed threshold \(h\) has an exact constant-severity floor:

```math
s < (1-\lambda)h
```

implies that the recurrence never reaches the threshold.

This is an exact mathematical property of the simplified recurrence.

The experiment separately evaluates noisy finite-horizon detector behavior because real observations are not constant deterministic severity streams.

---

## Q2 — Does a detector stay calibrated when the observation horizon is unknown?

Many change detectors are calibrated over a predefined observation horizon.

That assumption is uncomfortable for Project Nexus because the point of the architecture is deep-time continuity. A detector commissioned today should not become statistically certain to alarm merely because the individual remained alive much longer than the engineer expected.

v2.0 therefore asks:

```text
Calibrate at horizon N.

Without changing the threshold, test the same detector at:
    N
    4N
    16N
```

This section is called **horizon robustness**.

It is a finite stress test, not a proof of infinite-horizon validity.

---

## Q3 — Can one observation channel distinguish world drift from instrument drift?

No, not in the constructed case.

The experiment deliberately generates:

```text
CREEP:
    world changes
    instrument remains stable

INSTRUMENT:
    world remains stable
    instrument changes
```

while forcing channel 1 to be **bit-identical** in both cases.

Therefore:

```text
observed channel 1 under CREEP
==
observed channel 1 under INSTRUMENT
```

Any deterministic algorithm receiving only that channel must produce the same result for both.

This is not a matter of detector quality.

It is an identifiability limit.

The experiment then adds a second independent observation channel and tests whether disagreement between channels can expose the difference.

Important:

> Cross-channel disagreement detects disagreement. It does not automatically identify which channel represents truth.

Additional provenance, calibration, redundancy, intervention, or metrological reference is still required for causal attribution.

---

## Q4 — What happens when reality returns to an old regime?

Green Sky is not:

```text
blue -> green forever
```

It is:

```text
blue -> green -> blue
```

That distinction matters.

A cumulative detector may successfully notice departure from blue while remaining permanently latched afterward.

A leaky detector may eventually clear because it forgets.

A retained-epoch comparator may clear because it recognizes that the system has returned to a known state.

Those three outcomes look superficially similar in an alarm table but are architecturally different.

v2.0 therefore separates:

```text
ref_blue
```

from:

```text
ref_blue_green_known
```

The first knows only the original blue epoch.

The second assumes that blue and green are already retained references.

The second detector is therefore testing **recurrence recognition**, not the authorization or learning of a new epoch.

---

## Q5 — Can any detector offer an unknown-horizon statistical guarantee?

The legacy `raw_sqrt` comparator uses:

```math
\frac{|S_k|}{\sqrt{k}}.
```

It performs well over the finite horizons tested here.

However, good behavior through \(16N\) does not make it an indefinitely valid sequential test.

v2.0 therefore includes a **Gaussian-mixture e-process** as an explicit anytime-valid control under its stated iid Gaussian null model.

Its purpose is not to declare an e-process the Nexus solution.

Its purpose is to include at least one detector whose null guarantee is designed to be time-uniform, so that:

```text
finite-horizon robustness
```

can be distinguished from:

```text
formal anytime validity under a specified model.
```

---

# 6. What the experiment is NOT

The experiment is a research harness.

It is **not**:

- the production THDE implementation;
- a complete model of the high-dimensional Nexus cognitive state;
- a proof that every Nexus stability mechanism is leaky;
- a proof that CUSUM is wrong;
- a proof that `raw_sqrt` is correct;
- a proof that an e-process should be adopted;
- an implementation of Cyrae;
- an implementation of CA;
- an implementation of reference migration;
- a metrological authority system;
- a complete Green Sky solution;
- a 10,000-year safety proof;
- Nexus canon.

The scalar detector called "leaky" is an experimental analog of one recurrence form associated with THDE-related reasoning.

It must not be read as:

```text
this detector == complete THDE
```

Similarly, the experiment's scalar observation \(x_k\) is not equivalent to the real Nexus high-dimensional state.

---

# 7. Experimental timeline

At the default configuration:

```text
1 tick = 1 month
12 ticks = 1 year
```

The primary experiment spans:

```text
500 years   original blue baseline
150 years   gradual transition toward green
150 years   stable green plateau
150 years   gradual return toward blue
100 years   blue tail after return
---------------------------------------
1050 years total
```

The default primary horizon is therefore:

```text
1050 years
=
12,600 monthly observations
```

Horizon stress tests then extend null observation streams to multiples of that baseline horizon.

---

# 8. The six signal conditions

The output repeatedly refers to six conditions. They mean:

## `null`

```text
world stable
instrument stable
noise only
```

Purpose: false-alarm calibration and validation.

---

## `creep`

```text
world slowly changes
both instruments observe the same world change
```

Purpose: evaluate gradual world displacement.

This is a growing state displacement from a fixed baseline. It is **not** a direct implementation of THDE's internal `severity_k`.

---

## `instrument`

```text
world stable
instrument 1 slowly drifts
instrument 2 remains stable
```

Channel 1 is intentionally constructed to be identical to `creep`.

Purpose: demonstrate the single-channel identifiability problem.

---

## `greensky`

```text
blue
↓ gradual change
green plateau
↓ gradual reverse change
blue again
```

Purpose: test first departure, stable changed reality, and return to an old regime.

---

## `shock`

```text
stable baseline
↓
abrupt 6-sigma step
```

Purpose: provide the easy fast-change control.

If a detector cannot notice the shock, its behavior on slow drift is not very interesting.

---

## `confound`

```text
world moves one direction
instrument bias moves the opposite direction
channel 1 largely cancels the two
```

Purpose: demonstrate that apparent observational stability can hide simultaneous movement in both the world and the measuring apparatus.

---

# 9. Detector families

The experiment intentionally compares mechanisms with different mathematical properties.

The goal is not to select a production winner.

## 9.1 Leaky absolute-deviation accumulators

Tested at:

```text
lambda = 0.9
lambda = 0.99
lambda = 0.999
```

Simplified concept:

```math
q_{k+1} = \lambda q_k + |x_k-\mu|.
```

These represent finite-memory accumulation.

Larger \(\lambda\) means slower forgetting.

---

## 9.2 Raw absolute-deviation sum with fixed threshold

Concept:

```math
Q_k = \sum_{i=1}^{k}|x_i-\mu|.
```

It accumulates non-negative evidence forever.

At a fixed finite horizon it can be calibrated.

At a much longer horizon, however, accumulated baseline noise eventually destroys that calibration.

This detector exists partly to demonstrate why "just set \(\lambda=1\)" is not sufficient.

---

## 9.3 Centered cumulative sum divided by \(\sqrt{k}\)

Legacy comparator:

```math
Z_k =
\frac{\left|\sum_{i=1}^{k}(x_i-\mu)\right|}{\sqrt{k}}.
```

This normalizes the scale of an ordinary random walk over a finite horizon.

It behaved strongly in the tested horizon stress conditions.

It is retained as a useful comparator, but v2.0 explicitly does **not** call it anytime-valid.

---

## 9.4 CUSUM detectors

The experiment includes several one-sided CUSUMs and one two-sided scalar CUSUM.

Conceptually:

```math
C_k^+ =
\max(0,C_{k-1}^+ + r_k-\nu).
```

The parameter \(\nu\) is a reference/slack term associated with the magnitude of the mean displacement being targeted.

An important historical error was the claim that \(\nu\) created a floor on detectable **drift rate**.

The experiment falsified that interpretation.

A sufficiently slow ramp can eventually create a large displacement. Once the displacement exceeds the CUSUM reference scale, the detector can accumulate strongly.

Thus:

```text
rate
!=
displacement
```

This distinction is one of the reasons the historical failed prediction P4 remains preserved.

---

## 9.5 Fixed blue reference

The blue-only EWMA reference asks approximately:

> "Does the current smoothed state remain close to the original blue reference?"

It is deliberately unable to declare green legitimate.

Therefore it alarms through the green plateau.

That behavior is not necessarily a bug. It exposes the distinction between:

```text
change detection
```

and:

```text
reference authorization.
```

---

## 9.6 Known blue+green epoch bank

This comparator is given both blue and green as already-retained references.

It asks:

> "Does the current regime resemble any already-known epoch?"

It can therefore recognize the green plateau without treating it as unknown.

This is a recurrence-recognition experiment.

It does **not** answer:

```text
Who created the green reference?
Who authorized it?
When was promotion permitted?
What evidence justified it?
```

Those are architecture questions outside this detector.

---

## 9.7 Cross-channel disagreement detector

This detector monitors disagreement between two observation channels.

It is intended to show the minimum informational requirement exposed by the `creep`/`instrument` construction.

Its correct interpretation is:

```text
independent disagreement evidence helps break single-channel ambiguity
```

not:

```text
channel 2 automatically tells us objective truth.
```

---

## 9.8 Gaussian-mixture e-process

This is the experiment's anytime-valid statistical control.

Under the modeled iid Gaussian null, the e-process provides a time-uniform sequential testing framework.

Its inclusion answers a methodological question:

> What does a detector specifically designed for indefinite sequential monitoring look like compared with detectors whose thresholds were calibrated at one fixed horizon?

Its model assumptions matter.

A guarantee under iid Gaussian noise is not automatically valid under:

- autocorrelation;
- heavy tails;
- nonstationarity;
- heteroscedasticity;
- adversarial observations;
- high-dimensional dependence;
- sensor aging;
- changing measurement schemas.

---

# 10. Calibration methodology

Most detectors are empirically calibrated to approximately:

```text
5% probability of at least one false alarm
over the primary 1050-year null run.
```

That is important.

The threshold is not chosen merely so that 5% of **individual samples** cross it.

It is intended to control whether a run produces any alarm over the configured horizon.

The horizon-robustness experiment then deliberately asks whether that calibration survives when the observation period becomes much longer without recalibration.

The e-process differs because its threshold comes from an analytic anytime construction rather than the same fixed-horizon empirical calibration procedure.

---

# 11. How to read the reference results file

The file:

```text
nexus4_leak_blindness_v2_0_reference.md
```

is the human-readable output of one official reference execution.

It is primarily an **output artifact**, not explanatory documentation.

Read its sections as follows.

---

## 11.1 Header and run metadata

This identifies:

- script version;
- script hash;
- Python version;
- NumPy version;
- primary horizon;
- numbers of random seeds;
- false-alarm target.

These details matter for reproducibility.

If a future run differs materially, compare environment and command parameters before assuming the experiment changed scientifically.

---

## 11.2 Scope guardrails

These lines constrain interpretation.

They are not decorative disclaimers.

For example:

```text
The leaky absolute-deviation detector is a scalar analog,
not the complete THDE runtime.
```

means that no result may legitimately be rewritten as:

```text
"THDE itself has been proven incapable of X."
```

unless the actual THDE implementation has separately been shown to instantiate the relevant mathematical assumptions.

---

## 11.3 Self-tests

All self-tests should pass before interpreting the run.

They verify such things as:

```text
creep.x == instrument.x
Green Sky really returns to baseline
CUSUM vectorization matches the sequential recurrence
```

If these fail, the run should be treated as invalid until diagnosed.

---

## 11.4 Calibration table

Columns:

### `threshold mode`

How the alarm threshold was obtained.

Examples:

```text
empirical_fixed_horizon
analytic_anytime
```

### `h`

The actual detector threshold.

Threshold magnitudes cannot be compared directly across detector families because their statistics have different units and scales.

### `base-horizon null FA`

Observed false-alarm probability over the primary null horizon.

This is a calibration sanity check.

---

## 11.5 Post-onset detection-rate table

This table asks:

> After a change begins, how often did the detector eventually alarm?

For `null`, there is no change onset, so the null column remains an any-alarm false-alarm rate.

Important:

A detector with:

```text
creep = 1.00
```

has not necessarily solved deep-time drift.

It only means that the configured creep excursion was eventually detected in all evaluated runs.

Detection delay and horizon calibration still matter.

---

## 11.6 Creep false alarms and detection delay

This table separates:

```text
pre-onset false alarm
```

from:

```text
post-onset detection.
```

This separation was added because a detector should not receive credit for "detecting" a change if it had already alarmed before the change existed.

### `median delay years`

Number of simulated years between onset of the gradual world change and successful post-onset detection.

Lower is faster.

But fastest is not automatically best.

A detector that reacts quickly while becoming almost certain to false-alarm over a longer lifetime may be unacceptable for deep-time use.

---

## 11.7 Green Sky reversal behavior

This is one of the most architecturally important tables.

### `green plateau alarm fraction`

Fraction of the genuinely stable green epoch during which the detector remains in alarm.

A value of:

```text
1.00
```

means it spends the entire 150-year green plateau saying the state remains anomalous relative to its current reference logic.

### `quiet after return`

Fraction of runs in which the detector is no longer alarming after the sky has returned to blue.

### `alarm after return`

Fraction still alarming after return.

Interpret the reason for clearing.

For example:

```text
leaky detector clears
```

may mean:

```text
old evidence decayed away
```

whereas:

```text
known epoch bank clears
```

may mean:

```text
the state matches a retained historical reference.
```

Those are not equivalent cognitive capabilities.

---

## 11.8 MDR50 table

MDR50 means:

> The smallest configured linear-ramp rate detected in at least approximately 50% of runs over this finite experimental horizon.

Units:

```text
sigma per simulated year
```

Lower means greater sensitivity to the configured linear ramp.

The companion column converts this into an intuitive scale:

```text
years required for a 1-sigma displacement
at that linear rate.
```

This metric is useful for comparing finite-horizon sensitivity.

It is **not** an asymptotic proof of arbitrary-slow-drift detection.

---

## 11.9 Horizon robustness table

This table is critical for the deep-time question.

Each detector is calibrated once at the primary horizon.

Its threshold is then frozen.

Null noise is observed for:

```text
x1  = original horizon
x4  = four times original horizon
x16 = sixteen times original horizon
```

If false-alarm probability rises dramatically, then the detector's original calibration depended on knowing the observation horizon.

Example interpretation:

```text
0.03 -> 0.28 -> 0.85
```

means:

> A threshold that appeared well calibrated at the design horizon becomes very unreliable as monitoring continues much longer.

Conversely:

```text
0.03 -> 0.03 -> 0.03
```

means:

> No degradation was observed through the finite x16 stress test.

It does **not** by itself prove infinite-horizon validity.

That distinction is why the e-process control exists.

---

## 11.10 Exact leaky-memory analytic controls

These are not Monte Carlo results.

They are simplified mathematical controls.

### Constant severity

For:

```math
q_{k+1}=\lambda q_k+s,
```

the equilibrium is:

```math
q_\infty=\frac{s}{1-\lambda}.
```

Therefore:

```math
s_\text{floor}=(1-\lambda)h
```

for threshold \(h\).

A severity below that value never reaches the threshold in the simplified deterministic recurrence.

### Effective memory

For a normalized linear EWMA, the table reports an effective sample-size relation:

```math
N_{\mathrm{eff}}
=
\frac{1+\lambda}{1-\lambda}.
```

This helps explain why extending elapsed observation time does not indefinitely increase the effective memory of a leaky statistic.

These controls are mathematical intuition for simplified recurrences.

They are not implementation evidence about Nexus.

---

# 12. Why the historical failed predictions remain in the output

The experiment preserves P1-P8 because they were registered before the pilot results were known.

Three were wrong:

```text
P3
P4
P5
```

They remain deliberately visible.

Deleting or rewriting them would destroy the provenance of the experiment.

## P3 — fixed raw accumulator

The prediction claimed that the raw fixed-threshold accumulator could not meaningfully be calibrated.

That was wrong at a finite known horizon.

It can be calibrated.

What the later horizon test showed instead is more interesting:

> The fixed calibration collapses when the observation horizon becomes much longer.

So the original objection had a useful intuition but the wrong mechanism.

---

## P4 — CUSUM slack

The prediction incorrectly treated CUSUM's \(\nu\) as a floor on detectable drift **rate**.

The configured Green Sky ramp eventually reaches a large 6-sigma displacement, so even slow change becomes a substantial level shift.

CUSUM detects it.

This prediction was conceptually wrong and remains marked FAIL.

---

## P5 — `raw_sqrt` as sensitivity winner

The pilot expected the normalized cumulative statistic to have the lowest finite-horizon MDR.

A low-slack CUSUM performed slightly better.

That difference was small, and sensitivity alone did not become the decisive criterion.

The more interesting separation emerged in the horizon-robustness test.

---

# 13. Post-pilot replication targets

After the pilot exposed weaknesses in the original predictions, new claims were registered as R1-R6.

These are explicitly labeled **post-pilot replication targets** so nobody mistakes them for predictions made before the first results were seen.

They test such things as:

- collapse of raw fixed-threshold calibration at longer horizons;
- successful CUSUM detection of the configured 6-sigma ramp;
- approximate finite-horizon sensitivity similarity between `raw_sqrt` and low-slack CUSUM;
- finite-horizon stability of the e-process control;
- cross-channel discrimination behavior;
- distinction between blue-only and blue+green-known reference semantics.

This historical distinction matters:

```text
P-series:
    pre-pilot predictions

R-series:
    post-pilot replication targets
```

Do not merge them into one score.

---

# 14. Main findings of v2.0

The experiment should not be reduced to "detector X won."

The useful findings are structural.

## Finding A — fast shocks are easy

Almost every ordinary detector handles the configured abrupt 6-sigma step.

The interesting failure surface is therefore not ordinary shock detection.

---

## Finding B — leakage creates finite effective memory

The simplified recurrence has an exact equilibrium, and the normalized EWMA has finite effective memory determined by \(\lambda\).

Increasing wall-clock observation time does not transform a finite-memory statistic into infinite memory.

That mathematical fact is independent of whether the actual Nexus THDE severity function satisfies the simplified assumptions.

---

## Finding C — fixed-horizon calibration can fail badly in deep time

Several detectors that look properly calibrated over the 1050-year horizon accumulate large false-alarm probabilities when run much longer without recalibration.

This matters because a long-lived Nexus individual should not require engineers to know its death date in advance merely to choose a safe alarm threshold.

---

## Finding D — finite tested robustness and anytime validity are different concepts

`raw_sqrt` behaved very well through x16.

That is useful evidence.

It is still not the same thing as a formal time-uniform guarantee.

The e-process exists specifically to preserve this distinction.

---

## Finding E — a single channel cannot solve the world/instrument ambiguity

If two causal worlds generate the same observation stream, no single-channel algorithm can distinguish those worlds.

This is an information problem, not an optimization problem.

Nexus therefore requires additional independent evidence if it wants causal attribution rather than mere anomaly detection.

---

## Finding F — forgetting and recognition can produce the same "alarm cleared" output for different reasons

A leaky detector may clear because historical evidence decays.

A reference bank may clear because the current state matches a retained epoch.

Those are architecturally different mechanisms.

For deep-time cognition, the second is potentially useful because it preserves history rather than erasing it.

---

## Finding G — detecting change does not authorize a new truth reference

The experiment intentionally leaves reference promotion unresolved.

A detector can say:

```text
"current observations no longer match blue"
```

without being allowed to say:

```text
"green is now the authoritative reference forever."
```

That governance problem belongs in the broader Nexus architecture.

---

# 15. Architectural interpretation

The experiment motivates requirements, not production component choices.

A reasonable interpretation chain is:

```text
MEASURED RESULT
      ↓
GENERAL REQUIREMENT
      ↓
ARCHITECTURAL DESIGN QUESTION
```

not:

```text
detector with best table value
      ↓
make detector canonical
```

For example:

```text
MEASURED:
fixed-horizon thresholds can degrade badly as lifetime grows

REQUIREMENT:
deep-time monitoring should explicitly account for unknown observation horizon

DESIGN QUESTION:
where should Nexus maintain time-uniform or horizon-aware evidence?
```

Similarly:

```text
MEASURED:
one channel cannot distinguish world drift from instrument drift

REQUIREMENT:
causal attribution requires independent evidence

DESIGN QUESTION:
what independent sensory, calibration, lineage, or metrological architecture
does Nexus actually possess?
```

---

# 16. Nexus responsibility boundaries

This experiment must not be used to recreate a giant CA god-object.

Current working responsibility boundaries should remain explicit during interpretation.

```text
CA
    high-level cognitive-regime, retention, escalation,
    and resource-allocation policy

Cyrae
    epistemic observation, evidence status,
    and uncertainty/homeostatic assessment

THDE
    bounded path-dependent state evolution and hysteresis

HTCE
    active cognitive-field generation, exploration,
    coalitions, resonance, and collapse

TMS
    live realization, trajectory, working memory,
    and historical substrate

HVD
    cognitive database semantics and retrieval

HDF5
    durable long-term/permanent persistence

QMT
    continuity across transformation

HIGC
    constitutional admissibility
```

The experiment does not independently establish where a new deep-time sequential statistic belongs.

That remains an architectural decision.

---

# 17. Questions the experiment deliberately leaves open

The following remain unresolved and should be treated as future work.

## 17.1 What is real THDE `severity_k`?

The experiment uses simplified scalar observables.

Transfer to actual THDE depends on:

- how severity is computed;
- whether it is signed or unsigned;
- whether it is instantaneous or trajectory-derived;
- whether it is scalar, vector, tensor, or manifold-valued;
- how rate-independent hysteresis interacts with it;
- whether references migrate;
- whether multiple timescales are already present.

This requires source and implementation inspection.

---

## 17.2 What counts as an independent observation channel?

A second sensor is only useful if it provides sufficiently independent evidence.

Two sensors sharing:

```text
the same calibration source
the same preprocessing
the same physical failure mode
the same ontology mistake
```

may not provide meaningful independence.

---

## 17.3 Who authorizes reference migration?

The experiment can recognize a pre-known green epoch.

It cannot determine:

```text
when green first becomes an accepted epoch
who authorizes that
what evidence is required
how blue remains historically preserved
whether the new reference is local, contextual, or global
```

---

## 17.4 Should slow-drift detection resist change or trigger review?

If the world is genuinely becoming green, mechanical resistance to the observation may be epistemically wrong.

A likely architecture question is whether cumulative drift should:

```text
block change
```

or instead:

```text
escalate observation
increase retention
open competing hypotheses
request independent calibration
trigger review
```

The experiment does not decide that policy.

---

## 17.5 How is retrospective evidence recovered?

Cumulative drift may only become recognizable decades after its constituent events occurred.

By then ordinary detail may already have been consolidated.

This creates a special retention problem:

```text
trigger happens late
but explanatory evidence existed earlier
```

Potential surviving temporal probes include:

- predictions;
- anomalies;
- testimony;
- calibration events;
- ontology transitions;
- interventions;
- constitutional decisions;
- identity/continuity events.

The experiment exposes the need but does not implement the recovery architecture.

---

## 17.6 What happens under non-Gaussian deep-time noise?

The e-process control assumes a specific null.

Real deep-time measurements may include:

```text
autocorrelation
heavy tails
changing variance
sensor replacement
schema migration
missing data
environmental cycles
adversarial interference
```

Future experiments should deliberately violate the iid Gaussian assumption.

---

## 17.7 How does this transfer to high-dimensional Nexus cognition?

Sky color is represented here as a scalar experimental observable.

Real Nexus state may be:

- hyperdimensional;
- manifold-valued;
- structured;
- multimodal;
- relational;
- temporally embedded.

A production mechanism may therefore require geometry-aware sequential evidence rather than scalar thresholds.

---

# 18. How the four companion files fit together

The complete experiment directory should be understood as:

```text
Nexus4_ObjectiveC_Experiment_v2_0_bundle/
│
├── README_Nexus4_ObjectiveC_Experiment_v2_0.md
│      THIS DOCUMENT
│      scope, history, rationale, reading guide
│
├── nexus4_leak_blindness_v2_0.py
│      executable experiment
│
├── RUN_PROTOCOL_nexus4_leak_blindness_v2_0.md
│      replication rules and adversarial-review instructions
│
├── nexus4_leak_blindness_v2_0_reference.json
│      machine-readable official reference result
│
└── nexus4_leak_blindness_v2_0_reference.md
       human-readable official reference result
```

Each file has a different role.

---

# 19. Recommended reading order

For someone discovering this experiment months or years later:

## First

Read:

```text
README_Nexus4_ObjectiveC_Experiment_v2_0.md
```

Understand why the experiment exists.

## Second

Read:

```text
RUN_PROTOCOL_nexus4_leak_blindness_v2_0.md
```

Understand the scientific and provenance rules.

## Third

Inspect:

```text
nexus4_leak_blindness_v2_0.py
```

Understand exactly what was measured.

## Fourth

Read:

```text
nexus4_leak_blindness_v2_0_reference.md
```

Interpret the official reference run using the explanations in this document.

## Fifth

Use:

```text
nexus4_leak_blindness_v2_0_reference.json
```

for automated comparison, regression checks, and cross-model replication.

---

# 20. Replication workflow

A clean independent replication should look like:

```text
researcher/model receives
    |
    +-- README / scope
    +-- RUN_PROTOCOL
    +-- Python experiment
    |
    v
runs experiment independently
    |
    v
produces its own JSON
    |
    v
records environment and hashes
    |
    v
only afterward compares against official reference JSON
```

For blind multi-model replication, the official reference result may be withheld until after each model has produced its own run.

This prevents the reference output from acting as an answer key.

---

# 21. What should be preserved if the experiment evolves

Future versions should preserve scientific provenance.

Do not silently rewrite history.

At minimum preserve:

```text
script version
script hash
run protocol version
original P-series predictions
their historical verdicts
post-pilot R-series targets
reference JSON
reference Markdown output
this experiment overview
```

If a prediction is wrong:

```text
mark it FAIL
explain why
add a new prediction under a new identifier
```

Do not edit the old prediction until it appears to have been correct all along.

Similarly, if a detector implementation is repaired, preserve which experiment version contained the prior behavior.

---

# 22. Short interpretation of the official v2.0 reference run

The official reference result should be read approximately as follows:

1. **The configured fast shock is easy.**
2. **The configured slow ramp is detected by many detector families.**
3. **Therefore simple eventual detection of the 6-sigma Green Sky ramp does not distinguish the interesting architectures.**
4. **Fixed-horizon false-alarm behavior is a major separator.**
5. **Several standard fixed-threshold sequential detectors become increasingly alarm-prone as observation time is extended without recalibration.**
6. **`raw_sqrt` remained empirically stable through the tested x16 horizon but is retained as a finite-horizon legacy comparator, not an anytime-valid proof.**
7. **The Gaussian-mixture e-process provides the experiment's explicit time-uniform control under its assumed Gaussian null.**
8. **Single-channel detection cannot distinguish constructed world drift from instrument drift because the two channel-1 streams are identical.**
9. **Independent-channel disagreement can expose that ambiguity, but disagreement is not itself truth.**
10. **A fixed blue reference regards the entire stable green epoch as anomalous.**
11. **A bank that already contains both blue and green can recognize green as a known epoch.**
12. **That recognition does not solve first-time reference promotion.**
13. **The simplified leaky recurrence has exact finite-memory/fixed-point properties, but those properties must not be generalized to the complete Nexus architecture without showing that the real implementation satisfies the same assumptions.**

---

# 23. Bottom line

The experiment began as a test of a proposed **slow-drift blindness** problem.

It evolved into a more useful decomposition.

The deep-time design problem is not simply:

```text
LEAKY vs CUSUM
```

and it is not simply:

```text
Which detector has the lowest MDR?
```

The actual problem is closer to:

```text
Can Nexus notice persistent gradual change
while remaining statistically calibrated over an unknown lifetime,
distinguish change in the world from change in its instruments,
recognize recurrence without forgetting history,
and escalate novel regimes without letting the detector itself
declare what reality is allowed to become?
```

That is the scope within which the v2.0 results should be read.

The experiment contributes measurable evidence to that question.

It does not close the architecture.

---

# 24. Artifact classification

This entire experiment family should remain classified as:

```text
RESEARCH
EXPERIMENTAL
NON-CANONICAL
```

unless and until specific findings are independently incorporated into ratified Nexus architecture.

A result can be experimentally verified without making the mechanism that produced it canonical.

That distinction is intentional and must survive future reuse of these files.
