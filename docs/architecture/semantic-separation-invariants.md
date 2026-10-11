# Canonical Semantic Separation Invariants

**Status:** CANONICAL ARCHITECTURAL INVARIANT  
**Adopted:** 2026-10-11  
**Scope:** Rheo-Chasmar Aeon framework-wide  
**Normative force:** This document constrains subsystem design, implementation,
testing, research interpretation, and application profiles. A subsystem that
silently collapses two categories defined here is architecturally non-conformant.

---

## 1. Canon

Rheo-Chasmar adopts the following separation law:

> **Identity is not state.**  
> **State is not history.**  
> **History is not memory.**  
> **Memory is not evidence.**  
> **Evidence is not similarity.**  
> **Similarity is not truth.**  
> **Truth is not admissibility.**  
> **Admissibility is not desirability.**  
> **Desirability is not authority.**  
> **Cognitive pressure is not action.**

Compactly:

\[
\boxed{
I \not\equiv S \not\equiv H \not\equiv M \not\equiv E
\not\equiv \Sigma \not\equiv T \not\equiv A
\not\equiv D \not\equiv U,\qquad P \not\equiv X
}
\]

The symbols are semantic domains, not scalar variables:

- \(I\): identity;
- \(S\): current state;
- \(H\): historical trajectory;
- \(M\): memory representation;
- \(E\): evidence;
- \(\Sigma\): similarity/retrieval relation;
- \(T\): truth or adjudicated truth-status;
- \(A\): constitutional admissibility;
- \(D\): desirability/homeostatic preference;
- \(U\): authority/permission;
- \(P\): cognitive pressure;
- \(X\): externally or internally committed action.

The chain is **not** a claim that each term is produced by the one immediately
before it. It is a prohibition against semantic collapse.

---

## 2. Why this is canonical

Rheo is deliberately decomposed into subsystems because different questions
require different kinds of answer.

Examples:

- HVD may represent and retrieve.
- TMS may realize and preserve active state and trajectory.
- HTCE may determine active cognitive participation and relevance.
- Cyrae may alter bounded cognitive pressure.
- HIGC may adjudicate constitutional admissibility.
- THDE may govern permitted path-dependent evolution.
- QMT may adjudicate continuity across transformation.
- CA may orchestrate cognition.
- Maera or another actuator may render or execute an authorized result.

No one of those responsibilities creates the others merely by existing.

The semantic-separation law is therefore a framework invariant: **representation,
retention, retrieval, belief, constraint, preference, permission, modulation,
and actuation remain distinct operations.**

---

## 3. Typed-domain rule

Every implementation MUST make cross-domain transitions explicit.

A canonical implementation should behave as though the following types were
non-interchangeable even when represented by the same programming-language
primitive:

\[
\begin{aligned}
&IdentityId \in \mathcal I, \\
&State \in \mathcal S, \\
&History \in \mathcal H, \\
&MemoryRecord \in \mathcal M, \\
&EvidencePacket \in \mathcal E, \\
&SimilarityScore \in \mathcal \Sigma, \\
&TruthStatus \in \mathcal T, \\
&Admissibility \in \mathcal A, \\
&Desirability \in \mathcal D, \\
&AuthorityGrant \in \mathcal U, \\
&CognitivePressure \in \mathcal P, \\
&Action \in \mathcal X.
\end{aligned}
\]

No implicit cast such as the following is permitted:

~~~text
similarity_score > threshold  => TRUE
memory_record_exists          => EVIDENCE
TRUE                          => ADMISSIBLE
ADMISSIBLE                    => DESIRABLE
DESIRABLE                     => AUTHORIZED
high_cognitive_pressure       => EXECUTE
~~~

A transition between domains requires a named operation with declared
provenance, assumptions, uncertainty, failure semantics, and owner.

---

## 4. The ten separations

### 4.1 Identity is not state

A stable logical identity can occupy many states over time:

\[
s_t = \operatorname{Express}(i,t).
\]

Therefore state equality is neither necessary nor sufficient for identity
equality:

\[
i_a=i_b \centernot\Rightarrow s_a=s_b,
\]

and

\[
s_a=s_b \centernot\Rightarrow i_a=i_b.
\]

A restored, migrated, sleeping, degraded, or temporarily quiescent organism may
remain the same logical entity while its current state changes. Conversely, two
distinct HVDs may temporarily contain observationally identical states without
becoming one identity.

QMT continuity, durable logical identifiers, and applicable constitutional
rules—not snapshot equality alone—adjudicate continuity claims.

### 4.2 State is not history

Let a history be a finite trajectory

\[
h=(s_0,\Delta_1,s_1,\ldots,\Delta_n,s_n).
\]

The endpoint projection

\[
\operatorname{end}(h)=s_n
\]

is generally many-to-one: different histories can terminate in the same current
state.

Hence:

\[
\operatorname{end}(h_1)=\operatorname{end}(h_2)
\centernot\Rightarrow h_1=h_2.
\]

Rheo is path-dependent precisely because endpoint equality does not erase
trajectory.

### 4.3 History is not memory

Memory is a retained, encoded, indexed, reconstructed, or consolidated
representation of some historical information:

\[
m = \operatorname{Remember}(h,c),
\]

where \(c\) denotes retention context, schema, salience, compression,
consolidation, or policy.

`Remember` is not assumed injective. Two distinct histories may yield the same
retained memory, and a memory representation may contain derived summaries,
inferences, hypotheses, indexes, or reconstructions that are not themselves raw
historical events.

TMS/HDF5 may preserve enough information to reconstruct portions of history;
that does not make the storage representation identical to the trajectory.

### 4.4 Memory is not evidence

A memory record is not automatically evidentiary.

Memory may contain:

- observations;
- inferences;
- contradicted propositions;
- stale beliefs;
- simulations;
- dreams/counterfactuals;
- summaries;
- cached retrieval results;
- advisory knowledge.

Evidence requires an explicit evidentiary relation to a proposition or state and
must retain provenance sufficient for the applicable adjudicator:

\[
\operatorname{Supports}(e,p,\rho),
\]

where \(e\in\mathcal E\), \(p\) is a proposition, and \(\rho\) is provenance.

Therefore:

\[
m\in\mathcal M \centernot\Rightarrow m\in\mathcal E.
\]

Likewise, fresh evidence can exist before it has been admitted to durable or
active memory.

### 4.5 Evidence is not similarity

Similarity is a relation or score used to compare representations:

\[
\sigma(x,y) \in \mathcal \Sigma.
\]

Evidence is provenance-bearing support for a claim.

A high HVD/ANN/HTLA similarity may retrieve a candidate that has no evidentiary
standing. A low-similarity observation may be decisive evidence for a genuinely
novel condition.

Consequently no threshold \(\theta\) may be treated as a universal evidentiary
rule:

\[
\sigma(x,y)\ge\theta
\centernot\Rightarrow
\operatorname{EvidenceFor}(x,y).
\]

Similarity may help **find** something. It does not, by itself, establish why it
should be believed.

### 4.6 Similarity is not truth

For a proposition \(p\), let \(\tau_W(p)\) denote truth in world/model \(W\), and
let \(\hat\tau(p\mid E)\) denote the system's epistemic/adjudicated status given
evidence \(E\).

Neither is a function of similarity alone.

There exist possible cases with:

\[
\sigma(x,y)\approx 1 \quad \text{and} \quad \tau_W(p)=FALSE,
\]

and cases with:

\[
\sigma(x,y)\ll 1 \quad \text{and} \quad \tau_W(p)=TRUE.
\]

Examples include adversarial lookalikes, benign analogues, unprecedented true
events, and genuinely novel observations.

Rheo implementations should normally persist evidence, provenance, and
epistemic status rather than pretending to possess omniscient access to
\(\tau_W\).

### 4.7 Truth is not admissibility

Truth answers a semantic/epistemic question:

> Is proposition \(p\) true, false, unknown, contradicted, or otherwise
> adjudicated?

HIGC admissibility answers a constitutional question:

> May state, transition, or action \(x\) exist within the applicable
> constitutional geometry?

These functions have different domains:

\[
\tau : \mathcal P_{rop} \rightarrow \mathcal T,
\]

\[
\alpha_G : \mathcal C \rightarrow
\{ADMISSIBLE,BOUNDARY,OUTSIDE,UNRESOLVED\}.
\]

A true fact can describe a prohibited state or action. A false hypothesis can be
admissible to consider inside an exploratory cognitive field. Truth therefore
does not confer constitutional permission.

### 4.8 Admissibility is not desirability

Let the HIGC-admissible region be

\[
\mathcal G_A = \{x\mid \alpha_G(x)=ADMISSIBLE\}.
\]

Let desirability/homeostatic value be

\[
d_c : \mathcal C \rightarrow \mathcal D
\]

for cognitive/application context \(c\).

Typically many points in \(\mathcal G_A\) have different desirability:

\[
x,y\in\mathcal G_A,\quad d_c(x)\ne d_c(y).
\]

A state can be constitutionally legal yet operationally poor, risky, inefficient,
uncomfortable, or far from a Cyrae value attractor.

Conversely an apparently desirable outcome can be constitutionally prohibited.

For a Cyrae value anchor \(H_{val}\), the safe relation is conceptually:

\[
H_{val}\in\mathcal G_A,
\]

not:

\[
H_{val}=\mathcal G_A.
\]

The attractor is a preferred condition inside the allowable region; it is not
the constitutional region itself.

### 4.9 Desirability is not authority

Preference does not create permission.

Let

\[
\operatorname{Auth}(u,a,c)\in\{0,1\}
\]

denote whether principal/capability \(u\) authorizes action \(a\) in context
\(c\).

Then, for any desirability score \(d_c(a)\),

\[
d_c(a) \centernot\Rightarrow \operatorname{Auth}(u,a,c)=1.
\]

The same desired action may be authorized for one actor and prohibited for
another. A highly desirable action may still require explicit user approval,
constitutional delegation, safety certification, or an actuator-specific grant.

### 4.10 Cognitive pressure is not action

Cyrae and related control systems may produce bounded pressures that alter the
conditions of cognition:

\[
\pi_t \in \mathcal P.
\]

These pressures may modulate HTCE quantities such as attention, inhibition,
salience, competition, exploration, damping, trajectory length, or abstention
pressure.

They do not constitute an action:

\[
\pi_t \centernot\Rightarrow a_t\in\mathcal X.
\]

A conformant actuation path requires an explicit proposal and all applicable
gates. At minimum, for consequential actions:

\[
Execute(a)
\Rightarrow
Proposed(a)
\land EvidenceSufficient(a)
\land Admissible(a)
\land Authorized(a)
\land ActuatorGate(a).
\]

Cyrae may alter the probability or priority with which candidates are considered:

\[
P(Candidate(a)\mid \pi_t),
\]

but it may not be silently identified with:

\[
P(Execute(a)\mid \pi_t).
\]

This is the formal version of the architectural statement:

> **Cyrae changes the physics of cognition; it does not independently speak,
> authorize, or act.**

---

## 5. Non-compensation rule

Constitutional constraints are non-compensatory.

If any HIGC constraint is violated,

\[
\exists j:\;c_j=VIOLATED
\Rightarrow
\alpha_G(x)=OUTSIDE,
\]

independently of desirability, similarity, reward alignment, Cyrae pressure, or
other favorable scores:

\[
\alpha_G(x)=OUTSIDE
\quad \forall d_c(x),\sigma,\pi.
\]

No amount of “good” similarity, utility, novelty, confidence, or homeostatic
pressure may average away a constitutional violation.

---

## 6. Explicit-morphism rule

Rheo allows information to move between semantic domains, but every such move
must be explicit.

Examples:

\[
H \xrightarrow{\operatorname{retain}} M
\]

\[
E \xrightarrow{\operatorname{adjudicate}} \hat T
\]

\[
S \xrightarrow{\operatorname{HIGC}} A
\]

\[
S \xrightarrow{\operatorname{value}} D
\]

\[
P \xrightarrow{\operatorname{modulate}} HTCE
\]

\[
Candidate \xrightarrow{\operatorname{authorize+gate}} X
\]

Each morphism must declare:

1. source and target domain;
2. owning subsystem;
3. assumptions;
4. provenance inputs;
5. uncertainty/failure semantics;
6. whether it is lossy;
7. whether it is reversible/rebuildable;
8. whether it creates authority (normally it must not);
9. tests proving that adjacent semantic categories are not silently collapsed.

---

## 7. Subsystem consequences

### HVD / HTLA / ANN

- Similarity retrieves candidates; it does not establish truth.
- A nearest neighbor is not evidence merely because it is near.
- Exact database identity is not inferred from vector similarity.

### TMS / HDF5

- Retention and reconstruction do not make memory equal history.
- Physical realization does not define logical identity.
- Replay is a reconstruction mechanism, not a license to rewrite provenance.

### HTCE

- Relevance, resonance, and candidate survival are cognitive-field operations,
  not truth or authority grants.
- A collapsed cognitive candidate still requires downstream constitutional and
  authority checks where applicable.

### Cyrae / TUCR

- Homeostatic desirability and cognitive pressure remain bounded regulatory
  quantities.
- They cannot override HIGC, create evidence, create authority, or execute
  consequential actions.

### HIGC

- Admissibility is constitutional, non-compensatory, and separate from truth and
  desirability.
- `UNRESOLVED` must not be coerced to `ADMISSIBLE`.

### THDE

- Historical trajectory can constrain how state may evolve without turning
  history into identity.
- Hysteresis is path dependence, not constitutional truth.

### QMT / Identity Architecture

- Continuity adjudication may use history, memory, constitution, and
  transformation evidence, but none of those inputs is individually identical
  to identity.

### CA / Maera / Actuators

- Orchestration and rendering do not acquire authority by fluency, confidence,
  similarity, desirability, or Cyrae pressure.
- Consequential action requires an explicit authority boundary.

---

## 8. Architectural review checklist

A design review MUST ask:

1. Has a memory record been treated as evidence without provenance?
2. Has an ANN/HTLA similarity score been treated as truth?
3. Has truth been treated as constitutional permission?
4. Has HIGC admissibility been treated as utility/desirability?
5. Has desirability been treated as authorization?
6. Has Cyrae pressure been wired directly to actuation?
7. Has a current snapshot been treated as identity or complete history?
8. Has a storage representation been treated as the historical trajectory
   itself?
9. Has any subsystem acquired authority merely because it computed a score?
10. Is every cross-domain conversion named and testable?

Any “yes” is a separation violation requiring correction or an explicit
architecture decision that supersedes this canon.

---

## 9. Proof and verification companion

The formal non-equivalence results, countermodels, and property-based proof
obligations are specified in:

`docs/mathematics/semantic-separation-theorems.md`

The architecture decision adopting this canon is recorded in:

`docs/adr/0002-semantic-separation-canon.md`

These documents form one normative package.
