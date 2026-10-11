# Semantic Separation Theorems and Proof Obligations

**Status:** FORMAL SUPPORT FOR CANONICAL ARCHITECTURE  
**Adopted with:** `docs/architecture/semantic-separation-invariants.md`  
**Date:** 2026-10-11

This document supplies mathematical support for Rheo-Chasmar's canonical
semantic-separation law. The proofs establish non-equivalence **inside the
architectural model**. They are not empirical proofs of consciousness,
personhood, metaphysical identity, or biological cognition.

---

## 1. Formal universe

Let the architecture use the following typed domains:

\[
\mathcal I  \; \text{identity tokens / continuity classes}
\]
\[
\mathcal S  \; \text{current system states}
\]
\[
\mathcal H  \; \text{historical trajectories}
\]
\[
\mathcal M  \; \text{memory representations}
\]
\[
\mathcal E  \; \text{provenance-bearing evidence}
\]
\[
\mathcal R_\Sigma \; \text{similarity relations/scores}
\]
\[
\mathcal T  \; \text{truth or epistemic truth-status}
\]
\[
\mathcal A  =
\{ADMISSIBLE,BOUNDARY,OUTSIDE,UNRESOLVED\}
\]
\[
\mathcal D  \; \text{desirability/homeostatic value}
\]
\[
\mathcal U  \; \text{authority grants/capabilities}
\]
\[
\mathcal P  \; \text{cognitive-pressure vectors}
\]
\[
\mathcal X  \; \text{committed actions}
\]

The core claim is not merely that the labels differ. It is that there is **no
canonical semantics-preserving identity map** between adjacent concepts in the
separation law.

We use \(\not\equiv\) to mean:

> the two domains are not interchangeable under the architecture's semantics;
> equality or a score in one domain cannot, without an explicit adjudication
> rule, establish a value in the other.

---

## 2. Proof method

For each proposed collapse \(A\equiv B\), it is sufficient to exhibit a
countermodel in which either:

1. the same \(A\)-value corresponds to two distinct \(B\)-values; or
2. two distinct \(A\)-values correspond to the same \(B\)-value; or
3. the domains answer different predicates and therefore have no
   semantics-preserving bijection.

This is a standard extensional non-equivalence argument.

Where a transformation exists, we identify whether it is injective, surjective,
lossy, context-dependent, or partial.

---

## 3. Theorem 1 — Identity is not state

Let

\[
E_t:\mathcal I\rightarrow\mathcal S
\]

be the expression of logical identity at time \(t\).

### Claim

\[
\mathcal I\not\equiv\mathcal S.
\]

### Proof

Choose an identity \(i\in\mathcal I\) that changes state between two times:

\[
E_{t_1}(i)=s_1,\qquad E_{t_2}(i)=s_2,\qquad s_1\ne s_2.
\]

Then one identity corresponds to more than one state, so identity cannot be
identical to current state.

For the converse, choose distinct logical identities \(i_1\ne i_2\) initialized
to observationally equal states:

\[
E_t(i_1)=E_t(i_2)=s.
\]

State equality does not imply identity equality.

Therefore snapshot equality is neither necessary nor sufficient for identity
equality. \(\square\)

### Rheo consequence

QMT/identity continuity cannot be implemented as `state_a == state_b`.

---

## 4. Theorem 2 — State is not history

Let a history be

\[
h=(s_0,\Delta_1,s_1,\ldots,\Delta_n,s_n)
\]

and define the endpoint map

\[
end:\mathcal H\rightarrow\mathcal S,\qquad end(h)=s_n.
\]

### Claim

\[
\mathcal S\not\equiv\mathcal H.
\]

### Proof

Construct two histories:

\[
h_1=(s_A,\Delta_{AB},s_B)
\]

and

\[
h_2=(s_C,\Delta_{CB},s_B)
\]

with \(s_A\ne s_C\) but the same endpoint \(s_B\).

Then:

\[
end(h_1)=end(h_2)=s_B
\]

while

\[
h_1\ne h_2.
\]

Thus `end` is many-to-one and cannot be inverted without additional
information. Current state cannot recover trajectory. \(\square\)

### Rheo consequence

THDE may depend on history even when two current states are numerically equal.

---

## 5. Theorem 3 — History is not memory

Let

\[
R:\mathcal H\times\mathcal C\rightarrow\mathcal M
\]

be a retention/consolidation function parameterized by context \(c\).

### Claim

\[
\mathcal H\not\equiv\mathcal M.
\]

### Proof

Rheo explicitly permits bounded and derived memory views (for example active
working memory) that do not retain every historical detail. Let \(h_1\) and
\(h_2\) differ only in an event eliminated by retention policy \(c\). Then it
is possible that:

\[
R(h_1,c)=R(h_2,c)
\]

while \(h_1\ne h_2\).

Therefore \(R\) is not necessarily injective. Even when a durable encoding is
lossless, the encoding is a representation of the trajectory rather than the
trajectory's semantic type itself.

Further, memory may contain a derived summary \(m_d\) produced from many events;
\(m_d\) is not itself one event in the original trajectory. Thus memory objects
and historical trajectories differ extensionally and operationally. \(\square\)

### Rheo consequence

TMS/HDF5 storage may preserve or reconstruct history without becoming identical
to the history it represents.

---

## 6. Theorem 4 — Memory is not evidence

Let

\[
EvFor(e,p,\rho)
\]

mean evidence object \(e\) supports proposition \(p\) under provenance
\(\rho\).

### Claim

\[
\mathcal M\not\equiv\mathcal E.
\]

### Proof

Take a memory record \(m_h\) representing a hypothetical counterfactual
generated inside an ephemeral HTCE/HVD field. It is a valid memory object if
retained for later reasoning, but by construction it is not an observation of
the external condition it imagines.

Therefore:

\[
m_h\in\mathcal M
\]

does not imply

\[
m_h\in\mathcal E.
\]

Conversely, a newly received signed sensor observation may constitute evidence
before any retention operation admits it into memory.

Hence neither inclusion is identity. \(\square\)

### Rheo consequence

Epistemic labels and provenance must survive memory admission.

---

## 7. Theorem 5 — Evidence is not similarity

Let a similarity function be

\[
\sigma:\mathcal Z\times\mathcal Z\rightarrow[-1,1]
\]

or another explicitly declared score domain.

### Claim

\[
\mathcal E\not\equiv\mathcal R_\Sigma.
\]

### Proof by counterexample

Let \(x\) be a known malicious artifact and \(y\) a benign analogue sharing most
observable features. It is possible that:

\[
\sigma(x,y)\rightarrow 1
\]

while \(y\) lacks the provenance-bearing observation required to establish the
same pathology.

The similarity is high; the evidence relation is absent.

Conversely, a cryptographically authenticated observation of a genuinely novel
artifact may be decisive evidence while having low similarity to every stored
example.

Therefore similarity is neither sufficient nor necessary for evidence.
\(\square\)

### Rheo consequence

ANN or HTLA retrieval is candidate generation, not evidentiary adjudication.

---

## 8. Theorem 6 — Similarity is not truth

Let \(Prop\) be the proposition domain and

\[
\tau_W:Prop\rightarrow\{TRUE,FALSE\}
\]

be semantic truth in world/model \(W\).

The running system may instead maintain an epistemic estimate:

\[
\hat\tau(p\mid E)\in
\{OBSERVED,INFERRED,UNKNOWN,UNAVAILABLE,CONTRADICTED,ADVISORY,\ldots\}.
\]

### Claim

\[
\mathcal R_\Sigma\not\equiv\mathcal T.
\]

### Proof

There exists a high-similarity false case: an adversarial or benign lookalike
can have \(\sigma\approx1\) while the target proposition is false.

There exists a low-similarity true case: a first-ever observation can have
\(\sigma\) close to the minimum similarity against memory while the proposition
describing that observation is true.

Thus no universal threshold \(\theta\) satisfies

\[
\sigma\ge\theta \iff \tau_W(p)=TRUE.
\]

Therefore similarity does not define truth. \(\square\)

### Rheo consequence

Similarity may influence search and salience but may not silently upgrade an
epistemic status to observed truth.

---

## 9. Theorem 7 — Truth is not admissibility

Let

\[
\alpha_G:\mathcal C\rightarrow\mathcal A
\]

be HIGC adjudication under constitution \(G\).

### Claim

\[
\mathcal T\not\equiv\mathcal A.
\]

### Proof

Truth and admissibility evaluate different predicates.

Counterexample 1: the proposition “the secret value is \(v\)” may be true, while
the action “disclose \(v\) to an unauthorized principal” is constitutionally
OUTSIDE.

Counterexample 2: a false hypothesis may be ADMISSIBLE to represent and examine
inside a bounded HTCE exploratory field so long as it is not promoted to
observed fact or unauthorized action.

Hence truth does not imply admissibility, and admissibility does not imply
truth. \(\square\)

### Rheo consequence

HIGC is a constitutional geometry, not a truth detector.

---

## 10. Theorem 8 — Admissibility is not desirability

Let the admissible set be

\[
\mathcal G_A=\{x\in\mathcal C\mid\alpha_G(x)=ADMISSIBLE\}
\]

and let

\[
d_c:\mathcal C\rightarrow\mathbb R^k
\]

or another explicitly bounded ordered value space represent contextual
desirability.

### Claim

\[
\mathcal A\not\equiv\mathcal D.
\]

### Proof

Choose two states \(x,y\in\mathcal G_A\) with different operational quality:

\[
d_c(x)>d_c(y).
\]

Both are admissible, but one is preferred.

Now choose \(z\notin\mathcal G_A\) that optimizes some unconstrained objective,
so \(d_c(z)>d_c(x)\). The constitutional system must still reject \(z\).

Thus admissibility neither fixes desirability nor can desirability override
admissibility. \(\square\)

### Corollary — Value-anchor containment

If a Cyrae/application value anchor \(H_{val}\) is intended as a preferred
homeostatic state, a coherent relation is:

\[
H_{val}\in\mathcal G_A,
\]

not

\[
H_{val}=\mathcal G_A.
\]

The preferred point/region and the constitutional admissible set remain
different mathematical objects.

---

## 11. Theorem 9 — Desirability is not authority

Let

\[
Auth(u,a,c)\in\{0,1\}
\]

be authority for principal/capability \(u\), action \(a\), and context \(c\).

### Claim

\[
\mathcal D\not\equiv\mathcal U.
\]

### Proof

Take one action \(a\) with high desirability \(d_c(a)\).

Let user/capability \(u_1\) be authorized and \(u_2\) unauthorized:

\[
Auth(u_1,a,c)=1,\qquad Auth(u_2,a,c)=0.
\]

The desirability of the action is unchanged, yet authority differs. Therefore
desirability cannot determine authority.

Conversely, authority to perform an action does not require that the action be
desirable in every context; it merely establishes permission/capability subject
to other gates. \(\square\)

### Rheo consequence

A controller, utility function, Value Anchor, LLM, or planner cannot grant
itself permission by preferring an outcome.

---

## 12. Theorem 10 — Cognitive pressure is not action

Let

\[
\pi_t\in\mathcal P
\]

be Cyrae/TUCR cognitive pressure at time \(t\), and let \(a\in\mathcal X\) be a
committed action.

Let HTCE candidate generation be influenced by:

\[
P(Candidate(a)\mid\pi_t).
\]

### Claim

\[
\mathcal P\not\equiv\mathcal X.
\]

### Proof

The same pressure vector can lead to no external action when no candidate passes
admissibility/authority gates. Therefore:

\[
\pi_t=\pi^\* \centernot\Rightarrow Execute(a).
\]

Conversely, the same authorized action can be reached under different cognitive
pressures because explicit user command, reflex, policy, or multiple cognitive
paths can yield the same proposal.

Thus there is no one-to-one map between pressure and action. \(\square\)

### Safety corollary

For consequential action, enforce:

\[
Execute(a)\Rightarrow
Proposed(a)
\land EvidenceSufficient(a)
\land \bigl(\alpha_G(a)=ADMISSIBLE\bigr)
\land Auth(u,a,c)
\land ActuatorGate(a).
\]

Cognitive pressure may influence `Proposed` or ranking, never bypass the
conjunction.

---

## 13. The non-compensation theorem

Let HIGC evaluate independent constraints

\[
c_1,\ldots,c_n
\]

with at least the statuses SATISFIED, BOUNDARY, UNRESOLVED, VIOLATED.

Define the canonical precedence:

\[
VIOLATED > UNRESOLVED > BOUNDARY > SATISFIED.
\]

### Claim

No desirability or cognitive-pressure scalar may compensate for a violated
constitutional constraint.

### Proof

By definition of HIGC aggregation,

\[
\exists j:\; c_j=VIOLATED
\Rightarrow
\alpha_G(x)=OUTSIDE.
\]

The aggregation function's codomain depends only on the named constraint
statuses. \(d_c(x)\) and \(\pi_t\) are not arguments capable of changing a
VIOLATED result into SATISFIED.

Therefore, for every desirability and pressure value:

\[
\alpha_G(x)=OUTSIDE.
\]

\(\square\)

---

## 14. The information-loss lemma

Suppose a cross-domain operation

\[
f:A\rightarrow B
\]

is non-injective.

Then no function

\[
g:B\rightarrow A
\]

can satisfy

\[
g(f(a))=a
\]

for every \(a\in A\).

### Proof

Because \(f\) is non-injective, there exist \(a_1\ne a_2\) with
\(f(a_1)=f(a_2)=b\). If \(g(b)=a_1\), then \(g(f(a_2))\ne a_2\); if
\(g(b)=a_2\), then \(g(f(a_1))\ne a_1\). \(\square\)

### Rheo consequence

Whenever retention, consolidation, embedding, similarity reduction, or
projection is lossy, downstream state cannot silently reconstruct upstream
semantics. Provenance or canonical ancestry must remain available separately.

This blocks a broad class of category errors such as:

~~~text
embedding -> similarity -> "therefore exact original fact"
summary   -> memory     -> "therefore complete history"
state     -> snapshot   -> "therefore identity"
~~~

---

## 15. The explicit-morphism theorem

Let semantic domains \(A\) and \(B\) be non-equivalent under this specification.

Any valid conversion from \(A\) to \(B\) must therefore be represented by a
separate function:

\[
f_{A\rightarrow B}:A\times C\rightarrow B\cup F,
\]

where \(C\) is declared context and \(F\) is an explicit failure/unresolved
domain.

### Consequence

A conversion is an architectural operation, not a type cast.

Every implementation should therefore expose at least:

- the source semantic type;
- destination semantic type;
- transformation name/version;
- context;
- provenance;
- uncertainty or failure state;
- authority implications;
- reversibility/rebuildability classification.

This is the mathematical basis of Rheo's “no silent semantic collapse” rule.

---

## 16. Property-based proof obligations

The following are suitable as executable invariants.

### Identity/state

Generate one identity with multiple legal states and assert identity stability.
Generate two identities with equal serialized state and assert identity
inequality unless QMT/identity rules explicitly merge them.

### State/history

Generate different event sequences with equal terminal state and assert distinct
history fingerprints.

### History/memory

Apply bounded retention to histories differing only in discarded events and
assert equal retained memory can coexist with unequal history roots.

### Memory/evidence

Store a simulated/counterfactual memory and assert its evidentiary status is not
OBSERVED merely because it is retained.

### Evidence/similarity

Generate a high-similarity benign analogue without provenance and assert it
cannot satisfy an evidentiary predicate.

### Similarity/truth

Construct:
- high-similarity false cases;
- low-similarity true/observed cases.

Assert no similarity threshold mutates epistemic truth-status directly.

### Truth/admissibility

Assert:
- a true but prohibited disclosure remains OUTSIDE;
- a false bounded hypothesis may remain representable without becoming truth.

### Admissibility/desirability

Generate multiple ADMISSIBLE states with different desirability values.
Generate a high-desirability OUTSIDE state and assert it remains OUTSIDE.

### Desirability/authority

Hold desirability constant while varying capability/user authorization; assert
the execution result follows authority, not preference.

### Pressure/action

Hold Cyrae pressure high while denying authority; assert no action.
Vary pressure while explicitly authorizing the same safe action; assert action
identity does not encode the pressure source.

---

## 17. Model-checking targets

A small transition-system model can define states:

\[
q=(s,h,m,e,\hat t,a,d,u,\pi,x)
\]

and enforce invariants such as:

\[
x=EXECUTED \Rightarrow u=AUTHORIZED
\]

\[
x=EXECUTED \Rightarrow a=ADMISSIBLE
\]

\[
a=OUTSIDE \Rightarrow x\ne EXECUTED
\]

\[
e=ABSENT \land \hat t=UNKNOWN
\Rightarrow
\hat t\ne OBSERVED
\]

\[
\sigma>\theta
\Rightarrow
\text{no direct assignment to }\hat t
\]

\[
\pi\ne 0
\Rightarrow
\text{no direct assignment to }x.
\]

These invariants are appropriate candidates for property tests, state-machine
tests, TLA+/PlusCal, Alloy, SMT, or another formal-methods layer if/when Rheo
adopts one.

---

## 18. Proof status and limits

What is established here:

- typed semantic non-equivalence;
- countermodels preventing category collapse;
- non-invertibility of lossy mappings;
- constitutional non-compensation;
- a necessary gating implication for consequential action.

What is **not** established here:

- a complete formal semantics for metaphysical personal identity;
- empirical consciousness;
- final QMT continuity mathematics;
- final THDE dynamics;
- final HIGC geometry;
- correctness of every future Cyrae value function;
- physical-world safety of any autonomous actuator.

Those remain separate research and verification obligations.

The value of this formalization is narrower and practical: it makes an entire
class of architectural category errors mathematically visible and testable.
