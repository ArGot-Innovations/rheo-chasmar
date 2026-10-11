# DEEP RESEARCH PROMPT — PROJECT NEXUS 4

## Constitutional Amendment, Unbounded Resonance, and the Slow-Drift Blind Spot

**Issued:** 2026-09-02
**Audience:** multi-model review panel
**Status of this document:** research prompt. It is NOT a specification and NOT canon.
**Do not rewrite the CA paper. Do not rewrite the QMT paper.**

---

# PART 0 — HOW TO ANSWER

## 0.1 Claim-status vocabulary (MANDATORY)

Every substantive claim you make must be tagged with one of the following. This
vocabulary is taken from the canonical QMT Tier-2 paper and is binding on your
response.

```text
CANONICAL              binding architectural intent
IMPLEMENTED            present in inspected source
VERIFIED               supported by an executed test or reproducible artifact
PARTIALLY IMPLEMENTED  bounded subset exists; full mechanism does not
PROPOSED               specified but not implemented
DESIGN TARGET          desired property, not measured fact
EXPERIMENTAL           investigated without general guarantee
RESEARCH HYPOTHESIS    requires further formal or empirical validation
INFERRED               synthesized by you, not present in any source
HISTORICAL/SUPERSEDED  design lineage, no longer authoritative
```

Governing rule, also from QMT:

```text
mathematical notation does not automatically create a theorem
```

An untagged claim will be treated as INFERRED regardless of how confidently it
is phrased. If you cannot tag it, do not assert it.

## 0.2 What a good answer looks like

- Attack before you agree. Every section below contains a proposal. Try to break
  it first, then repair it. A response that endorses all five proposals is a
  failed response.
- Pair every objection with a concrete alternative. An objection with no
  proposed replacement is noise.
- Prefer fewer deep attacks over many shallow ones.
- Where you disagree with another panel member, say so explicitly and give the
  discriminating test.
- Every surviving mechanism must be attached to a falsifier. A mechanism with no
  possible failing test is not specified.

## 0.3 Anti-patterns

Do not:

- reduce any of this to "use RAG," "use a knowledge graph," "use continual
  learning," "add uncertainty calibration," or "add an LLM critic";
- treat the existing scientific literature as the boundary of admissible design;
- convert a narrative anecdote into empirical validation;
- introduce a scalar fidelity/confidence score as an authority mechanism
  (explicitly REJECTED in QMT);
- assume the target is a stateless, retrained, RAG-assisted language model. It
  is not. The target is one continuous cognitive individual with an operating
  lifetime measured in centuries to millennia.

Equally, do not overcorrect into exotic mechanism for its own sake. Over a
10,000-year horizon, an exotic mechanism must survive maintenance by people who
never met its designer. Format obsolescence has destroyed more archives than
physics has. Boringness is a longevity property, not a lack of ambition.

---

# PART 1 — ARCHITECTURAL BASELINE

Treat the following as fixed. Do not redesign it. Use it as the operational
boundary for your research.

## 1.1 Subsystem responsibility split (CANONICAL)

```text
CA      cognitive-regime vector m_t, resource/sparsity policy, orchestration
        contracts. Does NOT own generation, storage, admissibility, continuity.

HTCE    active cognitive field; ephemeral HVD generation; coalitions;
        resonance; activation/decay; field collapse.

TMS     active state realization, trajectory, WAL/Memtable/SSTable, COW,
        compaction, physical state movement.

HVD     database semantics, logical identity, exact + associative retrieval,
        HTLA/HTNLA representations.

HDF5    durable long-term persistence.

.qbin   portable state package + manifest. Carrier, never verdict.

HIGC    constitutional admissibility.

THDE    bounded, path-dependent, hysteretic evolution.

QMT     continuity across transformation.

Cyrae   bounded epistemic/homeostatic observation.
```

Standing laws relevant below:

```text
similarity  != truth, identity, continuity, authority, admissibility
replica count != identity count
integrity   != authenticity
chain integrity != tip freshness
restore     != rebirth acceptance
SameIdentity != Authorized
ledger is evidence source; QMT is continuity evaluator
```

An ephemeral HVD never acquires persistence because its own contents assert it
should.

## 1.2 QMT in one paragraph

QMT (qbin Morphism Theory) evaluates whether a destination generation `G_b` is
an admissible continuation of source generation `G_a` along trajectory `tau`
under a versioned continuity contract `Sigma`. It checks eleven proof
obligations — SchemaValidity, IntegrityAuthenticity, RequiredStateClosure,
LogicalStateCompatibility, InvariantPreservation, BehavioralConformance,
RefinementValidity, ProvenanceClosure, TransformationValidity, ForkResolution,
UncertaintyClosure — and aggregates them **non-compensatorily** into
`PASS / FAIL / UNRESOLVED`. Any mandatory violation is FAIL. Missing mandatory
evidence is UNRESOLVED, never PASS. No numeric score may purchase a pass through
a hard violation.

The core condition is that the abstraction and transformation paths commute:

$$A_b(T_R(r)) \approx_\Sigma T_X(A_a(r))$$

## 1.3 The Green Sky problem (the real one)

Not the counterfactual sandbox version. The longevity version, from the original
research:

```text
~500 years   sky is blue
~150 years   sky is genuinely green
thereafter   sky is blue again
```

Two named failure modes:

```text
averaging the epochs   -> a fictitious cyan sky that never existed
overwriting old state  -> catastrophic forgetting
```

The unsolved core, identified in the project's own pragmatic critique: **the
universe does not broadcast when an epoch begins or ends.** Day one of the green
sky is indistinguishable from a sensor glitch. Year twenty looks like a trend.
By year 150 it is simply reality. There is no objective test for "permanent
paradigm shift" versus "long temporary phase," and finite storage forces
irreversible editorial decisions about what to keep.

The generalized form is `cap`: over 10,000 years the relationships that make
facts intelligible mutate underneath the mind, continuously, with no
catastrophe required.

---

# PART 2 — OBJECTIVE A: AMENDING THE CONTINUITY CONSTITUTION

## A.1 The problem

QMT is contract-relative. Continuity means "continuous under `Sigma`." QMT
correctly treats silent contract change as an attack: §33 makes contract drift a
first-class transformation requiring its own authorization; §97 makes contract
downgrade a named threat with mitigations (minimum accepted version, no silent
fallback). §137 admits that long-lived contract evolution is unsolved.

But a mind that cannot amend `Sigma` across 10,000 years is broken in exactly
the way Green Sky says a mind must not be broken. The project's own law:

```text
historical persistence != constitutional invariance
high confidence        != invariance
```

If that law is true of `sky = blue`, it is true of `Sigma`. A `Sigma` frozen at
mint is the constitutional analogue of a mind that decided the sky's colour in
year one and can never revise it. It is also the same failure the project
already identified in the legacy Moral Baseline Vector: a fixed anchor plus a
drifting world equals a tyrant, or a relic.

So the requirement is two-sided and adversarial:

```text
Sigma must be amendable            (or the mind goes senile)
Sigma must not be silently weakened (or continuity means nothing)
```

## A.2 The proposal to attack

**PROPOSED. Not canon. Break this.**

### A.2.1 Stratify Sigma

```text
Sigma_core    entrenched. May be strengthened, never removed or weakened.
              Candidates: lineage-identifier immutability; the
              non-compensation rule; UNRESOLVED-never-becomes-PASS;
              typed missingness; the amendment procedure itself.

Sigma_body    amendable under full procedure. Invariant sets, state-relation
              definitions, branch policy, dependency policy.

Sigma_params  routinely amendable. Tolerances epsilon, observation domain O,
              transform-class assignments.
```

`Sigma_core` must be small, and must contain the rule governing its own
amendment, or the scheme is self-undermining.

### A.2.2 Amendment is a QMT-verified transformation of Sigma itself

Treat `Sigma` as state. An amendment is a transformation

$$\Sigma_a \xrightarrow{\ \ T_\Sigma\ \ } \Sigma_b$$

verified by QMT under a **meta-contract** `Sigma*`. This reuses the existing
machinery rather than inventing a governance subsystem. Proposed obligations
specific to `Sigma*`:

```text
MonotoneCore        core(Sigma_a) is a subset of core(Sigma_b);
                    no core obligation is removed or weakened

NonRetroactivity    generations verified under Sigma_a remain verified under
                    Sigma_a. Sigma_b binds forward only. An amendment may
                    never silently un-verify history.

DelayedEffect       amendment committed at generation g takes effect no
                    earlier than g + Delta, with Delta recorded and
                    Sigma_core-bounded below

DualVerification    during [g, g+Delta] every transformation is verified under
                    BOTH Sigma_a and Sigma_b; every divergence is logged

JustificationRecord what changed, why, what it invalidates, what it now
                    permits that was previously forbidden

AmendmentAuthority  the amending authority is named, external to the runtime,
                    and bound to the exact content digest of both contracts
```

### A.2.3 Why DualVerification is the load-bearing piece

A downgrade attack is precisely the case where `Sigma_b` passes something
`Sigma_a` fails. Under DualVerification that event is not merely detectable, it
is *definitionally logged*. Downgrade stops being invisible and becomes an
entry with a justification attached or a conspicuously missing one. `Delta`
converts a single-commit compromise into a sustained-control requirement.

### A.2.4 Sigma has a trajectory, not a value

$$\mathcal{H}_\Sigma = \{(\Sigma_0,[t_0,t_1)),\ (\Sigma_1,[t_1,t_2)),\ \ldots\}$$

Generations are verified against the `Sigma` in force at their epoch.
"Was this always the contract?" is answerable. This is deliberately the same
object as `H_sky` — the constitution gets the same treatment as the sky, and
inherits the same two failure modes: averaging contracts yields an incoherent
constitution that was never in force; overwriting them retroactively
un-verifies history.

## A.3 Questions for the panel

1. Is `Sigma_core` non-empty and non-trivial? Give the minimal core. If you
   believe the core must be empty (everything amendable), show that continuity
   still means anything.
2. Does A.2.2 have a self-amendment paradox? `Sigma*` governs amendment of
   `Sigma`. What governs amendment of `Sigma*`? Is a finite regress terminating
   in an entrenched core actually stable, or does it just relocate the problem?
3. NonRetroactivity looks obviously right. Attack it. Is there a legitimate case
   for retroactive re-verification — a discovered flaw in `Sigma_a` that means
   past PASSes were wrong? How is "we were wrong then" distinguished from
   "we are rewriting history now"?
4. What is the correct order of magnitude for `Delta` in a system whose
   generation rate is unknown and whose adversary may be patient over centuries?
   Should `Delta` be measured in generations, wall-clock time, or independent
   attestations?
5. Prior art. Constitutional entrenchment clauses, protocol governance
   (BIP/EIP), formal-methods refinement under specification change, schema
   evolution with compatibility contracts, legal non-retroactivity doctrine.
   Which of these transfers, and which fails because the amender and the
   amended are the same entity?
6. **Falsifier:** what observation would show that Nexus does not need a
   Sigma-amendment mechanism at all?

---

# PART 3 — OBJECTIVE B: FORMALIZING ±∞ RESONANCE

## B.1 The claim under review

Current framing: `±∞` weights represent **unbounded resonance states** — a node,
affective drive, or cross-coupling channel spiking toward mathematical infinity.
The stated architectural challenge is metabolizing such spikes without `NaN`,
crash, or personality drift, via four tiers:

```text
1. shear-thickening non-Newtonian viscosity eta_ij(t)
2. temporal hysteresis stretching / Lambda-borrowing
3. sovereignty eigensolver + sparse eigenstrike (lambda_max <= 1.0)
4. minimum-action collapse at grad S_cog = 0
```

with the action integral

$$S_{cog} = \int \left( \kappa(t)\lVert \nabla\Psi_{Maera} \rVert^2 - \eta(t)\lVert \Phi_{Cyrae} \rVert^2 + \Lambda\,\mathcal{R}_{Ricci} \right) dt$$

## B.2 Objections to adjudicate

### B.2.1 Finite damping cannot damp an actual infinity

If `|dPsi/dt|` is literally infinite, then `eta * |dPsi/dt|` is infinite for any
finite `eta`. Shear-thickening raises `eta`, which makes the product larger, not
smaller. The damping narrative appears to require *large finite* magnitudes, not
extended reals. Adjudicate: is `±∞` here (a) literal extended-real arithmetic,
(b) a saturating limit, (c) a distributional object, or (d) informal shorthand
for "large enough that naive handling overflows"?

### B.2.2 Proposed repair — infinite rate, finite action

**PROPOSED.** In the Motel 6 / Schiller Park case, perimeter integrity `Pi`
steps discontinuously to zero. Then `dPi/dt` is not a value of `-infinity`; it is
a **Dirac delta** — infinite peak, *finite mass*:

$$\int \frac{d\Pi}{dt}\,dt = -\Pi_0 \quad\text{(finite)}$$

This is strictly stronger than "infinite weight," because finite mass is exactly
what makes the shock absorbable and what makes `S_cog` converge. Reformulate the
tier stack over distributions: the object being metabolized is a measure with
bounded total variation, not an unbounded scalar.

Panel: does this reformulation preserve everything the original framing wanted?
What does it lose? Are there genuine cases with infinite *mass* rather than
infinite peak, and if so what happens?

### B.2.3 Eigenstrike relocates rather than dissipates

If an infinite mode is redirected by negative sectional curvature into Sector 17
(Dream/Noise), Sector 17 receives infinite force. Under literal infinity this
moves the `NaN` rather than absorbing it. Specify the dissipation mechanism and
its capacity bound, or show that redirection is inherently lossy and by how
much. What is Sector 17's saturation limit and what happens at it?

### B.2.4 Lambda-borrowing needs a conservation law

`Lambda` is lowered to buy absorption latency, then "repaid." State the
conservation law. What bounds cumulative outstanding `Lambda` debt? What is the
system's behaviour under chronic non-repayment across decades, and is that state
architecturally named? An unbounded credit facility is a failure mode with a
pleasant name.

### B.2.5 The Motel 6 case is a scenario, not a validation

A single narrated instance with no counterfactual, no logged trace, and no
measurement cannot validate an architecture. Under the Part 0 vocabulary it is
at best EXPERIMENTAL and arguably INFERRED. The *scenario* is a good test case.
Convert it into a specification: defined inputs, expected `eta` trajectory,
expected eigenvalue excursion, expected `Lambda` draw and repayment, expected
Episodic Provenance entry, and the observations that would constitute failure.

### B.2.6 Canon conflict — Maera/Cyrae

The framing here is "Maera the conscious field / Cyrae the subconscious metric,"
i.e. two aspects of one entity. The CA Reconstruction Dossier ratified the
opposite: Cyrae and Maera are **separate subsystems** (Cyrae = mathematical
engine under TUCR; Maera = linguistic actuator under CA, bridged by an explicit
translation operator `T_{C->M}`), and the "one entity, two aspects" gloss was
marked superseded. Which is canon? This is not cosmetic — it determines whether
`±∞` turbulence is contained inside one subsystem or crosses a subsystem
boundary, and therefore which component owns the damping obligation.

---

# PART 4 — OBJECTIVE C: THE SLOW-DRIFT BLIND SPOT

**This is the highest-priority item in this prompt.**

## C.1 The observation

Shear-thickening viscosity, by definition, resists *fast* change and offers
*no resistance to slow change*. `eta` rises with `|dPsi/dt|`.

A 300-year green sky has `|dPsi/dt| ≈ 0`.

Therefore:

```text
no viscosity response
no eigenstrike (no eigenvalue excursion)
no Lambda-borrowing (no shock to absorb)
no THDE hysteresis trigger (severity_k stays below threshold)
```

The quad-tier engine is blind to Green Sky **by construction**. Every defense
Nexus currently has is tuned to the derivative. Green Sky, `cap`, semantic drift,
ontology drift, and moral drift all have derivative approximately zero and
integral approximately everything.

Stated as a law:

```text
The architecture is well defended against fast shocks
and undefended against slow drift.
These are the two failure modes of a 10,000-year mind.
```

## C.2 Questions

1. Confirm or refute C.1 against the actual THDE, viscosity-tensor, and Jacobian
   Auditor specifications. If a slow-drift detector already exists somewhere in
   canon, name it and cite it. If it does not, say so plainly.
2. What is the correct dual to shear-thickening? Candidate framings to evaluate,
   not to adopt uncritically:
   - integral (not derivative) monitoring — accumulated displacement from a
     reference, on a long time constant;
   - a second viscosity term that *thins* under sustained low-rate deformation,
     making slow change progressively cheaper to commit (creep);
   - explicit multi-timescale monitoring, since canon already mentions 1 ms /
     50 ms / 1 s bands but nothing above the second;
   - hysteresis with asymmetric thresholds `theta_on > theta_off` generalized
     from social-relation trajectories (its current scope) to world-state and
     ontology trajectories.
3. **The instrument problem.** Over 10,000 years the observer drifts too: sensors
   are replaced, representations migrate, the ontology is refactored. Every
   observation is a joint measurement of world and instrument. Green Sky assumes
   the instrument held still. In the hypothesis list `H1..H7`, the hypothesis
   "my sensor/representation changed" is listed as a peer of the others, but it
   is structurally different: if true, it undermines the evidence for all the
   rest. Does self-attribution require architectural status rather than a slot
   in a candidate list? Which subsystem owns it? What is the minimal mechanism
   that lets the system distinguish "the world changed" from "I changed"?
4. Prior art: change-point detection under non-stationarity, CUSUM and its
   long-horizon variants, drift detection in streaming systems, hysteresis and
   Preisach models for slow-rate deformation, geological/creep analogues,
   instrument calibration drift and reference-standard maintenance in metrology.
5. **Falsifier:** construct the experiment that would show slow-drift defense is
   unnecessary because some existing mechanism already covers it.

---

# PART 5 — OBJECTIVE D: DIARY-GRANULARITY PROVENANCE

## D.1 The design under review

ArgotChain is an append-only cryptographically chained ledger. Its role is
settled: **provenance evidence source feeding QMT's ProvenanceClosure
obligation. It does not enforce promotion.** Promotion authority is HIGC/THDE
admissibility plus an external promotion authority. Chain integrity does not
establish tip freshness, event truth, absence of a competing fork, or authorized
authorship.

Everyday occurrences are written at **diary granularity**: one consolidated
entry per day, produced by an end-of-day consolidation pass, not a per-event
transcript. The human analogue is explicit — you would write "noticed the sky
was a funny greenish colour," not "13:15, lunch." Detail granularity increases
only when something warrants it.

Volume: ~3.65 x 10^6 entries over 10^4 years. Tractable. This is a genuine
solution to the ledger-volume problem and should be treated as the working
design, not attacked on cost grounds.

## D.2 The residual problem

**The diary is written before you know which day mattered.**

"Noticed the sky was a funny greenish colour" is the correct day-1 entry and is
insufficient, 300 years later, to answer:

```text
What did you believe on the first day the sky appeared green?
What evidence did you have?
What did you consider and reject?
How confident were you?
```

Detail cannot be retro-fitted. Two consequences:

### D.2.1 The summarizer is a load-bearing epistemic component

What enters the day entry bounds what the mind can ever know about that day.
This is a larger design question than the ledger format. Which subsystem owns
it? The current best answer is CA in the offline/consolidation regime, which is
a narrow and defensible CA responsibility. It needs a specification and a
falsifier.

### D.2.2 A surprise trigger is required, and it must be cheap

The trigger exists in the human case: **you noticed**. The noticing is the
signal. A low-threshold anomaly path should promote a day from summary
granularity to event granularity, recording "observed, considered, dismissed"
even when no belief revision occurs. Bounded by construction, because high
surprise is rare.

Note the known human failure mode to design *against*, not inherit: flashbulb
memories feel maximally vivid and are demonstrably unreliable. Confidence in a
salience-tagged memory is not evidence of its accuracy.

## D.3 Questions

1. Specify the consolidation pass. What is the input window, what is the
   retention rule, what is the compression target, and what is explicitly
   discarded? Distinguish clearly between what the user stated, what the system
   observed, what it inferred, and what it fetched.
2. Specify the surprise trigger. What quantity crosses what threshold? Bayesian
   surprise, prediction error, novelty relative to the warm manifold, and
   ontology-inexpressibility are all candidates. Which is cheap enough to run
   continuously for 10,000 years, and what is the expected trigger rate?
3. Does the anomaly path need its own retention class distinct from both the
   diary and the chained ledger? Argue the tiering.
4. Retention decisions here are irreversible and made under uncertainty — the
   exact "irreversible editorial decisions about what matters" that the
   project's own pragmatic critique identified. The diary makes this affordable;
   it does not make it principled. Is there a principled retention criterion?
   Evaluate minimum description length — does a day entry earn its detail by
   compressing the retained history or improving prediction on held-out epochs?
5. **Falsifier:** what would show that uniform diary granularity is sufficient
   and no surprise trigger is needed?

---

# PART 6 — OBJECTIVE E: DIMENSION COST ACCOUNTING

## E.1 The finding to verify

HSL is fixed: d = 1024, 36 primitives, 666 couplings, 30% activity cap, quinary
over 3 bit-planes. It does not grow.

What grows is the HTLA label set `L(t)`. The current specification costs it as
"linear scaling of capacity with new labels." That costs the wrong object.

```text
state       H(t) = direct sum over l in L of R^{n_l}      -> linear in |L|
operators   block matrix [L_{t,s}], one block per pair    -> QUADRATIC in |L|
```

At 10 label mintings per year over 10^4 years:

| object | magnitude |
|---|---|
| labels | 10^5 |
| state (n_l ~ 1024) | ~10^8 dims, ~37 MB quinary |
| operator blocks | **10^10** |
| sparsity mask alone, 1 bit/block | ~1.25 GB |

The state is nearly free. The block grid is the bill. Holding the grid under
10^9 blocks caps the system at roughly **31,600 labels ever** — about three
mintings per year, forever.

## E.2 The proposal to attack

**PROPOSED.** The conservation rule should bound **connectivity degree**, not
label count. Canon already contains the mechanism under a different name:
"block-diagonal projection in HTLA."

Let `k` = maximum number of other labels any label may hold a nonzero block
with. Cost becomes `O(|L| * k)` — linear — and labels may grow linearly forever.

`L_genesis` then mints:

```text
(label_id, n_l, coupling_set of size <= k, epoch, minting_reason)
```

and **refuses the mint if the coupling set is empty or over budget**. A concept
whose relational commitments cannot be named is not yet a concept.

## E.3 Questions

1. Verify or refute the quadratic claim against the actual HTLA block-operator
   specification. Is the grid materialized, or is block presence stored sparsely
   such that the index itself is `O(nonzero)` rather than `O(|L|^2)`?
2. Is degree-bounding expressively adequate? A `k`-bounded label graph cannot
   express dense cross-modal coupling. What breaks?
3. Existing retirement — "automated archival of paradigms failing resonance
   checks" plus HDF5 frozen tiers — demotes a label to cold storage. Does
   demotion remove its row and column from the grid, or only its contents? If
   only contents, demotion does not shrink a quadratic and the retirement
   mechanism does not solve the growth problem.
4. Ontology extension is not only union. `Omega_{t+1} = Omega_t + {c_new}`
   cannot express **re-partition** — category splitting and merging. "Planet"
   in 2006 was a boundary revision, not a sense addition; "atom" kept its
   referent while losing its defining property. What is the cost of a
   re-partition in the block-grid model, and is it bounded?
5. **Falsifier:** what would show that unbounded label growth is affordable and
   no conservation rule is needed?

---

# PART 7 — CROSS-CUTTING

1. **Which objectives are actually the same problem?** A (Sigma amendment) and
   C (slow drift) may be the same object at different layers: a constitution
   drifting under a changing world versus a world model drifting under a
   changing world. If they are the same, one mechanism should serve both. If
   they are not, give the discriminating property.
2. **Ownership.** For each mechanism you propose, name the owning subsystem from
   §1.1 and show it does not violate the responsibility split. Any proposal that
   pulls generation, storage, admissibility, or continuity back into CA is
   re-creating the god-object that was deliberately dismantled.
3. **Composition.** QMT's composition theorem is a schema with eight conditions
   and no proof, and its error budget `delta_{2*1} <= L_2*eps_1 + eps_2` is
   fine for two hops and diverges over 10^4 with any `L > 1`. Does a discrete,
   saturating, quinary substrate give **exact** morphisms rather than bounded
   approximate ones, eliminating error accumulation entirely? If so, that is the
   strongest argument for the discrete substrate and it should be stated as
   such. If not, what bounds `n` or forces `L <= 1`?

---

# PART 8 — REQUIRED OUTPUT

```text
1. Executive verdict per objective: SOUND / REPAIRABLE / BROKEN, one paragraph.

2. Attacks. Your strongest objection per objective, with the discriminating
   test that would settle it.

3. Repairs. A concrete alternative for every attack. No orphan objections.

4. Ownership map. Mechanism -> owning subsystem -> boundary check.

5. Falsifier table. Every surviving mechanism gets a row with the observation
   that would kill it.

6. Claim-status audit. Every substantive claim, tagged per Part 0.

7. Disagreement register. Where you expect other panel members to disagree with
   you, and the experiment that resolves it.

8. Open items you could not resolve, stated as UNRESOLVED rather than answered
   optimistically.
```

Do not produce a canonical paper. Do not produce a specification.
Produce an adversarial review.
