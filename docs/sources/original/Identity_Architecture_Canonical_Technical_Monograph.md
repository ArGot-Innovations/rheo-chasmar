# IDENTITY ARCHITECTURE
## Constitutional Continuity, Admissible Evolution, and Event-Sourced Selfhood
### Canonical Technical Monograph and Engineering Field Guide

**Reference edition:** 2026-08-31  
**Implementation checkpoint:** `ArGot-Innovations/ammunIty@b12eaedc246d872db7f3018fbd1e8fa99083f5ce`  
**Scope:** Identity Architecture as a general Nexus-derived architecture, with AmmunIty as the current executable reference profile and the historical Educated Bookseller architecture as an application lineage.  
**Purpose:** A technically rigorous, mathematically explicit, source-reconciled reference for designing persistent machine identity without confusing identity with state, memory, similarity, roleplay, storage placement, or historical biography.

---

## Abstract

Identity Architecture addresses a problem that ordinary agent systems usually leave implicit: what does it mean for a software organism to remain the same entity while its state, memory, physical placement, knowledge, policies, relationships, and even internal realization change? A language model can imitate a persona, a vector database can retrieve semantically similar memories, a snapshot can preserve bytes, and an event log can preserve biography; none of those operations alone establishes identity. The architecture therefore treats identity as a constitutional and temporal systems property governed by explicit authority boundaries.

The canonical construction begins with an explicitly established constitutional baseline, written as \(G_0\). \(G_0\) is not a learned average of whatever the system happened to observe and is never silently inferred from a clean run. It identifies protected invariants, domain scope, provenance anchors, and the initial conditions against which later change can be interpreted. Around that baseline, HIGC - the HSL Invariant Geometry Calculus - defines an admissible set of states and transitions. THDE - the Temporal Homeostatic Dynamics Engine - owns bounded, path-dependent evolution and candidate transition semantics. QMT owns continuity across transformation, migration, rehydration, or representational remapping. TMS - the Transdimensional Memory Substrate - owns active state realization, trajectory, copy-on-write sharing, and replayable materialization. HVD retains database semantics and associative memory without becoming identity authority. HDF5 supplies durable long-term/permanent persistence rather than live constitutional judgment.

The current AmmunIty implementation makes a meaningful subset of this architecture executable. Its Phase 1 identity layer implements an immutable \(G_0\), a deterministic identity-state vocabulary and adjudicator, and an append-only SHA-256 hash-chained Identity Event Ledger. Phase 3A materializes the verified ledger into a rebuildable active-TMS view without turning that mutable projection into truth. Phase 3B implements a symbolic HIGC profile with seven independently auditable constraints and four aggregate geometry states: `ADMISSIBLE`, `BOUNDARY`, `OUTSIDE`, and `UNRESOLVED`. Phase 3C introduces immutable THDE candidate states, exact provenance references, candidate-content digests, explicit hypothetical evidence, full trajectory verification, candidate-specific HIGC evaluation, and a deterministic non-actuating transition gate. Every Phase 3C evaluation explicitly preserves `host_mutation_authorized = false`.

This produces a central distinction:

\[
\boxed{\text{identity} \neq \text{state} \neq \text{history} \neq \text{memory} \neq \text{location} \neq \text{relationship}}.
\]

History matters because identity is temporal, but history is not identity. Memory matters because continuity must be reconstructed, but memory is not constitutional authority. State matters because identity is expressed through state, but snapshot equality is neither necessary nor sufficient for sameness. Relationship matters because entities exist in changing fields, but a relationship edge must not become an immutable identity attribute merely because it once existed. Physical placement matters for realization, yet moving an HVD, replaying an active TMS view, or rehydrating from durable persistence should not create a new entity when QMT continuity conditions are satisfied.

The monograph formalizes these separations. It models the constitutional admissible region as an intersection of named constraints; expresses current HIGC aggregation as a non-compensatory logic rather than a scalar risk score; models biography as a cryptographically linked event trajectory; treats active-TMS identity memory as a replay function of verified history; binds hypothetical THDE evidence to the exact candidate content through a digest; and distinguishes admissibility, evolution, causal prediction error, persistence, and actuation. It also corrects several historical ambiguities: older application papers used continuous Cyrae ODEs where the current Phase 5 architecture specifies a discrete bounded recurrence; older writing sometimes treated RPE as available from ordinary state differences, whereas current architecture requires pre-action prediction binding and temporal causality; and some documents described HDF5 too narrowly as snapshot/archive machinery, whereas current Nexus architecture defines it more broadly as durable long-term/permanent persistence.

The result is not a claim that machine identity, consciousness, or phenomenal selfhood has been solved. It is a falsifiable engineering theory for preserving constitutional continuity under change. It specifies what can be tested now, what remains architectural direction, and what evidence would be required before stronger claims are justified.

# Reader's Guide and Claim-Status Legend

Identity Architecture has evolved through research papers, application designs, implementation sprints, source code, and Nexus-wide architecture corrections. This document therefore labels claims by epistemic and engineering status rather than flattening every historical statement into a single apparent truth.

| Status | Meaning |
|---|---|
| **CANONICAL** | Current binding architectural intent after resolving conflicts among sources. |
| **IMPLEMENTED** | Present in inspected executable source code at the implementation checkpoint. |
| **VERIFIED** | Supported by explicit regression requirements, executed verification evidence, or a reproducible implementation artifact. |
| **PARTIALLY IMPLEMENTED** | A bounded subset exists, but the full intended authority or runtime mechanism does not. |
| **ACTIVE DEVELOPMENT** | Current handoff or immediate implementation direction. |
| **PROPOSED** | Architecturally specified but not yet implemented. |
| **RESEARCH HYPOTHESIS** | Requires empirical, formal, or longitudinal validation. |
| **APPLICATION-SPECIFIC** | Belongs to AmmunIty, the Educated Bookseller, Key Vault, or another embodiment rather than universal Identity Architecture. |
| **HISTORICAL / SUPERSEDED** | Useful lineage, but replaced by newer architecture. |
| **INFERRED** | A formalization or consequence synthesized here from current contracts; not necessarily a source-level name. |

The document uses **constitutional** in an engineering sense: a set of protected invariants, authority boundaries, and admissibility conditions. It does not imply a legal constitution. Similarly, biological vocabulary such as dopamine, serotonin, immune response, homeostasis, and organism is used as computational analogy unless a section explicitly states otherwise.

A recurring reading rule is: **do not promote a derived view into an authority layer merely because it is convenient to query**. A TMS materialization may be faster than replaying a ledger, but that does not make it the continuity source of truth. An HVD neighbor may be similar to known malware, but that does not make similarity a constitutional verdict. A Cyrae coordinate may be numerically high, but that does not authorize remediation. An `ADMISSIBLE` THDE candidate is eligible for further reasoning, not automatically executable.

# Source Hierarchy and Reconciliation Rules

The source corpus contains an important historical split. The August 15 master paper, *Identity Architecture: Emergent Tradecraft, Continuous Affective Controllers, and Event-Sourced Ledgers in Edge-Native Organisms*, is the conceptual seed. It introduced persistent tradecraft, professional ego, event-sourced biography, quinary cognition, and a digital-organism model. However, it is application-heavy and predates several architectural corrections. The current executable AmmunIty identity subsystem and newer Nexus/HVD/Cyrae architecture therefore outrank it where they conflict.

The working hierarchy used here is:

**Tier 0 - current Nexus and identity architecture contracts.** Current HVD/Nexus master architecture, recursive HVD architecture, current TMS/HDF5 responsibility boundaries, and the newest Cyrae-lite Phase 5 architecture define cross-system ownership and terminology.

**Tier 1 - current executable identity implementation.** `ammunity/identity/` at commit `b12eaed...`, together with `identity_phase1.md`, `higc_phase3b.md`, and `thde_phase3c.md`, establishes the strongest evidence for what Identity Architecture currently does in software.

**Tier 2 - current application architecture.** AmmunIty pathology/HVD integration specifies how neutral observations, associative pathology memory, identity adjudication, HIGC, and active TMS are wired in a concrete system.

**Tier 3 - historical Identity Architecture application papers.** Educated Bookseller, bookstore UI/financial-governance research, and the August 15 master paper explain why persistent trade identity was proposed and supply domain examples. They are not allowed to universalize bookstore economics, autonomous corporate behavior, or old controller equations into the core architecture.

**Tier 4 - derivative reviews and architecture indexes.** Generated architecture matrices and comparative reports are useful as coverage maps and criticism, not as final authority.

Conflict resolution follows five rules:

1. Newer explicit authority boundaries override older descriptive shortcuts.
2. Executable source establishes implementation status but does not automatically redefine the long-term architecture.
3. A general Nexus contract outranks an application-specific convenience when the two concern shared infrastructure.
4. Missing implementation is not silently treated as implemented because the research paper describes it.
5. Historical ideas are preserved when still useful, but clearly labeled as application-specific or superseded.

# Part I - Why Identity Architecture Exists

## 1. Persona Is Not Identity

A conventional language-agent stack can reproduce a persona through a system prompt, few-shot examples, retrieved notes, or a profile object. That mechanism can be useful, but it is fundamentally a rendering contract: given context, emit behavior that looks consistent with a role. The role may disappear when context is lost, change when prompt order changes, or be copied to a second process with no principled answer to whether the two instances are the same entity.

Identity Architecture begins by rejecting the equivalence

\[
\text{consistent roleplay} \equiv \text{persistent identity}.
\]

A role is one possible expression of identity. Identity must survive cases in which expression changes: a bookseller can learn a new genre, an antimalware host can install a kernel update, a vault can rotate cryptographic material, a cognitive database can move to a different node, and a subsystem can be reconstructed after a crash. If every change creates a new identity, continuity is useless. If every change is automatically accepted as the same identity, compromise and drift become indistinguishable from legitimate adaptation.

The architecture therefore asks a harder question: **what must remain invariant, what may change, who has authority to approve the change, and what provenance proves that the resulting state belongs to the same trajectory?**

## 2. State Is Not Identity

Let \(x_t\in\mathcal X\) denote the system state at time \(t\). Snapshot identity would define sameness as

\[
x_{t_1}=x_{t_2}.
\]

That definition is unusable for living systems because almost every legitimate operation changes state. The opposite extreme is equally bad: if every state reachable in time is automatically treated as the same identity, a compromised host, poisoned policy, or replaced constitutional anchor inherits identity merely by temporal succession.

Canonical Identity Architecture instead treats identity as a constrained relation over a trajectory:

\[
\mathcal I(e,t) = \big(G_0,\, \tau_{0:t},\, \mathcal A_{G_0},\, \Pi_t,\, \mathcal C_t\big),
\]

where this monograph uses the notation:

- \(G_0\): constitutional baseline;
- \(\tau_{0:t}\): verified identity-relevant trajectory up to time \(t\);
- \(\mathcal A_{G_0}\): admissible region induced by constitutional constraints;
- \(\Pi_t\): current realization/provenance mapping;
- \(\mathcal C_t\): continuity evidence needed to establish that the present realization belongs to the same entity.

This tuple is an **INFERRED formalization**, not a claim that current code stores a five-field identity object. Its purpose is to make explicit what the architecture already separates operationally.

## 3. History Is Necessary but Is Not Identity

The event trajectory records biography: observations, adjudications, baseline establishment, HIGC assessments, and eventually remediation episodes and continuity transformations. Biography influences future interpretation, but the entity is not the set of everything that ever happened to it.

Suppose a relationship \(r=(A,B,\text{trusted-at-}t_0)\) is recorded at time \(t_0\). If that event becomes an immutable identity attribute, trust can never legitimately change. The event should remain immutable as history, while current relationship state is derived from later events. Thus:

\[
\text{immutable event history} \not\Rightarrow \text{immutable current relation}.
\]

This distinction is foundational to TMS trajectory semantics: changing relationships can affect future policy without converting history into identity.

## 4. Memory Is Not Identity

Memory can be lost, reconstructed, compacted, migrated, indexed, or structurally shared. If identity were equal to a particular memory representation, any compaction or reconstruction would create a new entity. Identity therefore cannot depend on one Memtable, one SSTable, one HDF5 file path, one ANN graph, or one process-local cache.

The architecture instead separates logical continuity from physical realization. TMS owns active state and trajectory realization; HDF5 owns durable long-term/permanent persistence; HVD owns database identity and record semantics; QMT is reserved for continuity across transformations. The identity question is not "are these bytes at the same address?" but "does the new realization preserve the required constitutional and provenance relation?"

## 5. The Identity Problem as Controlled Change

The identity problem can be summarized as a controlled-change problem:

```text
current verified trajectory
          |
          v
     current state
          |
          +---- proposed change / observed change
          v
  constitutional interpretation
          |
          +---- HIGC admissibility
          +---- THDE bounded evolution
          +---- QMT continuity
          |
          v
same entity / boundary / unresolved / violation
```

The architecture must simultaneously avoid two failure modes:

- **rigidity failure**: no meaningful adaptation is permitted because identity is defined as frozen state;
- **drift failure**: arbitrary adaptation is permitted because history or model confidence is mistaken for constitutional permission.

The solution is to allow change inside explicit authority and continuity boundaries.

# Part II - Core Ontology and Authority

## 6. The Constitutional Baseline \(G_0\)

\(G_0\) is the explicit constitutional baseline. In the current AmmunIty profile, `G0Baseline` is an immutable dataclass containing a UUID-like baseline identifier, creation timestamp, host identity anchor, OS information, kernel information, protected roots, a package-state reference, selected artifact baselines, provenance, schema version, and a SHA-256 content digest.

The most important property of \(G_0\) is not its field list; it is its **authority semantics**. It is established through an explicit operator action. It is not automatically created on first launch, after a clean scan, or after repeated observations. This prevents circular trust bootstrap:

\[
\text{current state looks clean} \;
\not\Rightarrow\; \text{current state is constitutional truth}.
\]

A system that automatically treats its first observation as healthy can be initialized while already compromised. Explicit baseline creation does not eliminate baseline-poisoning risk, but it makes the trust decision visible, reviewable, and attributable.

Current persistence hardening further encodes constitutional intent. Baseline creation refuses to overwrite an existing baseline, writes into a private directory, uses a temporary file, flushes and `fsync`s content, publishes with an atomic no-clobber hard link, and `fsync`s the containing directory. This is an implementation of the policy "constitutional genesis is not an ordinary mutable preference."

## 7. \(G_0\) Is Not the Entire Identity

A baseline alone is not identity. It is the reference constitution against which trajectory and evolution are interpreted. If identity were simply \(G_0\), the system could never legitimately evolve. The canonical relation is better represented as

\[
\text{Identity at }t = \text{constitutional origin} + \text{verified continuity} + \text{admissible evolution}.
\]

The baseline anchors what cannot be silently rewritten; later layers determine what changes can be accepted without erasing that origin.

## 8. Global Constitution and Local Tolerance

The historical architecture introduced a valuable distinction between a stable constitutional baseline and a local tolerance layer, often written \(T_{local}\). The intent is to let repeated benign local behavior influence handling without mutating \(G_0\).

A useful formal decomposition is

\[
\mathcal A_t = \mathcal A_{G_0} \cap \mathcal T_t,
\]

where \(\mathcal A_{G_0}\) is the hard constitutional region and \(\mathcal T_t\) is a potentially time-varying local tolerance policy. This expression must be interpreted carefully: \(\mathcal T_t\) may narrow or shape operational treatment, but it may not enlarge the system across a hard constitutional prohibition unless explicit authority exists to revise the constitution itself.

Current AmmunIty does **not** implement learned \(T_{local}\). Current code deliberately refuses to learn identity from repetition. Any paper claiming that present AmmunIty automatically turns recurring behavior into identity is therefore historical or proposed, not implemented.

## 9. Identity State Vocabulary

The current application vocabulary contains:

```text
KNOWN_BASELINE
EXPECTED
LOCALLY_TOLERATED
NOVEL
SUSPICIOUS
MALICIOUS
CONTAINED
REMEDIATING
INDETERMINATE
SENSOR_FAILURE
ANALYSIS_FAILURE
```

This enum is useful but must not be mistaken for the universal ontology. Some states describe constitutional relation (`EXPECTED`, `NOVEL`), some describe security interpretation (`MALICIOUS`, `SUSPICIOUS`), some describe operational treatment (`CONTAINED`, `REMEDIATING`), and some describe epistemic failure (`INDETERMINATE`, `SENSOR_FAILURE`, `ANALYSIS_FAILURE`).

A mature implementation should preserve these dimensions separately where possible rather than force every concern into one label. An inferred factorization is

\[
S_t = (C_t, P_t, O_t, E_t),
\]

with constitutional state \(C_t\), pathology state \(P_t\), operational state \(O_t\), and epistemic state \(E_t\). The existing enum is a practical Phase 1 surface, not proof that a single categorical axis is theoretically sufficient.

## 10. Authority Matrix

| Layer | Owns | May derive | Must not silently own |
|---|---|---|---|
| **G0 authority** | constitutional genesis/reference | digest, protected scope | learned tolerance, remediation policy |
| **Identity Event Ledger** | immutable biography/provenance chain | verified ordered events | full active-memory realization |
| **TMS** | active realization, trajectory materialization, COW, locality | replayable current views | constitutional truth merely because data is live |
| **HIGC** | admissible set and boundary classification | named constraint outcomes | reward trade-offs, historical storage |
| **THDE** | bounded evolution/candidate transition semantics | candidate eligibility | actuation unless separately granted |
| **QMT** | continuity across transformation | continuity certificate/check | database record semantics |
| **HVD** | database identity, records, exact/associative query | similarity/context | constitutional identity authority |
| **Cyrae-lite** | derived homeostatic control state | advisory modulation | history, baseline mutation, hard security authority |
| **Maera / actuator** | outward constrained expression/action | rendering/action projection | hidden identity rewrite |
| **HDF5** | durable long-term/permanent persistence | generations/checkpoints | live hot constitutional queries |

The architecture is strongest when these boundaries are treated as security properties, not merely code organization.

# Part III - Mathematical Theory of Constitutional Identity

## 11. State Space and Constraint Family

Let the identity-relevant system state live in a heterogeneous state space \(\mathcal X\). In Nexus this may ultimately be represented through HVD/HTLA structures rather than one flat Euclidean vector, so \(\mathcal X\) should not be assumed homogeneous.

Let the constitution induce a family of named constraints

\[
\mathcal H = \{h_1,h_2,\ldots,h_m\}.
\]

For scalar barrier-like constraints, a conventional safe set would be

\[
\mathcal A_{G_0} = \{x\in\mathcal X : h_j(x)\ge 0\;\forall j\}.
\]

Current HIGC is more epistemically expressive than a simple real-valued barrier because each constraint can be `SATISFIED`, `BOUNDARY`, `VIOLATED`, or `UNRESOLVED`. Therefore the current architecture is better modeled by a typed evaluation

\[
\gamma_j : (x,e,G_0) \rightarrow \{S,B,V,U\},
\]

where \(e\) is the available evidence/provenance context.

The aggregate geometry is non-compensatory:

\[
\Gamma(x,e)=
\begin{cases}
\text{OUTSIDE}, & \exists j:\gamma_j=V,\\
\text{UNRESOLVED}, & \neg\exists j:\gamma_j=V\land\exists j:\gamma_j=U,\\
\text{BOUNDARY}, & \text{otherwise }\exists j:\gamma_j=B,\\
\text{ADMISSIBLE}, & \forall j:\gamma_j=S.
\end{cases}
\]

This precedence is critical. A known constitutional violation cannot be numerically averaged away by several favorable signals, and missing evidence cannot be converted into permission.

## 12. Four-Valued Geometry and Epistemic Honesty

Binary safe/unsafe logic is insufficient when evidence can fail. The four-valued HIGC state distinguishes ontology from epistemology:

- `OUTSIDE` means the architecture has evidence of violation.
- `UNRESOLVED` means it lacks enough evidence to establish location in the admissible set.
- `BOUNDARY` means no hard violation is known, but an unestablished change or contextual condition touches a protected boundary.
- `ADMISSIBLE` means all currently defined constraints are satisfied.

The difference between `OUTSIDE` and `UNRESOLVED` prevents a common security bug: treating absence of evidence as evidence of health. The difference between `BOUNDARY` and `OUTSIDE` prevents a second bug: treating every unfamiliar state as malicious.

This can be viewed as a partial-information geometry. Let \(K\) be the set of known facts and \(U\) the set of required but unknown facts. HIGC refuses to evaluate a missing fact as an implicit neutral scalar. The architecture preserves the semantic pair

\[
(\text{numeric forcing}=0,\;\text{epistemic state}=\text{UNAVAILABLE})
\]

when downstream matrix operations need a numeric placeholder. Zero in the matrix is therefore not interpreted as "the prediction was exactly correct." The typed state carries the truth condition.

## 13. Homeostatic Distance Is Not Identity Distance

It is useful to define a preferred operational subset \(\mathcal X^*\subseteq\mathcal A_{G_0}\). A homeostatic error can then be

\[
H(x)=\inf_{y\in\mathcal X^*} d(x,y).
\]

This is a regulation metric, not a direct identity metric. Two states can have different homeostatic error while remaining the same identity; a system may be injured but still be itself. Conversely, two states can have similar homeostatic error while belonging to different identities if constitutional anchors or continuity differ.

Therefore

\[
d(x_1,x_2)\text{ small} \not\Rightarrow \operatorname{SameIdentity}(x_1,x_2).
\]

This is why ANN/HNSW similarity is never sufficient identity evidence.

## 14. Identity as a Path Property

Let a trajectory be

\[
\tau = (x_0,e_1,x_1,e_2,\ldots,e_n,x_n),
\]

where \(e_i\) are identity-relevant events or transitions. Identity continuity is a path property because legitimacy may depend on how the system arrived at \(x_n\), not only on the final state.

Two final states may be byte-identical while having different provenance. For example, an attacker can overwrite a host, then restore visible files while leaving an invalid trust chain. Snapshot equivalence does not repair invalid continuity. Conversely, a legitimate package upgrade can produce a very different state while preserving provenance and remaining within constitutional evolution rules.

An inferred continuity predicate can therefore be written

\[
\operatorname{Cont}(G_0,\tau, x_n)=
\operatorname{LedgerValid}(\tau)\land
\operatorname{AdmissiblePath}(\tau)\land
\operatorname{TransformPreserved}(\tau).
\]

Current code implements only parts of this: ledger validity, candidate provenance resolution, and HIGC classification. Full transformation continuity is the future QMT responsibility.

## 15. Constitutional Equivalence vs Snapshot Equality

Define a relation \(\sim_I\) over realized states:

\[
x_a\sim_I x_b
\]

when there exists a verified admissible transformation path from the same constitutional origin and the required QMT invariants are preserved. This relation is intentionally stricter than semantic similarity and looser than exact state equality.

For a well-designed identity system, \(\sim_I\) should ideally be reflexive and transitive over accepted transformations. Symmetry is subtler because historical transformations may not be reversible. Identity continuity is therefore often better treated as a directed reachability relation than as a pure mathematical equivalence relation:

\[
x_a \leadsto_I x_b.
\]

The distinction matters for migrations, irreversible key rotations, or irreversible remediation. The entity can remain continuous even when returning to the exact prior state is impossible.

## 16. Constitutional Change vs Ordinary Change

Identity Architecture should distinguish at least three kinds of change:

\[
\Delta x = \Delta x_{operational}+\Delta x_{adaptive}+\Delta x_{constitutional}.
\]

Operational change occurs inside existing rules. Adaptive change modifies tolerated behavior while preserving the constitution. Constitutional change changes the protected rule set itself and therefore requires a stronger authority path. The current implementation intentionally supports operational observation and candidate evaluation but does not implement autonomous constitutional amendment.

A key safety principle follows:

\[
\text{frequent observation} \not\Rightarrow \text{constitutional amendment}.
\]

Otherwise an attacker could normalize malicious behavior simply by sustaining it long enough.

# Part IV - Event-Sourced Biography and Continuity

## 17. The Identity Event Ledger

The current AmmunIty `identity/tms.py` retains legacy TMS naming for compatibility, but the object is specifically an **Identity Event Ledger / Continuity Ledger**, not the complete Nexus TMS. Each immutable event contains an event ID, timezone-aware timestamp, event type, subject, source, evidence mapping, predecessor hash, event hash, and schema version.

Conceptually, for canonical serialization \(c(E_i)\), the hash is

\[
H_i = \operatorname{SHA256}\big(c(E_i)\big),
\]

with `previous_event_hash` storing \(H_{i-1}\). Chain verification requires

\[
\operatorname{prev}(E_i)=H_{i-1}
\]

for every event after genesis, in addition to verifying each content hash.

The current append path verifies the existing chain, takes an exclusive `flock`, appends one JSONL record, flushes, and `fsync`s. Read iteration takes a shared lock and verifies the chain before yielding events. This is an intentionally simple implementation, but its semantics are important: existing identity biography is not edited in place.

## 18. Event Immutability Does Not Mean Current-State Immutability

Event sourcing is frequently misunderstood. An append-only ledger says "the record of what happened is immutable," not "the system can never change its mind."

If event \(E_1\) says `relationship=A_trusts_B` and event \(E_2\) later says that trust was revoked, both facts remain in biography. Current trust is a projection

\[
R_t = \operatorname{Fold}(E_0,\ldots,E_t),
\]

not a permanent property copied from the earliest event.

The same principle applies to identity adjudication. The ledger may contain an earlier `EXPECTED` state and a later `MALICIOUS` state. It is wrong to say that the entity is permanently expected because that status appears in history.

## 19. Hash Chains: What They Prove and What They Do Not

A valid hash chain proves internal structural consistency relative to the inspected sequence. It can detect many forms of in-place tampering, deletion in the middle of the observed chain, accidental corruption, or reordering. It does **not** by itself prove:

- that the original events were true;
- that a malicious but authorized writer did not append false events;
- that no separate fork exists elsewhere;
- that the current copy is the globally latest copy;
- that timestamps are externally trustworthy;
- that the host was uncompromised when evidence was produced.

Thus continuity integrity is necessary but not sufficient epistemic truth. Sensor provenance, authority signatures, external anchoring, fork policy, and future distributed-consensus rules may be needed for stronger guarantees.

## 20. Replayable Active TMS

Phase 3A introduces a replayable identity materialization on the shared TMS. The model is

\[
M_t = \operatorname{Replay}(E_0,E_1,\ldots,E_t),
\]

where \(M_t\) is not a new source of constitutional truth. It is an efficiently queryable projection.

The current active-TMS view uses two collections:

```text
identity_events
identity_active_state
```

`identity_events` stores immutable materializations keyed by event ID. If the active TMS contains a different payload for an event ID that the verified ledger says should have another value, the bridge refuses to overwrite the conflict. `identity_active_state` stores rebuildable latest-state projections such as `g0`, `latest_adjudication`, `latest_higc_assessment`, and observation-specific keys.

This yields the authority direction:

```text
verified Identity Event Ledger
              |
              | deterministic replay/materialization
              v
        active TMS view
              |
              +--> fast retrieval
              +--> downstream state consumers
              +--> later temporal indexing
```

Deleting the active view loses performance and availability, not identity truth, provided the verified ledger and durable backing remain intact.

## 21. TMS Is More Than the Identity Event Ledger

The compatibility name `TMSStore` is historically misleading. Canonical TMS is the broader Transdimensional Memory Substrate. It owns active state realization and the log-structured persistence path, including WAL, Memtable, SSTables, compaction/recovery, copy-on-write structural sharing, trajectory, and physical locality.

The Identity Event Ledger is one continuity component layered into that broader memory architecture. The monograph therefore uses:

- **Identity Event Ledger** for the append-only hash-chained biography;
- **TMS** for the live active-memory substrate.

This terminology prevents a subtle architecture collapse in which a JSONL audit log is mistaken for the entire live memory system.

## 22. HDF5 Durable Persistence

Some older identity documentation described HDF5 as "archival/snapshot/restore only." That wording is too narrow under the current Nexus architecture. The canonical role is **durable long-term/permanent persistence**. Snapshotting, flush, generation storage, restoration, and rehydration are mechanisms within that role.

The intended direction is staged persistence rather than peer hot querying:

```text
active TMS state
      |
      v
coherent immutable generation/checkpoint
      |
      v
HDF5 durable long-term persistence
```

HDF5 therefore does not become the identity authority merely because it can preserve a durable state image. Continuity still depends on provenance and constitutional interpretation.

## 23. QMT and Continuity Across Transformation

QMT is the architectural owner of continuity when state changes representation or physical realization. Examples include:

- TMS compaction changing physical layout;
- process restart and deterministic rehydration;
- host migration;
- serialization/deserialization;
- HVD placement changes;
- schema-preserving remapping;
- future distributed movement or failover.

A future QMT check can be thought of as validating a transformation \(T\):

\[
T:(x,\Pi_a)\mapsto(x',\Pi_b)
\]

such that protected invariants and continuity witnesses are preserved. The architecture deliberately separates this from HIGC: HIGC asks whether a state is constitutionally admissible; QMT asks whether the transformed realization is continuous with the same entity.

# Part V - HIGC: Constitutional Geometry

## 24. Why HIGC Is Not a Risk Score

Risk scoring usually aggregates evidence into a scalar:

\[
r = \sum_j w_j f_j(x).
\]

That form is dangerous for constitutional identity because one severe violation can be compensated by several favorable terms. A host identity mismatch or definitive pathology should not become acceptable because the scan also produced many clean observations.

Current HIGC therefore uses named symbolic constraints. The Phase 3B AmmunIty profile contains:

```text
g0_integrity
continuity_integrity
host_identity_continuity
constitutional_scope
definitive_pathology_absence
evidence_resolvability
identity_change_boundary
```

Each is evaluated independently. Aggregate precedence is logical rather than compensatory.

## 25. Current Phase 3B Constraint Semantics

### 25.1 `g0_integrity`

- `SATISFIED`: a finalized baseline exists and its content digest verifies.
- `UNRESOLVED`: no baseline has been established.
- `VIOLATED`: persisted baseline integrity fails.

A clean scan without \(G_0\) is therefore not admissible identity; the geometry is unresolved.

### 25.2 `continuity_integrity`

- `SATISFIED`: identity ledger / required trajectory is verified.
- `VIOLATED`: continuity is structurally invalid.
- `UNRESOLVED`: candidate provenance or required trajectory cannot be fully resolved.

Phase 3C expands this from a binary verified/invalid interpretation to verified/unresolved/invalid so missing provenance is not conflated with known corruption.

### 25.3 `host_identity_continuity`

The current profile compares `hostname`, `machine`, and `system` against the explicit \(G_0\) host anchor. A mismatch is a violation. Kernel version is captured in the baseline but intentionally not frozen as a Phase 3B host-identity invariant, because normal kernel updates should not automatically create a new entity.

This is a useful example of constitutional design: what the system records can be richer than what it freezes as identity.

### 25.4 `constitutional_scope`

Requested roots must lie within the protected \(G_0\) domain and coverage must be resolved. Scope outside the protected domain is `OUTSIDE` **the current constitutional geometry**; it is not automatically malware. Missing/incomplete/unquantified coverage is unresolved.

### 25.5 `definitive_pathology_absence`

A definitive `FOUND` observation violates the constraint. Clean evidence from another sensor cannot average that violation away.

### 25.6 `evidence_resolvability`

Sensor failure, analysis failure, indeterminate observations, or incomplete/unquantified coverage produce unresolved geometry. This is the key epistemic-honesty gate.

### 25.7 `identity_change_boundary`

Contextual evidence and unestablished state change produce a boundary condition rather than a violation. Novelty is therefore neither automatically benign nor automatically malicious.

## 26. HIGC as a Control Barrier Function

The current Phase 5 architecture generalizes HIGC toward a Control Barrier Function interpretation. Let Cyrae or another controller propose a modulation \(m_{proposed}\). The constitutionally filtered modulation can be formalized as

\[
m_{actual}=\arg\min_m \|m-m_{proposed}\|_2^2
\]

subject to all hard HIGC constraints and, in a continuous/discrete control formulation, appropriate barrier conditions.

The key concept is **minimal permissible deviation**, not "large penalty if unsafe." A penalty permits trade-offs; a barrier prohibits crossing.

Current AmmunIty Phase 3B does **not** implement this projection operator. It is shadow geometry: it classifies. Treating the CBF equation as already deployed enforcement would overstate the implementation.

## 27. HIGC Does Not Own Evolution

HIGC answers "where is this state relative to the admissible set?" It should not silently decide how quickly a system changes, how hysteresis accumulates, whether a rollback is preferable, or what trajectory to explore. Those belong to THDE and related control layers.

The separation can be written:

\[
\text{HIGC}: x\mapsto \Gamma(x),
\]

\[
\text{THDE}: (x_t,\tau_t,u_t)\mapsto \{x_{t+1}^{(k)}\}_{k}.
\]

HIGC constrains candidate targets; THDE generates/evaluates bounded change.

## 28. Safe Recovery From an Unsafe Source

A subtle Phase 3C correction is that the source state need not already be admissible before evaluating a recovery candidate. If a host is outside the safe set because it is compromised, a rule "only evolve from admissible sources" would make recovery impossible.

Instead:

```text
source may be OUTSIDE
        |
        v
hypothetical candidate target
        |
        v
candidate-specific HIGC
        |
        +--> admissible recovery direction
        +--> boundary hold
        +--> outside reject
        +--> unresolved hold
```

The target is judged constitutionally, while provenance still proves how the candidate relates to the source trajectory.

# Part VI - THDE: Bounded Evolution Without Identity Drift

## 29. THDE Responsibility

THDE owns bounded evolution semantics. The present implementation is intentionally conservative: it creates and evaluates immutable hypothetical transitions but does not realize them on the host.

This design is strategically important. Before a system gains write authority, it should first demonstrate that it can represent hypothetical change, bind evidence to the exact hypothesis, verify provenance, apply constitutional gates, and fail closed under missing evidence.

## 30. Candidate State Contract

Current `THDECandidateState` contains:

```text
state_id
source_state_id
proposed_delta
provenance_references
generated_by
created_at
contract_version
```

`proposed_delta` is recursively frozen after canonical JSON serialization. Dictionaries become immutable mappings; lists become tuples; non-finite numeric values are rejected by JSON serialization. The candidate requires at least one unique TMS provenance reference.

Crucially, `proposed_delta` is **not** declared to be the final HVD or HTLA state schema. Phase 3C deliberately avoids freezing a provisional database representation into Identity Architecture while the standalone HVD contract continues to evolve.

## 31. Candidate Content Digest

Identity of a hypothetical candidate cannot rely only on `state_id`. Otherwise evidence generated for candidate content \(c\) could be replayed after mutating the candidate while reusing the same ID.

Current code computes

\[
d(c)=\operatorname{SHA256}(\operatorname{canon}(c)),
\]

where the serialization excludes the derived `host_mutation_authorized` flag. Candidate evidence carries this digest. Evaluation rejects evidence if the candidate content no longer matches.

This closes a form of semantic ABA/aliasing:

```text
state_id = X, content = A  -> evidence EA
state_id = X, content = B  -> EA must NOT be reusable
```

The content digest makes the evidence relation specific to the actual hypothesis.

## 32. Exact Provenance References

A `TMSProvenanceReference` contains an event ID and a `sha256:<64 hex>` event hash and must point to the immutable `identity_events` collection. The reference is not an authority grant. It is a claim that a candidate depends on exact verified historical evidence.

Let

\[
P(c)=\{(id_k,H_k)\}
\]

be candidate provenance and

\[
V(\tau)=\{(id_i,H_i)\}
\]

be the verified trajectory event set. Exact provenance resolution requires

\[
P(c)\subseteq V(\tau).
\]

Near matches, same IDs with different hashes, or hashes not present in the supplied trajectory remain unresolved.

## 33. Verified Trajectory Adapter

The Phase 3C adapter verifies the **full supplied trajectory**, not merely the individual referenced events. It checks:

1. each event content hash;
2. duplicate event IDs;
3. exact predecessor-hash chain continuity;
4. exact candidate reference resolution.

It produces three states:

- `VERIFIED`: chain valid and every candidate reference resolves;
- `UNRESOLVED`: chain valid but one or more candidate references are absent/mismatched;
- `INVALID`: chain itself is structurally or cryptographically invalid.

This distinction produces an important precedence:

\[
\text{known violation} + \text{missing provenance} \rightarrow \text{OUTSIDE},
\]

while

\[
\text{no known violation} + \text{missing provenance} \rightarrow \text{UNRESOLVED}.
\]

Missing evidence never upgrades a candidate.

## 34. Explicit Hypothetical Evidence

Current candidate evidence contains the candidate state ID and digest, a nonempty observation set, requested roots, scope status, and explicit hypothetical host identity containing `hostname`, `machine`, and `system`.

The explicit host identity requirement prevents a dangerous implementation shortcut: evaluating a hypothetical future or counterfactual state while accidentally reading the *current* machine's `platform.*` values. Candidate evaluation must describe the candidate, not silently substitute the realized host.

The requirement for at least one explicit observation similarly prevents

\[
\varnothing \Rightarrow \text{clean}.
\]

An empty evidence set means missing evidence, not health.

## 35. Evaluation Envelope and TOCTOU Closure

`THDECandidateHIGCEvaluation` binds:

```text
candidate_state_id
candidate_digest
candidate evidence
verified trajectory context
candidate-specific HIGC check
```

Its `assess_transition()` function passes the exact event sequence used during HIGC evaluation into the THDE classifier. This prevents a time-of-check/time-of-use mismatch in which constitutional evaluation uses trajectory \(\tau_A\) and later provenance resolution uses \(\tau_B\).

The invariant is

\[
\tau_{HIGC}=\tau_{THDE}.
\]

If candidate content changes after evidence generation, assessment fails before classification.

## 36. Deterministic Phase 3C Gate

Current classification is:

\[
D(c)=
\begin{cases}
\text{REJECTED\_OUTSIDE}, & \Gamma(c)=\text{OUTSIDE},\\
\text{UNRESOLVED}, & \neg\operatorname{ProvResolved}(c),\\
\text{UNRESOLVED}, & \Gamma(c)=\text{UNRESOLVED},\\
\text{HELD\_BOUNDARY}, & \Gamma(c)=\text{BOUNDARY},\\
\text{CANDIDATE\_ADMISSIBLE}, & \Gamma(c)=\text{ADMISSIBLE}\land\operatorname{ProvResolved}(c).
\end{cases}
\]

Every branch remains non-actuating.

## 37. Admissible Is Not Authorized

This is one of the most important laws in the current implementation:

\[
\boxed{\text{candidate admissible} \not\Rightarrow \text{host mutation authorized}}.
\]

Every serialized Phase 3C candidate/evaluation/assessment reports `host_mutation_authorized = false`. A future actuator must require an independent authority layer: operator confirmation, policy grant, signed remediation token, reflex authority, or another explicitly specified mechanism.

Without this separation, a bug in geometric classification becomes a destructive host action. The architecture intentionally inserts a hard gap between **reasoning about a state** and **realizing a state**.

## 38. Future THDE Mechanics

The long-term THDE design may include hysteresis, bounded jumps, rollback reasoning, transition velocities, path-dependent stability, and safe-set projection. Those functions are not current implementation simply because the acronym THDE exists in code.

A future generic recurrence might take the form

\[
x_{t+1}=\Pi_{\mathcal A}\big(f(x_t,u_t,h_t)\big),
\]

where \(h_t\) is hysteretic/path-dependent state and \(\Pi_{\mathcal A}\) is an admissibility projection. The current Phase 3C code stops before \(\Pi_{\mathcal A}\) or any actuator.

# Part VII - HVD, Associative Memory, and the Identity Boundary

## 39. Why HVD Is Not Identity Authority

HVD is a cognitive database. It can store structured records, heterogeneous hypervectors, exact keys, associative neighborhoods, contextual memory, and future nested/ephemeral cognitive databases. None of those functions makes it constitutional authority.

A similarity result

\[
\operatorname{sim}(q,x)>\theta
\]

means the query is geometrically close under the chosen representation and metric. It does not mean the query is the same entity, malicious, trusted, continuous, or admissible.

Current AmmunIty therefore treats pathology association as contextual evidence. It can raise the need for review or contribute to a boundary state, but it cannot rewrite \(G_0\), create \(T_{local}\), or promote similarity into definitive pathology.

## 40. Exact Identity and Approximate Similarity Are Different Relations

Database identity is usually exact: a stable `DatabaseID`, collection ID, record key, or durable reference. Associative similarity is approximate. Constitutional identity is a third relation based on continuity and invariants.

The architecture therefore maintains three separate relation families:

\[
R_{db},\quad R_{sim},\quad R_{identity}.
\]

Confusing them creates severe errors. For example, two HVD records can be near-identical semantically but represent different hosts. One host can change its hypervector substantially while remaining the same constitutional entity. An ANN index can be rebuilt with a different graph topology without changing the identity of any database record.

## 41. ANN/HNSW Is Derived Acceleration State

ANN indexes should be treated as reconstructable acceleration artifacts. They may be discarded and rebuilt. They do not own truth, continuity, admissibility, or identity. This mirrors the active-TMS projection principle: fast derived state is useful precisely because authority remains somewhere more stable.

## 42. Recursive and Ephemeral HVDs

The newer recursive HVD architecture removes genealogical parent/child identity assumptions. Temporary cognitive databases can coexist in HTCE fields and share underlying TMS state through copy-on-write without implying inheritance.

For Identity Architecture, this yields a strong rule:

\[
\text{identity}\neq\text{relationship}\neq\text{lifetime}\neq\text{location}\neq\text{storage sharing}.
\]

An ephemeral HVD can represent a counterfactual candidate without becoming the identity of the realized host. Two candidate HVDs can share 99.9% of physical storage without becoming the same logical database. A candidate can disappear without erasing the realized entity's continuity.

This becomes especially important in future Phase 5F counterfactual remediation, where hypothetical trajectories must remain advisory and must never contaminate the real Identity Event Ledger.

## 43. Counterfactual Identity Fields

A future counterfactual field may be modeled

\[
\mathcal F_t^{cf}=\{D_i^{cf}(t)\}_{i=1}^{N_t},
\]

where each \(D_i^{cf}\) is a logically complete ephemeral HVD/Nexus scope with a proposed remediation or evolution hypothesis. HIGC can classify each candidate, THDE can reason about transition behavior, and Cyrae can estimate homeostatic consequences. Yet the real identity trajectory remains unique until an authorized action is executed and observed through canonical channels.

The separation is:

```text
counterfactual field        realized identity trajectory
        |                              |
        | no authority                 | authoritative events
        v                              v
candidate HVDs  --advice--> authorized action -> new observed event
```

Simulation is not biography.

# Part VIII - Cyrae, Homeostasis, and Temporal Causality

## 44. Historical Continuous Cyrae

The original master paper represented Cyrae as an 11-dimensional continuous controller:

\[
C(t)=[NE,DA,5HT,ACh,Glu,GABA,P,C,A,V,S]^T
\]

with a nonlinear ODE resembling

\[
\dot C=-\Lambda C+\sigma(W_C C+W_EE_{err}+W_RRPE+W_N\eta+b).
\]

This was a productive research model, but it is **HISTORICAL / SUPERSEDED** for Cyrae-lite Phase 5. A continuous ODE adds integration drift and restart complexity to an event-sourced architecture whose state changes are fundamentally checkpointed and discrete.

## 45. Current Discrete Bounded Cyrae-Lite

The current architecture uses

\[
C_{k+1}=\operatorname{clip}_{[0,1]^{11}}\left(\Lambda C_k+B u_k\right),
\]

with decay chosen so that

\[
\rho(\Lambda)<1.
\]

In the absence of new forcing, the controller returns toward its resting state. The state is rebuildable from canonical history rather than owning a private durable database.

This matters to Identity Architecture because regulatory state must not become a shadow source of identity. Cyrae observes and modulates; it does not define \(G_0\), rewrite history, or grant continuity.

## 46. Homeostatic Error, Novelty, Prediction Error, and RPE Are Different

The current Phase 5 architecture explicitly separates several quantities that earlier work sometimes overloaded.

### Homeostatic error

\[
H(x_t)=\inf_{y\in\mathcal X^*}d(x_t,y).
\]

### State prediction error

For forward model \(\hat x_{t+1}=F(x_t,a_t)\),

\[
e^{state}_{t+1}=d(x_{t+1},\hat x_{t+1}).
\]

### Remediation outcome

For a properly pinned pre-action baseline \(x_b\) and resolved post-action state \(x_c\),

\[
O_e = H(x_b)-H(x_c).
\]

A positive value means the episode moved closer to the preferred set under the chosen metric.

### Reward prediction error

If the expected outcome \(\widehat O_e\) was bound **before** execution,

\[
\delta_e=O_e-\widehat O_e.
\]

or, in a more general TD form,

\[
\delta_t=r_t+\gamma V(s_{t+1})-V(s_t).
\]

The key point is not the algebra. It is the temporal contract. A legitimate RPE requires a prediction that existed before the action, an executed intervention, a causally comparable outcome horizon, and sufficient provenance.

## 47. Why a Single Snapshot Cannot Produce RPE

An `ActiveMemorySnapshot` is a cross-section. It describes a state, not a causal episode. Subtracting two arbitrary snapshots does not establish that the difference was caused by a remediation.

If an administrator repairs one file while a sensor fails and a package update occurs, raw

\[
x_{t+1}-x_t
\]

mixes intervention effect with exogenous change. Treating that vector as RPE would teach the controller false causal associations.

Phase 5A therefore requires

```text
RPE = UNAVAILABLE
RemediationOutcome = UNAVAILABLE
```

until temporal lineage, episode tracking, prediction binding, and causal outcome resolution exist.

## 48. Missing Is Not Zero

If RPE is unavailable, the numeric DA/RPE forcing position may be masked to zero to preserve matrix dimensions, but semantic status remains `UNAVAILABLE` or `CONFOUNDED`.

This preserves the distinction

\[
0_{observed}\neq 0_{masked\ because\ unknown}.
\]

The former means a measured zero residual; the latter means "do not inject a fabricated value." Identity Architecture adopts the same principle broadly: absence of evidence cannot be silently converted into a favorable state.

## 49. Remediation Episodes and Identity Biography

Future Phase 5C introduces a `RemediationEpisode` lifecycle with states such as `PROPOSED`, `PREDICTED`, `EXECUTED`, `PENDING_OBSERVATION`, `RESOLVED`, and `CONFOUNDED`. This is highly relevant to identity because an autonomous system's biography must distinguish recommendation from execution and execution from observed effect.

A proposed action is not part of realized identity state. An executed action becomes historically relevant, but its effect is not known until canonical observations resolve it. A counterfactual simulation is never promoted to biography unless an actual authorized action follows.

## 50. Cyrae-HIGC Authority Ordering

Cyrae may propose modulation; HIGC remains the absolute constitutional gate. Therefore

\[
\text{homeostatic benefit} \not\Rightarrow \text{constitutional permission}.
\]

A change that improves a performance metric but violates a protected security invariant remains prohibited. This is the control-theoretic expression of "the organism cannot optimize itself out of being itself."

# Part IX - Domain-Grounded Tradecraft and Professional Ego

## 51. The Original Insight: Inherited Tradecraft

The historical Educated Bookseller architecture asked how a digital worker could possess something richer than a prompt: a persistent professional identity shaped by domain knowledge, habits, standards, preferences, and experience. The phrase **professional ego** is useful when interpreted operationally rather than anthropomorphically.

A professional ego can be modeled as a structured domain-grounded policy context

\[
E_{prof}=(G_0,K_{domain},P_{practice},\tau_{experience},T_{local}),
\]

where \(K_{domain}\) is domain knowledge, \(P_{practice}\) is professional policy/heuristics, \(\tau_{experience}\) is verified experience, and \(T_{local}\) represents bounded local tolerance or learned practice.

The insight is that expertise should not be regenerated from scratch at every inference. However, the architecture must keep **expertise** separate from **constitutional identity**. A worker can learn new expertise without becoming a new entity, and a malicious learned habit should not rewrite \(G_0\).

## 52. Universal Pattern vs Bookseller Profile

The bookseller embodiment included catalog knowledge, customer interaction, merchandising, returns, financial governance, brand behavior, and potentially autonomous operational decisions. Those are not universal identity primitives. The universal pattern is:

```text
constitutional baseline
      +
domain ontology / tradecraft
      +
verified experience
      +
bounded adaptation
      +
expression policy
```

The same pattern can instantiate:

- a bookseller;
- an antimalware immune system;
- a password vault guardian;
- an infrastructure SRE agent;
- a scientific research agent;
- a robotic field system.

The domain profile determines what \(G_0\) protects and what observations mean; the core architecture determines how those judgments become identity-relevant safely.

## 53. Knowledge, Skill, Preference, and Identity Must Remain Distinct

A mature identity model should avoid storing all persistent traits in one bag. At minimum:

- **knowledge**: propositions/models the entity can update;
- **skill**: procedures/policies for performing tasks;
- **preference**: soft tendencies that may evolve;
- **relationship**: time-varying edges to other entities;
- **identity invariant**: protected property whose change requires constitutional authority;
- **biography**: immutable record of events;
- **current state**: derived present condition.

This separation prevents history from fossilizing relationships and prevents ordinary learning from becoming an identity rewrite.

## 54. Maera and Expression

Historical Identity Architecture couples Cyrae-like internal regulation to Maera-like outward expression. Canonically, Maera should remain downstream: it renders or actuates a constrained representation of internal state. It does not own hidden truth.

A clean expression contract is

\[
y_t = \mathcal M(x_t,C_t,p_t),
\]

where \(p_t\) is an authorized expression policy. Changing tone, verbosity, interface style, or UI presentation does not necessarily change identity. This is another reason persona and identity must be separated.

## 55. Financial and Corporate Cybernetics Are Application-Specific

The original master paper explored solvency, autonomous banking, storefront economics, corporate/legal delegation, and programmatic financial survival. Those ideas may be valuable for a commercial digital organism, but they are **APPLICATION-SPECIFIC**. Identity Architecture should supply authority/provenance mechanisms for such actions without declaring financial autonomy to be part of identity itself.

Likewise, legal-personhood or corporate-agency claims require jurisdiction-specific legal analysis. An engineering event ledger can document delegated authority; it cannot create legal authority merely by recording that authority in software.

# Part X - AmmunIty as the Executable Reference Organism

## 56. Why AmmunIty Is a Strong Reference Profile

AmmunIty forces Identity Architecture to answer concrete questions that a purely conversational agent can evade. Is a clean scan enough to say the host is healthy? Is a new package state legitimate adaptation or compromise? What if the scanner fails? What if associative memory recognizes a suspicious pattern but no definitive detector fires? What if the continuity log is corrupted? Can a candidate remediation be evaluated without executing it?

These questions make authority mistakes observable. The current reference flow is approximately:

```text
deterministic sensors
       |
       v
neutral Observation
       |
       +---------------------+
       |                     |
       v                     v
IdentityAdjudicator     HIGC geometry
       |                     |
       +----------+----------+
                  |
                  v
        Identity Event Ledger
                  |
                  v
          shared active TMS

contextual HVD pathology memory feeds Observation context,
not constitutional authority.
```

Phase 3C adds a separate hypothetical path downstream of verified trajectory and candidate evidence.

## 57. Neutral Observation Boundary

Sensors should report what they observed rather than directly declaring identity. This is a crucial epistemic interface. The adjudicator and HIGC can interpret the same neutral facts differently because they answer different questions.

For example:

- `FOUND` can produce a malware verdict and an HIGC violation;
- `STATE_CHANGE` can produce `NOVEL` adjudication and HIGC `BOUNDARY`;
- `SENSOR_FAILURE` can produce a failure state and HIGC `UNRESOLVED`;
- contextual HVD evidence can produce suspicion without definitive pathology.

This prevents each detector from becoming its own constitutional sovereign.

## 58. Current Deterministic Adjudicator Precedence

The Phase 1 adjudicator roughly follows:

```text
invalid continuity -> ANALYSIS_FAILURE
FOUND              -> MALICIOUS
sensor failure     -> SENSOR_FAILURE
analysis failure   -> ANALYSIS_FAILURE
uncertain scope    -> INDETERMINATE
contextual evidence-> SUSPICIOUS
state change       -> NOVEL
no G0              -> INDETERMINATE
clean in G0 scope  -> EXPECTED
otherwise          -> NOVEL
```

This is an AmmunIty application policy, not the universal definition of identity. Its architectural value is that the policy is deterministic and fail-closed. A negative ClamAV result does not become proof of overall host health, and a clean observation without \(G_0\) does not bootstrap identity.

## 59. HIGC Runs Beside Adjudication

Current Phase 3B intentionally leaves `IdentityAdjudicator` as the application decision authority while HIGC runs as shadow constitutional geometry. The same evidence enters two functions:

\[
A_t=\operatorname{Adjudicate}(G_0,O_t,\tau_t),
\]

\[
G_t=\operatorname{HIGC}(G_0,O_t,\tau_t).
\]

The outputs are persisted separately. This avoids a risky "big bang" replacement of existing security behavior before the geometry layer is validated.

## 60. Persistence Failure Semantics

The orchestration service carefully distinguishes ledger failure from active-view failure.

If the Identity Event Ledger cannot verify, continuity is invalid and current identity claims fail closed. If writing a new identity event fails, the result is degraded to analysis failure because the system cannot claim a verified continuing trajectory.

By contrast, if active TMS materialization fails while the ledger remains verified, the system reports operational degradation but does not rewrite already-established ledger truth. This is the correct authority asymmetry:

\[
\text{projection failure} \neq \text{history corruption}.
\]

## 61. Current Source-Level Implementation Surface

At the inspected commit, the identity package includes:

```text
adapter.py        neutral scan -> Observation mapping
adjudicator.py    deterministic Phase 1 identity interpretation
baseline.py       explicit immutable G0
candidate.py      candidate evidence + trajectory verification + HIGC envelope
higc.py           symbolic Phase 3B geometry
memory.py         replayable active-TMS materialization
service.py        runtime orchestration
state.py          typed identity vocabulary
thde.py           immutable Phase 3C candidate/transition gate
tms.py            append-only Identity Event Ledger
```

This is significant because the architecture is no longer only a speculative paper. But it remains bounded: there is no autonomous host mutation authority, learned \(T_{local}\), full QMT, full Cyrae Phase 5 temporal causality, or deployed HIGC projection operator.

# Part XI - Security and Threat Model

## 62. Baseline Poisoning

If an attacker controls the host before \(G_0\) establishment, an explicit baseline can still capture a compromised state. Identity Architecture reduces circular trust but cannot conjure trustworthy genesis from an untrusted environment.

Mitigations for stronger deployments may include:

- offline or measured-boot attestation during baseline creation;
- package/vendor signature verification;
- TPM-backed measurements;
- multi-party operator approval;
- external witness signatures;
- clean-install provenance;
- policy that refuses baseline creation when required sensors are unresolved.

The architecture should state clearly which trust root it actually possesses.

## 63. Baseline Mutation and Rollback

Current no-clobber baseline storage prevents ordinary overwrite through the public API, but filesystem-level attackers with sufficient privilege can still replace files. Digest validation detects unauthorized content change only if the expected digest-bearing object remains available and the attacker cannot rewrite every trust anchor coherently.

A mature system should defend against rollback to an old but internally valid \(G_0\) through external version anchors, monotonic counters, or durable signed generation metadata.

## 64. Ledger Truncation, Forking, and Rewriting

A local hash chain detects internal breaks, but an attacker who can replace the entire ledger with a shorter internally consistent fork can evade purely local chain validation. Future hardening should consider:

\[
\text{chain validity} + \text{tip freshness} + \text{fork policy} + \text{writer authority}.
\]

External tip anchoring or durable checkpoint generations can make truncation/rollback harder.

## 65. Provenance Laundering

A candidate must not cite broad statements such as "based on recent history." Exact `(event_id,event_hash)` references make the dependency auditable. Yet exact references are useful only if the referenced event itself is legitimate. Candidate provenance is not a substitute for sensor provenance.

A complete provenance graph may eventually need chains such as:

```text
candidate
  -> identity event
      -> observation
          -> sensor execution
              -> binary/config/version attestation
```

## 66. Candidate Evidence Rebinding

The digest binding in Phase 3C closes a class of attack in which evidence for one candidate is reused after the candidate changes. The required invariant is

\[
d(c_{evaluated})=d(c_{evidence}).
\]

Any mismatch invalidates the evaluation envelope.

## 67. TOCTOU Across Trajectories

Candidate evaluation must not use one history at HIGC time and another at THDE time. Binding the exact trajectory event tuple into the evaluation envelope prevents a simple time-of-check/time-of-use split. In a distributed future, stronger version/tip IDs or immutable checkpoint handles will likely be needed.

## 68. Sensor Failure as False Improvement

One of the most dangerous causal bugs is interpreting lost visibility as recovery. Suppose `weak_count` changes from 5 to unavailable. Numerically treating unavailable as zero would produce an apparent improvement of five. Typed epistemic state prevents this:

\[
5\rightarrow\text{UNAVAILABLE}\not\Rightarrow\Delta=-5.
\]

The numeric channel may be masked while the epistemic channel explicitly records loss of observability.

## 69. ANN Authority Escalation

An attacker can manipulate embeddings or exploit collision/similarity behavior to create misleading neighbors. Because HVD similarity is advisory, this should raise context rather than directly authorize destructive action. Any architecture that turns `cosine_similarity > threshold` into constitutional truth violates the current authority model.

## 70. Active-View Corruption

The active TMS projection is rebuildable, but corruption can still affect consumers if not detected. Current materialization refuses to overwrite an existing event ID with conflicting bytes, and `verify_against()` can compare materialized events to verified ledger truth. Future consumers should attach provenance/version information to derived views so stale state is not silently accepted.

## 71. Actuation Escalation

A severe future risk is accidental coupling of candidate classification to a host actuator:

```text
CANDIDATE_ADMISSIBLE -> execute()
```

That mapping is explicitly forbidden today. Safe actuation should require an independent capability or authorization object with scope, expiry, action class, target binding, and ideally a digest of the exact approved candidate.

## 72. Constitutional Drift Through Tolerance

Learned local tolerance creates a poisoning channel if repetition alone increases permission. A safe \(T_{local}\) system needs bounded influence, decay, evidence quality, non-crossable HIGC constraints, and perhaps promotion rules requiring explicit review. Tolerance must never silently rewrite \(G_0\).

## 73. "Identity" as a Privilege Escalation Word

Software often grants extra privileges to components labeled "identity," "trusted," or "system." Identity Architecture must resist this semantic shortcut. Being the same entity does not imply authorization for every action. Authentication, identity continuity, authorization, and actuation are separate predicates:

\[
\operatorname{SameIdentity}\not\Rightarrow\operatorname{Authorized}(a).
\]

# Part XII - Verification, Evidence, and Current Implementation Status

## 74. What Is Implemented at `b12eaed...`

The inspected `main` revision includes:

- explicit immutable \(G_0\) construction and integrity checking;
- no-clobber baseline creation with private filesystem permissions and durable write steps;
- deterministic Phase 1 identity adjudication;
- append-only hash-chained Identity Event Ledger;
- replayable active-TMS materialization;
- Phase 3B HIGC symbolic geometry and seven constraint types;
- persistence of HIGC assessments to the continuity ledger and active view;
- Phase 3C immutable candidate state/transition contracts;
- exact TMS provenance references;
- candidate content digest binding;
- explicit candidate observations and hypothetical host identity;
- full supplied-trajectory verification;
- candidate-specific HIGC evaluation;
- deterministic THDE transition classification;
- explicit no-host-mutation authority on candidate objects and evaluation results.

The latest inspected commit message specifically describes digest-bound candidate evidence, full verified-trajectory adaptation, explicit hypothetical host identity evaluation, candidate/trajectory/HIGC evaluation envelopes, adversarial regressions, and zero state-realization authority.

## 75. Regression Obligations Encoded in Current Documentation

Phase 3B requires cases including:

- valid \(G_0\), verified continuity, resolved clean in-scope observations -> `ADMISSIBLE`;
- no \(G_0\) -> `UNRESOLVED`;
- contextual/state-change evidence -> `BOUNDARY`;
- definitive pathology -> `OUTSIDE`;
- requested scope outside \(G_0\) -> `OUTSIDE` without equating it to malware;
- sensor or scope uncertainty -> `UNRESOLVED`;
- invalid continuity -> `OUTSIDE`;
- HIGC persistence without rewriting \(G_0\) or adjudicator outcome.

Phase 3C adds obligations including:

- immutable candidates and recursive payload freezing;
- mandatory TMS provenance;
- mandatory explicit observations;
- mandatory explicit hypothetical host identity;
- digest binding to exact candidate content;
- inability to reuse evidence after candidate mutation;
- full trajectory content-hash and predecessor verification;
- rejection of duplicate/broken trajectories;
- unresolved missing provenance;
- no use of live `platform.*` identity for explicit hypothetical candidates;
- deterministic mapping from HIGC states to THDE decisions;
- no baseline/ledger mutation during candidate evaluation;
- `host_mutation_authorized = false` in every result.

These are strong implementation contracts. They are not yet a proof of long-term security or universal identity continuity.

## 76. What Has Not Been Demonstrated

The current system does **not** establish:

- autonomous learned \(T_{local}\) with formal anti-poisoning guarantees;
- autonomous constitutional amendment;
- full HIGC CBF projection/enforcement on actuators;
- full THDE hysteresis, bounded jumps, stochastic evolution, or rollback execution;
- QMT continuity across arbitrary migrations/rehydrations;
- complete Cyrae Phase 5 temporal lineage and causal RPE;
- distributed ledger fork resolution;
- Byzantine writer tolerance;
- cryptographically attested sensor truth;
- production-scale security against root compromise;
- formal proof that the four-valued constraint set is complete;
- a philosophical solution to personal identity or machine consciousness;
- phenomenal continuity across restart;
- AGI.

The architecture should be judged on the engineering claims it actually makes.

## 77. Verification vs Falsification

A test that confirms expected behavior for selected cases provides evidence but does not prove the architecture correct for all states. A stronger program uses property-based, adversarial, model-based, and metamorphic testing.

Useful universal properties include:

### Non-compensation

For any evidence set containing a known hard violation,

\[
\Gamma(E)=\text{OUTSIDE}
\]

regardless of additional satisfied constraints.

### Epistemic non-promotion

Removing required evidence must never turn `OUTSIDE`, `BOUNDARY`, or `UNRESOLVED` into `ADMISSIBLE` unless the removed evidence was itself erroneous and the correction is explicitly established.

### Replay determinism

For verified history \(\tau\), rebuilding the active identity view twice should produce observationally equivalent derived state:

\[
\operatorname{Replay}(\tau)=\operatorname{Replay}(\tau).
\]

This sounds tautological, but implementation non-determinism, timestamps, iteration order, and serialization can violate it.

### Candidate evidence integrity

For any mutation \(c'\neq c\) changing canonical candidate content,

\[
d(c')\neq d(c)
\]

except cryptographic collision probability.

### No-actuation property

For all current Phase 3C evaluation paths,

\[
\operatorname{HostMutationAuthorized}(c)=\text{false}.
\]

### Projection non-authority

Deleting and rebuilding active TMS must not change authoritative identity history.

# Part XIII - Architecture Evolution and Superseded Models

## 78. From Digital Worker Persona to Constitutional Identity

The earliest Identity Architecture work was motivated by a persistent bookseller that could inherit tradecraft and behave like a long-lived worker rather than a fresh chatbot session. That application exposed a real need, but it bundled identity with profession, UI expression, customer relationships, and commercial operations.

The current architecture generalizes the insight: **profession is a domain profile, not the definition of self**. Identity becomes a substrate-independent constitutional continuity contract that can host many professions and applications.

## 79. From "Argotchain Is Memory" to Layered Continuity

Historical papers often described an event-sourced Argotchain-like ledger as the organism's memory. The newer architecture is more precise:

- ledger = immutable biography/provenance;
- TMS = active memory/trajectory realization;
- HVD = database semantics and associative memory;
- HDF5 = durable long-term/permanent persistence;
- QMT = continuity across transformation.

This decomposition is strictly stronger because no one storage object is forced to answer every memory and identity question.

## 80. From Continuous Cyrae to Discrete Rebuildable Control

The old continuous ODE model was mathematically expressive but poorly matched to deterministic event replay. Current Cyrae-lite uses discrete bounded recurrence and typed missing signals. The biological coordinate names remain useful motifs, but the implementation is computational rather than a neurotransmitter simulation.

## 81. From Snapshot Difference to Causal Episode

Earlier controller concepts could interpret sequential state change as reward prediction error. Current Phase 5 rejects that. A valid RPE requires a pre-action prediction, executed action, comparable baseline/current states, and causal attribution. Until the event ledger and TMS temporal projector support that contract, RPE is `UNAVAILABLE`.

## 82. From Soft Safety Penalty to Absolute HIGC Constraint

Historical reward/controller descriptions risked making safety another weighted term. Current architecture treats HIGC as a non-compensatory constitutional constraint and conceptually as a CBF. No amount of favorable homeostasis may buy permission to violate a protected invariant.

## 83. From HDF5 "Snapshot Store" to Durable Persistence Layer

The most recent Nexus architecture clarifies that HDF5 is the durable long-term/permanent persistence store. Snapshot, archive, restoration, and rehydration are mechanisms, not the full concept. Active memory remains TMS.

## 84. From Genealogical Recursion to Field-Based HVD Cognition

Older recursive designs can tempt parent/child inheritance semantics. Current recursive HVD architecture defines field membership and structural sharing without making genealogy identity. This is essential for counterfactual identity work: a candidate can derive structurally from a realized state without inheriting authority or becoming a literal child identity.

# Part XIV - Engineering Blueprint

## 85. Recommended Dependency Order

A safe implementation sequence is:

```text
1. explicit G0 + integrity + provenance
2. neutral observation contract
3. append-only Identity Event Ledger
4. deterministic adjudication
5. shared TMS active replay materialization
6. HIGC shadow geometry
7. immutable THDE candidate contract
8. exact trajectory/provenance binding
9. candidate-specific HIGC evaluation
10. pure candidate projector
11. THDE hysteresis / rollback reasoning
12. QMT transformation-continuity contract
13. TMS temporal lineage index
14. remediation episode lifecycle
15. pre-action prediction binding
16. causal RPE
17. capability-scoped actuation
18. ephemeral-HVD counterfactual evaluation
19. bounded T_local learning
20. only then consider constitutional-amendment machinery
```

The order is deliberately biased toward **observation and proof before authority**.

## 86. Suggested Generic Interfaces

A future domain-independent API could resemble:

```python
class ConstitutionalBaseline(Protocol):
    baseline_id: str
    content_digest: str

class IdentityHistory(Protocol):
    def verify(self) -> ContinuityStatus: ...
    def events(self) -> Sequence[IdentityEvent]: ...

class ConstitutionalGeometry(Protocol):
    def evaluate(
        self,
        baseline: ConstitutionalBaseline,
        evidence: EvidenceSet,
        continuity: ContinuityStatus,
    ) -> GeometryAssessment: ...

class EvolutionEngine(Protocol):
    def propose(
        self,
        source: StateRef,
        evidence: EvidenceSet,
        provenance: Sequence[EventRef],
    ) -> Sequence[CandidateState]: ...

class ContinuityVerifier(Protocol):
    def verify_transform(
        self,
        source: StateRef,
        target: StateRef,
        proof: TransformProof,
    ) -> ContinuityAssessment: ...

class Actuator(Protocol):
    def execute(
        self,
        candidate: CandidateState,
        authorization: CapabilityToken,
    ) -> ExecutionReceipt: ...
```

The exact names are illustrative. The architectural requirement is that one interface does not silently collapse all six responsibilities.

## 87. Candidate Authorization Token

When actuation eventually exists, an authorization object should bind at least:

```text
authorization_id
candidate_digest
action_class
target_scope
issuer
issued_at
expires_at
required_preconditions
max_side_effect_scope
revocation / nonce data
```

Then execution can require

\[
\operatorname{Auth.candidateDigest}=d(c).
\]

This prevents a capability approved for one candidate from being reused for a modified candidate.

## 88. Identity-Safe Compaction

Because TMS uses log-structured storage, compaction is a cognitive risk boundary. Physical rewriting must preserve logical event/state semantics. A compaction operation should satisfy an observational equivalence property for all identity-relevant queries:

\[
Q(M_{before})=Q(M_{after})
\]

for the supported query set \(Q\), while retaining provenance necessary for replay and QMT continuity.

Compaction may change layout and merge representations; it must not silently erase the distinction between historical event and current derived state.

## 89. Identity-Safe Migration

A future migration protocol should freeze a coherent source generation, produce a continuity manifest, move/rehydrate state, verify hashes and schema mappings, and only then switch active realization. A high-level sequence is:

```text
quiesce / checkpoint logical state
      |
      v
emit signed continuity manifest
      |
      v
transfer durable + active reconstruction inputs
      |
      v
rehydrate target
      |
      v
QMT verify logical continuity
      |
      +--> fail: remain on source / rollback
      `--> pass: atomically promote target
```

Physical movement should not be observable as identity replacement.

## 90. Domain Profile Contract

A reusable Identity Architecture should let each application define:

- constitutional baseline schema;
- hard invariants;
- boundary conditions;
- required evidence types;
- uncertainty semantics;
- domain-specific adjudication vocabulary;
- candidate projector;
- allowed action classes;
- tolerance/learning rules;
- durability and audit requirements;
- QMT continuity invariants.

This isolates domain semantics from the shared identity machinery.

# Part XV - Identity Lifecycle, Rebirth, and Distributed Continuity

## 91. Genesis, Activation, Suspension, Recovery, and Termination

A complete identity architecture needs explicit lifecycle states that are independent of ordinary operational status. A process can stop without the entity being terminated; an HVD can become inactive without its durable identity being deleted; a host can be quarantined while its identity remains continuous. Therefore lifecycle should be modeled separately from security or constitutional state.

An inferred lifecycle vocabulary is:

```text
UNESTABLISHED -> ESTABLISHED -> ACTIVE -> SUSPENDED -> RECOVERING -> ACTIVE
                                      \-> RETIRED
                                      \-> TERMINATED
```

`UNESTABLISHED` means no constitutional genesis exists. `ESTABLISHED` means G0 exists but the entity may not yet be running. `ACTIVE` means a current realization is serving. `SUSPENDED` means activity is intentionally halted while continuity material remains. `RECOVERING` means a new realization is being reconstructed and has not yet passed continuity checks. `RETIRED` means the entity is intentionally inactive but may remain auditable. `TERMINATED` means the architecture has intentionally ended continuity and a later system should not silently reuse the old identity.

These lifecycle states are **INFERRED** rather than current AmmunIty enums. They are useful because they prevent a process lifecycle from becoming an identity lifecycle by accident.

## 92. System Rebirth Is a Continuity Operation

Nexus uses a broader idea of System Rebirth: reconstructing active cognition from durable state after process loss, host loss, or intentional restart. Identity-safe rebirth requires more than deserializing bytes. At minimum:

1. identify the durable constitutional baseline and accepted generation;
2. verify baseline and durable-generation integrity;
3. verify the Identity Event Ledger trajectory and selected tip;
4. reconstruct active TMS state from authoritative history/durable generations;
5. rebuild derived HVD/ANN/controller state;
6. verify QMT continuity between the prior and reconstructed realization;
7. only then promote the reconstructed realization to `ACTIVE`.

The rebirth operation can be represented as

\[
R:(G_0,\tau,D_{durable})\rightarrow x'_{active},
\]

subject to

\[
\operatorname{Verify}(G_0)\land\operatorname{Verify}(\tau)\land
\operatorname{QMT}(x_{prior},x'_{active}).
\]

The system should fail into `RECOVERING` or a safe unresolved state rather than inventing continuity when required material is missing.

## 93. What Survives Process Death

Different kinds of state have different survival obligations.

| State class | Expected survival | Why |
|---|---|---|
| G0 constitution | durable | genesis/reference cannot depend on process memory |
| Identity Event Ledger | durable | biography/provenance continuity |
| Active TMS projection | rebuildable | performance view, not sole truth |
| ANN/HNSW | rebuildable | acceleration state |
| Cyrae-lite control vector | rebuildable | derived deterministic controller state |
| THDE hypothetical candidates | usually ephemeral unless explicitly staged | simulation must not become biography by default |
| RemediationEpisode | durable-derived once implemented | causal episode must survive restart |
| Local UI session state | usually ephemeral | not constitutional |
| HDF5 generations | durable | long-term/permanent persistence |

The survival table makes a useful design test: if a state is declared durable, explain why replay cannot reconstruct it. If a state is declared ephemeral, explain why losing it cannot change constitutional truth.

## 94. Promotion Is an Authority Operation

An ephemeral object should not be able to declare itself durable or identity-bearing. Promotion from hypothetical/ephemeral state into realized identity requires external authority.

Let candidate \(c\) be ephemeral and \(a\) an authorization capability. A legitimate promotion can be abstracted as

\[
\operatorname{Promote}(c,a)\rightarrow e_{executed}
\]

only if

\[
\operatorname{DigestBound}(a,c)\land
\operatorname{Authorized}(a)\land
\operatorname{Admissible}(c)\land
\operatorname{Fresh}(a).
\]

The resulting execution event, not the candidate object itself, enters identity biography. This keeps counterfactual computation and realized history categorically distinct.

## 95. Stable Logical Identity vs Physical Address

A durable identity reference should be independent of process IDs, file paths, memory addresses, hostnames used for placement, or current TMS extent locations. Those are realization attributes.

A useful stable-reference model is

```text
identity://<namespace>/<entity-id>
```

resolved through a continuity-aware directory to the current active realization. The URI shape is illustrative, but the principle is canonical: durable identity should not be encoded as a current physical path.

If an entity migrates from node A to node B, its resolver target changes while the durable identity remains constant if QMT continuity passes.

## 96. Distributed Identity and the Single-Writer Illusion

A local append-only ledger is straightforward because serialization order is controlled by one store. Distribution introduces harder questions: concurrent writers, partitions, forked tips, delayed observations, and conflicting candidate histories.

The architecture should not assume that adding replication preserves the semantics of a single local chain. Let two nodes independently extend a common tip \(H_k\):

\[
H_k\rightarrow H_{k+1}^{A},\qquad H_k\rightarrow H_{k+1}^{B}.
\]

Both branches can be internally valid. The identity problem becomes a policy question: are the branches concurrent aspects that can merge, mutually exclusive state transitions, or evidence that continuity is unresolved?

Different event types may need different merge laws. Commutative observations might merge as a set; constitutional mutations may require total ordering and quorum; actions with side effects may be non-mergeable. A universal "last timestamp wins" rule would be unsafe.

## 97. Fork Classification

A distributed continuity layer should distinguish at least:

- **benign concurrency**: independent observations that can coexist;
- **causal divergence**: two branches represent incompatible transitions;
- **stale extension**: a writer extended an obsolete tip;
- **malicious equivocation**: an authorized writer produced incompatible signed histories;
- **network uncertainty**: insufficient information to choose a branch.

The natural response to unresolved causal divergence is not arbitrary merge but a typed continuity state such as `FORK_UNRESOLVED`. HIGC can then treat required continuity as unresolved rather than assuming health.

## 98. Identity Across Replicas

Replication creates copies of state, not copies of identity. If three replicas serve the same logical HVD/identity, they are three realizations of one logical entity when they participate in one continuity contract. Conversely, cloning a durable generation into an isolated sandbox should not automatically grant the clone the same realized identity.

This yields:

\[
\text{replica count}\neq\text{identity count}.
\]

Identity count depends on continuity and authority semantics, not byte-copy count.

A clone intended for testing should receive an explicit derived/sandbox identity or ephemeral scope so its actions cannot append to the production biography.

## 99. Split-Brain Safety

During a partition, two replicas may each believe they are active. If both can mutate externally visible state, continuity can split irreversibly. Identity-safe high availability therefore needs a lease, quorum, fencing token, or equivalent mechanism for mutation authority.

The invariant is:

\[
\text{at most one valid mutation authority for a non-mergeable identity transition.}
\]

Read-only cognition can often remain multi-active. Mutation authority is the scarce resource.

## 100. Continuity Checkpoints and Durable Tips

To resist rollback and support efficient recovery, durable generations should bind to an identity-ledger tip and schema/geometry versions. A continuity manifest could include:

```text
entity_id
baseline_id
ledger_tip_event_id
ledger_tip_hash
ledger_length_or_sequence
tms_generation_id
hvd_schema_version
geometry_version
created_at
issuer/signature
```

A recovered generation is acceptable only when its manifest and ledger ancestry agree. This prevents a stale but internally valid snapshot from silently becoming current.

# Part XVI - Formal Invariants and Proof Obligations

## 101. Separation Invariants

Identity Architecture relies on negative guarantees: things one layer must never be able to imply by itself.

### Similarity non-authority

\[
\forall q,x:\operatorname{ANNMatch}(q,x)\not\Rightarrow\operatorname{IdentityDecision}(q).
\]

### Materialization non-authority

\[
\operatorname{TMSView}(\tau)\not\Rightarrow\operatorname{NewHistory}.
\]

### Candidate non-realization

\[
\operatorname{Candidate}(c)\not\Rightarrow\operatorname{Realized}(c).
\]

### Admissibility non-authorization

\[
\operatorname{Admissible}(c)\not\Rightarrow\operatorname{Authorized}(c).
\]

### History non-identity

\[
E_i\in\tau\not\Rightarrow \operatorname{CurrentIdentityProperty}(E_i).
\]

These are architectural proof obligations that should appear in tests and API design.

## 102. Monotonic Authority Principle

Derived layers may lose information or summarize, but they must not manufacture stronger authority than their inputs provide. If the upstream state is `UNRESOLVED`, a downstream derived view may remain unresolved or become more conservative, but should not become `ADMISSIBLE` solely due to projection.

Let \(\preceq\) denote an information/authority order where unresolved is not stronger than verified. For a derived function \(F\), a desired property is

\[
F(x)\preceq x
\]

with respect to authority. This is not numeric monotonicity; it is a lattice-style rule that derivation cannot create provenance it did not receive.

## 103. Non-Compensation Theorem for Current HIGC Logic

Given the current aggregate function \(\Gamma\), if any constraint is `VIOLATED`, adding any number of `SATISFIED`, `BOUNDARY`, or `UNRESOLVED` constraints cannot change the aggregate result from `OUTSIDE`.

Proof follows directly from first-match precedence:

\[
\exists j:\gamma_j=V \Rightarrow \Gamma=O.
\]

The proposition is trivial mathematically but profound architecturally: the implementation encodes constitutional non-compensation structurally rather than relying on a sufficiently large weight.

## 104. Uncertainty Non-Permission Theorem

For current aggregate logic, if no violation exists but at least one constraint is unresolved, the result is `UNRESOLVED` even if all remaining constraints are satisfied or boundary. Thus missing required evidence cannot yield `ADMISSIBLE`.

\[
\neg\exists V\land\exists U\Rightarrow\Gamma=U.
\]

This property should be preserved as the constraint set grows.

## 105. Replay Idempotence

For a deterministic materializer \(R\) and verified event sequence \(\tau\), applying replay twice to a clean target should yield the same logical state:

\[
R(\tau)=R(\tau).
\]

More operationally, if `materialize(τ)` is idempotent, a second call should introduce no conflicting immutable event records and should produce the same latest-state projection. Current `IdentityMemoryBridge` is designed toward this property by retaining identical existing event payloads and refusing conflicting ones.

## 106. Prefix Consistency

If \(\tau_a\) is a verified prefix of \(\tau_b\), replay of \(\tau_b\) should extend the biography of \(\tau_a\) rather than reinterpret already immutable event payloads:

\[
\tau_a\preceq\tau_b \Rightarrow
R(\tau_b)|_{events(\tau_a)} = R(\tau_a)|_{events(\tau_a)}.
\]

Current event-ID conflict checks support this property for immutable materialized events.

## 107. Candidate Immutability Obligation

Once evidence is bound to candidate \(c\), every later operation must either consume the same canonical candidate content or reject it. Formally:

\[
\operatorname{EvidenceFor}(e,c)\land d(c')\neq d(c)
\Rightarrow \neg\operatorname{Accept}(e,c').
\]

This prevents post-check mutation from bypassing constitutional evaluation.

## 108. Provenance Closure

A candidate with provenance references outside the verified trajectory cannot be fully evaluated as continuous. Current Phase 3C returns unresolved rather than attempting a fuzzy match.

\[
P(c)\nsubseteq V(\tau)\Rightarrow
\operatorname{Continuity}(c)=U
\]

unless the trajectory itself is invalid, in which case continuity becomes violated. This gives known corruption precedence over missing evidence.

## 109. Actuation Capability Conservation

No pure computation should create an actuation capability. If a candidate evaluator receives no mutation authority, its output must contain none:

\[
\operatorname{cap}(output)\subseteq\operatorname{cap}(input).
\]

Current Phase 3C effectively uses the empty host-mutation capability set. Future APIs should preserve capability conservation explicitly.

## 110. Identity Continuity Is Not Necessarily Reversible

Key rotation, irreversible remediation, or schema migration can preserve identity while preventing exact restoration. Therefore QMT should not require an inverse transformation in every case. It should verify preservation of declared invariants and provenance across a directed transformation.

A useful distinction is:

\[
T^{-1}\text{ exists} \quad \text{vs.}\quad \operatorname{ContinuityPreserved}(T).
\]

The second may hold when the first does not.

# Part XVII - Pathology, Remediation, and Constitutional Self-Repair

## 111. Pathology Is a Relation to Constitution

In a homeostatic immune-system interpretation, pathology is not merely "something a malware scanner dislikes." It is a state or process that violates protected invariants or degrades the system's ability to maintain them.

This suggests a domain-independent distinction:

- **definitive pathology evidence**: establishes a known violation under the current profile;
- **contextual pathology evidence**: raises concern but remains boundary/context;
- **state change**: difference from prior/baseline without pathology conclusion;
- **epistemic failure**: inability to know whether pathology is present.

The categories are intentionally non-equivalent.

## 112. Self-Repair Without Self-Rewrite

A self-repairing system must be able to change state to restore invariants while preserving identity. This is the core reason the architecture cannot define identity as exact snapshot equality.

Let current state \(x_t\notin\mathcal A\). A remediation proposes \(c\) such that

\[
c\in\mathcal A,\qquad d(c,\mathcal X^*) < d(x_t,\mathcal X^*).
\]

If provenance and authority are valid, executing the repair should produce a new state in the same identity trajectory. The system changes specifically so it can remain itself.

## 113. Remediation Authority Is Separate From Diagnosis

A definitive diagnosis can justify urgency without granting a particular repair strategy. Multiple remediations may exist with different side effects. HIGC can reject constitutionally unsafe candidates even when the source is clearly pathological.

Thus:

\[
\operatorname{PathologyDetected}\not\Rightarrow
\operatorname{AnyRemediationAuthorized}.
\]

This is especially important for destructive actions such as deleting binaries, rotating keys, changing filesystem ownership, or disabling services.

## 114. Containment vs Identity Mutation

Containment changes the operational environment around an entity, often without changing its constitutional identity. Quarantining a process, moving a file into a restricted namespace, or suspending network access may be reversible operational interventions.

Identity Architecture should record containment events in biography while avoiding the claim that containment itself creates a new identity. It may change current operational state \(O_t\) while leaving constitutional origin intact.

## 115. Repair Outcome vs Reward

A repair can improve homeostatic distance without being a "reward" in the psychological sense. Phase 5 appropriately treats the quantity as a measured remediation outcome first. Only after a prior prediction exists can the residual become an RPE.

This protects identity learning from a serious semantic collapse:

```text
observed improvement != predicted improvement residual
```

A successful repair with no prior prediction has an outcome but no legitimate RPE.

## 116. Recovery From Incomplete Evidence

When a system is outside or suspected outside the admissible set but sensors are failing, aggressive remediation may be dangerous. The correct state can be simultaneously pathological in one dimension and unresolved in another. Current HIGC precedence keeps known violations as `OUTSIDE`, but downstream actuation policy should still account for unresolved side-effect evidence.

A future actuator may require both:

\[
\operatorname{TargetAdmissible}(c)
\]

and

\[
\operatorname{SideEffectEvidenceSufficient}(c).
\]

Constitutional target safety and operational confidence are distinct gates.


# Part XVIII - Research Program and Falsification

## 117. The Central Scientific Question

The strongest research claim Identity Architecture can responsibly make is not "this system has a self." It is:

> A long-lived software organism can preserve a stable constitutional identity while permitting bounded adaptation, if constitutional invariants, immutable biography, active state realization, admissible evolution, and transformation continuity are assigned to separate auditable mechanisms.

That claim is testable.

## 118. Longitudinal Identity Drift Experiments

Run systems for long horizons under benign change, adversarial perturbation, migration, compaction, sensor loss, and domain learning. Measure:

- rate of false constitutional violations;
- rate of false admissibility;
- unresolved-state frequency and duration;
- baseline/tolerance drift;
- trajectory verification failures;
- replay divergence;
- candidate evidence mismatch detection;
- actuation-policy violations;
- ability to recover from outside-set states.

The architecture fails if it either freezes legitimate operation or gradually accepts forbidden state through accumulated tolerance.

## 119. QMT Continuity Tests

For transformations \(T_1,\ldots,T_n\), test whether continuity composes:

\[
QMT(T_2\circ T_1) \stackrel{?}{=} QMT(T_2)\land QMT(T_1)
\]

under the intended invariant set. Test cross-platform serialization, schema evolution, byte-order changes, storage migration, and process restart. Identify which transformations are continuity-preserving and which require explicit identity transition or constitutional amendment.

## 120. Fork and Rollback Adversaries

Construct two internally valid history forks from the same prefix. A purely local hash chain cannot choose the legitimate tip. Evaluate external anchors, signed writer policies, monotonic counters, and distributed witness schemes. The research objective is not to make forks impossible, but to make fork ambiguity explicit and fail closed.

## 121. Tolerance Poisoning Experiments

When \(T_{local}\) is implemented, attack it with slow, repeated, low-amplitude malicious behavior. Test whether the tolerance system gradually normalizes behavior that HIGC should prohibit. Required invariant:

\[
\forall t,\quad \mathcal T_t \text{ cannot authorize } x\notin\mathcal A_{G_0}.
\]

## 122. Causal Remediation Experiments

Once Phase 5B-5E exist, create controlled remediation episodes with known exogenous disturbances. Compare raw snapshot differences against matched-component causal attribution. A valid RPE subsystem should avoid rewarding sensor blindness and avoid punishing an effective remediation for unrelated environmental changes.

## 123. Identity Under Counterfactual Explosion

Future ephemeral HVD cognition may evaluate very large numbers of candidate worlds. Test whether candidate handles, provenance, and digests prevent cross-candidate evidence leakage or ABA reuse. The real trajectory must remain untouched regardless of counterfactual volume.

## 124. Formal Methods Opportunities

Several components are suitable for formal specification:

- HIGC precedence can be model-checked as a finite-state logic;
- baseline no-clobber and ledger append invariants can be specified in TLA+;
- candidate/evidence digest binding can be expressed as refinement invariants;
- actuation capabilities can be checked with a small authorization calculus;
- replay/materialization equivalence can be property-tested;
- QMT transformation continuity may admit category-theoretic or algebraic formulations once its invariant set is concrete.

Formalism should follow executable contracts rather than inventing mathematical grandeur detached from implementation.

## 125. What Would Falsify the Architecture

Identity Architecture would need major revision if experiments show any of the following are unavoidable rather than implementation bugs:

- legitimate long-lived adaptation cannot be separated from constitutional drift;
- continuity cannot be preserved across ordinary storage transformation without freezing physical representation;
- four-valued HIGC semantics produce intolerable unresolved deadlock under realistic evidence failure;
- event sourcing creates irreducible ambiguity that cannot be bounded by stronger provenance;
- local tolerance cannot learn usefully without becoming a baseline-poisoning channel;
- counterfactual candidate evaluation cannot be isolated from realized authority at required scale;
- QMT cannot define transformation continuity without circularly assuming the identity it is meant to verify.

A research architecture becomes stronger, not weaker, when it states what evidence would cause it to change.

# Part XIX - Expert Field Guide

## 126. Twenty-Five Canonical Laws

1. **Persona is not identity.** Consistent expression can be copied without continuity.
2. **State is not identity.** Legitimate change must be possible.
3. **History is not identity.** Biography influences current interpretation without freezing every past relation into selfhood.
4. **Memory is not identity.** Rebuildable representations may change without creating a new entity.
5. **Location is not identity.** Moving realization must not silently replace the logical entity.
6. **Storage sharing is not inheritance.** Copy-on-write candidates can share bytes without sharing authority.
7. **Similarity is not identity.** ANN/HNSW is advisory acceleration state.
8. **G0 is explicit.** Never bootstrap constitutional trust from an implicitly observed "clean" state.
9. **G0 is not ordinary mutable configuration.** Constitutional change requires explicit authority.
10. **Repetition is not constitutional amendment.** Tolerance learning must be bounded.
11. **Event immutability is not current-state immutability.** Later events can revise current derived relations without deleting history.
12. **Ledger validity is not sensor truth.** Cryptographic structure proves integrity of the record, not truth of every claim in it.
13. **Active TMS is a realization layer, not constitutional truth merely because it is fast.**
14. **HDF5 is durable long-term/permanent persistence, not a peer live constitutional backend.**
15. **HIGC is non-compensatory.** Hard violations cannot be averaged away.
16. **Unresolved is not admissible.** Missing evidence cannot become permission.
17. **Boundary is not outside.** Novelty/context is not automatically pathology.
18. **THDE owns bounded evolution; HIGC owns admissibility.**
19. **A recovery candidate may be evaluated even when the source is outside.**
20. **Candidate evidence binds to candidate content, not merely an ID.**
21. **Candidate provenance must resolve exactly against a verified trajectory.**
22. **Candidate admissible is not host mutation authorized.**
23. **Cyrae is advisory and rebuildable; it does not own authoritative history.**
24. **RPE requires temporal causality.** Snapshot difference is not reward prediction error.
25. **QMT owns continuity across transformation.** Physical equivalence and semantic similarity are insufficient.

## 127. Architecture Decision Checklist

Before adding an identity feature, ask:

- Is this fact constitutional, adaptive, relational, historical, epistemic, or merely operational?
- Which layer has authority to change it?
- What is the source of truth?
- Can the value be reconstructed? If so, why is it durable?
- What happens when evidence is missing?
- Does a fast cache accidentally become authority?
- Is an ANN result being promoted beyond similarity?
- Does the operation mutate \(G_0\) or only derived state?
- Is a hypothetical candidate cleanly separated from realized trajectory?
- Is candidate evidence digest-bound?
- Is provenance exact and trajectory-verified?
- Can a known violation be numerically averaged away?
- Can lost observability look like improvement?
- Can repeated malicious behavior become tolerated?
- Can a process restart or migration preserve logical identity?
- Is continuity being confused with byte equality?
- Is same identity being confused with authorization?
- Does actuation require a separate capability?
- Can every identity-relevant mutation be audited?
- What test would falsify the design assumption?

## 128. Minimal Mental Model

For day-to-day engineering, remember this flow:

```text
G0 says what must not be silently rewritten.
Events say what happened.
TMS realizes what is active now.
HVD remembers/query-relates structured cognition.
HIGC says what is admissible.
THDE says how change may be explored.
QMT says whether transformed realization is still continuous.
Cyrae says how far regulation appears from homeostasis.
Authorization says what may actually be done.
HDF5 preserves durable long-term generations.
```

If one component starts answering three or four of those sentences by itself, the architecture is probably collapsing an authority boundary.

# Appendix A - Mathematical Reference

## A.1 HIGC typed aggregate

\[
\Gamma(x,e)=
\begin{cases}
O, & \exists j:\gamma_j=V\\
U, & \neg V\land\exists j:\gamma_j=U\\
B, & \neg(V\lor U)\land\exists j:\gamma_j=B\\
A, & \forall j:\gamma_j=S
\end{cases}
\]

with \(A=\) admissible, \(B=\) boundary, \(O=\) outside, \(U=\) unresolved.

## A.2 Event hash chain

For canonical event encoding \(c(E_i)\):

\[
H_i=\operatorname{SHA256}(c(E_i)),\qquad
\operatorname{prev}(E_i)=H_{i-1}.
\]

## A.3 Active view replay

\[
M_t=\operatorname{Replay}(E_0,\ldots,E_t).
\]

Authority requirement:

\[
M_t \text{ is derived; } \tau_{0:t} \text{ remains continuity authority.}
\]

## A.4 Candidate digest

\[
d(c)=\operatorname{SHA256}(\operatorname{canon}(c)).
\]

Evidence validity requires

\[
d(c)=d_{evidence}.
\]

## A.5 Provenance resolution

\[
P(c)\subseteq V(\tau).
\]

## A.6 Homeostatic error

\[
H(x)=\inf_{y\in\mathcal X^*}d(x,y).
\]

## A.7 Remediation outcome

\[
O_e=H(x_b)-H(x_c).
\]

## A.8 Remediation RPE

\[
\delta_e=O_e-\widehat O_e,
\]

valid only when \(\widehat O_e\) is bound before action and the outcome is causally resolvable.

## A.9 Cyrae-lite recurrence

\[
C_{k+1}=\operatorname{clip}_{[0,1]^{11}}(\Lambda C_k+B u_k),
\qquad \rho(\Lambda)<1.
\]

## A.10 HIGC-filtered modulation

\[
m_{actual}=\arg\min_m\|m-m_{proposed}\|_2^2
\]

subject to constitutional barrier constraints. This is a canonical Phase 5 control model, not yet a deployed Phase 3B actuator.

## A.11 Directed identity continuity

\[
x_a\leadsto_I x_b
\]

when a verified constitutional transformation path connects the realizations under the eventual QMT continuity contract.

# Appendix B - Epistemic and Lifecycle Tables

## B.1 HIGC state semantics

| State | Meaning | Permission implication |
|---|---|---|
| `ADMISSIBLE` | All defined constraints satisfied | Eligible for later reasoning; not automatic actuation |
| `BOUNDARY` | Unestablished change/context reaches boundary | Hold/review/project; no automatic actuation |
| `OUTSIDE` | At least one known invariant violation | Reject as constitutionally inadmissible under current profile |
| `UNRESOLVED` | Required evidence/continuity cannot be resolved | Fail closed; obtain evidence |

## B.2 Trajectory resolution

| State | Meaning | HIGC continuity mapping |
|---|---|---|
| `VERIFIED` | Full chain valid; exact references resolve | `SATISFIED` |
| `UNRESOLVED` | Chain valid; refs absent/mismatched | `UNRESOLVED` |
| `INVALID` | Chain structurally/hash invalid | `VIOLATED` |

## B.3 THDE decision

| Decision | Meaning | Host mutation |
|---|---|---|
| `candidate_admissible` | HIGC admissible and provenance exact | false |
| `held_boundary` | Candidate at boundary | false |
| `rejected_outside` | Candidate outside | false |
| `unresolved` | Evidence/provenance insufficient | false |

## B.4 Future RPE lifecycle

| Stage | Meaning | RPE status |
|---|---|---|
| `PROPOSED` | recommendation exists | unavailable |
| `PREDICTED` | expected outcome bound pre-action | pending |
| `EXECUTED` | authorized action occurred | pending |
| `PENDING_OBSERVATION` | awaiting comparable outcome | pending |
| `RESOLVED` | causal outcome available | available |
| `CONFOUNDED` | comparison contaminated/incompatible | confounded |

# Appendix C - Implementation Status Matrix

| Capability | Status at reference edition | Notes |
|---|---|---|
| Explicit immutable G0 | **IMPLEMENTED** | One finalized baseline; digest validation; no public overwrite path |
| Baseline provenance | **IMPLEMENTED** | Provenance string + host/package/artifact references |
| Identity Event Ledger | **IMPLEMENTED** | Append-only JSONL, SHA-256 content + predecessor chain |
| Deterministic adjudicator | **IMPLEMENTED** | AmmunIty-specific precedence |
| Active TMS materialization | **IMPLEMENTED** | Rebuildable projection from verified ledger |
| HVD contextual pathology memory | **IMPLEMENTED / APPLICATION-SPECIFIC** | Advisory association only |
| HIGC shadow geometry | **IMPLEMENTED** | Phase 3B, seven named constraints |
| HIGC CBF actuation filter | **PROPOSED** | Canonical Phase 5 direction, not Phase 3B runtime |
| THDE candidate contract | **IMPLEMENTED** | Phase 3C immutable hypothetical states |
| Exact candidate provenance | **IMPLEMENTED** | Event ID + hash references |
| Candidate content digest binding | **IMPLEMENTED** | SHA-256 canonical content digest |
| Full trajectory adapter | **IMPLEMENTED** | Duplicate/hash/predecessor/ref checks |
| Candidate-specific HIGC | **IMPLEMENTED** | Explicit hypothetical evidence/host identity |
| Candidate projector | **ACTIVE DEVELOPMENT / PROPOSED** | Next Phase 3C handoff |
| THDE hysteresis/jumps/rollback mechanics | **PROPOSED** | No realization authority yet |
| Learned T_local | **PROPOSED** | Explicitly absent today |
| QMT transformation continuity | **PROPOSED** | Architectural owner established; full mechanism not current |
| Cyrae-lite current-state homeostasis | **ACTIVE DEVELOPMENT** | Current Phase 5A direction |
| TMS temporal lineage index | **PROPOSED** | Phase 5B |
| RemediationEpisode ledger lifecycle | **PROPOSED** | Phase 5C |
| Pre-action outcome prediction binding | **PROPOSED** | Phase 5D |
| Causal remediation RPE | **PROPOSED** | Phase 5E; currently unavailable |
| Ephemeral-HVD counterfactual identity evaluation | **PROPOSED** | Phase 5F |
| Autonomous host mutation | **NOT AUTHORIZED** | Current Phase 3C explicitly false |
| Durable HDF5 long-term persistence | **CANONICAL / integration-dependent** | Broader Nexus storage role; not identity authority |

# Appendix D - Glossary

**Adjudication** - Application-specific deterministic interpretation of observations into a current identity/security state.

**Admissible set** - Region of state/transition space satisfying current constitutional constraints.

**Active TMS view** - Rebuildable, efficiently queryable projection of verified identity history onto the Transdimensional Memory Substrate.

**Biography** - Immutable sequence of identity-relevant events; not identical to current identity.

**Candidate** - Hypothetical non-realized state proposed for bounded evaluation.

**Constitution** - Engineering set of protected invariants, authority boundaries, scope, and admissibility rules.

**Continuity** - Property that a later realization belongs to the same entity trajectory despite legitimate transformation.

**G0** - Explicit constitutional baseline/genesis reference.

**HDF5** - Durable long-term/permanent persistence layer in current Nexus architecture.

**HIGC** - HSL Invariant Geometry Calculus; owner of constitutional admissibility geometry.

**HVD** - Hyperdimensional Vector Database; cognitive database semantics and exact/associative retrieval.

**Identity Event Ledger** - Append-only hash-chained biography/provenance log used by current AmmunIty Identity Architecture.

**Maera** - Downstream expression/actuation renderer in related Nexus architecture; not identity authority.

**QMT** - Continuity mechanism/owner across transformation, migration, rehydration, or representational remapping.

**RPE** - Reward Prediction Error; valid only when a prediction made before action can be compared to a causally resolved outcome.

**THDE** - Temporal Homeostatic Dynamics Engine; owner of bounded/path-dependent evolution semantics.

**T_local** - Proposed bounded local tolerance/adaptation layer that must not silently mutate G0.

**TMS** - Transdimensional Memory Substrate; mandatory active state/trajectory realization and persistence substrate.

**UNRESOLVED** - Typed state indicating required evidence is insufficient; never equivalent to safe/admissible.

# Appendix E - Source Concordance

The monograph is grounded primarily in the following source families. Identifiers are human-readable rather than tool-internal.

**S1 - Identity Architecture seed paper.** `identity-architecture-master-paper.txt`, August 15, 2026. Historical conceptual source for professional ego, inherited tradecraft, event-sourced biography, quinary cognition, and digital-organism framing. Several controller/storage assumptions are superseded.

**S2 - Current Identity Architecture implementation guide.** `ammunity/resources/docs/identity_phase1.md`, current through Phase 3B at the inspected repository revision. Defines canonical terminology, G0 semantics, Identity Event Ledger, active TMS projection, HIGC shadow geometry, and current authority boundaries.

**S3 - HIGC Phase 3B contract.** `ammunity/resources/docs/higc_phase3b.md`. Defines geometry states, seven named constraints, precedence, runtime placement, and validation obligations.

**S4 - THDE Phase 3C contract.** `ammunity/resources/docs/thde_phase3c.md`. Defines bounded candidate evaluation, candidate evidence, exact trajectory verification, candidate-specific HIGC, decision semantics, and zero host-mutation authority.

**S5 - G0 implementation.** `ammunity/identity/baseline.py`. Source-level baseline schema, content digest, package/artifact references, private filesystem handling, and atomic no-clobber creation.

**S6 - Identity Event Ledger implementation.** `ammunity/identity/tms.py`. Source-level immutable event schema, content hash, predecessor chaining, locking, verification, and fsync append behavior.

**S7 - Active identity memory implementation.** `ammunity/identity/memory.py`. Source-level replayable projection onto shared TMS and conflict semantics.

**S8 - Deterministic adjudicator.** `ammunity/identity/adjudicator.py`. Current Phase 1 application precedence and failure semantics.

**S9 - HIGC implementation.** `ammunity/identity/higc.py`. Source-level symbolic constraint and aggregate geometry evaluation.

**S10 - THDE implementation.** `ammunity/identity/thde.py`. Source-level candidate/transition contracts, provenance references, classification, and `host_mutation_authorized = false`.

**S11 - Candidate evaluation implementation.** `ammunity/identity/candidate.py`. Source-level candidate digest, explicit hypothetical evidence, trajectory adapter, evaluation envelope, and TOCTOU protection.

**S12 - Identity orchestration service.** `ammunity/identity/service.py`. Current runtime wiring among observations, G0, adjudication, HIGC, ledger, and active TMS.

**S13 - Cyrae-Lite Phase 5 Architecture.** Current discrete bounded recurrence, typed unavailability, HIGC-as-CBF direction, temporal-lineage ownership, RemediationEpisode/RPE requirements, and Phase 5A-5F roadmap.

**S14 - HVD/Nexus 4 master architecture family.** Source for HVD/TMS/HDF5 ownership, database semantics, recursive cognition, and the separation of identity from physical placement/storage sharing.

**S15 - HVD Recursive Cognitive Architecture.** Source for field-based ephemeral HVD relationships, HTCE/TMS addressability, structural sharing, and non-genealogical recursion.

**S16 - AmmunIty Pathology Knowledge Architecture.** Application source for neutral observation semantics and the rule that HVD associative pathology memory remains contextual rather than authoritative.

**S17 - Educated Bookseller / bookstore research family.** Historical application sources for professional tradecraft, domain identity, expression, UI, commercial operation, and financial cybernetics. Used as lineage, not universal authority.

## Repository checkpoint

The latest inspected `main` commit is:

```text
b12eaedc246d872db7f3018fbd1e8fa99083f5ce
Phase 3C: add candidate-specific HIGC trajectory evaluation
```

The commit description states that it adds digest-bound candidate evidence, full verified-trajectory adaptation, explicit hypothetical host identity evaluation, candidate/trajectory/HIGC evaluation envelopes, adversarial regressions, and synchronized Phase 3C documentation while preserving zero state-realization or host-mutation authority.

# Conclusion

Identity Architecture has matured from an application-specific idea about giving a digital worker persistent tradecraft into a much more general systems architecture for **constitutional continuity under change**. Its most important achievement is not any single algorithm. It is the refusal to collapse categories that are easy to conflate.

The constitution is not the current state. Biography is not the current relation graph. Memory is not authority. Similarity is not identity. A database handle is not a self. Physical storage is not continuity. A controller is not a sovereign. A candidate is not an action. A clean observation is not a trustworthy genesis. Missing evidence is not zero. Admissibility is not authorization. And a durable snapshot is not, by itself, proof that the same entity continues.

The current executable architecture already embodies several of those separations: explicit immutable \(G_0\), append-only continuity history, replayable active TMS, symbolic non-compensatory HIGC, digest-bound hypothetical candidates, exact provenance, full trajectory verification, and zero candidate actuation authority. Those mechanisms are modest compared with the ultimate ambitions of Nexus, but they are precisely the kind of modesty a credible identity system needs: authority is added only after evidence and contracts exist.

The next frontier is temporal and transformational. THDE must gain richer bounded-evolution mechanics without becoming an actuator. QMT must define what continuity means across migration and representational change. TMS must expose canonical temporal lineage. The Identity Event Ledger must support remediation episodes and pre-action predictions before Cyrae can calculate genuine causal RPE. Learned local tolerance must become useful without becoming a poisoning channel. Ephemeral HVD fields must support enormous counterfactual search without leaking simulated biography into realized identity.

If those steps succeed, Identity Architecture will not have "proved a soul." It will have done something more concrete and testable: provided a rigorous engineering substrate in which a long-lived digital organism can change, learn, move, recover, and reason counterfactually without silently losing track of what it is, what happened to it, what it is allowed to become, and who has authority to make the change real.

