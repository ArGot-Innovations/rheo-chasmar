# Hypervector Linear Transdimensional Algebra (HTLA)

## Labeled Direct-Sum Calculus, Recoverability Contracts, and Quinary Reference Semantics for Project Nexus 4

**Document class:** Tier-2 subsystem-math source  
**Corpus role:** S8 replacement candidate  
**Reference edition:** 2026-08-31  
**Architectural scope:** Project Nexus 4 / HVD / HTNLA interface  
**Authority rule:** This document supplies subsystem mathematics and engineering contracts. It is subordinate to Tier-0 Nexus architecture wherever a conflict exists.

---

## Abstract

Hypervector Linear Transdimensional Algebra (HTLA) is the labeled-state linear calculus used by Project Nexus 4 to represent and transform heterogeneous finite-dimensional state without erasing the semantic boundaries between its components. Its core state object is a finite external direct sum

\[
\mathcal H_L=\bigoplus_{\ell\in L}\mathbb R^{n_\ell},
\]

where each label \(\ell\) identifies a component space with its own dimension and interpretation. Linear transformations between labeled direct sums are represented as typed block operators. Their endomorphism structure admits a Peirce decomposition induced by the canonical component projections; equivalently, the label-indexed hom-spaces form a finite real-linear preadditive category, a special case of the "ring with several objects" viewpoint.

The mathematical ingredients used by HTLA—finite direct sums, block matrices, bilinear forms, singular-value decomposition, regularized inverse maps, Johnson-Lindenstrauss embeddings, and concentration inequalities—are established mathematics. HTLA does not claim otherwise. Its system-level contribution is the disciplined assembly of those tools into a labeled mathematical ABI for Nexus, together with explicit semantic typing, typed missingness, transformation provenance, recoverability contracts, and compatibility with the deterministic quinary reference geometry used by the current Nexus v4 demonstrator.

That reference geometry uses the alphabet

\[
\mathcal Q=\{-2,-1,0,+1,+2\}
\]

on \(d=1024\) coordinates, represented by sign and magnitude bit planes with structural invariants, a reference occupancy wall \(K_{\mathrm{wall}}=307\), and an intentionally information-losing binding operation. Partial recovery is therefore not represented as an unqualified inverse. A coordinate-level recovery attempt terminates as `EXACT`, `AMBIGUOUS`, `UNKNOWN`, or `IMPOSSIBLE`.

This paper gives that four-way outcome a formal home rather than leaving it as a labeled list. Section 7.5 shows that coordinate-level recovery states form a refinement lattice of possibility sets, in the same technical sense used for domain reduction in constraint satisfaction (Mackworth, 1977) and for approximation semantics in abstract interpretation (Cousot & Cousot, 1977); classifies the reference binding rule's outcomes exhaustively rather than by example; and proves a monotonicity property under binder uncertainty. That property gives several of this paper's failure modes—rank-loss laundering, regularization laundering, derived-index authority escalation—a single formal description: each is an instance of a mechanism reporting a more determinate outcome than its input epistemic state permits. This is the one place in the paper where a genuinely new, if narrow, mathematical object is introduced for Nexus rather than an established one applied; it is held to the same evidentiary standard as everything else here—construction, exhaustive or proved verification, and an entry in the claim-status audit.

This paper also corrects several historical HTLA claims that do not survive mathematical or executable scrutiny. In particular, it retires the description of the block structure as a generic graded algebra without a grading law; removes a backwards "faithful but not full" categorical claim; distinguishes inner products from semidefinite or directed compatibility scores; replaces an incorrect numerical worked example with executed values; repairs the source/target variance of the labeled pseudoinverse implementation; scopes Johnson-Lindenstrauss results to finite-set distortion rather than lossless dimensional conversion; restores the linear-in-\(t\) operator-norm branch of the Hanson-Wright inequality; and treats logarithmic gradient complexity, quantum acceleration, persistent topology, Fisher-Rao geometry, gauge-equivariant extensions, Neural-ODE variants, and spacetime analogies as research hypotheses unless separately established.

The result is a conservative subsystem specification: mathematically ordinary where the mathematics is ordinary, exact and checked where this paper adds something new at the epistemic layer, and falsifiable wherever implementation or performance claims extend beyond standard theory.

---

## Claim-status vocabulary

This document uses the project-wide vocabulary exactly as defined by the Nexus corpus:

`CANONICAL`, `IMPLEMENTED`, `VERIFIED`, `PARTIALLY IMPLEMENTED`, `ACTIVE DEVELOPMENT`, `PROPOSED`, `DESIGN TARGET`, `EXPERIMENTAL`, `RESEARCH HYPOTHESIS`, `APPLICATION-SPECIFIC`, `HISTORICAL/SUPERSEDED`, `INFERRED`.

A Tier-2 paper does not promote its own local claims into Tier-0 canon. `CANONICAL` is used here only for contracts already established by the higher-tier Nexus architecture. `VERIFIED` is reserved for standard mathematical results, direct proofs, or specific executed artifacts identified in this paper.

---

# 1. Architectural Role and Scope

HTLA is the stable **linear mathematical ABI** between heterogeneous Nexus state and the operators that act on that state.

Within the current Nexus decomposition, HTLA does not own cognition, constitutional admissibility, temporal evolution, substrate realization, durable persistence, or identity. Those responsibilities belong to other layers. HTLA instead answers a narrower family of questions:

1. How can one logical state contain components of different dimensions without pretending they share one undifferentiated coordinate system?
2. How are linear mappings between those components typed and composed?
3. How are cross-label similarities or compatibilities defined without silently inventing semantic equivalence?
4. How are dimension-changing transformations represented when they are approximate or information-losing?
5. How is approximation error retained as an explicit contract?
6. How does the linear layer interface with the current quinary reference geometry?
7. Where does linear HTLA stop and nonlinear HTNLA begin?

Conceptually:

```text
heterogeneous labeled state
          |
          v
        HTLA
  direct sums + typed
   block linear maps
          |
          +------> similarity / compatibility
          |
          +------> dimension-changing morphisms
          |
          +------> low-rank approximation
          |
          +------> recoverability metadata
          |
          v
        HTNLA
 nonlinearities / competition /
 nonlinear associative transforms
```

The phrase **mathematical ABI** is intentional but limited. HTLA is not itself a binary file format. It is a stable semantic interface: a consumer should be able to determine the labels, component dimensions, permitted mappings, transformation provenance, approximation assumptions, and recoverability semantics even if the physical representation changes.

Accordingly:

```text
HTLA semantics != physical storage encoding
HTLA label     != memory address
HTLA similarity != identity
HTLA similarity != truth
HTLA reconstruction != proof of continuity
```

TMS may move or reorganize the physical realization of state while preserving the HTLA contract. ANN/HNSW may accelerate retrieval over derived embeddings, but approximate-nearest-neighbor rank does not become an HTLA truth condition.

---

# 2. Relationship to Prior Art

## 2.1 Finite direct sums and block linear algebra

The state space

\[
\bigoplus_{\ell\in L}\mathbb R^{n_\ell}
\]

and the corresponding block representation of linear maps are standard finite-dimensional linear algebra. HTLA does not introduce direct sums or block matrices.

The relevant design decision is to preserve the decomposition as part of the software-visible semantic contract rather than flatten it away and reconstruct its meaning from undocumented offsets.

Because \(L\) is finite,

\[
\bigoplus_{\ell\in L}\mathbb R^{n_\ell}
\cong
\prod_{\ell\in L}\mathbb R^{n_\ell}
\cong
\mathbb R^N,
\qquad
N=\sum_{\ell\in L}n_\ell,
\]

after an ordering of labels is chosen.

Therefore HTLA does **not** depend on the false proposition that heterogeneous state cannot be flattened. It depends on the stronger engineering requirement that flattening must not erase the component schema.

```text
flattenable != semantically interchangeable
```

## 2.2 Named Tensor Notation and labeled arrays

Named Tensor Notation, introduced by Chiang, Rush, and Barak, attaches names to tensor axes so that operations can refer to semantic axes rather than absolute positions. That work is close prior art for the principle that shape metadata changes the meaning and safety of numerical operations.

HTLA makes a different primary modeling choice: its top-level object is a direct sum of independently typed component spaces, and its linear morphisms are source-label-to-target-label blocks. Named tensors can encode or emulate such layouts by convention, so this distinction should not be overstated as an impossibility result. The defensible difference is that direct-sum component identity, block coupling, typed missingness, and the Nexus recoverability contract are intrinsic to HTLA's subsystem interface rather than being conventions layered on ordinary tensor axes.

Scientific-array libraries such as xarray and unit-aware systems such as Pint are useful engineering analogies for the same reason: labels and metadata constrain meaningful operations. They are not the mathematical foundation of HTLA.

## 2.3 Peirce decomposition and rings with several objects

The historical HTLA description of its label-block structure as a generic "graded \(\mathbb R\)-algebra" is retired. A grading in the usual algebraic sense requires a degree structure and a compatible multiplication law. A bare semantic label set supplies neither.

The appropriate structure arises from the canonical label projections. Let

\[
e_\ell:\mathcal H\to\mathcal H
\]

project onto component \(\ell\) and include the result back into \(\mathcal H\). These satisfy

\[
e_\ell^2=e_\ell,
\qquad
e_\ell e_m=0 \quad (\ell\neq m),
\qquad
\sum_{\ell\in L}e_\ell=I.
\]

The endomorphism ring then decomposes into corners

\[
\operatorname{End}(\mathcal H)
=
\bigoplus_{t,s\in L}
e_t\operatorname{End}(\mathcal H)e_s.
\]

This is the Peirce decomposition associated with the complete orthogonal idempotent family.

Equivalently, the labels may be treated as objects of a finite real-linear preadditive category with

\[
\operatorname{Hom}(s,t)
=
\operatorname{Lin}(\mathbb R^{n_s},\mathbb R^{n_t})
\cong
\mathbb R^{n_t\times n_s}.
\]

This is the structure Barry Mitchell described in the "ring with several objects" framework. HTLA specializes that established structure to Nexus labeled state; it does not claim to originate it.

## 2.4 Hyperdimensional computing and vector symbolic architectures

Hyperdimensional Computing (HDC) and Vector Symbolic Architectures (VSA) provide the broad prior-art context for high-dimensional symbolic representation, binding, bundling, similarity retrieval, and approximate unbinding. Kanerva's HDC work, Plate's Holographic Reduced Representations, and later comparative VSA literature all establish that high-dimensional binding schemes differ in their algebraic properties and that unbinding can be approximate or non-self-inverse.

The current Nexus contribution is therefore not the discovery that binding can lose information. It is the software and epistemic decision to **surface the degree of recoverability explicitly** rather than return a numerically plausible vector and let downstream code mistake approximation for knowledge.

The current quinary reference contract reports:

```text
EXACT
AMBIGUOUS
UNKNOWN
IMPOSSIBLE
```

for partial recovery. That status layer is Nexus-specific application semantics over a broader VSA/HDC context.

## 2.5 What this paper claims as the subsystem contribution

Consider a telemetry pipeline in which one sensor stops reporting because it has failed, while every other sensor continues to report a genuine reading of zero. A flattened, unlabeled numerical representation cannot distinguish these cases: both arrive as a zero in the same slot, and a dense kernel downstream treats a dead sensor as a confirmed observation of nothing wrong. Section 3.4's typed missingness exists specifically so this distinction survives the representation. The same discipline has a second, sharper consequence for retrieval: an indefinite or asymmetric cross-label compatibility score (Section 5.3) is not a merely fussy classification if it is fed into a nearest-neighbor index such as HNSW that assumes a true metric space. The triangle inequality the index relies on need not hold for such a score, and the index can then return the wrong neighbors with no error raised anywhere. Neither failure is exotic; both are the ordinary way heterogeneous state quietly breaks once its labels and its uncertainty stop being carried through the computation.

The defensible contribution is the assembly that closes failures of this kind:

- finite labeled direct-sum state as the stable Nexus linear ABI;
- typed source/target block mappings;
- explicit semantic coupling rather than accidental flattening;
- typed distinction between zero and missing/unavailable state;
- explicit transform provenance and distortion contracts;
- a deterministic quinary reference representation;
- coordinate-level partial-unbind epistemic states;
- executable reference behavior and falsification-oriented tests.

No claim is made that direct sums, block matrices, SVD, random projections, pseudoinverses, Peirce decompositions, or concentration inequalities are individually new. The one component of this assembly that is not simply an established tool applied carefully is the formal treatment of the partial-unbind epistemic states in Section 7.5: there, the four recovery outcomes are given a lattice structure, an exhaustively verified classification against the reference binding rule, and a proved monotonicity property, rather than being left as a labeled list.

---

# 3. Labeled Direct-Sum State

## 3.1 Component schema

Let \(L\) be a finite ordered set of semantic labels. For each label \(\ell\in L\), define a component space

\[
V_\ell=\mathbb R^{n_\ell},
\qquad
n_\ell\in\mathbb N.
\]

The HTLA state space is

\[
\boxed{
\mathcal H_L
=
\bigoplus_{\ell\in L}V_\ell
=
\bigoplus_{\ell\in L}\mathbb R^{n_\ell}
}.
\]

An element is

\[
H=(H_\ell)_{\ell\in L},
\qquad
H_\ell\in V_\ell.
\]

A Nexus record may therefore contain, for example,

```text
spectral_state        : R^4096
identity_state        : R^1024
homeostatic_state     : R^11
control_state         : R^6
resource_state        : R^32
```

without implying that those coordinates share the same physical unit, semantic basis, normalization, or interpretation.

## 3.2 Ordered labels and flattening

For execution it is often useful to flatten the direct sum. Given an explicit label order

\[
L=(\ell_1,\ldots,\ell_m),
\]

define

\[
\operatorname{flat}_L(H)
=
\begin{bmatrix}
H_{\ell_1}\\
\vdots\\
H_{\ell_m}
\end{bmatrix}
\in
\mathbb R^N,
\qquad
N=\sum_{j=1}^m n_{\ell_j}.
\]

The inverse operation requires the same ordered schema.

The ordering is not cosmetic. It participates in the serialization and slicing ABI. Two implementations that iterate an unordered set of labels can construct different physical layouts from the same mathematical labels.

Therefore a conforming implementation must preserve:

```text
ordered label sequence
per-label dimension
schema/version identifier
offset map or reconstructible ordering rule
```

Sets may be used to test membership or equality. They must not determine positional block layout.

## 3.3 Label identity is stronger than dimensional equality

Two labels may have equal dimensions without being semantically compatible:

\[
V_a\cong\mathbb R^{1024},
\qquad
V_b\cong\mathbb R^{1024}.
\]

Equal dimensions merely make many matrices shape-compatible. They do not authorize the substitution

\[
H_a \equiv H_b.
\]

A practical component contract may include:

```text
label
dimension
scalar/encoding type
coordinate semantics
units or normalization
schema version
allowed transforms
provenance policy
missingness/validity contract
```

Hence:

```text
equal dimension != equal meaning
```

## 3.4 Algebraic zero is not epistemic absence

The zero vector

\[
0_\ell\in V_\ell
\]

is an ordinary mathematical value.

It must not be overloaded to mean:

```text
UNAVAILABLE
UNKNOWN
UNOBSERVED
SENSOR_FAILURE
NOT_APPLICABLE
MISSING
```

If a sensor fails, a state component is not permitted to become the zero vector merely because a dense numerical kernel needs a number. A computation may use a masked numerical surrogate internally, but the epistemic state must remain attached.

This principle is load-bearing because a zero often carries domain meaning. In a security profile, for example:

```text
weak_credentials = 0
```

means something fundamentally different from:

```text
weak_credentials = UNAVAILABLE
```

The first is an observed value. The second is a failure to establish a value.

A conforming HTLA object should therefore pair value state with validity state whenever missingness is possible.

---

# 4. Typed Block Operators

## 4.1 Source and target direct sums

Let \(S\) and \(T\) be finite ordered source and target label sets. Define

\[
\mathcal H_S
=
\bigoplus_{s\in S}\mathbb R^{p_s},
\qquad
\mathcal H_T
=
\bigoplus_{t\in T}\mathbb R^{q_t}.
\]

An HTLA linear map

\[
\mathcal L:
\mathcal H_S
\rightarrow
\mathcal H_T
\]

is a block family

\[
\mathcal L
=
[L_{t,s}]_{t\in T,\;s\in S},
\qquad
L_{t,s}\in
\mathbb R^{q_t\times p_s}.
\]

For input

\[
x=(x_s)_{s\in S},
\]

the target component is

\[
y_t
=
\sum_{s\in S}L_{t,s}x_s.
\]

Every term belongs to \(\mathbb R^{q_t}\), so the component sum is well typed.

## 4.2 Dimension change is ordinary rectangular linear algebra

A block

\[
L_{t,s}:\mathbb R^{p_s}\rightarrow\mathbb R^{q_t}
\]

may be square, tall, or wide. "Transdimensional" here means that a declared source component and target component can have different dimensions.

It does not imply that dimension change is invertible, lossless, or mathematically exotic.

Depending on rank, a block may be:

```text
injective
surjective
bijective
rank-deficient
ill-conditioned
approximately reconstructible
irreversibly information-losing
```

Those properties must be established from the actual block and its domain assumptions.

## 4.3 Configured zero block versus unresolved relationship

If the subsystem defines that source \(s\) has no linear influence on target \(t\), then

\[
L_{t,s}=0
\]

is a meaningful configured statement.

It means:

> this operator contains no linear coupling from \(s\) to \(t\).

It does **not** mean:

> a coupling probably exists but has not yet been learned or observed.

Unknown coupling must be represented separately.

This distinction prevents model incompleteness from being silently turned into a strong negative claim.

A sparse coupling pattern can be represented by a directed graph

\[
G\subseteq S\times T
\]

where

\[
(t,s)\notin G
\quad\Rightarrow\quad
L_{t,s}=0.
\]

If the graph itself is part of the declared operator contract, structural block sparsity is semantically meaningful rather than merely a storage optimization.

## 4.4 Identity operator

For a fixed schema \(L\), the identity operator is block diagonal:

\[
(\mathcal I_L)_{\ell,m}
=
\begin{cases}
I_{n_\ell}, & \ell=m,\\
0, & \ell\neq m.
\end{cases}
\]

Then

\[
\mathcal I_L H=H.
\]

## 4.5 Composition

Suppose

\[
\mathcal M:
\bigoplus_{s\in S}\mathbb R^{p_s}
\rightarrow
\bigoplus_{u\in U}\mathbb R^{r_u}
\]

and

\[
\mathcal L:
\bigoplus_{u\in U}\mathbb R^{r_u}
\rightarrow
\bigoplus_{t\in T}\mathbb R^{q_t}.
\]

Then

\[
(\mathcal L\circ\mathcal M)_{t,s}
=
\sum_{u\in U}
L_{t,u}M_{u,s}.
\]

Each product has shape

\[
(q_t\times r_u)(r_u\times p_s)
=
q_t\times p_s.
\]

The intermediate label \(u\) is therefore a typed contraction index.

Ordinary matrix multiplication already checks dimensions. HTLA adds the requirement that the semantic source/target labels also match the declared composition.

## 4.6 Peirce decomposition

For \(\mathcal H=\bigoplus_{\ell\in L}V_\ell\), let \(e_\ell\) be the canonical projection/inclusion idempotent. Then

\[
e_\ell^2=e_\ell,
\qquad
e_\ell e_m=0 \;(\ell\neq m),
\qquad
\sum_{\ell}e_\ell=I.
\]

For any \(A\in\operatorname{End}(\mathcal H)\),

\[
A
=
\left(\sum_t e_t\right)
A
\left(\sum_s e_s\right)
=
\sum_{t,s}e_tAe_s.
\]

Because the label set is finite and these matrix corners occupy independent component slots,

\[
\boxed{
\operatorname{End}(\mathcal H)
=
\bigoplus_{t,s}
e_t\operatorname{End}(\mathcal H)e_s
}.
\]

The corner

\[
e_t\operatorname{End}(\mathcal H)e_s
\]

is naturally identified with

\[
\operatorname{Hom}(V_s,V_t).
\]

This gives the correct algebraic interpretation of the block family without inventing a grading operation on labels.

## 4.7 The finite preadditive category of labels

Let \(\mathcal C_L\) have labels as objects and

\[
\operatorname{Hom}_{\mathcal C_L}(s,t)
=
\operatorname{Lin}(V_s,V_t).
\]

Each hom-set is a real vector space, and composition is bilinear. Therefore \(\mathcal C_L\) is a finite real-linear preadditive category, and its endomorphism ring is exactly the Peirce decomposition of Section 4.6 viewed with composition as the ring product.

A prior HTLA draft additionally asserted a flattening functor that was "faithful but not full," while defining the labeled hom-set as all linear maps between the flattened spaces. Under those definitions the induced hom-set map is already both surjective and injective—full and faithful—so that claim is `HISTORICAL/SUPERSEDED`. A genuinely non-full embedding is possible only after restricting admissible morphisms, for example by enforcing a coupling graph; HTLA's core calculus does not require such a restriction.

---

# 5. Label-Aware Bilinear Forms, Kernels, and Similarity

## 5.1 Aligned-label weighted form

For compatible states \(H,K\in\mathcal H_L\), define

\[
B_w(H,K)
=
\sum_{\ell\in L}
w_\ell
\langle H_\ell,K_\ell\rangle,
\qquad
w_\ell\ge 0.
\]

If every weight is strictly positive,

\[
w_\ell>0 \quad \forall \ell,
\]

then \(B_w\) is an inner product.

Its induced norm is

\[
\|H\|_w
=
\sqrt{
\sum_\ell
w_\ell\|H_\ell\|_2^2
}.
\]

## 5.2 Zero weights produce a seminorm

If some weight \(w_j=0\), choose nonzero \(H\) supported entirely on component \(j\). Then

\[
H\neq 0
\]

but

\[
B_w(H,H)=0.
\]

Therefore the induced quantity is only a seminorm on the complete state space.

This is not pedantry: a zero-weight component has been deliberately made invisible to that geometry.

## 5.3 Cross-label compatibility

Suppose source component \(\ell\) may be compared to target component \(m\) through an explicit mapping

\[
P_{\ell\rightarrow m}:
V_\ell\rightarrow V_m.
\]

A directed cross-label compatibility may be written

\[
C_W(H,K)
=
\sum_{\ell,m}
w_{\ell m}
\left\langle
P_{\ell\rightarrow m}H_\ell,
K_m
\right\rangle.
\]

This makes the semantic bridge explicit. The system does not compare unlike components merely because a flattening makes the dot product executable.

## 5.4 When a cross-label form is actually an inner product

Under a fixed flattening, any bilinear form may be written

\[
B_A(H,K)
=
\operatorname{flat}(H)^T
A
\operatorname{flat}(K).
\]

For this to be an inner product on the real state space, \(A\) must be symmetric positive definite:

\[
A=A^T,
\qquad
x^TAx>0 \quad \forall x\neq 0.
\]

If \(A\) is symmetric positive semidefinite but singular,

\[
A\succeq 0,
\]

then the induced quantity is a seminorm, not a norm.

If \(A\) is asymmetric or indefinite, the construction may still be useful as a directed compatibility score, but it must not inherit inner-product or metric terminology.

This corrects the weaker historical statement that positive semidefiniteness alone sufficed for a true inner product.

## 5.5 Normalized similarity

For a valid positive-definite weighted inner product,

\[
\operatorname{sim}_w(H,K)
=
\frac{
B_w(H,K)
}{
\|H\|_w\|K\|_w
}
\]

whenever both norms are nonzero.

An implementation may use

\[
\operatorname{sim}_{w,\epsilon}(H,K)
=
\frac{
B_w(H,K)
}{
\|H\|_w\|K\|_w+\epsilon
}
\]

with \(\epsilon>0\) as a numerical safeguard. The \(\epsilon\) term is not part of the abstract cosine definition.

If the numerator is a general directed compatibility score that has not been proven to arise from an inner product, a safer normalization is

\[
\operatorname{score}(H,K)
=
\frac{
C_W(H,K)
}{
\|H\|_\alpha\|K\|_\beta+\epsilon
},
\]

using independently valid norms.

## 5.6 Similarity is derived evidence

HTLA similarity participates in retrieval and comparison. It does not become an identity or authority relation.

The forbidden implication is

\[
\operatorname{sim}(H,K)\approx 1
\quad\Longrightarrow\quad
\text{same identity}.
\]

The equally forbidden implication is

\[
\operatorname{sim}(H,K)\approx 1
\quad\Longrightarrow\quad
\text{represented proposition is true}.
\]

The Nexus rule is:

```text
similarity != identity
similarity != truth
similarity != continuity
similarity != authorization
similarity != constitutional admissibility
```

ANN/HNSW indexes may accelerate the discovery of high-similarity candidates, but the index remains derived acceleration state.

---

# 6. Dimension-Changing Morphisms and Recoverability Contracts

## 6.1 General linear morphism

A dimension-changing HTLA block is

\[
E_{t\leftarrow s}:
\mathbb R^{p_s}
\rightarrow
\mathbb R^{q_t},
\qquad
E_{t\leftarrow s}(x)=Px.
\]

The rank-nullity theorem immediately bounds what can be recovered.

If

\[
q_t<p_s,
\]

then no linear map can be injective over the entire source space. The null space is nontrivial:

\[
\ker(P)\neq\{0\}.
\]

For \(v\in\ker(P)\),

\[
P(x+v)=Px.
\]

The output therefore cannot distinguish \(x\) from \(x+v\).

This yields the core rule:

```text
dimension reduction != lossless transformation
```

## 6.2 Moore-Penrose pseudoinverse

For a matrix

\[
P=U\Sigma V^T,
\]

the Moore-Penrose pseudoinverse is

\[
P^+
=
V\Sigma^+U^T,
\]

where nonzero singular values are inverted.

It provides the canonical least-squares/minimum-norm generalized inverse. It does not reconstruct null-space information destroyed by the forward map.

## 6.3 Tikhonov-regularized inverse map

The historical HTLA text used

\[
P^+_\lambda
=
V(\Sigma^2+\lambda I)^{-1}\Sigma U^T,
\qquad
\lambda>0.
\]

A more precise name is **Tikhonov-regularized inverse map** or **regularized pseudoinverse operator**.

In singular coordinates its filter factors are

\[
f_\lambda(\sigma_i)
=
\frac{\sigma_i}{\sigma_i^2+\lambda}.
\]

Then

\[
P_\lambda^+P
=
V
\operatorname{diag}
\left(
\frac{\sigma_i^2}
{\sigma_i^2+\lambda}
\right)
V^T.
\]

For positive \(\lambda\), nonzero singular directions are attenuated. The map is therefore deliberately biased and is not an exact inverse even when \(P\) is square and nonsingular.

## 6.4 Reconstruction error

For

\[
y=Px
\]

and reconstructed state

\[
\hat x=P_\lambda^+y,
\]

define

\[
e_{\mathrm{rec}}(x)
=
\|x-\hat x\|_2.
\]

Depending on the subsystem, a richer contract may also retain:

```text
relative error
componentwise error
confidence interval
rank / numerical rank
condition number
null-space dimension
training/reference domain
out-of-distribution indicator
transform version
```

An inverse-shaped output is therefore not epistemically equivalent to the original state.

```text
inverse estimate != original state
```

## 6.5 Johnson-Lindenstrauss embeddings

A suitably normalized random projection can preserve pairwise Euclidean distances over a finite set.

For a finite set \(X\) with \(N=|X|\), Johnson-Lindenstrauss-type results permit embedding into dimension on the order of

\[
m
=
O\!\left(
\frac{\log N}{\epsilon^2}
\right)
\]

up to theorem-specific constants and probability parameters, such that for relevant pairs

\[
(1-\epsilon)\|x-y\|_2^2
\le
\|P(x-y)\|_2^2
\le
(1+\epsilon)\|x-y\|_2^2.
\]

The correct architectural conclusion is limited:

> A specified finite set may retain selected pairwise geometry within a stated probabilistic distortion envelope.

JL does **not** establish:

```text
lossless dimensional reduction
semantic preservation for every property
exact invertibility
identity preservation
truth preservation
```

## 6.6 Transform contract

Every dimension-changing morphism used as a load-bearing Nexus transform should carry an explicit contract. A minimum descriptor is:

```text
transform_id
source_label
target_label
source_dimension
target_dimension
matrix / construction version
rank or numerical-rank estimate
intended reference domain
distortion metric
distortion bound or measured error
failure probability, if probabilistic
decoder / reconstruction rule
regularization parameters
provenance
schema version
```

For an approximate transform chain

\[
x
\xrightarrow{P_1}
z
\xrightarrow{P_2}
y,
\]

the combined map is

\[
y=P_2P_1x.
\]

Approximation obligations compose; exactness does not appear by composition.

```text
approximation provenance composes
exactness does not
```

---

# 7. Nexus Quinary Reference Geometry

## 7.1 Status of this section

The material in this section is `CANONICAL` as a current Nexus reference-geometry contract and `APPLICATION-SPECIFIC` relative to general HTLA mathematics. It must not be universalized into every future HTLA substrate.

The current demonstrator uses

\[
d=1024
\]

coordinates with alphabet

\[
\mathcal Q
=
\{-2,-1,0,+1,+2\}.
\]

## 7.2 Three-plane encoding

Each coordinate can be represented through:

- sign plane \(S\);
- magnitude-1 plane \(M_1\);
- magnitude-2 plane \(M_2\).

Define the activity mask

\[
A=M_1\lor M_2.
\]

The structural invariants are

\[
M_1\land M_2=0
\]

and

\[
S\land\neg A=0.
\]

The first prevents a coordinate from simultaneously encoding magnitude 1 and magnitude 2. The second prevents a sign bit from remaining active on a structural vacuum coordinate.

These are representation invariants, not semantic truth conditions.

## 7.3 Reference sparsity wall

The current reference geometry imposes

\[
\|A\|_0\le 307.
\]

At the maximum occupancy,

\[
1-\frac{307}{1024}
=
0.7001953125,
\]

or approximately \(70.02\%\) structural vacuum.

This is a versioned occupancy constraint of the reference implementation.

It is **not** a theorem that all useful HSL/HTLA representations must be 70% sparse.

**Why a wall exists at all.** The abstract calculus of Sections 3–6 places no bound on occupancy; any finite direct sum and any linear map between them is admissible there. The reference geometry adds a requirement the abstract algebra does not carry: coordinate-level recovery must be mechanically classifiable into `EXACT`, `AMBIGUOUS`, and `IMPOSSIBLE` (Section 7.5) within a fixed per-coordinate bit budget. As occupancy rises, more composite/binder pairs collide under that budget and the classification degrades from precise to unreliable. \(K_{\mathrm{wall}}=307\) is where the current reference implementation's testing places that degradation point for \(d=1024\) under the alphabet \(\mathcal Q\); it is a property of this budget and this alphabet, established by testing rather than derived from a formula, and a future revision with a different bit budget would place a wall elsewhere or might not need one at all.

## 7.4 Reference quinary binding

For quinary coordinates \(q_i,r_i\in\mathcal Q\), the current canonical binding rule is

\[
(q\otimes r)_i
=
\begin{cases}
0,
& q_i=0 \text{ or } r_i=0,\\[4pt]
\operatorname{sgn}(q_ir_i)
\min(|q_i|,|r_i|),
& \text{otherwise}.
\end{cases}
\]

The operation is deterministic and closed over \(\mathcal Q\).

It is also information-losing.

For example, a composite magnitude of 1 does not uniquely reveal whether a constituent had magnitude 1 or 2, because the minimum operation collapses several distinct input pairs into the same output.

Therefore binding is not permitted to imply exact invertibility.

## 7.5 Partial-unbind epistemic states

A coordinate-level partial-unbind procedure returns both a value candidate, where meaningful, and an epistemic status:

| State | Meaning |
|---|---|
| `EXACT` | The constituent input value is uniquely recoverable under the binding contract. |
| `AMBIGUOUS` | More than one constituent value is compatible with the observed composite and known binder. |
| `UNKNOWN` | The binding operation removed information required to recover the constituent. |
| `IMPOSSIBLE` | The observed composite/binder relation violates the assumed binding contract. |

These states are not interchangeable.

In particular:

```text
UNKNOWN != zero
AMBIGUOUS != approximate exactness
IMPOSSIBLE != merely low confidence
```

**7.5.1 The four outcomes are a lattice of possibility sets, not an unordered list.** For a fixed coordinate, let \(\mathcal Q=\{-2,-1,0,+1,+2\}\) be the reference alphabet and \(\otimes\) the binding rule of Section 7.4. Given an observed composite value \(c\) and a set of binder hypotheses \(R\subseteq\mathcal Q\) (a single known binder is \(|R|=1\)), define the possibility set

\[
\operatorname{Poss}(c,R)=\{\,q\in\mathcal Q : \exists\, r\in R,\ q\otimes r=c\,\}.
\]

Ordering possibility sets by inclusion is the same construction used for domain reduction in constraint satisfaction, where a variable's domain narrows as constraints are applied and an empty domain signals inconsistency (Mackworth, 1977), and for approximation semantics in abstract interpretation, where program properties are tracked as elements of a lattice ordered by precision (Cousot & Cousot, 1977). Under this construction,

\[
\operatorname{EXACT}\iff|\operatorname{Poss}(c,R)|=1,
\qquad
\operatorname{AMBIGUOUS}\iff|\operatorname{Poss}(c,R)|>1,
\qquad
\operatorname{IMPOSSIBLE}\iff\operatorname{Poss}(c,R)=\varnothing.
\]

`UNKNOWN` is not a fourth case of this same construction; it denotes that the retained state does not support forming \(\operatorname{Poss}(c,R)\) at all, which typically arises from iterative or search-based reconstruction procedures rather than from the deterministic coordinate-level rule treated here. At the level of this section, only `EXACT`, `AMBIGUOUS`, and `IMPOSSIBLE` are produced by the construction above.

**7.5.2 Classification of the reference binding rule.** Exhaustive enumeration over all 25 pairs \((r,c)\in\mathcal Q\times\mathcal Q\), with \(R=\{r\}\), gives:

| Outcome | Count of 25 | Example |
|---|---|---|
| `EXACT` | 12 | \(r=-2,\ c=-2\Rightarrow\operatorname{Poss}=\{2\}\) |
| `AMBIGUOUS` | 5 | \(r=-1,\ c=-1\Rightarrow\operatorname{Poss}=\{1,2\}\) |
| `IMPOSSIBLE` | 8 | \(r=-1,\ c=-2\Rightarrow\operatorname{Poss}=\varnothing\) |

This is a complete enumeration of the reference alphabet, not a sample. `IMPOSSIBLE` is not a rare edge case for this operation: nearly a third of composite/binder pairs are inconsistent with the piecewise rule of Section 7.4, which follows directly from that rule fixing the composite to \(0\) whenever either operand is \(0\) and otherwise fixing sign and taking a minimum.

**7.5.3 Monotonicity under binder uncertainty.**

\[
\boxed{
R_1\subseteq R_2 \implies \operatorname{Poss}(c,R_1)\subseteq\operatorname{Poss}(c,R_2)
\quad\text{for every }c\in\mathcal Q.
}
\]

This is immediate from \(\operatorname{Poss}\) being a union over binder hypotheses—monotonicity of union under an enlarging index set—and has additionally been checked exhaustively for this paper: over all 1215 triples \((R_1,R_2,c)\) with \(R_1\subseteq R_2\subseteq\mathcal Q\), zero violations occur.

The content of the property is what it forbids, not the set-theoretic fact itself. Because possibility sets can only grow or stay the same as binder knowledge becomes less certain, a mechanism cannot legitimately report a *more* determinate epistemic state—moving from `AMBIGUOUS` toward `EXACT`, or from `IMPOSSIBLE` toward anything—purely as a consequence of *less* certain inputs. A component that appears to do so is not resolving uncertainty; it is discarding the record of it.

**7.5.4 Where this recurs elsewhere in this paper.** Section 13's failure modes restate as instances of one property rather than as an unrelated list:

- **Rank-loss laundering** (13.4) reports a value recovered from a lower-rank operator as though the discarded null-space directions were never relevant.
- **Regularization laundering** (13.5) reports a single Tikhonov-regularized point estimate as an exact solution rather than as the `AMBIGUOUS` representative it is (Section 6.3).
- **Derived-index authority escalation** (13.6) treats an ANN/HNSW nearest-neighbor result—itself only ever derived, approximate state—as identity or ground truth.

Each is a concrete violation of the monotonicity property above: a component reporting more certainty downstream than the epistemic state flowing into it can support.

## 7.6 Historical binding formulation

Earlier HTLA/HTNLA research used circular convolution and, in some variants, nonlinear saturation such as `tanh`. That formulation is `HISTORICAL/SUPERSEDED` as the current Nexus reference binding contract.

This does not make circular convolution mathematically invalid; it remains established VSA prior art. It means only that the current Nexus reference implementation uses the explicit quinary information-loss contract because it makes recoverability mechanically inspectable.

## 7.7 Verification scope

The Nexus verification record reports successful tests in the specified reference environment for:

```text
quinary dense/packed round trips
active-mask invariants
sign-vacuum invariants
reference binding behavior
partial-inverse admissibility on tested cases
all-vacuum edge behavior
```

Those results verify bounded executable properties of the demonstrator. They do not establish universal robustness across every future architecture, dtype, platform, or binding family.

---

# 8. Low-Rank Block Compression

## 8.1 Independent truncated SVD

For block

\[
L_{t,s}
\in
\mathbb R^{q_t\times p_s}
\]

with singular-value decomposition

\[
L_{t,s}
=
U\Sigma V^T,
\]

let

\[
\widetilde L_{t,s}^{(r)}
=
U_r\Sigma_rV_r^T
\]

be the rank-\(r\) truncated SVD.

By the Eckart-Young-Mirsky theorem, truncated SVD is an optimal rank-\(r\) approximation under the Frobenius norm and spectral norm.

The Frobenius error is

\[
\|L_{t,s}-\widetilde L_{t,s}^{(r)}\|_F^2
=
\sum_{j>r}\sigma_j^2.
\]

## 8.2 Global block error identity

Let \(\mathcal L\) be the full flattened block operator and \(\widetilde{\mathcal L}\) its independently compressed block approximation.

Because the blocks occupy disjoint matrix regions,

\[
\boxed{
\|\mathcal L-\widetilde{\mathcal L}\|_F^2
=
\sum_{t,s}
\|L_{t,s}-\widetilde L_{t,s}\|_F^2
}.
\]

If each block uses rank \(r_{t,s}\),

\[
\|\mathcal L-\widetilde{\mathcal L}\|_F^2
=
\sum_{t,s}
\sum_{j>r_{t,s}}
\sigma_{t,s,j}^2.
\]

This is an exact accounting identity for the chosen blockwise approximation.

## 8.3 Propagated state error

Let

\[
E
=
\mathcal L-\widetilde{\mathcal L}.
\]

Then

\[
\mathcal Lx-\widetilde{\mathcal L}x
=
Ex
\]

and

\[
\|\mathcal Lx-\widetilde{\mathcal L}x\|_2
\le
\|E\|_2\|x\|_2
\le
\|E\|_F\|x\|_2.
\]

This converts operator approximation into a state-error upper bound.

Domain-specific systems may prefer tighter empirical bounds over the actual admissible input region.

## 8.4 Storage complexity

An uncompressed dense block requires

\[
q_tp_s
\]

scalar parameters.

A rank-\(r\) factorization using \(U_r,\Sigma_r,V_r\) requires approximately

\[
r(q_t+p_s+1)
\]

scalars.

Compression is therefore storage-beneficial when

\[
r(q_t+p_s+1)
<
q_tp_s.
\]

The corresponding multiply can be evaluated as

\[
L_{t,s}x_s
\approx
U_r
\left[
\Sigma_r
\left(
V_r^Tx_s
\right)
\right].
\]

No performance advantage should be claimed without measuring the actual memory hierarchy, batch size, accelerator kernel behavior, and block dimensions.

## 8.5 Semantic reason for blockwise compression

The strongest HTLA-specific reason for blockwise compression is not that it always compresses better than a global factorization. It is that the approximation remains attached to the exact semantic relationship it approximates:

```text
source label
target label
rank
discarded singular energy
error tolerance
version
```

Different mappings may therefore have different approximation budgets without erasing their label identities.

---

# 9. Noise, Concentration, and Probabilistic Claims

## 9.1 Why concentration belongs behind explicit assumptions

HTLA is deterministic linear algebra unless a stochastic model is introduced. A concentration inequality is not automatically a property of a block operator.

Any probabilistic statement must identify:

```text
random variable
independence assumptions
centering assumptions
tail class
matrix/operator being conditioned on
norm convention
failure probability
```

## 9.2 Standard Hanson-Wright form

For an independent mean-zero sub-Gaussian random vector \(X\) with coordinate sub-Gaussian scale bounded by \(K\), the Hanson-Wright inequality has the form

\[
\Pr\left(
\left|
X^TAX-\mathbb E[X^TAX]
\right|>t
\right)
\le
2
\exp\left[
-c
\min
\left(
\frac{t^2}{K^4\|A\|_F^2},
\frac{t}{K^2\|A\|_{\mathrm{op}}}
\right)
\right].
\]

The second branch is **linear in \(t\)**.

A historical HTLA appendix used a purported generalized expression whose sub-Gaussian endpoint produced a quadratic operator-norm branch. That expression does not recover the standard theorem and is therefore `HISTORICAL/SUPERSEDED`.

## 9.3 Heavy-tailed extensions

Rigorous concentration results for \(\alpha\)-sub-exponential variables exist, including work by Götze, Sambale, and Sinulis. Those results involve theorem-specific assumptions and multi-level dependence on matrix norms.

HTLA does not define a new generic heavy-tail Hanson-Wright formula.

If future Nexus work requires a heavy-tailed noise model, it must instantiate an external theorem with matching assumptions or derive and prove a new result.

## 9.4 Simple Gaussian injection example

If a subsystem explicitly adds

\[
\widetilde y
=
y+\gamma\xi,
\qquad
\xi\sim\mathcal N(0,I_m),
\]

then

\[
\mathbb E
\|\widetilde y-y\|_2^2
=
\gamma^2m.
\]

By Jensen's inequality,

\[
\mathbb E
\|\widetilde y-y\|_2
\le
\gamma\sqrt m.
\]

This statement is model-specific and should not be generalized to arbitrary blockwise noise injection without recomputing the resulting covariance.

---

# 10. HTLA / HTNLA Boundary

HTLA is the linear layer.

A typical nonlinear extension is

\[
z_t
=
b_t
+
\sum_s
W_{t,s}x_s
+
r_t,
\]

followed by

\[
y_t
=
\phi_t(z_t).
\]

Competition such as k-WTA may then act on the resulting component.

The moment a nonlinear \(\phi_t\) is introduced, the transformation no longer belongs to the pure HTLA calculus.

## 10.1 Nonlinearity and invertibility

It is too crude to state that "nonlinearity destroys invertibility."

Some nonlinear functions are injective on their domains. For example, `tanh` is mathematically one-to-one from \(\mathbb R\) onto \((-1,1)\).

However, invertibility of an entire nonlinear Nexus transformation can still fail because of:

```text
non-injective activation
clipping or quantization
saturation and severe numerical conditioning
k-WTA or thresholding
unknown or discarded bias/gate state
dimension reduction
information-losing binding
projection into an admissible subset
```

The correct statement is therefore:

> Exact inversion is available only when the complete composed transformation is injective on the relevant domain and all information required by the inverse has been retained.

The current quinary binding is explicitly not injective, so the four-state partial-unbind contract remains necessary regardless of whether some other nonlinear component is invertible.

## 10.2 k-WTA and complexity

A fixed retention fraction does not change the asymptotic complexity class of multiplying a dense \(D\times D\) matrix by a vector.

If k-WTA retains

\[
k=\rho D
\]

coordinates for constant \(\rho\), then a naive dense-row evaluation against the sparse vector costs on the order of

\[
O(Dk)
=
O(\rho D^2)
=
O(D^2).
\]

The constant factor may improve. The asymptotic class does not.

Real complexity reductions can come from other structure, including:

```text
FFT-based convolution
structural block sparsity
bounded-degree coupling graphs
low-rank factors
specialized sparse kernels
hierarchical or approximate routing
```

Any claim of \(O(D\log D)\), \(O(\log|L|)\), or another class reduction must identify the mechanism that produces it.

---

# 11. Reference Implementation Contract

## 11.1 Requirements

A minimally conforming block implementation should:

1. preserve ordered source labels;
2. preserve ordered target labels;
3. validate per-label dimensions;
4. reject inconsistent block shapes;
5. treat absent configured blocks as zero only when the operator contract says they are absent;
6. retain missingness separately from numerical zero;
7. flatten using declared ordering, never unordered set iteration;
8. reverse source/target roles for inverse-shaped operators;
9. expose regularization parameters;
10. retain transform provenance and schema version in production code.

## 11.2 Corrected numerical example

Consider

\[
M
=
\begin{bmatrix}
1&0&2\\
0&1&1\\
1&1&0
\end{bmatrix},
\qquad
b
=
\begin{bmatrix}
4\\3\\2
\end{bmatrix},
\qquad
\lambda=0.1.
\]

Using

\[
M_\lambda^+
=
V
\operatorname{diag}
\left(
\frac{\sigma_i}{\sigma_i^2+\lambda}
\right)
U^T,
\]

the executed singular values are

\[
\sigma(M)
\approx
[2.53208889,\;1.34729636,\;0.87938524].
\]

The executed regularized solution is

\[
\boxed{
h_\lambda
\approx
[0.69415113,\;1.27169222,\;1.63529520]^T
}
\]

with residual

\[
\boxed{
\|Mh_\lambda-b\|_2
\approx
0.1051721250.
}
\]

The historical values

\[
[0.86,\;1.14,\;1.57]^T
\]

and residual \(0.38\) do not follow from the stated formula and are retired.

## 11.3 Why a labeled pseudoinverse must reverse direction

Suppose

\[
\mathcal L:
\mathcal H_S
\rightarrow
\mathcal H_T.
\]

Then an inverse-shaped map must have type

\[
\mathcal L^+:
\mathcal H_T
\rightarrow
\mathcal H_S.
\]

Therefore:

```text
inverse source labels = original target labels
inverse target labels = original source labels
```

This variance reversal is not optional metadata. It is the type of the map.

The historical reference implementation computed pseudoinverse numbers but retained the original source/target label roles. The resulting matrix looked plausible but failed as soon as the returned operator was applied to a target-shaped hypervector.

## 11.4 Executed reference class

The following compact implementation was executed for this rewrite. It uses explicit ordered labels and reconstructs the inverse block layout with source/target roles exchanged.

```python
import numpy as np
from dataclasses import dataclass

@dataclass(frozen=True)
class HyperVector:
    components: dict[str, np.ndarray]

class BlockOperator:
    def __init__(
        self,
        blocks,
        target_labels,
        source_labels,
    ):
        self.blocks = blocks
        self.target_labels = list(target_labels)
        self.source_labels = list(source_labels)

        self.target_dims = {}
        for t in self.target_labels:
            dims = {
                block.shape[0]
                for block in self.blocks.get(t, {}).values()
            }
            if len(dims) != 1:
                raise ValueError(f"inconsistent target dimension: {t}")
            self.target_dims[t] = next(iter(dims))

        self.source_dims = {}
        for s in self.source_labels:
            dims = {
                self.blocks[t][s].shape[1]
                for t in self.target_labels
                if s in self.blocks.get(t, {})
            }
            if len(dims) != 1:
                raise ValueError(f"inconsistent source dimension: {s}")
            self.source_dims[s] = next(iter(dims))

    @staticmethod
    def _offsets(labels, dims):
        result = {}
        offset = 0
        for label in labels:
            result[label] = (offset, offset + dims[label])
            offset += dims[label]
        return result, offset

    def dense(self):
        rows, nr = self._offsets(
            self.target_labels,
            self.target_dims,
        )
        cols, nc = self._offsets(
            self.source_labels,
            self.source_dims,
        )

        A = np.zeros((nr, nc))

        for t in self.target_labels:
            r0, r1 = rows[t]
            for s in self.source_labels:
                block = self.blocks.get(t, {}).get(s)
                if block is None:
                    continue
                c0, c1 = cols[s]
                A[r0:r1, c0:c1] = block

        return A

    def pseudoinverse(self, regularization=0.0):
        A = self.dense()
        U, sigma, Vt = np.linalg.svd(
            A,
            full_matrices=False,
        )

        filt = sigma / (sigma**2 + regularization)
        A_plus = Vt.T @ np.diag(filt) @ U.T

        old_rows, _ = self._offsets(
            self.target_labels,
            self.target_dims,
        )
        old_cols, _ = self._offsets(
            self.source_labels,
            self.source_dims,
        )

        inverse_blocks = {}

        # New target = old source.
        for old_source in self.source_labels:
            c0, c1 = old_cols[old_source]
            inverse_blocks[old_source] = {}

            # New source = old target.
            for old_target in self.target_labels:
                r0, r1 = old_rows[old_target]
                inverse_blocks[old_source][old_target] = (
                    A_plus[c0:c1, r0:r1]
                )

        return BlockOperator(
            inverse_blocks,
            target_labels=self.source_labels,
            source_labels=self.target_labels,
        )

    def apply(self, hv):
        result = {}

        for t in self.target_labels:
            y = np.zeros(self.target_dims[t])

            for s, block in self.blocks.get(t, {}).items():
                y += block @ hv.components[s]

            result[t] = y

        return HyperVector(result)
```

For the test operator with original type

```text
in:R^3 -> {out1:R^2, out2:R^1}
```

the returned regularized pseudoinverse has type

```text
{out1:R^2, out2:R^1} -> in:R^3
```

and reproduces the executed solution and residual above.

## 11.5 Verification limits

The executed example verifies one concrete correction. Production verification should additionally cover:

```text
rectangular operators
rank-deficient operators
zero singular values
regularization = 0
regularization > 0
different source/target label orders
multiple source labels
multiple target labels
configured zero blocks
malformed block shapes
schema mismatch
dense <-> block round trip
float32 / float64 behavior
deterministic serialization
```

Passing one worked example does not establish correctness for every malformed or adversarial layout.

---

# 12. Complexity and Scalability

## 12.1 Dense block cost

For a block

\[
L_{t,s}\in\mathbb R^{q_t\times p_s},
\]

dense application costs

\[
O(q_tp_s)
\]

scalar multiply-add operations in the ordinary model.

For a coupling graph \(G\subseteq T\times S\), a full block-sparse operator costs approximately

\[
O\left(
\sum_{(t,s)\in G}
q_tp_s
\right).
\]

This is the relevant structural complexity expression.

## 12.2 When label sparsity changes asymptotics

If every possible pair of \(m\) labels is coupled and block sizes remain comparable, the number of blocks may scale as

\[
O(m^2).
\]

If a semantic coupling graph has bounded degree,

\[
|E(G)|=O(m),
\]

then the number of active blocks scales linearly in label count.

That is a real complexity-class change caused by **structural block sparsity**.

It is different from keeping a fixed fraction of coordinates inside every dense block.

## 12.3 Label-routing complexity: status and open hypothesis

Sparse mixture-of-experts research demonstrates a principle relevant to HTLA: conditional activation can make per-example computation depend on the active subset rather than total stored model capacity, and hierarchical routing can, under particular data structures and access assumptions, produce logarithmic routing depth. Neither result by itself implies a universal logarithmic HTLA backward pass, and no general theorem establishes that HTLA gradient computation scales as \(O(\log|L|)\); an earlier draft's claim to that effect is `HISTORICAL/SUPERSEDED`.

The correctly scoped statement is:

> **RESEARCH HYPOTHESIS.** Under a declared hierarchical routing structure, bounded active coupling degree, bounded block dimensions, and a routing implementation whose lookup cost is \(O(\log|L|)\), the per-example cost attributable to label routing and active-block evaluation may scale logarithmically in total label cardinality. End-to-end gradient complexity must include router scoring, communication, normalization, globally coupled losses, and backward propagation.

## 12.4 Falsification protocol

A valid experiment should vary \(|L|\) geometrically while fixing or reporting:

```text
block dimensions
active blocks per example
coupling graph degree
routing algorithm
batch size
optimizer
dtype
hardware
communication topology
compiler/kernel versions
```

Measure separately:

```text
router time
forward active-block time
backward active-block time
communication
peak memory
end-to-end wall time
```

Compare candidate scaling models rather than asserting one in advance.

---

# 13. Failure Modes and Adversarial Cases

HTLA becomes dangerous when mathematically legal numerical operations are mistaken for semantically legal system operations.

## 13.1 Schema collision

Two components share dimension \(n\) but use different coordinate meanings. A careless flattening allows one to be fed into an operator trained for the other.

Mitigation:

```text
stable labels
schema versions
source/target validation
explicit compatible maps
```

## 13.2 Zero/missing collapse

Unavailable evidence is numerically replaced by zero and downstream logic interprets zero as an observed clean or absent condition.

Mitigation:

```text
typed validity state
mask propagation
fail-closed decision layer
```

## 13.3 Indefinite "similarity" kernel

A cross-label matrix \(A\) is asymmetric or indefinite, yet code treats \(x^TAy\) as an inner product and uses metric assumptions that do not hold.

Mitigation:

```text
symmetry test
eigenvalue / Cholesky test where appropriate
explicit compatibility-score naming
```

The next three failure modes are each an instance of the monotonicity property proved in Section 7.5.3: a component reports more certainty downstream than its input epistemic state can support.

## 13.4 Rank-loss laundering

A dimension-reducing transform discards information, but reconstruction is later treated as if it were the source state.

Mitigation:

```text
rank/null-space metadata
transform provenance
error contract
recoverability status
```

## 13.5 Regularization laundering

A Tikhonov solution is called an "inverse" without stating \(\lambda\), making deliberate bias look like exact recovery.

Mitigation:

```text
regularization parameter in transform identity
separate Moore-Penrose and Tikhonov APIs
```

## 13.6 Derived-index authority escalation

ANN/HNSW returns a near neighbor and downstream code uses that result as identity, truth, or authorization.

Mitigation:

```text
retrieval candidate only
exact identity/provenance check
HIGC / authority checks outside HTLA
```

## 13.7 Unordered-label nondeterminism

A map is flattened by iterating Python sets or hash-map order that differs between producers and consumers.

Mitigation:

```text
ordered labels are part of ABI
canonical serialization
round-trip tests
```

## 13.8 Approximation-budget drift

Low-rank or projection tolerances change between versions without recording the change.

Mitigation:

```text
versioned transform contract
error-budget regression tests
migration/QMT review when continuity matters
```

---

# 14. Speculative Extensions

Nothing in this section is required to define or operate HTLA. Every item is intentionally separated from the load-bearing calculus.

## 14.1 Fisher-Rao label geometry

**Status: RESEARCH HYPOTHESIS**

If a differentiable statistical family

\[
p_\theta(t\mid s)
\]

is explicitly defined over label transitions or another HTLA-relevant stochastic object, the Fisher information matrix can provide a Riemannian metric on the parameter manifold.

A raw cross-label weight matrix is not automatically a Fisher metric. A probability model, normalization, differentiability assumptions, and statistical interpretation must first exist.

## 14.2 Persistent topology

**Status: RESEARCH HYPOTHESIS**

Persistent or zigzag homology may become useful if Nexus defines a time-varying coupling graph or filtration whose topological features answer a concrete engineering question.

A sparse quinary vector alone does not define a topological filtration.

Required future specification includes:

```text
topological object
filtration or zigzag sequence
distance / weight function
persistence statistic
decision that consumes the statistic
falsification criterion
```

## 14.3 Heavy-tail robust solvers

**Status: RESEARCH HYPOTHESIS**

Robust estimators or published sub-exponential concentration results may be relevant under a concrete heavy-tailed noise model. The current HTLA core does not define such a model.

## 14.4 Quantum block encoding

**Status: RESEARCH HYPOTHESIS**

Generic quantum block-encoding and quantum singular-value-transformation techniques can in principle act on suitable structured matrices when efficient state preparation and oracle access are available.

No HTLA-specific quantum speedup follows merely from labels, Peirce blocks, or direct-sum notation.

Any future claim must include:

```text
oracle/access model
state-preparation cost
conditioning
query complexity
gate complexity
measurement/output cost
classical baseline
```

## 14.5 Gauge-equivariant extensions

**Status: RESEARCH HYPOTHESIS**

If label spaces carry specified group representations and block operators are constrained to be intertwiners, an HTNLA extension may use representation-aware nonlinearities that preserve equivariance.

Labels alone do not define a gauge group, bundle, or action.

## 14.6 Neural-ODE extension

**Status: RESEARCH HYPOTHESIS**

A time-varying labeled state could be modeled by

\[
\dot H(t)
=
F(H(t),t)
\]

with block-structured vector fields. This requires existence/regularity assumptions, an integration contract, and a reason continuous time is preferable to the existing discrete subsystem dynamics.

## 14.7 Emergent-spacetime analogy

**Status: RESEARCH HYPOTHESIS / heuristic only**

Nothing in the HTLA direct-sum or Peirce calculus derives physical spacetime or Einstein field equations.

Information geometry and curvature may inspire mathematical regularizers or visualizations. They are not evidence of physical equivalence.

---

# 15. Claim-Status Audit

| Claim / object | Status | Basis |
|---|---|---|
| HTLA is Nexus's labeled direct-sum linear calculus | CANONICAL | Higher-tier Nexus monograph |
| \(\mathcal H=\bigoplus_\ell\mathbb R^{n_\ell}\) | CANONICAL | Nexus contract; standard linear algebra |
| Finite direct sum can be flattened to \(\mathbb R^N\) after ordering | VERIFIED | Standard finite-dimensional linear algebra |
| Ordered labels are required for deterministic positional slicing | PROPOSED | Engineering ABI requirement; fixes known implementation defect |
| Algebraic zero is distinct from typed missingness | CANONICAL | Nexus epistemic contract |
| Block application \(y_t=\sum_sL_{t,s}x_s\) | CANONICAL | Nexus contract; standard block algebra |
| Block composition \((LM)_{t,s}=\sum_uL_{t,u}M_{u,s}\) | VERIFIED | Standard block algebra |
| Peirce decomposition of \(\operatorname{End}(\mathcal H)\) | VERIFIED | Direct proof; established ring theory |
| Finite real-linear preadditive category / ring-with-several-objects view | VERIFIED | Established category/ring theory |
| Historical generic "graded algebra" wording | HISTORICAL/SUPERSEDED | No label degree law was defined |
| Historical flattening functor "faithful but not full" under unrestricted hom-sets | HISTORICAL/SUPERSEDED | Under those definitions it is full and faithful |
| Strictly positive aligned weights define an inner product | VERIFIED | Inner-product axioms |
| Zero weights yield only a seminorm on the full space | VERIFIED | Direct counterexample |
| General cross-label bilinear form is an inner product when induced operator is SPD | VERIFIED | Standard bilinear-form theory |
| PSD but singular cross-label operator yields a seminorm | VERIFIED | Null-space argument |
| Asymmetric/indefinite cross-label form is a compatibility score, not a metric | PROPOSED | Terminological safety contract |
| Similarity does not establish identity/truth/authorization | CANONICAL | Higher-tier Nexus authority separation |
| Dimension reduction is not generally injective | VERIFIED | Rank-nullity theorem |
| Moore-Penrose pseudoinverse is not lost-information recovery | VERIFIED | Generalized-inverse theory |
| Tikhonov map with \(\lambda>0\) is not an exact inverse | VERIFIED | Singular-coordinate calculation |
| JL preserves selected finite-set distances under stated assumptions | VERIFIED | Johnson-Lindenstrauss theorem |
| JL implies semantic preservation or exact recovery | HISTORICAL/SUPERSEDED | Not entailed by theorem |
| Blockwise truncated SVD error formula | VERIFIED | Eckart-Young-Mirsky |
| Global squared Frobenius block-error identity | VERIFIED | Disjoint block support |
| Quinary alphabet \(\{-2,-1,0,+1,+2\}\), \(d=1024\) | CANONICAL | Current Nexus reference geometry |
| Bit-plane invariants \(M_1\wedge M_2=0\), \(S\wedge\neg A=0\) | CANONICAL | Current reference contract; bounded demonstrator tests reported |
| \(K_{\mathrm{wall}}=307\) | CANONICAL | Current reference-implementation constraint |
| 70.02% vacuum is a universal HTLA law | HISTORICAL/SUPERSEDED | It is implementation-specific |
| Current quinary binding rule | CANONICAL | Current Nexus reference geometry |
| EXACT / AMBIGUOUS / UNKNOWN / IMPOSSIBLE partial-unbind states | CANONICAL | Current Nexus epistemic contract |
| Partial-unbind states form a refinement lattice of possibility sets under \(\otimes\) | VERIFIED | Direct construction; analogous to CSP domain reduction and abstract interpretation |
| Reference binding rule classifies as 12 EXACT / 5 AMBIGUOUS / 8 IMPOSSIBLE of 25 pairs | VERIFIED | Exhaustive enumeration over \(\mathcal Q\times\mathcal Q\) |
| \(R_1\subseteq R_2\implies\operatorname{Poss}(c,R_1)\subseteq\operatorname{Poss}(c,R_2)\) | VERIFIED | Direct proof (union monotonicity); exhaustively checked over 1215 triples, zero violations |
| Circular-convolution-plus-saturation is current Nexus reference binding | HISTORICAL/SUPERSEDED | Replaced by quinary reference contract |
| Corrected regularized solution \([0.69415113,1.27169222,1.63529520]^T\) | VERIFIED | Executed NumPy calculation in this rewrite |
| Corrected residual \(0.1051721250\) | VERIFIED | Executed NumPy calculation in this rewrite |
| Labeled pseudoinverse must reverse source/target roles | VERIFIED | Type direction plus executed reference example |
| Standard Hanson-Wright operator-norm branch is linear in \(t\) | VERIFIED | Rudelson-Vershynin |
| Historical homemade heavy-tail exponent substitution | HISTORICAL/SUPERSEDED | Does not recover standard theorem |
| Generic logarithmic-in-label-count HTLA gradient complexity | RESEARCH HYPOTHESIS | No general theorem established |
| Sparse active blocks can decouple active compute from total potential blocks under explicit assumptions | INFERRED | Structural cost model; analogous to conditional computation |
| HTLA-specific quantum speedup | RESEARCH HYPOTHESIS | No such result established |
| Persistent homology is load-bearing HTLA machinery | RESEARCH HYPOTHESIS | No current filtration/decision contract |
| Fisher-Rao label curvature | RESEARCH HYPOTHESIS | Requires explicit statistical manifold |
| Gauge-equivariant HTNLA | RESEARCH HYPOTHESIS | Requires group representations and equivariant maps |
| Neural-ODE HTNLA | RESEARCH HYPOTHESIS | Requires continuous-time model and validation |
| Spacetime equivalence | RESEARCH HYPOTHESIS | Heuristic only; no physical derivation |

---

# 16. Validation and Falsification Program

A replacement Tier-2 subsystem paper should be executable enough that important claims can fail.

## 16.1 Schema invariants

Test:

```text
duplicate labels rejected
dimension mismatch rejected
wrong target block height rejected
wrong source block width rejected
unordered serialization cannot change layout
canonical flatten/unflatten round trip
```

## 16.2 Algebraic properties

For randomly generated valid schemas and operators:

\[
\mathcal I H=H,
\]

\[
(\mathcal L+\mathcal M)H
=
\mathcal LH+\mathcal MH,
\]

\[
(\mathcal A\mathcal B)\mathcal C
=
\mathcal A(\mathcal B\mathcal C)
\]

within numerical tolerance.

Verify block composition against flattened dense composition.

## 16.3 Similarity tests

For positive weights:

```text
symmetry
positive definiteness on nonzero random states
cosine bounds within numerical tolerance
```

For zero weights, explicitly demonstrate nonzero null states.

For general cross-label matrices, reject "inner product" configuration when symmetry or positive-definiteness checks fail.

## 16.4 Transform tests

For every production dimension-changing transform:

```text
record rank
measure reconstruction distribution
measure distortion on reference set
test out-of-distribution behavior
verify transform id/version
verify decoder pairing
```

For random projections, compare empirical pairwise distortion against the declared contract.

## 16.5 Quinary representation tests

Verify:

```text
dense <-> packed round trip
M1 & M2 == 0
S & ~A == 0
active count <= K_wall
binding closure over quinary alphabet
partial-unbind status cases
all-vacuum edge
malformed composite -> IMPOSSIBLE
```

## 16.6 Approximation tests

For SVD compression:

```text
reported block error == measured block Frobenius error
global squared error == sum block squared errors
state-output error respects operator-norm bound
```

## 16.7 Implementation regression for inverse direction

Construct a nontrivial multi-label operator

```text
source: {a:R^2, b:R^1}
target: {x:R^1, y:R^2}
```

and assert:

```text
pinv.source_labels == original.target_labels
pinv.target_labels == original.source_labels
pinv.dense().shape == reverse(original.dense().shape)
```

Then compare against the dense NumPy generalized inverse or regularized reference.

## 16.8 Complexity falsification

Do not benchmark only arithmetic kernels. Include routing and communication.

A complexity claim survives only if the measured end-to-end curve matches the stated access model.

---

# 17. Canonical Engineering Laws for HTLA

The subsystem can be summarized by the following laws.

1. **Labels are semantic types, not decorative names.**
2. **Equal dimensions do not imply compatible meanings.**
3. **Finite direct sums may be flattened, but the schema must survive flattening.**
4. **Configured zero coupling is different from unknown coupling.**
5. **Numerical zero is different from epistemic absence.**
6. **Every block has an explicit source and target type.**
7. **Inverse-shaped maps reverse source and target roles.**
8. **Dimension reduction carries an information-loss obligation.**
9. **Approximate reconstruction is not original-state recovery.**
10. **Similarity is evidence, never authority.**
11. **A general compatibility score is not an inner product unless it satisfies the inner-product axioms.**
12. **Positive semidefiniteness without definiteness yields a seminorm.**
13. **Compression error must remain measurable and attributable to the block that introduced it.**
14. **A fixed sparsity fraction is not, by itself, a complexity-class reduction.**
15. **Probabilistic theorems require explicit stochastic assumptions.**
16. **Reference-geometry constants are versioned implementation constraints, not universal laws.**
17. **Partial unbinding must surface ambiguity and information loss.**
18. **Speculative mathematics does not become load-bearing by proximity to verified mathematics.**
19. **HTLA does not own identity, truth, constitutional admissibility, or physical realization.**
20. **Every performance or scaling claim must point to a theorem, an executed benchmark, or an explicit research hypothesis.**

---

# 18. Conclusion

HTLA is intentionally less exotic than its historical prose sometimes suggested.

At its mathematical core, it is a finite labeled direct-sum calculus with typed block linear maps. Peirce decomposition supplies the correct algebraic account of the block structure. Standard bilinear-form theory distinguishes genuine inner products from seminorms and directed compatibility functions. Rank-nullity, generalized inverses, regularization, and Johnson-Lindenstrauss theory provide explicit limits on what dimension-changing maps can preserve. Truncated SVD supplies measurable blockwise approximation. Standard concentration theory can be used when its assumptions are actually instantiated.

The Nexus-specific engineering value lies in what is built around those ordinary mathematical objects: labels are retained as semantic types; missingness is not collapsed into zero; mappings carry source and target meaning; transform error and provenance remain visible; the current quinary reference geometry exposes structural invariants; and information-losing binding reports `EXACT`, `AMBIGUOUS`, `UNKNOWN`, or `IMPOSSIBLE` rather than manufacturing certainty.

One piece of that engineering value now has a proof behind it rather than a description. Section 7.5 shows those four recovery outcomes form a refinement lattice of possibility sets under the reference binding rule, classifies that rule's behavior by exhaustive enumeration rather than example, and proves—checking every case for this alphabet—that possibility sets can only grow or hold steady as binder knowledge becomes less certain. Three of Section 13's failure modes reduce directly to violations of that one property. This is the paper's one genuinely new formal object; everywhere else, what Nexus contributes is the discipline of the assembly, not the mathematics being assembled.

That makes HTLA useful as a mathematical ABI precisely because it refuses to let numerical convenience erase epistemic or semantic structure.

The final governing distinction is:

```text
mathematical shape compatibility
        !=
semantic compatibility
        !=
recoverability
        !=
identity
        !=
authority
```

HTLA owns the first layer and supplies explicit contracts that help the rest of Nexus reason safely about the others.

---

# References

1. Chiang, D., Rush, A. M., & Barak, B. (2023). *Named Tensor Notation*. Transactions on Machine Learning Research. arXiv:2102.13196. https://arxiv.org/abs/2102.13196

2. Mitchell, B. (1972). *Rings with Several Objects*. Advances in Mathematics, 8, 1-161. https://doi.org/10.1016/0001-8708(72)90002-3

3. Kanerva, P. (2009). *Hyperdimensional Computing: An Introduction to Computing in Distributed Representation with High-Dimensional Random Vectors*. Cognitive Computation, 1, 139-159. https://doi.org/10.1007/s12559-009-9009-8

4. Plate, T. A. (2003). *Holographic Reduced Representation: Distributed Representation for Cognitive Structures*. CSLI Publications.

5. Schlegel, K., Neubert, P., & Protzel, P. (2022). *A comparison of vector symbolic architectures*. Artificial Intelligence Review, 55, 4523-4555. https://doi.org/10.1007/s10462-021-10110-3

6. Johnson, W. B., & Lindenstrauss, J. (1984). *Extensions of Lipschitz mappings into a Hilbert space*. Contemporary Mathematics, 26, 189-206. https://doi.org/10.1090/conm/026/737400

7. Golub, G. H., Hoffman, A., & Stewart, G. W. (1987). *A generalization of the Eckart-Young-Mirsky matrix approximation theorem*. Linear Algebra and its Applications, 88-89, 317-327. https://doi.org/10.1016/0024-3795(87)90114-5

8. Rudelson, M., & Vershynin, R. (2013). *Hanson-Wright inequality and sub-gaussian concentration*. Electronic Communications in Probability, 18. https://doi.org/10.1214/ECP.v18-2865

9. Götze, F., Sambale, H., & Sinulis, A. (2019). *Concentration inequalities for polynomials in alpha-sub-exponential random variables*. arXiv:1903.05964. https://arxiv.org/abs/1903.05964

10. Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., & Dean, J. (2017). *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*. arXiv:1701.06538. https://arxiv.org/abs/1701.06538

11. Fedus, W., Zoph, B., & Shazeer, N. (2021). *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity*. arXiv:2101.03961. https://arxiv.org/abs/2101.03961

12. Gilyén, A., Su, Y., Low, G. H., & Wiebe, N. (2019). *Quantum singular value transformation and beyond: exponential improvements for quantum matrix arithmetics*. Proceedings of STOC 2019. arXiv:1806.01838. https://arxiv.org/abs/1806.01838

13. Low, G. H., & Chuang, I. L. (2019). *Hamiltonian Simulation by Qubitization*. Quantum, 3, 163. https://doi.org/10.22331/q-2019-07-12-163

14. Carlsson, G., & de Silva, V. (2010). *Zigzag Persistence*. Foundations of Computational Mathematics, 10, 367-405. https://doi.org/10.1007/s10208-010-9066-0

15. Cohen, T., Weiler, M., Kicanaoglu, B., & Welling, M. (2019). *Gauge Equivariant Convolutional Networks and the Icosahedral CNN*. Proceedings of the 36th International Conference on Machine Learning, PMLR 97, 1321-1330. https://proceedings.mlr.press/v97/cohen19d.html

16. Chen, R. T. Q., Rubanova, Y., Bettencourt, J., & Duvenaud, D. (2018). *Neural Ordinary Differential Equations*. Advances in Neural Information Processing Systems 31. arXiv:1806.07366. https://arxiv.org/abs/1806.07366

17. *Project Nexus 4: Canonical Architecture, Cognitive Runtime, and Engineering Field Guide*. Reference edition 2026-08-28. Internal Tier-0 architecture source.

18. *PROJECT_NEXUS_V4_VERIFICATION_REPORT*. Project Nexus reference-demonstrator verification record, 2026-07-20. Internal verification source.

19. Mackworth, A. K. (1977). *Consistency in networks of relations*. Artificial Intelligence, 8(1), 99-118. https://doi.org/10.1016/0004-3702(77)90007-8

20. Cousot, P., & Cousot, R. (1977). *Abstract interpretation: a unified lattice model for static analysis of programs by construction or approximation of fixpoints*. Conference Record of the 4th ACM Symposium on Principles of Programming Languages (POPL), 238-252.

---

# Appendix A. ASCII Formula Reference

```text
State space:
H_L = direct_sum_(l in L) R^(n_l)

Element:
H = (H_l)_(l in L)

Block:
L_(t,s) : R^(p_s) -> R^(q_t)

Application:
y_t = sum_(s in S) L_(t,s) x_s

Composition:
(L o M)_(t,s) = sum_(u in U) L_(t,u) M_(u,s)

Peirce decomposition:
End(H) = direct_sum_(t,s) e_t End(H) e_s

Aligned weighted form:
B_w(H,K) = sum_l w_l <H_l,K_l>

Dimension-changing map:
E_(t<-s)(x) = P x

Regularized inverse:
P_plus_lambda =
    V diag(sigma_i / (sigma_i^2 + lambda)) U^T

Reconstruction error:
e_rec(x) = ||x - x_hat||_2

Blockwise compression:
L_(t,s) ~= U_r Sigma_r V_r^T

Global Frobenius error:
||L - L_tilde||_F^2
    = sum_(t,s) ||L_(t,s) - L_tilde_(t,s)||_F^2

Quinary alphabet:
Q = {-2, -1, 0, +1, +2}

Activity mask:
A = M1 OR M2

Bit-plane invariants:
M1 AND M2 = 0
S AND (NOT A) = 0

Reference sparsity wall:
||A||_0 <= 307

Quinary binding:
(q tensor r)_i = 0
    if q_i = 0 or r_i = 0
otherwise
(q tensor r)_i =
    sign(q_i r_i) * min(|q_i|, |r_i|)

Partial unbind:
{EXACT, AMBIGUOUS, UNKNOWN, IMPOSSIBLE}
```

---

# Appendix B. Minimal Implementation Checklist

```text
[ ] labels have stable identifiers
[ ] label order is explicit
[ ] dimensions are validated
[ ] source and target schemas are distinct
[ ] zero-block meaning is declared
[ ] unknown mapping is not silently zero
[ ] missing values are not silently numeric zero
[ ] compatibility matrices are classified:
        SPD -> inner product
        PSD singular -> seminorm
        otherwise -> compatibility score
[ ] dimension-changing maps have transform IDs
[ ] rank / distortion / regularization are recorded
[ ] inverse-shaped maps reverse source/target roles
[ ] low-rank approximation records error budget
[ ] quinary bit-plane invariants are tested
[ ] partial unbind returns epistemic status
[ ] ANN similarity remains advisory
[ ] speculative extensions are not load-bearing
[ ] performance claims point to benchmarks or remain hypotheses
```
