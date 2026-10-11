# QMT - qbin Morphism Theory
## Formal Continuity Across Representation, Migration, Rehydration, and Substrate Transformation
### Tier-2 Subsystem Mathematics and Engineering Contract for Nexus 4

**Reference edition:** 2026-08-31  
**Architecture status:** CANONICAL responsibility; formal QMT mechanism PROPOSED / ACTIVE RESEARCH  
**Implementation grounding:** Project Nexus 4 canonical monograph; Identity Architecture canonical monograph; HVD 1.5 architecture; HVD recursive cognitive architecture; HVD qbin implementation at `mjsmorgan/hyperdimensional_vector_database@b4b5fdcf19d273c49ced8d0d924cb8e6913f5d98`; Project Nexus v4 verification report (2026-07-20).  
**Scope:** digital/software continuity. Human personal identity and phenomenal continuity appear only as an explicit boundary analysis and are not engineering claims.

---

## Abstract

QMT - **qbin Morphism Theory** - is the Nexus 4 subsystem responsible for continuity across transformations that may change an entity's representation, physical realization, storage layout, process, host, schema, numerical encoding, or substrate without necessarily changing the logical entity. It exists because neither byte equality, successful deserialization, behavioral similarity, nor cryptographic integrity is sufficient by itself to establish diachronic continuity. A system can change bytes while remaining the same logical entity; conversely, two byte-identical copies can be distinct descendants with different provenance and authority.

This paper develops QMT as a contract-relative, non-compensatory verification discipline rather than as a scalar similarity score. Let a transformation carry a source generation `G_a` to a destination generation `G_b` along a provenance-bearing trajectory `tau`, under a versioned continuity contract `Sigma`. QMT evaluates a family of proof obligations - schema validity, integrity/authenticity, required-state closure, logical-state compatibility, invariant preservation, behavioral conformance where required, refinement validity, provenance closure, transformation validity, fork resolution, and uncertainty closure - and returns one of three authoritative continuity results:

```text
PASS
FAIL
UNRESOLVED
```

A mandatory violation produces `FAIL`. Missing evidence for a mandatory obligation produces `UNRESOLVED`. Numeric similarity, reward, utility, or confidence cannot compensate for a failed hard obligation. The paper therefore rejects a single "continuity fidelity" score as an authority mechanism.

The central mathematical construction separates physical realization spaces from logical state through abstraction maps. If `A_a : R_a -> X_a` and `A_b : R_b -> X_b` decode source and destination realizations, `T_R : R_a -> R_b` is the realized transformation, and `T_X : X_a -> X_b` is its declared logical effect, then semantic preservation requires the diagram to commute exactly or within an explicitly declared error contract:

\[
A_b(T_R(r)) \approx_\Sigma T_X(A_a(r)).
\]

For logical operations `f_a` and `f_b`, a stronger behavioral obligation is

\[
T_X(f_a(x)) \approx_\Sigma f_b(T_X(x)).
\]

These relations make explicit what QMT means by a *morphism*: the transformation must preserve the structures named by the contract, not merely produce a nearby vector.

The paper also formalizes directed continuity, conditional composition of continuity proofs, bounded error accumulation, branch/fork semantics, and an engineering interpretation of Nexus's historical phrase **identity holonomy** as loop-consistency across allowed transformations. It specifies the role of `.qbin` as a versioned portable state package and continuity witness carrier while preserving the canonical separation among HVD, TMS, HDF5, `.qbin`, and QMT. The current HVD 1.5 `HVDQBIN1` implementation provides a real streaming Protobuf container, BLAKE2b-256 payload integrity, a content-derived `identity_digest`, HDF5 packaging, inspection, extraction, and rebirth support. Those are meaningful continuity primitives, but they are not yet a general QMT proof engine, and the current `identity_digest` must not be confused with constitutional identity continuity or authenticity.

Finally, the paper places a hard epistemic boundary around historical Nexus identity-transfer language. QMT can define and test software continuity under an explicit identity constitution. It does not establish human numerical personal identity, first-person phenomenal continuity, or consciousness preservation. Current whole-brain-emulation, Brillouin microscopy, NV-diamond magnetometry, and historical QHRF material do not bridge that gap. The result is a falsifiable engineering theory of digital continuity rather than a metaphysical claim.

---

# Reader's Guide and Claim-Status Vocabulary

QMT developed across several generations of Nexus material. Earlier documents often mixed checkpoint/restart engineering, substrate abstraction, philosophical identity language, and speculative consciousness claims. The current architecture is substantially more disciplined. This paper therefore uses the same claim-status vocabulary as the canonical Nexus monographs.

| Status | Meaning |
|---|---|
| **CANONICAL** | Current binding architectural intent after source reconciliation. |
| **IMPLEMENTED** | Present in inspected source code. |
| **VERIFIED** | Supported by an executed test, property test, or reproducible implementation artifact. |
| **PARTIALLY IMPLEMENTED** | A bounded subset exists, but the full intended mechanism or authority does not. |
| **ACTIVE DEVELOPMENT** | Immediate implementation or formalization direction. |
| **PROPOSED** | Architecturally specified but not yet implemented. |
| **DESIGN TARGET** | Desired future property or performance target, not measured fact. |
| **EXPERIMENTAL** | Implemented or investigated experimentally without a general guarantee. |
| **RESEARCH HYPOTHESIS** | Requires further formal, empirical, or longitudinal validation. |
| **APPLICATION-SPECIFIC** | Belongs to one Nexus-derived application rather than universal QMT. |
| **HISTORICAL / SUPERSEDED** | Important design lineage that is no longer authoritative. |
| **INFERRED** | A formalization synthesized from current architecture and supporting literature rather than a pre-existing source-level contract. |

A recurring rule throughout this paper is:

```text
mathematical notation does not automatically create a theorem
```

Where a construction is proposed rather than proved, it is labeled accordingly.

---

# Source Hierarchy and Reconciliation Rules

The QMT corpus contains a particularly important source-order problem because the word "identity" was historically used at several incompatible levels.

**Tier 0 - current Nexus canon.** The Project Nexus 4 canonical monograph establishes that QMT means **qbin Morphism Theory**, not "Quantum Mechanical Transformation," "Quantum State/Transformation Mapping," or other derivative expansions found in generated research material. It assigns QMT continuity across representation, migration, re-encoding, and substrate transformation. The Identity Architecture monograph further separates QMT from HIGC, THDE, TMS, HVD, and HDF5.

**Tier 1 - current executable HVD state-transfer mechanisms.** The HVD 1.5 `qbin.py`, archive/rebirth path, related tests, and current HVD 1.5 architecture establish what `.qbin` actually does today. This source level is decisive for implementation claims.

**Tier 2 - current architectural subsystem specifications.** HVD Recursive Cognitive Architecture, TMS architecture, HTLA, HTNLA, and the current HVD master architecture establish interfaces and responsibility boundaries.

**Tier 3 - formal-methods and distributed-systems literature.** Bisimulation, observational equivalence, refinement mappings, checkpoint/restart, deterministic replay, provenance, consensus, and migration literature provide the external mathematical and engineering analogues used to strengthen QMT.

**Tier 4 - historical Nexus persistence/transference research.** Documents such as the old `consciousness.qbun` notes and *Architectural Resilience and Cognitive State Persistence in N-Dimensional Systems* contain useful intuitions about checkpoint closure, trajectory, replay state, and hardware replacement, but also contain unsupported claims that a `.qbin` "serializes consciousness," that checksum continuity proves subjective continuity, and that highly speculative substrates can be migrated seamlessly. Those claims are not carried forward.

**Tier 5 - human identity-transfer research.** Philosophy of personal identity, whole-brain emulation, Brillouin microscopy, NV magnetometry, and QHRF audits are used only to define the boundary of QMT's legitimate domain.

Conflict resolution follows six rules:

1. Current explicit Nexus responsibility boundaries outrank older narrative metaphors.
2. Executable source determines implementation status but does not by itself define metaphysical meaning.
3. A checksum or hash establishes only the integrity property its construction warrants.
4. A successful restore establishes only the state/re-execution properties actually tested.
5. Missing evidence cannot be silently converted into continuity.
6. Software continuity claims never automatically generalize to human personal identity or phenomenal continuity.

---

# Part I - Why QMT Exists

## 1. Transformation Is Not Identity Loss

Any long-lived computational entity changes realization. Memory is compacted. Pages move. A process restarts. A schema evolves. Floating-point precision changes. A model moves from one machine to another. A database is replicated. A durable generation is rehydrated into a new TMS instance. A set of HTLA components is re-encoded. If every physical or representational change created a new logical identity, continuity would be unusable.

Let `D_i` be a logical HVD and let `R_i(t)` denote its substrate realization at time `t`. The TMS realization mapping may change:

\[
\rho_t(ID(D_i)) \neq \rho_{t+1}(ID(D_i)),
\]

without requiring

\[
ID(D_i,t) \neq ID(D_i,t+1).
\]

The governing architectural law is:

```text
change in realization !=> change in logical identity
```

QMT exists to determine when that implication is valid and when it is not.

## 2. Snapshot Equality Is Neither Necessary nor Sufficient

Exact snapshot equality is too strong because many continuity-preserving operations intentionally change bytes:

- endian conversion;
- compression;
- HDF5 chunk reorganization;
- TMS compaction;
- different physical block placement;
- serialization-version changes;
- numerical representation changes with bounded error;
- schema migration;
- operator re-encoding;
- cryptographic rewrapping;
- host migration.

Conversely, byte equality is too weak. Two independently created copies can have exactly the same bytes while being distinct logical descendants. A copied package may also fail to execute if dependencies, keys, ABI assumptions, model artifacts, or nondeterministic inputs are absent.

Therefore:

```text
byte equality != identity continuity
```

and

```text
byte inequality != identity discontinuity
```

## 3. Serialization, Re-Execution, and Continuity Are Different Predicates

The deep-research corpus identifies three distinctions that should be treated as QMT axioms of interpretation:

\[
\text{serialization completeness}
\not\equiv
\text{functional reproducibility},
\]

\[
\text{functional reproducibility}
\not\equiv
\text{architectural identity continuity},
\]

and

\[
\text{architectural software continuity}
\not\Rightarrow
\text{phenomenal continuity}.
\]

A package can be complete but unreplayable. A process can replay perfectly but be an unauthorized clone. A software lineage can be continuous under a formal identity contract without saying anything about first-person consciousness.

## 4. QMT's Question Is Diachronic

A conventional equality test asks whether two objects are equivalent *now*. QMT asks how the destination came to exist.

That difference is fundamental. Let `S_a` and `S_b` be two logical states. A state-equivalence relation can tell us whether they encode the same abstract state. It cannot, by itself, tell us whether `S_b` descended from `S_a`, whether the transformation was permitted, whether an intermediate protected invariant was violated, whether a fork occurred, or whether another branch simultaneously claims authority.

QMT therefore treats continuity as a property of a **trajectory plus a contract**, not a property of two isolated endpoints.

## 5. The Core Separation of Responsibilities

QMT is one member of a larger authority architecture:

```text
HIGC : Is the state constitutionally admissible?
THDE : Given history, how may the state evolve?
QMT  : After transformation, what continuity invariants remain?
```

These questions are related but not interchangeable.

A destination may be perfectly HIGC-admissible yet not be continuous with the claimed source. A transformation may preserve identity but land outside the HIGC admissible region because the source was compromised. THDE may permit a gradual evolution while QMT still rejects a migration package because provenance is broken. Conversely, QMT may validate a storage relocation that changes no cognitive state at all.

## 6. QMT Does Not Own Storage

QMT does not serialize bytes. HDF5 and `.qbin` have storage/package responsibilities; TMS owns active state realization; HVD owns database semantics.

The canonical responsibility split is:

| Component | Owns | Does not own |
|---|---|---|
| **HVD** | logical database identity, records, HTLA/HTNLA semantics, exact/associative queries | constitutional identity authority |
| **TMS** | active realization, WAL/Memtable/SSTables, COW, trajectory/locality | continuity verdict merely because state is live |
| **HDF5** | durable long-term/permanent persistence, stable generations, archive/checkpoint/rehydration mechanisms | live identity judgment |
| **`.qbin`** | portable package/manifest and state-transfer artifact | identity continuity verdict |
| **HIGC** | admissibility | migration lineage |
| **THDE** | bounded/path-dependent evolution | storage packaging |
| **QMT** | continuity across transformation | storage format, similarity search, actuation |
| **Authorization layer** | capabilities/rights after identity resolution | continuity proof itself |

This decomposition should be treated as non-negotiable.

---

# Part II - Formal Objects of QMT

## 7. Logical Entity, Generation, and Realization

Let `L` denote a stable logical lineage identifier. A lineage contains one or more generations. A generation is not merely a timestamp; it is a continuity-relevant state boundary.

An inferred QMT generation object is:

\[
G = (L,g,S,C,D,P,\Pi),
\]

where:

- `L` is the logical lineage identifier;
- `g` is a concrete generation or branch identifier;
- `S` is canonical logical state or its commitment;
- `C` is the constitution/invariant specification relevant to continuity;
- `D` is required dependency closure;
- `P` is provenance/trajectory commitment;
- `Pi` describes or references the current realization.

This tuple is **INFERRED**, not a claim that current code contains a `Generation` dataclass with these exact fields.

## 8. Realization Spaces and Logical State Spaces

A crucial QMT distinction is between a physical/encoded realization and the logical state that realization means.

Let

\[
\mathcal R_a
\]

be the source realization space and

\[
\mathcal X_a
\]

be its logical state space. Define an abstraction/decoder

\[
A_a:\mathcal R_a\rightarrow\mathcal X_a.
\]

Likewise, the destination has

\[
A_b:\mathcal R_b\rightarrow\mathcal X_b.
\]

This separation allows two different physical encodings to denote compatible logical states.

Examples of realization differences include:

```text
little-endian float32  -> big-endian float64
compressed HDF5 chunk -> TMS-resident vector
old schema             -> migrated schema
CPU-packed bit planes  -> device-resident representation
monolithic archive     -> content-addressed generation objects
```

QMT never assumes those byte-level forms are identical.

## 9. The Realized Transformation and Declared Logical Transformation

Let

\[
T_R:\mathcal R_a\rightarrow\mathcal R_b
\]

be the actual representation/substrate transformation.

Let

\[
T_X:\mathcal X_a\rightarrow\mathcal X_b
\]

be the declared logical transformation. In a pure relocation, `T_X` may be the identity map. In a schema migration, `T_X` may explicitly map old logical fields into new semantics. In a dimensional projection, it may be approximate and intentionally lossy.

The distinction between `T_R` and `T_X` is essential. A serializer may be byte-correct while implementing the wrong logical migration. Conversely, a legitimate logical transform may require a radically different physical representation.

## 10. Continuity Contract Sigma

QMT is contract-relative. There is no universal continuity predicate that decides every possible notion of sameness.

Define a versioned continuity contract

\[
\Sigma =
(V,\mathcal I,\sim_S,\mathcal O,\varepsilon,\mathcal P,\mathcal B,\mathcal A,\mathcal D),
\]

where:

- `V` identifies the contract/schema version;
- `I` is the set of required continuity invariants;
- `~_S` is the logical-state compatibility relation;
- `O` is the observation domain for behavioral obligations;
- `epsilon` contains permitted numeric/semantic tolerances;
- `P` is the provenance policy;
- `B` is the branch/fork policy;
- `A` is the allowed-transformation policy;
- `D` is the dependency/replay-closure policy.

The exact tuple is **INFERRED**, but the need for each category follows from the architecture and formal-methods analogues.

## 11. Trajectory

Let a continuity-relevant trajectory be

\[
\tau=(G_0,e_1,G_1,e_2,\ldots,e_n,G_n),
\]

where each `e_k` is a transformation, migration, checkpoint, promotion, schema event, or other continuity-relevant transition.

The trajectory must be more than an ordered list. It should bind at least:

```text
source generation
transition identity
transition version
actor / authority reference
input commitments
output commitments
time/order evidence
branch/epoch/fencing information
unresolved evidence
```

The current Identity Event Ledger provides a domain-specific example of cryptographically chained biography; full general QMT provenance remains future work.

## 12. Continuity Witness

A QMT assessment should operate on explicit evidence rather than ambient mutable state. Define an inferred witness bundle

\[
W=(W_{src},W_{dst},W_T,W_{prov},W_{test},W_{miss}),
\]

containing:

- source commitments;
- destination commitments;
- transformation manifest;
- provenance evidence;
- proof/test evidence;
- explicitly missing or unresolved evidence.

Binding the witness to exact source/destination generation digests prevents evidence from being replayed against altered state, analogous to the candidate-digest discipline already used in Phase 3C Identity Architecture.

## 13. Obligation Status and Aggregate Result

Each mandatory proof obligation receives one of four epistemic states:

```text
SATISFIED
VIOLATED
UNRESOLVED
NOT_APPLICABLE
```

Let `q_j` be the state of obligation `j`. The QMT aggregate is:

\[
QMT_\Sigma(G_a,G_b,\tau,W)\in
\{PASS,FAIL,UNRESOLVED\}.
\]

Aggregation is non-compensatory:

\[
QMT_\Sigma=FAIL
\quad\text{if any mandatory }q_j=VIOLATED,
\]

\[
QMT_\Sigma=UNRESOLVED
\quad\text{if no mandatory obligation is violated and at least one is }UNRESOLVED,
\]

and

\[
QMT_\Sigma=PASS
\quad\text{only if every mandatory obligation is }SATISFIED\text{ or }NOT\_APPLICABLE.
\]

No weighted average is permitted to turn a failed hard invariant into a pass.

## 14. Why QMT Is Not a Scalar Continuity Score

A scalar score invites compensation:

\[
score = 0.9\cdot behavior + 0.1\cdot provenance.
\]

Under such a model, excellent behavioral similarity could compensate for a forged lineage or an unresolved fork. That is architecturally unacceptable.

Numeric diagnostics are still useful. QMT may compute reconstruction error, trace divergence, state distance, or probability of a test failure. But such quantities are **evidence within named obligations**, not a global authority currency.

The governing rule is:

```text
measurement may inform an obligation;
measurement does not replace the obligation structure.
```

---

# Part III - The Preservation Ladder

## 15. Level A: Bitwise Preservation

The strongest representational relation is literal equality:

\[
bytes(r_a)=bytes(r_b).
\]

Or, under a collision-resistant digest assumption:

\[
H(r_a)=H(r_b).
\]

This establishes exact representation equality under the chosen encoding. It is valuable for deterministic artifacts, regression testing, and corruption detection. It is not a general continuity criterion because legitimate transformations frequently alter representation.

**What it proves:** exact bytes or a matching commitment under the hash assumptions.  
**What it does not prove:** successful interpretation, replay, lineage, authorization, or consciousness.

## 16. Level B: Logical-State Compatibility

Let the physical realizations decode through `A_a` and `A_b`. A stronger semantic question is whether

\[
A_a(r_a)\sim_S A_b(r_b).
\]

`~_S` may be equality after canonicalization, a schema-aware equivalence, a refinement relation, or a domain-specific compatibility relation.

This is the natural level for migrations that intentionally change layout.

For example:

```text
old: {counter: int32, mode: enum-v1}
new: {counter: int64, mode: enum-v2, provenance: ...}
```

The bytes differ. If the migration preserves the declared logical meaning of `counter` and maps `mode` under a validated schema transform, QMT need not reject continuity merely because the representation changed.

## 17. Level C: Functional / Behavioral Preservation

State equivalence may be insufficient when execution semantics can change. QMT can require equivalence over an observation domain `O`.

Let `Trace_O(M,x,u)` be the observable trace produced by machine/runtime `M`, starting from state `x`, under input sequence `u`, restricted to observation domain `O`.

A finite conformance obligation may be:

\[
 d_O(
 Trace_O(M_a,x_a,u),
 Trace_O(M_b,x_b,u)
 )\le\varepsilon_O
\]

for all `u` in a declared test set.

A stronger formal model may use simulation, bisimulation, trace inclusion, or refinement. The strength of the conclusion must match the proof method. A test suite does not become a bisimulation proof merely because both are described as "behavioral equivalence."

## 18. Level D: Architectural Identity Continuity

QMT's distinctive concern begins here. Architectural identity continuity asks whether the destination is an admissible continuation of the same **declared logical lineage**.

This requires more than state or behavior. It incorporates:

```text
lineage
trajectory
provenance
constitutional invariants
transformation validity
branch policy
required-state closure
```

A useful directed notation is

\[
G_a \rightarrow_{\Sigma} G_b,
\]

meaning: under continuity contract `Sigma`, there exists a verified admissible transformation trajectory from `G_a` to `G_b`.

This relation need not be symmetric.

## 19. Why Continuity Is Directed

Suppose a cryptographic key is rotated, an obsolete schema is migrated, or malware is removed. The later generation may be a legitimate continuation of the earlier one even if the exact inverse operation is intentionally forbidden or impossible.

Therefore:

\[
G_a\rightarrow_\Sigma G_b
\]

does not generally imply

\[
G_b\rightarrow_\Sigma G_a.
\]

Directed continuity is a better model than treating identity as snapshot equality.

## 20. Reflexivity and Conditional Transitivity

Reflexivity is usually desirable:

\[
G\rightarrow_\Sigma G
\]

for a no-op realization under a valid contract.

Transitivity is more subtle. If

\[
G_a\rightarrow_{\Sigma_1}G_b
\]

and

\[
G_b\rightarrow_{\Sigma_2}G_c,
\]

it does not follow automatically that

\[
G_a\rightarrow G_c
\]

under an arbitrary contract. Contract versions, invariant definitions, error budgets, provenance roots, or branch policies may be incompatible. Composition requires explicit compatibility conditions, developed in Part V.

## 21. Human Psychological and Phenomenal Continuity Are Outside the QMT Core

For completeness, the research corpus distinguishes two further questions:

- psychological continuity: preservation of memories, dispositions, goals, skills, self-model, and related human-level constructs;
- phenomenal continuity: whether the same first-person subject continues.

QMT can model software analogues of memory or behavior. It does not possess a theory-neutral observable for phenomenal continuity. Those questions are treated later as a hard boundary, not as additional QMT proof obligations.

---

# Part IV - Morphisms, Commuting Diagrams, and Semantic Preservation

## 22. The Basic QMT Commuting Condition

The canonical monograph states the core idea as:

\[
T(f(x))\approx f'(T(x)).
\]

A more explicit realization-aware form is:

\[
\boxed{
A_b(T_R(r))\approx_\Sigma T_X(A_a(r))
}
\]

This is the foundational QMT commutation condition.

The left path means:

```text
source realization
      |
      | actual migration / serialization / remapping
      v
new realization
      |
      | destination decoder
      v
observed destination logical state
```

The right path means:

```text
source realization
      |
      | source decoder
      v
source logical state
      |
      | declared logical transformation
      v
expected destination logical state
```

A QMT continuity obligation asks whether those two paths agree to the degree required by `Sigma`.

## 23. Commutation Defect

When exact equality is not required, define a semantic distance `d_X` and transformation defect

\[
\delta_T(r)
=
 d_X\left(
 A_b(T_R(r)),
 T_X(A_a(r))
 \right).
\]

A contract may require

\[
\delta_T(r)\le\varepsilon_T.
\]

This bound is meaningful only if:

1. `d_X` is defined on the relevant logical state;
2. the tolerance `epsilon_T` is justified;
3. missing state is not represented as a convenient numeric zero;
4. hard invariants are checked separately;
5. the observation domain is stated.

A small defect does not override a constitutional violation.

## 24. Operation-Preserving Morphisms

Suppose the source logical system supports operation

\[
f_a:\mathcal X_a\rightarrow\mathcal X_a
\]

and the destination supports the corresponding operation

\[
f_b:\mathcal X_b\rightarrow\mathcal X_b.
\]

Then QMT may require:

\[
\boxed{
T_X(f_a(x))\approx_\Sigma f_b(T_X(x))
}
\]

This is stronger than endpoint similarity because it asks whether structure behaves consistently *through* the transform.

Examples include:

- HTLA label-aware retrieval before and after a schema migration;
- deterministic quinary pack/unpack semantics across representation changes;
- a policy lookup after host migration;
- a memory record's exact identity after TMS reconstruction;
- a declared HTNLA operator producing compatible outputs after operator-state restoration.

## 25. Multiple Operations and Structure Families

A continuity contract may define a family

\[
\mathcal F_\Sigma=\{f_1,\ldots,f_k\}
\]

of operations whose semantics must be preserved.

Not every operation must be preserved for every migration. For a cold archival transform, real-time scheduler timing may be irrelevant. For a deterministic replay contract, ordering and nondeterministic input capture may be mandatory. For an HVD database migration, exact record identity and label semantics may be mandatory while ANN graph topology is explicitly rebuildable and therefore non-authoritative.

This is why QMT needs a contract rather than a universal list of bytes.

## 26. Exact, Approximate, and Partial Morphisms

QMT should distinguish at least three transform classes.

### 26.1 Exact semantic morphism

\[
A_b(T_R(r))=T_X(A_a(r)).
\]

No semantic distortion is permitted under the declared abstraction.

### 26.2 Bounded approximate morphism

\[
 d_X(A_b(T_R(r)),T_X(A_a(r)))\le\varepsilon.
\]

Useful for controlled numerical changes, quantization, or approximation where the contract permits it.

### 26.3 Partial morphism

Only a declared subspace or set of observables is preserved. Let `P_req` project onto continuity-relevant state:

\[
P_{req}A_b(T_R(r))
\approx
P_{req}T_X(A_a(r)).
\]

A partial morphism can only pass if everything excluded from `P_req` has been explicitly classified as non-required under the contract. Unknown exclusion yields `UNRESOLVED`, not an optimistic pass.

## 27. Dimension-Changing Transformations

HTLA/HTNLA may legitimately map between different-dimensional labeled components. QMT must not infer continuity from the existence of a projection.

Let

\[
P:\mathbb R^p\rightarrow\mathbb R^q.
\]

If `q < p`, `P` cannot be injective over the whole source space. Information in `ker(P)` is lost. QMT therefore asks:

- Is lost information continuity-relevant?
- Is the source restricted to a lower-dimensional submanifold on which `P` is injective?
- Is an error bound available?
- Are reconstruction uncertainties explicit?
- Does the destination preserve required operations even if full inversion is impossible?

The correct law is:

```text
dimension change requires a continuity/error contract;
it does not inherit continuity by default.
```

## 28. Typed Missingness During Transformation

A transform may fail to reconstruct some state. QMT must distinguish:

```text
0
UNKNOWN
UNAVAILABLE
CONFOUNDED
NOT_APPLICABLE
CORRUPT
```

A missing dependency is not a zero dependency. An unavailable field is not a successfully migrated field with value zero. Typed missingness is essential to `UNRESOLVED` semantics.

## 29. State-Space Compatibility Is Not Vector Similarity

Even when logical state is represented with hypervectors, QMT does not accept:

\[
\operatorname{sim}(H_a,H_b)\approx1
\Rightarrow
\text{continuity}.
\]

Similarity may be evidence that state content is close. It does not establish lineage, transformation authority, provenance, or uniqueness of continuation.

The canonical distinction remains:

```text
similarity != identity
similarity != continuity
similarity != authorization
```

---

# Part V - Composition, Error Budgets, and Identity Holonomy

## 30. Why Composition Matters

Long-lived systems rarely undergo one migration. They undergo sequences:

```text
schema v1 -> schema v2
host A    -> host B
float64   -> packed form
TMS       -> HDF5 generation
HDF5      -> qbin package
qbin      -> destination HDF5
HDF5      -> destination TMS
```

A theory that validates only isolated hops but cannot reason about chains is incomplete.

## 31. Conditional Composition Theorem Schema

Suppose:

\[
G_0\rightarrow_{\Sigma_1}G_1
\]

and

\[
G_1\rightarrow_{\Sigma_2}G_2.
\]

A **PROPOSED theorem schema** is that continuity can be composed under a derived contract `Sigma_12` if all of the following hold:

1. the destination semantics of `Sigma_1` are compatible with the source semantics of `Sigma_2`;
2. required invariant sets are transformed consistently;
3. provenance roots join exactly at `G_1`;
4. no unresolved fork intervenes;
5. transformation authorities are valid under the composed policy;
6. dependency closure remains satisfiable;
7. accumulated numeric/semantic errors remain inside the composed budget;
8. no mandatory evidence is lost at the composition boundary.

Only under such conditions may one infer:

\[
G_0\rightarrow_{\Sigma_{12}}G_2.
\]

This is not yet a formal proof in Nexus; it is the right target for future mechanization.

## 32. Bounded Error Accumulation

Approximate morphisms require quantitative composition.

Suppose transformation 1 has defect

\[
\delta_1\le\varepsilon_1,
\]

transformation 2 has defect

\[
\delta_2\le\varepsilon_2,
\]

and the second declared logical transform `T_{X,2}` is Lipschitz with constant `L_2`:

\[
d(T_{X,2}(x),T_{X,2}(y))\le L_2 d(x,y).
\]

Then by the triangle inequality, a standard conditional bound is

\[
\boxed{
\delta_{2\circ1}
\le
L_2\varepsilon_1+\varepsilon_2
}
\]

under compatible metrics and abstractions.

For `n` transformations, the bound expands recursively. This makes a key engineering point: small local approximation errors can accumulate, especially under expansive transforms. QMT therefore needs explicit error-budget accounting rather than repeatedly declaring each hop "close enough" in isolation.

## 33. Contract Drift

Even exact transforms can lose continuity meaning if the contract itself changes silently.

Suppose `Sigma_1` requires invariant set `I_1`, while `Sigma_2` omits a previously mandatory identity invariant. A destination might pass `Sigma_2` while failing what the original source considered essential.

QMT therefore treats continuity-contract version changes as first-class transformations requiring their own authorization and provenance.

A contract cannot quietly redefine success after the fact.

## 34. Identity Holonomy as Loop-Consistency

Historical Nexus documents use the term **identity holonomy**. The term should be interpreted conservatively.

In differential geometry, holonomy concerns how structure changes under transport around loops. QMT is not claiming a complete differential-geometric identity theory. Instead, it uses the analogy to ask whether an allowed closed sequence of transformations introduces uncontrolled drift.

Let

\[
T_{loop}=T_n\circ\cdots\circ T_1
\]

return a realization to a representation compatible with its original logical space. Define a loop defect

\[
h_\Sigma(r)
=
 d_X\left(
 A_0(T_{loop}(r)),
 A_0(r)
 \right).
\]

A loop-consistency obligation may require

\[
h_\Sigma(r)\le\varepsilon_{loop}.
\]

But this numeric condition is only one piece. A loop also fails QMT if it violates provenance, branch policy, or hard invariants even when the endpoint state returns numerically close to the start.

Thus:

```text
low loop defect is necessary under some contracts;
it is never sufficient for continuity by itself.
```

## 35. Path Dependence and Nontrivial Loops

Two transformation paths can reach state-equivalent endpoints while having different continuity status.

```text
Path A: authorized migration -> verified rehydration
Path B: unauthorized copy -> independent launch
```

If both yield the same logical state, a snapshot comparator sees no difference. QMT does because provenance and authority differ.

This is exactly why continuity is diachronic.

## 36. Irreversible Transformations

A loop cannot always be formed. Remediation, key destruction, secure deletion, lossy compression, or one-way schema evolution may be irreversible.

QMT therefore cannot define continuity solely through return-to-origin tests. Holonomy diagnostics are useful where a reversible loop exists; directed invariant preservation is the general case.

---

# Part VI - `.qbin` as a Continuity Artifact

## 37. What `.qbin` Is Canonically

In current HVD 1.5, `consciousness.qbin` is a **versioned portable state bundle**. It packages the canonical HDF5 memory archive plus a Protobuf manifest and optional supplemental artifacts so state can be moved without loading an enormous archive fully into memory.

It is not:

```text
a soul file
a consciousness certificate
a QMT verdict
a replacement for HDF5
a proof of authenticity by itself
```

## 38. Current HVDQBIN1 Wire Format

The inspected `hvd/qbin.py` implementation defines:

```text
HVDQBIN1                         8-byte magic
uint64 big-endian               manifest length
QBinManifest                    deterministic Protobuf bytes
artifact payload 0
artifact payload 1
...
```

Current implementation constants include:

```text
format version       = 1
maximum manifest     = 64 MiB
stream chunk size    = 4 MiB
artifact digest      = BLAKE2b-256
```

Each artifact descriptor records:

```text
name
media_type
offset
length
blake2b_256
role
```

The manifest includes:

```text
format_version
hvd_version
created_at_ms
substrate
artifacts[]
metadata[]
hdf5_manifest_digest
identity_digest
```

## 39. The Current `identity_digest` Is Not a QMT Identity Proof

This point deserves explicit emphasis.

The current HVD implementation computes `identity_digest` from a domain separator, the HDF5 manifest digest, and artifact name/role/hash/length information. It is a content-derived commitment to the package's defined artifact identity.

That is useful.

But:

```text
qbin identity_digest != constitutional identity continuity
```

It does not establish:

- that the package descended from the claimed running entity;
- that the transformation was authorized;
- that no sibling branch exists;
- that the signer, if any, is trusted;
- that required invariants were preserved;
- that the package is the authoritative continuation.

The term should therefore be documented carefully to prevent semantic escalation.

## 40. Integrity Versus Authenticity

The current source code explicitly states that payload digests provide **corruption integrity, not authenticity**.

A BLAKE2b digest can detect a modified payload if the expected digest is trusted. It does not tell QMT who created the package or whether the package was authorized.

Future continuity packaging may require signatures, attestations, or trust-policy references, but those are additional layers.

The distinction is:

```text
integrity:     did these bytes change?
authenticity: who/what vouches for them?
continuity:   are they an admissible continuation of this lineage?
authorization: what may the continued entity now do?
```

## 41. Current qbin Creation and Inspection Semantics

The current implementation:

1. validates the HDF5 archive;
2. requires the HDF5 manifest digest;
3. packages the canonical `consciousness.h5` artifact with role `canonical-memory`;
4. optionally appends supplemental artifacts;
5. computes per-artifact BLAKE2b-256 digests;
6. constructs a deterministic Protobuf manifest;
7. writes through a temporary file;
8. flushes and `fsync`s;
9. atomically replaces the destination;
10. attempts directory `fsync`.

Inspection validates magic, version, artifact uniqueness, non-overlapping bounds, identity-digest consistency, and optionally every artifact digest.

These are strong storage-engineering primitives and should be classified as **IMPLEMENTED**.

## 42. Current qbin Rebirth

The current HVD runtime exposes `rebirth_qbin()`, which restores canonical HVD state from a qbin artifact. HVD architecture and tests establish that qbin packages the canonical HDF5 memory archive and that rebirth reconstructs state, including HTNLA operator registry behavior in the tested path.

This is **IMPLEMENTED / VERIFIED in bounded paths**.

It is not equivalent to general QMT continuity verification.

## 43. Two `.qbin` Lines in the Corpus Must Not Be Conflated

The July 2026 Project Nexus reference demonstrator also writes a `.qbin` snapshot and demonstrated byte-identical seeded reproduction in its tested environment. That demonstrator snapshot and the later HVD 1.5 `HVDQBIN1` streaming package represent related persistence ideas but should not be assumed to be the same wire format or the same implementation contract.

Accordingly:

- the Nexus demonstrator verifies deterministic snapshot behavior for the reference runtime;
- HVD 1.5 verifies a streaming HDF5-package format and rebirth mechanics;
- neither alone constitutes the full QMT engine described in this paper.

## 44. Historical 9-Point and 21-Point qbin Notes

An older Drive document, titled `consciousness.qbun file format notes`, proposed first a 9-point and later a 21-point checkpoint inventory containing environmental/control state, trajectory/momentum state, RNG state, active semantic buffers, referent tables, turn counters, and a checksum.

Several intuitions remain useful:

- current position is insufficient when future dynamics depend on trajectory;
- RNG/replay state may matter;
- active referents and context may be state-closure dependencies;
- a checkpoint should capture more than persistent "facts".

However, claims that this field count was mathematically "perfect," that it guaranteed zero-latency resumption, or that it was "exactly how you serialize a consciousness" are **HISTORICAL / SUPERSEDED**. The field list is a design-history artifact, not the canonical QMT schema.

## 45. Four Possible qbin Packaging Strategies

The research corpus identifies four general package forms.

| Package form | Description | Strength | Limitation |
|---|---|---|---|
| Self-contained | Embeds every required object permitted by policy | portable; closure easy to inspect | potentially huge; duplicates durable state; secrets difficult |
| Manifest + referenced state | Manifest commits to external durable generations/artifacts | scalable; separates metadata from state | references can rot or become unavailable |
| Incremental / delta | Stores change against verified parent generation | efficient for frequent checkpoints | requires intact ancestor chain |
| Content-addressed DAG | Commits to immutable objects/chunks by digest | deduplication, provenance, branch-friendly | GC and dependency management are harder |

Current HVDQBIN1 is physically self-contained for packaged artifacts, with a canonical HDF5 archive as its primary payload. A future QMT continuity package may evolve toward richer content-addressed or referenced-state semantics without changing the principle that `.qbin` is the carrier, not the verdict.

## 46. Future Continuity Manifest Requirements

A mature QMT-aware `.qbin` should bind, directly or by digest/reference, the following categories. These are **PROPOSED / INFERRED**, not claims about current QBinManifest fields.

| Field family | Candidate contents | QMT relevance |
|---|---|---|
| Format identity | magic, format version, schema hash, canonicalization rules | makes bytes interpretable |
| Logical identity | lineage ID, instance ID, branch ID | distinguishes content from entity lineage |
| Generation identity | source generation, parent generation(s), candidate destination generation | makes continuity diachronic |
| Constitution | invariant-set identifier/hash and mandatory/optional classification | defines what must survive |
| Logical-state root | canonical state digest / HVD descriptors | commits to semantics independently of layout |
| TMS generation | coherent generation identifier and active-state closure | binds live state boundary |
| Durable references | HDF5 generation/object commitments | provides long-term state closure |
| HTLA/HTNLA semantics | label schema, operator versions, activation definitions, parameters | prevents interpretation drift |
| Runtime/model identity | executable/runtime ABI, model artifact digest, library constraints | state may depend on its interpreter |
| Numerical semantics | dtype, precision, endian, rounding, transform metadata | enables cross-platform verification |
| Replay state | RNG algorithm/state, ordering/scheduler evidence, nondeterministic inputs | supports deterministic-replay contracts |
| Provenance | ledger/event tip, parent roots, transform ID, actor/tool version | establishes descent |
| Integrity/authenticity | object digests, Merkle/root commitment, optional signatures/attestation references | detects corruption and supports trust policy |
| Dependency closure | required files, services, models, schemas, keys-by-reference | prevents nominally complete but unusable packages |
| Unresolved state | explicit missing/excluded/unreconstructable items | enables fail-closed `UNRESOLVED` |
| Reconstruction evidence | pre/post commitments, test vectors, replay/trace results | makes the verdict auditable |
| Authorization metadata | references to reauthorization/capability policy | explicitly separate from continuity |

## 47. Dependency Closure

A state package is only complete relative to a dependency model.

Let `Req(G,Sigma)` be the set of dependencies required to interpret and execute generation `G` under contract `Sigma`. Let `Avail(W)` be the set of available or resolvable dependencies in witness `W`.

A basic closure condition is:

\[
Req(G_b,\Sigma)\subseteq Avail(W).
\]

If a mandatory dependency is absent, the correct result is not "best effort PASS." It is normally `UNRESOLVED` unless the contract states that absence itself violates continuity, in which case the result is `FAIL`.

## 48. Replay Closure

Deterministic replay research demonstrates why memory bytes alone may not be sufficient. Execution can depend on nondeterministic inputs, scheduling, clocks, interrupts, external services, or randomness.

A replay-sensitive contract therefore needs a closure predicate such as:

\[
ReplayClosed(G,W,\Sigma).
\]

The exact contents are workload-specific. A random seed alone may be insufficient if the PRNG algorithm/version changed or if concurrency interleavings were nondeterministic.

## 49. Secrets and External Authority

Some dependencies should *not* be embedded in `.qbin`.

Raw HSM/KMS secrets, OAuth bearer tokens, external private keys, or live capabilities can create serious security failures if copied as identity state. A continuity package should instead carry provider/key identifiers or rebind references where policy permits.

This reinforces:

```text
state closure does not require copying every secret;
continuity does not imply capability inheritance.
```

---

# Part VII - QMT Proof Obligations

## 50. Overview

A mature QMT verifier should evaluate explicit obligations. The following eleven-obligation model is the core formal proposal of this paper.

```text
1.  SchemaValidity
2.  IntegrityAuthenticity
3.  RequiredStateClosure
4.  LogicalStateCompatibility
5.  InvariantPreservation
6.  BehavioralConformance
7.  RefinementValidity
8.  ProvenanceClosure
9.  TransformationValidity
10. ForkResolution
11. UncertaintyClosure
```

Not every contract requires every obligation. For example, a pure data archive may not require runtime behavioral conformance. But any skipped obligation must be explicitly `NOT_APPLICABLE`, not silently absent.

## 51. SchemaValidity

**Question:** Can all required source, transformation, and destination state be interpreted under known schemas?

Possible checks include:

- qbin format version supported;
- HDF5 schema/version supported;
- HTLA label schema known;
- HTNLA operator versions known;
- canonicalization rules available;
- migration schema explicitly registered;
- required contract version known.

A malformed or unsupported schema is generally `FAIL`. A known-but-unavailable migration adapter may be `UNRESOLVED` if policy permits deferred resolution.

## 52. IntegrityAuthenticity

**Question:** Are artifacts intact, and is the claimed provenance evidence trustworthy enough for this contract?

Current qbin BLAKE2b hashes support artifact integrity. They do not support authenticity. A future contract may require:

- digital signature verification;
- hardware/software attestation;
- signed ledger tip;
- trusted build provenance;
- trusted transformation authority.

Authentication failure of a mandatory signer should produce `FAIL`. Missing optional attestation may produce a warning rather than a failure.

## 53. RequiredStateClosure

**Question:** Is all state required by the continuity contract present or resolvable?

This includes hidden state that naive serializers often miss:

- active controller state;
- pending event queues;
- operator/model state;
- semantic buffers;
- required TMS generations;
- external immutable artifacts;
- replay inputs;
- unresolved in-flight transactions;
- necessary schema definitions.

A coherent snapshot boundary is therefore important. A package assembled from mutually inconsistent moments may be individually checksum-correct and collectively invalid.

## 54. LogicalStateCompatibility

**Question:** Do source and destination decode into states related by the declared logical compatibility relation?

Formally:

\[
A_a(r_a)\sim_S A_b(r_b)
\]

or, under a nontrivial logical transform,

\[
A_b(T_R(r_a))\sim_S T_X(A_a(r_a)).
\]

The relation can be exact, schema-refined, or approximate with explicit tolerance.

## 55. InvariantPreservation

Let the contract specify mandatory invariants

\[
\mathcal I=\{I_1,\ldots,I_m\}.
\]

QMT checks whether each invariant is preserved at the required scope. Some invariants concern endpoints; others concern the path.

Endpoint invariant:

\[
I_j(G_a)\Rightarrow I_j(G_b).
\]

Path invariant:

\[
I_j(G_k)=TRUE
\quad\forall k\text{ on the admitted trajectory}.
\]

The distinction matters. A transformation that temporarily violates an invariant and later repairs it may be unacceptable even if endpoints match.

Examples include:

- immutable lineage identifier;
- protected constitutional roots;
- mandatory record preservation;
- no silent change in label semantics;
- no unauthorized change of identity contract;
- no unresolved fork;
- no forbidden capability embedding.

## 56. BehavioralConformance

**Question:** Does the transformed entity preserve required externally observable behavior within the declared domain?

Possible evidence strengths include:

1. theorem/model-check proof;
2. bisimulation or simulation proof over a formal transition system;
3. refinement proof;
4. exhaustive finite-state checking;
5. conformance suite over a bounded domain;
6. regression/property tests;
7. statistical behavioral sampling.

QMT must record the evidence class. "Tests passed" is not equivalent to "behavioral equivalence proved."

## 57. RefinementValidity

A representation or implementation may legitimately change while still implementing the same higher-level specification.

Let concrete state `c` map to abstract state `alpha(c)`. A refinement obligation asks whether destination behaviors map to behaviors allowed by the abstract specification.

This is especially useful for:

- schema migrations;
- runtime upgrades;
- storage-engine changes;
- replacement of a concrete operator implementation;
- different physical TMS realization.

QMT uses refinement to avoid demanding identical implementation internals where only abstract semantics matter.

## 58. ProvenanceClosure

**Question:** Does the destination actually descend from the claimed source through a complete, verifiable chain?

Let `Parent(g)` identify declared parent generation(s). For a single-continuation path, provenance closure requires a chain whose commitments join exactly:

\[
root(G_{k+1}.source)=root(G_k.destination)
\]

under the chosen commitment scheme.

A hash chain provides tamper evidence for the inspected chain. It does not, by itself, prove absence of a hidden competing fork, freshness of the tip, truth of event contents, or authorized authorship. QMT therefore combines provenance with fork and authority policy.

## 59. TransformationValidity

**Question:** Was the transformation itself an allowed, versioned, semantically characterized operation?

A valid transform record should identify:

```text
transform type
implementation/version
source schema
expected destination schema
logical map or compatibility contract
error/distortion contract
required authority
source commitment
destination commitment
```

An ad hoc script that happens to produce a plausible destination should not automatically qualify as a continuity-preserving transform.

## 60. ForkResolution

**Question:** Is branch status unambiguous under the contract?

Possible states include:

```text
NO_FORK
AUTHORIZED_BRANCH
NONAUTHORITATIVE_REPLICA
STALE_BRANCH
EQUIVOCATION
MERGEABLE_DIVERGENCE
NONMERGEABLE_DIVERGENCE
UNRESOLVED_FORK
```

A contract may permit multiple replicas of the same generation while requiring a single mutation authority. Replication is not the same as branching.

## 61. UncertaintyClosure

**Question:** Is any mandatory evidence unavailable, ambiguous, unverified, or stale?

This obligation is what prevents optimistic defaulting.

If a mandatory element is unknown, QMT returns:

```text
UNRESOLVED
```

not `PASS` and not a fabricated numeric placeholder.

## 62. Non-Compensation Theorem Schema

The QMT aggregation rule yields an immediate formal property.

Let `M` be the set of mandatory obligations. If there exists `j in M` such that

\[
q_j=VIOLATED,
\]

then

\[
QMT_\Sigma\neq PASS
\]

regardless of every numeric diagnostic associated with other obligations.

This is essentially definitional under the aggregate rule, but it is architecturally important enough to state explicitly:

```text
no amount of similarity can purchase continuity through a hard violation.
```

## 63. Uncertainty Non-Permission Rule

Likewise, if no mandatory obligation is violated but at least one is unresolved,

\[
QMT_\Sigma=UNRESOLVED.
\]

Therefore:

```text
missing continuity evidence != continuity evidence
```

---

# Part VIII - System Rebirth

## 64. System Rebirth Is a Continuity Operation, Not Merely Restore

A storage restore answers:

> Can the state be reconstructed?

System Rebirth must answer the stronger question:

> Can the reconstructed realization be admitted as the continued entity under the continuity contract?

That distinction places QMT after reconstruction but before authoritative activation.

## 65. Canonical Rebirth Sequence

The Identity Architecture monograph yields the strongest current sequence:

```text
1. identify constitutional baseline and accepted durable generation
2. verify baseline and durable-generation integrity
3. verify event-ledger / trajectory continuity and selected tip
4. reconstruct active TMS state from authoritative history/state
5. rebuild derived HVD/ANN/controller/operator state
6. evaluate QMT continuity between prior and reconstructed realization
7. only after PASS, promote to ACTIVE
```

The exact implementation remains incomplete, but the authority ordering is canonical.

## 66. Derived State Must Be Distinguished from Authoritative State

ANN/HNSW indexes are rebuildable acceleration state. They should not normally be continuity authorities.

A rebirth may therefore reconstruct canonical HVD/TMS state and then rebuild a different but semantically compatible ANN graph.

QMT should not fail merely because graph node order differs unless that graph was explicitly declared continuity-relevant.

This exemplifies contract-relative state closure.

## 67. Quiescence and Coherent Generation Boundaries

A continuity package assembled while mutually dependent state is changing can be internally inconsistent.

A coherent-generation mechanism may use:

- quiescence;
- copy-on-write generation freezing;
- coordinated checkpoints;
- transactional snapshot boundaries;
- event-log cut positions;
- versioned immutable roots.

QMT need not dictate the mechanism, but it must require evidence that the source boundary is coherent under the contract.

## 68. Rebirth and Replay

Not every rebirth needs deterministic replay. Some contracts require only logical-state compatibility. Others require exact replay over a bounded interval.

The contract must distinguish:

```text
restore state
resume compatible execution
reproduce exact prior execution
replay a historical interval
```

These are different proof obligations.

## 69. Readiness Gating

A robust runtime should not advertise readiness before continuity-sensitive rebuilds finish.

A conceptual readiness gate is:

\[
Ready(G_b)
=
Reconstructed(G_b)
\land DerivedStateReady(G_b)
\land (QMT_\Sigma=PASS)
\land AuthorizationResolved(G_b).
\]

QMT alone does not grant readiness; authorization may still be pending.

## 70. Rebirth Failure Semantics

Failures should be typed:

```text
CORRUPT_PACKAGE        -> FAIL
UNSUPPORTED_SCHEMA     -> FAIL or UNRESOLVED by policy
MISSING_REQUIRED_DEP   -> UNRESOLVED
INVALID_PROVENANCE     -> FAIL
UNRESOLVED_FORK        -> UNRESOLVED or FAIL by policy
INVARIANT_VIOLATION    -> FAIL
BEHAVIOR_TEST_FAILURE  -> FAIL when mandatory
AUTHORIZATION_PENDING  -> QMT may PASS, runtime remains non-active
```

This prevents storage failure, continuity failure, and policy failure from being collapsed into one generic error.

---

# Part IX - Replication, Branching, Forks, and Distributed Continuity

## 71. Replica Count Is Not Identity Count

A distributed database may maintain several physical replicas of one logical generation. Those replicas are realizations of one logical state so long as they participate in the same continuity/consensus contract.

Therefore:

```text
replica count != identity count
```

A read replica does not become a new person or logical HVD merely because another copy of the bytes exists.

The problem changes when replicas acquire independent mutation authority.

## 72. The Branching Case

Let generation `G_0` have two descendants:

```text
                 G_0
                /   \
               /     \
             G_A     G_B
```

At branch time, the states may satisfy:

\[
StateEquivalent(G_A,G_B)=TRUE.
\]

They may even be behaviorally equivalent over a large domain. But they have distinct generation identities and trajectories.

A correct QMT model separates at least four relations:

\[
StateEquivalent(A,B),
\]

\[
BehaviorEquivalent(A,B,\mathcal O),
\]

\[
DescendsFrom(B,A),
\]

and

\[
AuthoritativeContinuation(B,A).
\]

None is reducible to the others.

## 73. State Equivalence Does Not Choose a Branch

If `G_A` and `G_B` are bit-identical, similarity or equality cannot identify which branch is authoritative. The distinction lies in provenance and authority.

This gives a useful adversarial test:

> Create two exact copies of a valid qbin. Give only one a valid promotion/fencing event. A QMT implementation must not grant both authoritative-continuation status merely because their package hashes match.

## 74. Single Mutation Authority for Non-Mergeable Transitions

For non-mergeable identity-critical mutations, distributed systems provide useful mechanisms:

- epochs/terms;
- fencing tokens;
- quorum leases;
- single-writer ownership;
- consensus-ordered mutation logs.

QMT need not require one specific protocol. It requires evidence that the contract's branch policy is satisfied.

A stale writer whose lease expired can have perfectly valid local bytes and still be an invalid authoritative continuation.

## 75. Mergeable Versus Non-Mergeable Divergence

Not every branch is catastrophic. Some state may be CRDT-like or otherwise safely mergeable. QMT should distinguish:

```text
mergeable state divergence
```

from

```text
non-mergeable constitutional divergence
```

For mergeable application state, a later generation may reconcile both branches under a defined merge transform. For identity-critical events - key rotation, constitutional amendment, promotion authority, irreversible remediation - merge semantics may be forbidden.

The branch policy belongs in `Sigma`.

## 76. Fork Detection Is Not Fork Prevention

A continuity system may detect two valid descendant histories after the fact without having prevented them. Detection and prevention are different guarantees.

QMT should record whether the proof is based on:

- a prevention mechanism that makes conflicting authority impossible under stated fault assumptions;
- a detection mechanism that identifies equivocation;
- an administrative reconciliation rule;
- unresolved evidence.

## 77. Rollback and Stale Generation Attacks

An attacker may present an old but internally valid package. Checksums pass. Schemas pass. State may be admissible. Yet activating it can erase legitimate subsequent history.

QMT therefore needs freshness/lineage evidence:

\[
Tip(G_b)\succeq Tip_{accepted}
\]

under the chosen ordering or epoch rule, unless an explicitly authorized rollback transform exists.

Rollback is a transformation, not an invisible restore.

## 78. Ledger Truncation

A valid prefix of a hash chain is still a valid prefix. Hash validity alone cannot prove that no later events existed.

QMT must therefore distinguish:

```text
chain integrity
```

from

```text
tip freshness / completeness
```

This mirrors the Identity Event Ledger caveat in the Identity Architecture monograph.

## 79. Distribution Does Not Confer Cognitive Authority

Replica quorum can establish agreement on bytes or mutation order. It does not prove that the content is semantically true, constitutionally admissible, or continuous with a claimed entity.

Thus:

```text
consensus != cognitive authority
```

and

```text
replicated provenance != automatically valid provenance
```

---

# Part X - Schema, Model, Numerical, and Storage Transformations

## 80. Schema Migration

Schema evolution is a prototypical QMT transform because it changes representation while intending to preserve meaning.

Let old state schema be `S_v1`, new schema be `S_v2`, and migration `M_12`.

QMT should require:

\[
A_{v2}(M_{12}(r_{v1}))\sim_\Sigma T_{12}(A_{v1}(r_{v1})).
\]

The migration contract should identify fields that are:

```text
preserved exactly
renamed
retyped
split
merged
derived
dropped intentionally
unresolved
```

Silent dropping of an identity-relevant field is a continuity failure.

## 81. Model and Operator Upgrade

HTNLA model parameters and operator definitions can affect behavior even when HVD records are unchanged.

Therefore state closure may require:

- operator registry version;
- parameter digests;
- activation definitions;
- label schema;
- normalization conventions;
- model artifact/version;
- training/inference mode where relevant.

A qbin that restores records but uses a semantically different operator set may reproduce data without reproducing behavior.

## 82. Numeric Precision and Endianness

Cross-platform transforms can change dtype or byte order.

For an exact integer field, QMT may require value equality. For a floating field, it may require:

\[
\|x_b-T_X(x_a)\|\le\varepsilon.
\]

The tolerance must be field-aware. Using one global epsilon across heterogeneous state is usually unjustified.

A better structure is:

\[
\varepsilon=(\varepsilon_1,\ldots,\varepsilon_k)
\]

or a typed metric per logical component.

## 83. Quantization

Quantization is intentionally lossy. A continuity contract must declare whether quantization error is acceptable for each required observable.

If a controller threshold can flip under quantization noise, a small vector norm error may still cause a large behavioral discontinuity. QMT therefore needs both numeric and behavioral obligations where threshold-sensitive dynamics matter.

## 84. TMS Compaction and Reconsolidation

TMS compaction changes physical storage organization and may remove redundant versions. Most compaction should be a pre-certified realization transform, not a heavyweight full QMT ceremony on every SSTable merge.

However, compaction becomes continuity-sensitive when it might destroy:

- provenance required by THDE;
- identity-event history;
- rollback points required by policy;
- unresolved causal episode evidence;
- branch/fork evidence.

This suggests QMT **transformation classes**.

## 85. Transformation Classes

A production system can avoid verifying every routine operation from first principles by defining certified transform classes.

Example:

| Class | Example | QMT handling |
|---|---|---|
| R0 realization-preserving | page movement, cache eviction | covered by substrate invariant; audit sampling |
| R1 canonical re-encoding | compression, endian-safe serialization | deterministic transform proof + integrity |
| R2 schema-preserving migration | HDF5 layout/schema upgrade | explicit logical compatibility proof |
| R3 behavior-sensitive migration | runtime/model/operator upgrade | state + behavioral/refinement obligations |
| R4 lineage-sensitive failover | leader promotion, disaster recovery | full provenance/fork/authority obligations |
| R5 lossy transform | dimensional reduction, quantization | explicit distortion and invariant-survival contract |

This classification is **PROPOSED** but operationally important.

## 86. Physical Relocation Within TMS

Recall the realization function

\[
\rho_t(ID(D_i))=R_i(t).
\]

If `R_i(t)` changes from resident to device-backed or replicated while logical state and provenance remain inside a certified TMS transform class, the identity should not change.

QMT is the theory that justifies this separation; TMS is the subsystem that performs the movement.

## 87. HDF5 Persistence

HDF5 is durable long-term/permanent persistence in current architecture. Archive, snapshot, flush, and rehydration are mechanisms it supports, not the entirety of its conceptual role.

QMT treats an HDF5 generation as a durable continuity witness source when:

- schema/manifest are valid;
- required datasets are closed;
- provenance binds the generation to the active lineage;
- the generation is sufficiently fresh/authorized for the requested rebirth.

HDF5 does not declare its own identity authority.

---

# Part XI - Security and Threat Model

## 88. QMT Security Principle

Continuity verification is an adversarial problem because a successful forgery can make unauthorized state appear to be a legitimate continuation.

The security objective is not merely "the file opens." It is:

> An attacker should not be able to cause an invalid, stale, forked, tampered, semantically transformed, or unauthorized destination to receive a `PASS` continuity verdict under the stated threat model.

## 89. Package Corruption

Threat: bits change in transit or storage.

Current mitigation: qbin artifact digests and HDF5 validation.

Expected QMT result: `FAIL` when a mandatory commitment fails.

## 90. Package Tampering With Recomputed Digests

Threat: attacker changes payload and recomputes unsigned hashes.

Unsigned integrity cannot distinguish this from a freshly created package.

Mitigation requires authenticity/provenance trust, such as signatures or trusted attestation where the contract demands it.

This is why current qbin digest verification is not sufficient for QMT authenticity.

## 91. Rollback

Threat: present an old valid generation as current.

Mitigation:

- accepted-tip commitments;
- epochs;
- monotonic generation counters;
- transparency/log anchoring;
- policy-controlled rollback transforms.

## 92. Fork / Equivocation

Threat: two conflicting descendants claim authority.

Mitigation:

- consensus/fencing;
- non-equivocation witnesses;
- branch registry;
- fail-closed fork resolution.

## 93. Provenance Laundering

Threat: copy valid provenance references from one state onto another.

Mitigation: bind provenance evidence to exact source/destination content digests and transformation manifest. Evidence reuse after state mutation must fail.

This mirrors the candidate-content-digest rule already established in Identity Architecture Phase 3C.

## 94. Witness Rebinding and TOCTOU

Threat: QMT verifies one destination, but activation uses another.

Mitigation:

- assessment binds exact destination commitment;
- promotion atomically consumes the verified commitment;
- any mutation invalidates the certificate;
- verifier and promoter share an immutable evidence envelope.

## 95. Dependency Smuggling

Threat: a package appears complete but loads mutable or attacker-controlled external dependencies.

Mitigation:

- content-address required external artifacts;
- record mutable-service dependencies explicitly;
- distinguish trusted immutable reference from ambient path lookup;
- fail or remain unresolved if dependency identity cannot be established.

## 96. Interpreter / Runtime Substitution

Threat: state is intact but executed under a semantically incompatible runtime.

Mitigation: include runtime/ABI/model/operator identities in state closure where behavior depends on them.

## 97. Contract Downgrade

Threat: verify under an older/weaker continuity contract that omits current mandatory invariants.

Mitigation:

- contract version bound into transformation witness;
- minimum accepted contract version;
- explicit contract-migration authority;
- no silent fallback.

## 98. `identity_digest` Semantic Escalation

Threat: an operator treats the qbin field named `identity_digest` as proof of entity identity.

Mitigation: API/documentation must state that it is a package-content identity commitment, not QMT continuity or authenticity.

Potential future rename or typed wrapper could reduce misuse, but backward compatibility considerations apply.

## 99. Authorization Escalation

Threat: a successful continuity verdict silently restores credentials, capabilities, API tokens, or destructive privileges.

Mitigation: authorization remains downstream and separate.

The core invariant is:

\[
SameIdentity \not\Rightarrow Authorized.
\]

## 100. Secret Duplication

Threat: qbin copies a secret that should be unique to one host or hardware trust boundary.

Mitigation: store rebind metadata rather than raw secret where possible; rotate/reissue credentials after migration.

## 101. Cross-Tenant / Cross-Lineage Confusion

Threat: state from lineage A is restored into lineage B's namespace because schemas match.

Mitigation: stable lineage IDs, explicit source/destination generation binding, namespace isolation, and contract checks.

## 102. Malformed Archive Attacks

The current Nexus verification report explicitly says resistance to deliberately malformed snapshot archives beyond checksum/schema rejection is not established.

Future hardening should test:

- decompression bombs;
- oversized manifests;
- overlapping artifact ranges;
- integer overflow in lengths/offsets;
- duplicate names;
- pathological HDF5 objects;
- parser differentials;
- symlink/path traversal during extraction;
- resource exhaustion.

Current qbin code already checks manifest size, artifact overlap, bounds, duplicate names, and truncation - useful progress, not a complete hostile-parser proof.

---

# Part XII - Continuity, Authentication, Authorization, and Capability

## 103. Four Separate Predicates

QMT should formalize four distinct questions:

```text
Continuity(E_a,E_b)
Authentication(E_b)
Authorization(E_b, action)
CapabilityPossession(E_b, cap)
```

They are not equivalent.

A QMT PASS may establish the first under `Sigma`. Authentication may establish that the reconstructed runtime controls a trusted key. Authorization may still deny an operation. Capability possession may require explicit reissue.

## 104. Why This Separation Matters

Suppose a high-privilege autonomous agent migrates to a new host. If identity continuity automatically cloned every secret and privilege, an attacker who obtains a valid snapshot could acquire the full authority of the original.

A safer model is:

```text
QMT PASS
   |
   v
identity/lineage recognized
   |
   v
fresh authentication / attestation as required
   |
   v
policy re-evaluation
   |
   v
capability reissue / denial
```

## 105. Continuity Certificate

A future QMT implementation may emit a certificate-like result:

```text
assessment_id
lineage_id
source_generation
destination_generation
contract_digest
transformation_digest
evidence_root
verifier_version
result
issued_at
```

This object should be interpreted as:

> the verifier found the specified continuity obligations satisfied for these exact commitments.

It should not carry implicit privileges.

## 106. Certificate Invalidity After Mutation

If destination state changes after assessment, the certificate no longer applies unless the new mutation is itself covered by a continuity-preserving transform class.

A simple rule is:

\[
Digest(G_b')\neq Digest(G_b)
\Rightarrow
Cert(G_b)\text{ does not certify }G_b'.
\]

This prevents stale verification from authorizing changed state.

---

# Part XIII - Proposed QMT Software Contract

## 107. Design Goal

The implementation should be pure, evidence-driven, replayable, and non-actuating.

QMT evaluates. It does not mutate HVD state, change TMS realization, promote a branch, or grant capability. Those are downstream actions that consume a QMT verdict.

## 108. Proposed Core Types

The following Python-like interfaces are **PROPOSED**, not current source.

```python
from dataclasses import dataclass
from enum import Enum
from typing import Mapping, Sequence, Protocol


class ObligationState(str, Enum):
    SATISFIED = "SATISFIED"
    VIOLATED = "VIOLATED"
    UNRESOLVED = "UNRESOLVED"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class QMTResult(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    UNRESOLVED = "UNRESOLVED"


@dataclass(frozen=True)
class GenerationRef:
    lineage_id: str
    generation_id: str
    branch_id: str | None
    logical_state_digest: str
    realization_digest: str | None
    provenance_tip: str
    contract_digest: str


@dataclass(frozen=True)
class TransformationManifest:
    transform_id: str
    transform_type: str
    transform_version: str
    source: GenerationRef
    destination: GenerationRef
    logical_mapping_id: str
    distortion_contract_id: str | None
    authority_reference: str


@dataclass(frozen=True)
class ObligationAssessment:
    name: str
    state: ObligationState
    evidence_digest: str | None
    explanation: str


@dataclass(frozen=True)
class QMTAssessment:
    source: GenerationRef
    destination: GenerationRef
    transformation: TransformationManifest
    result: QMTResult
    obligations: tuple[ObligationAssessment, ...]
    evidence_root: str
```

## 109. ContinuityContract Interface

```python
class ContinuityContract(Protocol):
    contract_id: str
    version: str

    def required_obligations(self) -> Sequence[str]: ...
    def state_relation(self, source, destination) -> ObligationState: ...
    def invariant_checks(self, trajectory) -> Sequence[ObligationAssessment]: ...
    def branch_policy(self, trajectory) -> ObligationAssessment: ...
    def dependency_policy(self, witness) -> ObligationAssessment: ...
```

The contract must be versioned and immutable for a specific assessment.

## 110. QMTVerifier Interface

```python
class QMTVerifier(Protocol):
    def assess(
        self,
        contract: ContinuityContract,
        source: GenerationRef,
        destination: GenerationRef,
        trajectory,
        witness,
    ) -> QMTAssessment:
        ...
```

The verifier must not read mutable live state that is not bound into the witness unless the contract explicitly permits and records such evidence.

## 111. Deterministic Aggregation

Aggregation should be trivial and auditable:

```python
def aggregate(mandatory_states):
    if any(s == VIOLATED for s in mandatory_states):
        return FAIL
    if any(s == UNRESOLVED for s in mandatory_states):
        return UNRESOLVED
    return PASS
```

Complexity belongs in proof obligations, not in an opaque final score.

## 112. Evidence Root

All assessment evidence can be committed under a Merkle-style or canonical digest root:

\[
E_{root}=H(canon(E_1,\ldots,E_n)).
\]

The exact structure is implementation-specific. The value is that an assessment can be audited later against the exact evidence used.

## 113. No Ambient Authority

A verifier should receive transformation authority references as evidence. It should not silently consult whichever local user happens to run the process and declare the transform authorized.

This makes results portable and reproducible.

## 114. QMT and the Identity Event Ledger

For AmmunIty/Identity Architecture, the existing event ledger can supply continuity-relevant provenance. But QMT should not be hard-wired to one application-specific event schema.

A generic adapter can transform verified domain events into a QMT trajectory/witness.

This preserves the universal rule:

```text
ledger is evidence source;
QMT is continuity evaluator.
```

## 115. QMT and HIGC

QMT may consume a HIGC continuity-relevant result if the contract requires constitutional admissibility of the path. But QMT must not replace HIGC's own authority.

For example:

```text
HIGC says candidate OUTSIDE
QMT says migration faithfully preserved the candidate
```

Both can be true. The migration can preserve the identity of an unsafe state. Activation should still be denied by HIGC/policy.

## 116. QMT and THDE

THDE may supply path-dependent transition evidence. QMT can ask whether the transformation preserved the relevant THDE state/history. QMT should not recompute hysteresis policy as its own subsystem.

## 117. QMT and TMS

TMS supplies:

- active generation boundaries;
- trajectory records;
- physical realization metadata;
- COW lineage of extents where relevant;
- archive staging.

QMT decides whether a transformation over those objects satisfies continuity.

## 118. QMT and HDF5

HDF5 supplies durable state. QMT verifies whether the selected durable generation is the correct and complete source/destination evidence under the contract.

## 119. QMT and HVD

HVD supplies logical database identity and semantic state. QMT must resolve transformations in terms of HVD semantics rather than ANN index topology or file paths.

## 120. QMT and TUCR

TUCR may orchestrate substrate projection and runtime reconstruction. QMT verifies the resulting continuity obligations. TUCR cannot self-certify continuity merely because it performed the migration.

---

# Part XIV - Verification and Falsification Program

## 121. Current Evidence Baseline

The current Nexus/HVD corpus provides real but bounded continuity primitives.

### 121.1 Project Nexus v4 reference verification

Verified in the July 2026 environment:

- quinary dense/packed round trips;
- structural-vacuum/sign invariants;
- HTNLA binding contract;
- partial-inverse admissibility;
- deterministic k-WTA;
- controller bounds in tested paths;
- warm-memory reconstruction;
- snapshot save/restore;
- byte-identical seeded snapshot reproduction.

These results demonstrate deterministic persistence properties in the tested environment. The report explicitly does **not** establish consciousness, universal cross-platform determinism, production security, long-horizon stability, broad performance/scaling, or hostile archive resistance.

### 121.2 HVD 1.5 qbin

Implemented:

- `HVDQBIN1` parsing/writing;
- deterministic Protobuf manifest serialization;
- HDF5 archive validation/packaging;
- per-artifact BLAKE2b-256 integrity;
- identity/content commitment;
- artifact bounds/overlap checks;
- qbin inspection;
- qbin rebirth;
- HTNLA state restoration in tested paths.

Not implemented as a general engine:

- full continuity contract;
- signed continuity manifest;
- generic provenance closure across arbitrary migrations;
- distributed fork resolution;
- continuity proof composition;
- cross-platform semantic normalization proofs;
- authorization-safe activation gating through a QMT certificate.

## 122. Unit Tests

Minimum future tests include:

1. exact no-op transform passes;
2. byte-different canonical re-encoding passes logical equivalence;
3. required invariant loss fails;
4. missing mandatory dependency yields unresolved;
5. unknown schema fails or unresolved by explicit policy;
6. corrupted qbin payload fails;
7. recomputed unsigned digests do not satisfy authenticity-required contract;
8. valid package with stale generation fails freshness policy;
9. unsupported contract downgrade fails;
10. QMT never mutates source/destination state.

## 123. Branch/Fork Tests

1. Two identical descendants, one authoritative promotion -> only promoted branch passes authoritative-continuation obligation.
2. Two descendants both claim same fencing epoch -> fail or unresolved under split-brain policy.
3. Replica copies without mutation authority remain replicas, not new identities.
4. Mergeable state branches reconcile only through registered merge transform.
5. Non-mergeable constitutional branches cannot be auto-merged.

## 124. Metamorphic Tests

Metamorphic testing is especially useful because QMT concerns transformations.

Examples:

- reorder physically independent HDF5 chunks -> continuity unchanged;
- rebuild ANN graph -> continuity unchanged;
- change file path -> continuity unchanged;
- alter logical label semantics without updating contract -> continuity fails;
- add irrelevant metadata -> continuity unchanged;
- mutate required state while preserving high ANN similarity -> continuity fails.

## 125. Composition Tests

Construct transform chains with known local bounds:

\[
T_1,T_2,\ldots,T_n.
\]

Verify:

- provenance joins exactly;
- composed error bound is respected;
- contract version changes are explicit;
- local PASS cannot hide an incompatible intermediate contract;
- closed-loop drift stays within declared holonomy tolerance where applicable.

## 126. Cross-Platform Tests

At minimum:

- little-endian vs big-endian canonicalization;
- Python/NumPy/library version changes;
- CPU architecture differences;
- BLAS implementation differences;
- float precision changes;
- deterministic Protobuf behavior;
- HDF5 version compatibility;
- device-resident reconstruction.

The goal is not necessarily byte identity. The goal is contract-defined logical and behavioral continuity.

## 127. Chaos and Distributed Tests

Inject:

- node failure during migration;
- leader failover;
- network partition;
- stale replica promotion attempt;
- simultaneous branch creation;
- delayed provenance event;
- partial qbin transfer;
- object-store reference unavailability.

QMT must fail closed or remain unresolved according to policy.

## 128. Security Mutation Tests

Mutate one field at a time:

```text
lineage_id
contract_digest
source_generation
artifact digest
transform version
runtime digest
provenance tip
branch epoch
required dependency
```

Each mutation should produce the expected obligation failure and never accidentally fall through to PASS.

## 129. Falsification Criteria

The QMT thesis would be materially weakened if any of the following hold:

- continuity cannot be defined without freezing physical representation;
- transformations routinely require circularly assuming the identity they are supposed to verify;
- branch ambiguity cannot be represented or failed closed;
- contract composition cannot prevent semantic downgrades;
- required state closure cannot be specified for real Nexus runtimes;
- approximate transforms accumulate unbounded semantic drift despite local passes;
- proofs cannot be bound to the exact state that is later activated.

These are engineering falsifiers, not rhetorical caveats.

---

# Part XV - Research Agenda

## 130. Formal Composition Theorem

The highest-value mathematical task is to prove a composition theorem for a restricted class of continuity contracts.

Research questions:

- Under what conditions is `->_Sigma` transitive?
- How do invariant sets transform across schema versions?
- How should approximate error budgets compose?
- Can proof-carrying transformations expose machine-checkable composition interfaces?

## 131. Minimal Sufficient Continuity Closure

What is the smallest witness set sufficient to establish continuity for a given class of agent?

Too little state creates false passes. Too much state makes migration impractical and may copy secrets unnecessarily.

This can be framed as a dependency/minimality problem over the continuity contract.

## 132. Proof-Carrying qbin

A future `.qbin` could carry not only state and a manifest but proof artifacts:

```text
schema proof
migration proof
invariant certificate
provenance proof
behavioral conformance evidence
attestation chain
```

QMT would verify these artifacts rather than rerunning every expensive proof.

This is a research direction, not current behavior.

## 133. Content-Addressed Continuity DAG

A long-lived lineage could use immutable content-addressed generations with explicit transform edges.

```text
G0 --T1--> G1 --T2--> G2
              \
               \--T3--> G2b
```

QMT then becomes a verifier over a provenance DAG plus contract rules.

This naturally exposes forks rather than hiding them.

## 134. Confidential Migration

Continuity proofs may need to operate without exposing all state.

Research directions include:

- trusted execution environments;
- remote attestation;
- selective disclosure;
- zero-knowledge proofs of limited invariants;
- encrypted content-addressed artifacts.

No claim is made that a general zero-knowledge QMT exists.

## 135. Approximate and Lossy Continuity

The hardest practical question is what happens when no exact migration exists.

A useful theory must distinguish:

- harmless representational loss;
- recoverable approximation;
- loss of non-required detail;
- loss of identity-relevant state;
- epistemically unknown loss.

A global score is inadequate. Typed per-invariant distortion contracts are more promising.

## 136. Continuity Under Learning During Migration

If the source continues learning while migration is in progress, the destination can become stale.

Possible approaches:

- quiescence;
- pre-copy plus dirty-state replay;
- write fencing;
- event catch-up;
- dual-run with a final authority cutover.

QMT must define the exact cutover generation and avoid two writable authorities.

## 137. Long-Lived Contract Evolution

A system operating for decades cannot assume one continuity constitution forever.

Research is needed on:

- authorized constitutional amendments;
- backward compatibility;
- invariant deprecation;
- migration of the continuity contract itself;
- historical interpretation of old generations under old schemas.

The contract's history must not become an excuse for silently rewriting identity.

## 138. QMT and Ephemeral HVD Promotion

Ephemeral counterfactual HVDs should not receive durable continuity merely because they existed in an HTCE thought field.

A future promotion flow may be:

```text
ephemeral candidate
   -> selected
   -> HIGC / THDE admissibility
   -> external promotion authority
   -> durable identity/generation assignment
   -> QMT establishes post-promotion continuity from the authorized source relation
```

The candidate cannot self-declare permanence.

---

# Part XVI - Human Identity and Phenomenal Continuity: Explicit Boundary Appendix

## 139. Why This Appendix Exists

Historical Nexus material sometimes treated `.qbin`, QHRF, hardware replacement, and continuity as though successful software state transfer would establish human-style or phenomenal identity. The deep research performed for this rewrite rejects that inference.

The boundary is part of QMT's rigor.

## 140. Five Separate Human Questions

A Chalmers-inspired decomposition separates:

1. behavioral continuity;
2. memory/psychological continuity;
3. consciousness;
4. numerical personal identity;
5. survival value or "as good as survival."

QMT directly addresses only formal/software analogues of the first two and architectural lineage under a stipulated software identity constitution.

| Question | Formalizable? | Empirically measurable now? | QMT authority |
|---|---:|---:|---|
| Software behavior | yes, relative to domain | yes | direct |
| Software memory/state | yes | yes | direct |
| Human psychological continuity | partial | partial | analogy only |
| Consciousness | no accepted theory-neutral criterion | no accepted direct measure | none |
| Human numerical identity | philosophically disputed | no direct measure | none |
| Survival value | normative | not a physical measurement | none |

## 141. Parfit and Branching

Parfit's fission cases are useful because they expose a structural fact QMT already encounters: one-to-many psychological or informational continuity is compatible with the failure of ordinary one-to-one numerical identity.

For software, Nexus can define an authoritative-continuation policy. That is an engineering convention over a lineage. It does not settle the metaphysics of persons.

## 142. Chalmers and Organizational Invariance

Chalmers's fading/dancing-qualia arguments provide a philosophical case for organizational invariance, but they are arguments, not a QMT theorem. Even if a functional isomorph is conscious, that does not automatically establish that it is numerically the same person as the source.

## 143. Gradual Replacement Versus Scan-and-Copy

QMT's path-based structure maps more naturally onto gradual transformation because a sequence of local transformations can preserve an explicitly verified trajectory.

But this is a structural analogy only. It does not prove phenomenal survival under gradual neural replacement, and the literature contains objections to privileging gradual replacement.

## 144. Whole-Brain Emulation State of the Field

The 2008 Sandberg-Bostrom roadmap and 2025 state-of-field research frame WBE as several distinct problems: structural capture, dynamic recording, model inference, simulation, and embodiment.

Current research has made major progress in connectomics and large-scale recordings, but no demonstrated system captures and emulates a complete human brain at a fidelity known to preserve all functionally relevant properties. The biological detail required for faithful emulation remains unresolved.

QMT therefore has no present human substrate-transfer object to certify.

## 145. Brillouin Microscopy

Brillouin microscopy measures high-frequency mechanical/viscoelastic properties of biological materials through Brillouin light scattering. It has legitimate biomedical uses.

No established scientific evidence connects its measurements to personal identity, autobiographical memory, or phenomenal continuity.

## 146. NV-Diamond Magnetometry

NV-diamond magnetometry measures magnetic fields via nitrogen-vacancy spin physics and has demonstrated biomagnetic sensing including action-potential-related signals in constrained experimental contexts.

No established scientific evidence makes it an identity, memory-content, or consciousness detector.

The inferential chain

\[
magnetic\ field
\Rightarrow cognition
\Rightarrow identity
\]

is invalid without separate validated models for each arrow.

## 147. QHRF

Historical QHRF material combined real sensing modalities into a proposed latent identity/continuity observable.

The deep-research audit found no validated likelihood model connecting Brillouin/NV measurements to an identity-preservation hypothesis. Therefore a Bayesian posterior such as

\[
P(identity\ preserved\mid measurement)
\]

has no empirical meaning unless a justified model for

\[
P(measurement\mid identity\ preserved)
\]

and relevant alternatives exists.

QHRF is therefore **HISTORICAL / SPECULATIVE** as an identity observable.

## 148. Explicitly Rejected Historical Material

The QMT paper does not preserve or reconstruct:

- numeric thresholds authorizing destructive human transfer;
- `authorized_to_proceed` logic for irreversible acts;
- IRB/consent templates for identity transfer;
- instrument procurement/calibration plans for such transfer;
- composite scalar identity-fidelity gates;
- claims that qbin checksum success proves consciousness survival.

Their removal is an epistemic correction, not a claim that philosophical discussion of identity is forbidden.

## 149. The Boundary Law

The strongest defensible statement is:

```text
QMT PASS
=> accepted digital continuity under a declared software contract
```

It does **not** imply:

```text
same human person
same first-person subject
consciousness preserved
immortality achieved
```

---

# Part XVII - Claim-Status Audit

## 150. Current Status Matrix

| Claim / mechanism | Status | Evidence boundary |
|---|---|---|
| QMT means qbin Morphism Theory | **CANONICAL** | Nexus monograph + HVD recursive architecture |
| QMT owns continuity across transformation | **CANONICAL** | current responsibility model |
| QMT is distinct from HIGC/THDE | **CANONICAL** | current architecture |
| TMS realization may change without logical identity change | **CANONICAL** | current HVD/TMS model |
| HDF5 is durable long-term/permanent persistence | **CANONICAL** | current architecture |
| qbin packages canonical HDF5 archive | **IMPLEMENTED** | HVD 1.5 source |
| HVDQBIN1 + Protobuf manifest | **IMPLEMENTED** | `hvd/qbin.py` |
| per-artifact BLAKE2b-256 integrity | **IMPLEMENTED** | `hvd/qbin.py` |
| qbin integrity is not authenticity | **CANONICAL / IMPLEMENTED boundary** | source code comment + behavior |
| qbin rebirth | **IMPLEMENTED** | runtime + tests |
| HTNLA operator state restored in tested qbin path | **VERIFIED** | HVD tests |
| Nexus reference snapshot save/restore | **VERIFIED** | 2026-07-20 verification report |
| seeded reference snapshot byte determinism in tested environment | **VERIFIED** | verification report |
| general cross-platform byte determinism | **NOT ESTABLISHED** | report explicitly disclaims |
| full QMT contract engine | **PROPOSED** | this formalization / architecture role |
| PASS/FAIL/UNRESOLVED QMT aggregate | **INFERRED / PROPOSED** | synthesized from formal continuity research |
| continuity composition theorem | **RESEARCH HYPOTHESIS** | conditions proposed, proof absent |
| identity holonomy as loop-consistency diagnostic | **INFERRED** | conservative formalization of canonical term |
| signed QMT continuity manifests | **PROPOSED** | not in current qbin v1 |
| distributed fork/fencing integration | **PROPOSED** | architecture research |
| scalar identity continuity score | **REJECTED** | non-compensatory authority model |
| `identity_digest` proves constitutional identity | **REJECTED** | current digest is content-derived |
| ANN similarity proves continuity | **REJECTED** | canonical authority separation |
| QHRF establishes personal identity | **HISTORICAL / SPECULATIVE** | no validated measurement model found |
| qbin restore proves consciousness preservation | **REJECTED** | category error; verification report disclaims |
| human phenomenal continuity through substrate replacement | **NOT ESTABLISHED** | philosophy/neuroscience boundary |

---

# Part XVIII - QMT Engineering Laws

## 151. Twenty-Five Canonical / Proposed Laws

1. **QMT means qbin Morphism Theory.**
2. **QMT evaluates continuity across transformation; it does not own serialization.**
3. **Logical identity is not physical realization.**
4. **Byte equality is neither necessary nor sufficient for continuity.**
5. **Serialization completeness is not functional reproducibility.**
6. **Functional reproducibility is not architectural identity continuity.**
7. **Similarity is evidence, never identity authority.**
8. **Continuity is evaluated over a trajectory, not only endpoints.**
9. **Continuity is contract-relative.**
10. **A continuity contract must be versioned.**
11. **Mandatory proof obligations are non-compensatory.**
12. **A mandatory violation yields FAIL.**
13. **Missing mandatory evidence yields UNRESOLVED.**
14. **Zero is not a synonym for unavailable.**
15. **Provenance integrity does not prove event truth or tip freshness.**
16. **Replica count is not identity count.**
17. **State equivalence does not resolve a fork.**
18. **Non-mergeable identity-critical mutations require unique mutation authority under the contract.**
19. **Continuity need not be symmetric.**
20. **Composition of local continuity proofs is conditional, not automatic.**
21. **Approximation error must compose under an explicit budget.**
22. **The qbin `identity_digest` is not a constitutional identity certificate.**
23. **A QMT PASS does not grant authorization or capabilities.**
24. **System Rebirth must verify continuity before authoritative activation.**
25. **Software continuity does not establish human phenomenal continuity.**

---

# Part XIX - Expert Field Checklist

## 152. Before Declaring a Transform Continuity-Preserving

Ask:

- What exact lineage is being continued?
- What is the source generation?
- What is the destination generation?
- What continuity contract/version applies?
- What is the actual realized transform?
- What logical transform is declared?
- Do the abstraction/transform paths commute?
- Which invariants are mandatory?
- Are any path invariants different from endpoint invariants?
- Is the dependency closure complete?
- Does replay require nondeterministic input capture?
- Is the destination behaviorally tested or formally proved, and at what strength?
- Is provenance complete?
- Is the tip fresh?
- Is a competing branch possible?
- Is the branch authoritative?
- Are errors bounded and composable?
- Is any required evidence unresolved?
- Is the evidence bound to the exact destination to be activated?
- Are authentication and authorization separately resolved?

If any mandatory answer is "unknown," the continuity verdict should not be `PASS`.

---

# Appendix A - Compact Mathematical Reference

## A.1 Generation

\[
G=(L,g,S,C,D,P,\Pi).
\]

## A.2 Abstraction maps

\[
A_a:\mathcal R_a\rightarrow\mathcal X_a,
\qquad
A_b:\mathcal R_b\rightarrow\mathcal X_b.
\]

## A.3 Realized and logical transforms

\[
T_R:\mathcal R_a\rightarrow\mathcal R_b,
\qquad
T_X:\mathcal X_a\rightarrow\mathcal X_b.
\]

## A.4 Basic commutation

\[
A_b(T_R(r))\approx_\Sigma T_X(A_a(r)).
\]

## A.5 Commutation defect

\[
\delta_T(r)=d_X(A_b(T_R(r)),T_X(A_a(r))).
\]

## A.6 Operation preservation

\[
T_X(f_a(x))\approx_\Sigma f_b(T_X(x)).
\]

## A.7 Directed continuity

\[
G_a\rightarrow_\Sigma G_b.
\]

## A.8 QMT result

\[
QMT_\Sigma(G_a,G_b,\tau,W)\in\{PASS,FAIL,UNRESOLVED\}.
\]

## A.9 Conditional error composition

\[
\delta_{2\circ1}\le L_2\varepsilon_1+\varepsilon_2.
\]

## A.10 Loop defect / identity-holonomy diagnostic

\[
h_\Sigma(r)=d_X(A_0(T_{loop}(r)),A_0(r)).
\]

## A.11 Core non-equivalences

\[
serialization\ completeness\not\equiv functional\ reproducibility,
\]

\[
functional\ reproducibility\not\equiv architectural\ identity\ continuity,
\]

\[
software\ continuity\not\Rightarrow phenomenal\ continuity.
\]

---

# Appendix B - ASCII Reference

```text
QMT = qbin Morphism Theory

source realization r_a
        |
        | A_a
        v
source logical state x_a
        |
        | T_X
        v
expected destination logical state

source realization r_a
        |
        | T_R
        v
destination realization r_b
        |
        | A_b
        v
observed destination logical state

QMT asks whether the two destination logical states agree
under the continuity contract Sigma.
```

```text
QMT_Sigma(G_a, G_b, tau, W)

mandatory violation present  -> FAIL
else mandatory evidence absent -> UNRESOLVED
else                           -> PASS
```

```text
HVD  -> logical database identity/state
TMS  -> live physical realization + trajectory
HDF5 -> durable long-term/permanent persistence
qbin -> portable package/manifest
QMT  -> continuity verification across transformation
```

```text
same identity != authorization
replica count != identity count
similarity != continuity
integrity != authenticity
restore != rebirth acceptance
```

---

# Appendix C - Historical Corrections Register

| Historical formulation | Current treatment |
|---|---|
| QMT expanded as Quantum Mechanical Transformation / other generated variants | **SUPERSEDED**; canonical expansion is qbin Morphism Theory |
| `.qbin` is the mind/consciousness itself | **REJECTED**; qbin is a state package |
| checksum proves unbroken consciousness | **REJECTED**; checksum proves bounded integrity property |
| 21 checkpoint fields are mathematically perfect | **REJECTED**; useful historical state-closure brainstorming only |
| arbitrary substrate migration is seamless | **RESEARCH HYPOTHESIS / unsupported** |
| Johnson-Lindenstrauss alone guarantees semantic continuity | **REJECTED**; distance preservation is conditional and limited |
| one continuity-fidelity scalar can gate identity | **REJECTED** |
| QHRF measurement provides identity posterior | **HISTORICAL / SPECULATIVE** absent validated likelihood model |
| HDF5 is merely snapshot/restore storage | **SUPERSEDED framing**; HDF5 is durable long-term/permanent persistence, with snapshot/archive/rehydration as mechanisms |
| ANN agreement establishes identity | **REJECTED** |

---

# Appendix D - Implementation Status by Layer

| Layer | Present capability | QMT relevance | Gap |
|---|---|---|---|
| Nexus demonstrator | deterministic bounded snapshot/restore in tested environment | proves persistence primitives | not general QMT |
| HVD 1.5 HDF5 | validated durable archive/rebirth path | durable source/destination generations | continuity contract absent |
| HVDQBIN1 | streaming package + manifest + digests | portable continuity artifact carrier | no general signature/continuity proof |
| HTLA/HTNLA persistence | operator state carried in HDF5/qbin path | semantic/runtime closure | cross-version proof needed |
| Identity Event Ledger | hash-chained domain biography | provenance source | application-specific, fork/freshness limits |
| HIGC | constitutional admissibility | may supply path constraints | not QMT |
| THDE | bounded/path-dependent evolution | may supply trajectory evidence | not QMT |
| QMT | canonical owner assigned | formal target | full engine not implemented |

---

# Appendix E - Selected References and Source Concordance

## E.1 Current Nexus / HVD sources

- **Project Nexus 4: Canonical Architecture, Cognitive Runtime, and Engineering Field Guide.** Canonical Technical Monograph, 2026. Section 26 and glossary establish QMT as **qbin Morphism Theory**, define the commuting-transformation concept, and explicitly leave the final QMT metric as research.
- **Identity Architecture: Constitutional Continuity, Admissible Evolution, and Event-Sourced Selfhood.** Canonical Technical Monograph, 2026. Establishes directed continuity, System Rebirth ordering, provenance/ledger semantics, and `SameIdentity != Authorized`.
- **HVD Recursive Cognitive Architecture.** 2026. Assigns QMT continuity/identity-holonomy responsibility and separates it from HDF5 serialization.
- **HVD 1.5 Architecture.** Current repository documentation. Defines TMS/HDF5/qbin packaging/rebirth responsibilities.
- **`hvd/qbin.py`.** `mjsmorgan/hyperdimensional_vector_database`, inspected at commit `b4b5fdcf19d273c49ced8d0d924cb8e6913f5d98`. Implements HVDQBIN1, Protobuf manifest, artifact integrity, package inspection, and HDF5 packaging.
- **Project Nexus v4.0 Verification Report.** 2026-07-20. Executed property-test evidence for the bounded reference runtime and its explicit limitations.
- **`consciousness.qbun file format notes`.** Historical Nexus checkpoint-state notes. Retained only as design lineage; metaphysical claims superseded.
- **Architectural Resilience and Cognitive State Persistence in N-Dimensional Systems.** Historical/research synthesis. Useful for identifying migration/state-closure questions; speculative continuity claims superseded.

## E.2 Formal methods and systems

- Abadi, M., and Lamport, L. (1991). **The Existence of Refinement Mappings.** *Theoretical Computer Science* 82(2), 253-284. Relevant to relating changed concrete implementations to preserved abstract behavior.
- Hennessy, M., and Milner, R. (1985). **Algebraic Laws for Nondeterminism and Concurrency.** *Journal of the ACM* 32(1), 137-161. Foundational context for observational/process equivalence.
- Dunlap, G. W., King, S. T., Cinar, S., Basrai, M. A., and Chen, P. M. (2002). **ReVirt: Enabling Intrusion Analysis through Virtual-Machine Logging and Replay.** OSDI. Relevant to recording nondeterministic events for replay.
- Clark, C., Fraser, K., Hand, S., Hansen, J. G., Jul, E., Limpach, C., Pratt, I., and Warfield, A. (2005). **Live Migration of Virtual Machines.** NSDI. Relevant to coherent migration across hosts.
- Ansel, J., Arya, K., and Cooperman, G. DMTCP checkpoint/restart work (2007-2009). Relevant to distributed process-state closure and transparent restart.
- Ongaro, D., and Ousterhout, J. (2014). **In Search of an Understandable Consensus Algorithm (Raft).** USENIX ATC. Relevant to epochs/terms and authoritative mutation ordering as an engineering analogue for fork control.
- W3C (2013). **PROV-DM / PROV-O family of provenance recommendations.** Relevant to explicit entities, activities, agents, and derivation relations.
- The HDF Group. **HDF5 Data Model and Datatype Documentation.** Relevant to durable typed storage while illustrating that file format does not determine application identity semantics.

## E.3 Human-boundary sources

- Parfit, D. (1984). **Reasons and Persons.** Oxford University Press. Branching, psychological continuity, and the claim that identity may not be what matters.
- Chalmers, D. J. (1995). **Absent Qualia, Fading Qualia, Dancing Qualia.** In *Conscious Experience*.
- Chalmers, D. J. (2010/2014). **The Singularity: A Philosophical Analysis** and **Mind Uploading: A Philosophical Analysis.** Used only for the human philosophical boundary.
- Bourget, D., and Chalmers, D. J. (2023). **Philosophers on Philosophy: The 2020 PhilPapers Survey.** Evidence of persistent expert disagreement, not an authority vote.
- Sandberg, A., and Bostrom, N. (2008). **Whole Brain Emulation: A Roadmap.** Future of Humanity Institute, Oxford.
- Zanichelli, N., Schons, M., Freeman, I., Shiu, P., and Arkhipov, A. (2025). **State of Brain Emulation Report 2025.** arXiv:2510.15745.
- Shapson-Coe, A., et al. (2024). **A Petavoxel Fragment of Human Cerebral Cortex Reconstructed at Nanoscale Resolution.** *Science* 384, eadk4858.
- Barry, J. F., et al. (2016). **Optical Magnetic Detection of Single-Neuron Action Potentials Using Quantum Defects in Diamond.** *PNAS* 113(49), 14133-14138.
- Kabakova, I., et al. (2024). **Brillouin Microscopy.** *Nature Reviews Methods Primers* 4:8.
- Bouvet, P., et al. (2025). **Consensus Statement on Brillouin Light Scattering Microscopy of Biological Materials.** *Nature Photonics* 19, 681-691.

---

# Conclusion

QMT's proper contribution is neither mystical nor trivial.

It is not mystical because a `.qbin` package is not a soul, a checksum is not consciousness, and no scalar can turn storage fidelity into human identity. It is not trivial because ordinary backup and restore do not answer the harder engineering question of whether a destination is an authorized continuation of a particular logical entity through representation change, schema evolution, process restart, durable rehydration, physical relocation, or distributed failover.

The mature QMT problem is therefore:

> Given a source generation, a destination generation, a transformation trajectory, a versioned continuity contract, and a bound evidence witness, determine whether the structures named by the contract commute across the transformation, whether required invariants and dependencies survive, whether the provenance chain is valid and fresh, whether branch status is resolved, and whether any mandatory evidence remains unknown.

The answer is typed:

```text
PASS
FAIL
UNRESOLVED
```

not a seductive confidence number.

This formulation makes QMT a genuine sibling to HTLA and HTNLA. HTLA specifies typed linear structure. HTNLA specifies typed nonlinear transformations and their information-loss contracts. QMT asks whether the structures that matter for continuity survive transformations of representation and realization over time.

The canonical mental model is:

```text
HIGC asks: is the state admissible?
THDE asks: how may the state evolve given history?
QMT asks: after transformation, is this still the accepted continuation?
```

QMT is thus best understood as **contract-relative diachronic verification**: a morphism discipline over logical state, realization, provenance, and authority boundaries. The current Nexus and HVD codebase already provides meaningful pieces - durable generations, qbin packaging, integrity checks, rebirth, deterministic bounded snapshot tests, event-sourced identity evidence - but the general QMT verifier remains an active formalization and engineering target.

That status is not a weakness. It is precisely what makes the next implementation phase testable.
