# RUN PROTOCOL — Nexus 4 Leak-Blindness Experiment

**Artifact status:** RESEARCH — experiment protocol and reference results.
**Not canon. Not a specification.**
Companion file: `nexus4_leak_blindness.py` (v1.1.0).

---

## 0. What this is and why it exists

Round one of the Project Nexus 4 adversarial review asked six models whether the
architecture is blind to slow drift. Five agreed it was. Of those five: one
fabricated an audit of specifications it never saw, two cited the research
prompt as evidence for a claim made in the research prompt, and only two
honestly returned UNRESOLVED. The panel produced consensus without evidence.

This experiment exists to remove that question from the language-model
deliberation layer entirely. It is deterministic, self-contained, runs in under
two minutes, and either supports the claim or falsifies it.

**Your job is not to decide whether slow-drift blindness is real. That is now a
measurement. Your job is to say what follows architecturally.**

---

## 1. How to run it

```bash
python3 nexus4_leak_blindness.py --seeds 40 --calib-seeds 200 --json my_run.json
```

Requirements: Python 3.10+, numpy. Nothing else. No network access needed.
Runtime is roughly 2–6 minutes at these settings, longer for larger `--seeds`.

For a fast smoke test: `--seeds 8 --calib-seeds 25` (about 30 seconds).

Report `python --version` and `numpy.__version__` with your results. Both are
printed in the script header automatically.

### What the script does

- Generates six observation streams: `null`, `creep`, `instrument`, `greensky`,
  `shock`, `confound`. One tick = one month. Default run = 1050 years
  (500 blue → 150-year transition → 150-year green plateau → 150-year return →
  100-year tail).
- Runs eleven detectors, including the THDE leaky-accumulator form, raw
  accumulators, one- and two-sided CUSUM, a multi-reference epoch bank, and a
  two-instrument differential.
- **Auto-calibrates every detector on the null condition to the same 5%
  false-alarm probability before comparison.** No detector is strawmanned. If
  you think a detector is disadvantaged, change its parameters and rerun — do
  not argue about it.
- Checks eight predictions registered before the first run and reports
  PASS / FAIL mechanically.

### Integrity rules for the script

- Evaluation seeds are disjoint from calibration seeds by construction.
- `creep` and `instrument` are built to produce **bit-identical** channel-1
  observations. This is asserted in `run_self_tests()`. If that assertion ever
  fails, the run is invalid — report it, do not work around it.
- **Do not edit the `PREDICTIONS` list.** Three of the eight were falsified in
  the reference run. That is the honest record and it stays. If you want to
  register new predictions, append them with a note saying when and why, and
  never modify or delete an existing one.

---

## 2. Reference run — MEASURED FACTS

Environment: Python 3.12.3, numpy 2.4.4, `--seeds 12 --calib-seeds 40`,
1050 years at 12 ticks/year = 12,600 ticks, σ = 1.0, excursion amplitude = 6.0σ.

Reproduce before disputing. These are measurements, not claims.

### M1 — Every detector catches the shock

Fire rate 1.00 on the `shock` condition for all ten single-channel detectors.
**Fast shocks were never the problem.** The existing quad-tier defense is aimed
at a case that is already covered by anything.

### M2 — Leaky accumulators are 7–13× less sensitive than non-leaking ones

Minimum detectable drift rate, in σ per year (lower is better):

| detector | MDR | years to accumulate 1σ |
|---|---|---|
| One-sided CUSUM, ν=0.02 | 0.0000385 | 25,960 |
| Raw accumulator, √k threshold | 0.0000408 | 24,498 |
| One-sided CUSUM, ν=0.1 | 0.0000790 | 12,656 |
| Two-sided CUSUM, ν=0.1 | 0.0000902 | 11,088 |
| One-sided CUSUM, ν=0.5 | 0.000176 | 5,674 |
| Raw accumulator, fixed threshold | 0.000206 | 4,865 |
| **Leaky (THDE), λ=0.999** | **0.000276** | 3,619 |
| **Leaky (THDE), λ=0.99** | **0.000310** | 3,223 |
| **Leaky (THDE), λ=0.9** | **0.000541** | 1,849 |
| Multi-reference epoch bank | 0.00184 | 544 |

The leak-blindness claim holds directionally. Raising λ from 0.9 to 0.999
improves sensitivity by less than 2× — a 100× increase in memory buys almost
nothing, because the leak sets the effective averaging window and sensitivity
scales only as its square root.

### M3 — Sensitivity does NOT separate the two best detectors. Horizon does.

CUSUM(ν=0.02) and raw-√k differ by 6% in MDR — inside the noise. But calibrate
each at the default horizon and then measure the null false-alarm rate at 4×
and 16× that horizon:

| detector | 1× | 4× | 16× |
|---|---|---|---|
| **Raw accumulator, √k threshold** | **0.00** | **0.00** | **0.00** |
| **Multi-reference epoch bank** | **0.00** | **0.00** | **0.00** |
| One-sided CUSUM, ν=0.02 | 0.00 | 0.17 | 0.83 |
| One-sided CUSUM, ν=0.1 | 0.17 | 0.17 | 0.67 |
| Two-sided CUSUM, ν=0.1 | 0.17 | 0.33 | 0.50 |
| One-sided CUSUM, ν=0.5 | 0.67 | 0.83 | 1.00 |
| Leaky (THDE), λ=0.9 | 0.00 | 0.00 | 0.50 |
| Leaky (THDE), λ=0.99 | 0.17 | 0.83 | 0.83 |
| Leaky (THDE), λ=0.999 | 0.00 | 0.00 | 0.83 |
| Raw accumulator, fixed threshold | 0.00 | **1.00** | **1.00** |
| Cross-channel differential | 0.00 | 0.00 | 0.83 |

**This is the finding nobody in round one anticipated, including the author of
the prompt.** Almost every standard detector is calibrated against an assumed
observation horizon. A 10,000-year individual does not know its horizon. Only
self-normalizing statistics — `S_k/√k`, and the epoch bank, which compares to
fixed anchors instead of accumulating — hold their calibration as the horizon
grows.

Reframed: the design question is not *leaky versus CUSUM*. It is **which
statistics remain calibrated under an unbounded and unknown observation
horizon.** That is a much smaller family.

### M4 — World drift and instrument drift are indistinguishable on one channel

`creep` (world moves, sensor stable) and `instrument` (sensor moves, world
stable) produce identical channel-1 streams by construction. Every
single-channel detector produces byte-identical results on both. This is not an
empirical finding; it is a proof by construction.

The two-instrument differential separates them cleanly:

| condition | cross-channel fire rate |
|---|---|
| `creep` (world moves, both sensors agree) | 0.00 |
| `instrument` (sensor 1 moves alone) | 1.00 |
| `confound` (world and sensor move opposite) | 1.00 |

**Integral tracking cannot solve the instrument problem at any sensitivity.
A second independent channel is not an optimization; it is the minimum
mechanism.** Any proposal that adds drift detection without adding an
independent reference has solved half the problem and should say so.

### M5 — Under a fixed reference, every detector latches for the whole green epoch

All ten single-channel detectors alarm for 100% of the 150-year green plateau
— a period during which the sky is genuinely, stably green and nothing is
wrong. Behaviour after the sky returns to blue:

- **Clears:** leaky λ=0.9, leaky λ=0.99, multi-reference epoch bank.
- **Still alarming:** everything else.

The leaky detectors clear by *forgetting*, which is the same property that costs
them sensitivity in M2. The epoch bank clears by *recognizing a return to a
retained reference*. Those are architecturally different reasons for the same
observable, and only the second is a capability.

### M6 — Three pre-registered predictions were falsified

| id | verdict | what actually happened |
|---|---|---|
| P3 | **FAIL** | `raw_fixed` *is* calibratable — at a known horizon. Its calibration then collapses to FA = 1.00 at 4× horizon (M3). The objection to it was right; the stated reason was wrong. |
| P4 | **FAIL** | CUSUM's slack ν is a floor on detectable **displacement**, not on detectable **rate**. Green Sky reaches 6σ of displacement, so ν=0.5 detects it easily. The prediction confused level with rate. |
| P5 | **FAIL** | `raw_sqrt` did not have the lowest MDR; CUSUM(ν=0.02) beat it by 6%, which is noise. Sensitivity does not separate them — horizon robustness does. |

P1, P2, P6, P7, P8 held.

---

## 3. SOURCE-VERIFIED FACTS

Established by direct inspection of Drive artifacts, with the source named.
Cite the section or mark UNRESOLVED.

- **SV1.** The original Green Sky sequence is ~500 years blue, ~150 years green,
  then blue again, with two named failure modes: averaging to a fictitious cyan,
  and overwrite-driven catastrophic forgetting.
  *Source: `Building_AI_that_outlasts_silicon_timestamps.txt`, ≈14:45–16:30.*
- **SV2.** THDE's discrete form in canon is a **leaky** accumulator:
  `q_{k+1} = λ q_k + severity_k` with `θ_on > θ_off`. Note the source hierarchy:
  HVD 1.5 §16.2 states this as a **TMS trajectory-preservation requirement**
  (preserve enough history that a future controller could compute something of
  this form), not as proof of an implemented detector. The N-dimensional
  architecture specification is the stronger evidence for the leaking form.
- **SV3.** Not every Nexus stability operator is rate-tuned. The N-dimensional
  specification lists Preisach / Prandtl-Ishlinskii / Bouc-Wen hysteresis
  operators with **rate-independent memory**. The round-one claim that "every
  stability barrier evaluates temporal derivatives" is **false**.
- **SV4.** QMT already contains the historical-verdict mechanism that round one
  proposed as new. §105 issues a continuity certificate bound to the exact
  contract digest, evidence root, and verifier version; §106 states
  `Digest(G_b′) ≠ Digest(G_b) ⇒ Cert(G_b) does not certify G_b′`. Typed
  deficiency certification is an extension of §106 from state change to contract
  change, not a new subsystem.
- **SV5.** The generated audio-overview transcripts in Drive are **DERIVED,
  non-canonical**. They were produced after the round-one answers, from those
  answers. Whisper config: model `small`, `beam_size 1`, `int8`, and a hotword
  list containing **no** subsystem names (no THDE, HTCE, TMS, HVD, QMT, HIGC,
  Cyrae, Maera, Sire). Every mangled term in those transcripts is a term absent
  from that list. They may not support CANONICAL or IMPLEMENTED status.

---

## 4. Rules for your response

1. **Reproduce before disputing.** If you disagree with a measured fact in §2,
   rerun the script and report your numbers, environment, and seed count. An
   argument that a measurement is wrong, unaccompanied by a run, will be
   discarded.
2. **You may not reinterpret §2 or §3 except by identifying a reproducibility
   flaw or a source-integrity flaw.** Name the flaw specifically.
3. **You may not cite this protocol as evidence for a claim made in this
   protocol.** Round one failed exactly this way.
4. **Claims about Nexus architecture must cite the inspected source section, or
   be marked UNRESOLVED.** Not "the specification indicates" — the section.
5. **A derived artifact may not establish status.** Only `/canon` establishes
   CANONICAL. Only inspected source establishes IMPLEMENTED. Only reproducible
   execution establishes VERIFIED. Research, review, and derived artifacts may
   propose, interpret, attack, and synthesize — they establish nothing.
6. **Tag every substantive claim:** CANONICAL, IMPLEMENTED, VERIFIED,
   PARTIALLY IMPLEMENTED, PROPOSED, DESIGN TARGET, EXPERIMENTAL,
   RESEARCH HYPOTHESIS, INFERRED, TESTIMONY, DERIVED, HISTORICAL/SUPERSEDED.
   Untagged claims are treated as INFERRED.
7. **Pair every objection with a concrete alternative.** An objection with no
   replacement is noise.
8. **Attack before you agree.** A response that endorses everything has failed.

---

## 5. OPEN QUESTIONS — what the measurements do not settle

These are the actual work. The numbers above are only the ground you stand on.

**Q1 — Does the measured result transfer to the real THDE?**
The experiment assumes `severity_k = |x_k − μ|` and a scalar observable. Nexus's
THDE consumes trajectory severity over a high-dimensional state with
rate-independent hysteresis operators alongside (SV3). Under what conditions
does the M2/M3 result transfer, and under what conditions does it not?

**Q2 — Does Nexus have a second independent observation channel?**
M4 shows a second channel is the minimum mechanism for world/instrument
attribution. If Nexus has only one, the instrument problem is unsolved
regardless of which detector is installed. If it has several, are they
independent, or do they share a failure mode? What is the actual sensory
architecture, cited?

**Q3 — Who authorizes reference migration, and what preserves the old epoch?**
M5 shows fixed references latch for 150 years and the epoch bank clears. It says
nothing about governance. Proposed rule to attack: *detection does not itself
move the reference; detection initiates a process that may authorize migration
while preserving the previous epoch.* Which subsystem owns each step? Note that
this makes reference migration structurally identical to Σ amendment — argue
whether they should share a mechanism or must not.

**Q4 — Review, not resistance.**
Green Sky may be reality. Gemini's proposed Maxwell-Weichert creep dual supplies
*mechanical resistance* to slow deformation — it fights the green sky. Is
resistance ever correct, or must a cumulative detector only ever open a review?
If only review, what is the interim posture while review is pending, given that
drift continues during it?

**Q5 — The retrospective-trigger problem.**
Five retention triggers fire when their event occurs. Cumulative drift fires
long after, when the detail it needs was consolidated away decades earlier. It
therefore needs a different control path: mark the interval suspect, freeze
aggressive consolidation, raise forward granularity, and retrieve the sparse
high-value records that survived — predictions, anomalies, testimony,
calibration events, ontology changes, constitutional decisions. Specify that
path, and specify what a prediction record must contain to serve as a temporal
probe into an otherwise consolidated interval.

**Q6 — Causal hypothesis collapse as a retention trigger.**
Residual magnitude is the wrong trigger; explanatory probability mass over
hypothesis *families* is representation-invariant where hypothesis *count* is
not. Define the measurable quantity, its threshold, its cost per tick, and its
expected trigger rate. Show it fires on the second instance of an anomaly that
kills a single-cause explanation, and not on the first.

**Q7 — What would falsify the whole layer?**
If the horizon-robust statistic from M3 plus a second channel from M4 fully
covers slow drift, is a CA-level cognitive-regime policy needed for this at all,
or is drift detection purely a Cyrae/THDE concern with CA owning nothing but the
resource allocation? State the experiment that decides it.

---

## 6. What to return

```text
1. Environment + your run's numbers for M1–M6. Note any divergence.
2. Reproducibility or source-integrity flaws found, specifically named.
3. Answers to Q1–Q7, each tagged per rule 6.
4. Attacks: your strongest objection per open question, with the
   discriminating test that would settle it.
5. Repairs: a concrete alternative for every objection.
6. Ownership map: mechanism -> subsystem -> boundary check against the
   responsibility split. Any proposal that pulls generation, storage,
   admissibility, or continuity into CA is re-creating the god-object.
7. New predictions you wish to register, with the date and reason.
8. UNRESOLVED items, stated as such rather than answered optimistically.
```

Do not produce a specification. Produce an adversarial review grounded in
measurements you reproduced.
