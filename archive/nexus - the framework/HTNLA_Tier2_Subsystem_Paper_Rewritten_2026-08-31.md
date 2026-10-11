# Hypervector Nonlinear Transdimensional Algebra (HTNLA)

## Labeled Nonlinear Maps, Reconstruction Semantics, and Sparse Block Dynamics for Project Nexus 4

**Document class:** Tier-2 subsystem-math source  
**Corpus role:** S9 replacement candidate  
**Reference edition:** 2026-08-31  
**Architectural scope:** Project Nexus 4 / HTLA / HVD / TMS / quinary reference interface  
**Authority rule:** This document supplies subsystem mathematics and engineering contracts. It is subordinate to Tier-0 Nexus architecture wherever a conflict exists.

---

## Abstract

Hypervector Nonlinear Transdimensional Algebra (HTNLA) is the nonlinear extension of the labeled block-linear substrate defined by Hypervector Linear Transdimensional Algebra (HTLA). It operates on heterogeneous direct-sum state, preserves explicit source and target label boundaries, and permits each target component to apply its own nonlinear map after receiving dimensionally typed contributions from one or more source components. A generic target component is

\[
z_t=b_t+\sum_{s:(t,s)\in E}W_{t,s}x_s+r_t,
\]

followed by

\[
y_t=\phi_t(z_t),
\]

and, where configured,

\[
y_t\leftarrow \operatorname{kWTA}_t(y_t).
\]

A multilayer network may be written

\[
H^{(k+1)}=\sigma^{(k)}\!\left(M^{(k)}H^{(k)}+b^{(k)}\right),
\]

with an optional, explicitly typed residual map

\[
H^{(k+1)}=R^{(k)}H^{(k)}+\sigma^{(k)}\!\left(M^{(k)}H^{(k)}+b^{(k)}\right).
\]

Despite its historical name, HTNLA is **not** a graded nonlinear algebra in the ordinary algebraic sense. Arbitrary nonlinear layer maps do not form a vector space under the usual operator addition, and no semigroup grading law has been defined over the label set. The mathematically defensible object is a family of dimensionally typed nonlinear maps, or finite networks of labeled nonlinear morphisms, constructed over the Peirce-organized block substrate supplied by HTLA.

The most important HTNLA contract is not nonlinearity itself but **explicit recoverability semantics**. Exact inversion is permitted only when the relevant composite map is injective on the declared domain. Pseudoinverse estimates, partial unbinding, iterative or resonator reconstruction, and unresolved information loss are not silently promoted into exact recovery. HTNLA therefore separates a five-way reconstruction-method taxonomy from the canonical Nexus quinary epistemic outcomes `EXACT`, `AMBIGUOUS`, `UNKNOWN`, and `IMPOSSIBLE`.

This paper also corrects several historical HTNLA claims that do not survive mathematical or executable scrutiny. A fixed percentage of post-activation k-WTA sparsity does not transform dense \(O(D^2)\) work into \(O(D\log D)\); an asymptotic improvement requires actual sparse block topology, bounded coupling degree, structured operators, conditional execution, or another subquadratic realization. Hard k-WTA is non-injective and non-differentiable at support changes. Tanh is mathematically bijective from \(\mathbb R\) to \((-1,1)\), so tanh alone is not a proof of information loss. A generic classical nonlinear map cannot simply be block-encoded as a unitary quantum operator. Historical percentage claims for recall, latency, energy, consciousness-related metrics, or identity preservation are excluded unless separately measured or proved.

The paper provides a deterministic NumPy reference implementation with genuine heterogeneous source and target dimensions, negative shape tests, explicit k-WTA tie-breaking, a constructive exact-inverse example, and witnesses for ReLU and k-WTA non-injectivity. It also defines the engineering boundary between HTNLA and HVD/TMS: TMS remains the authoritative live state substrate, HDF5 remains durable long-term persistence, and ANN/HNSW structures remain derived indexes whose model-generation and representation-generation consistency must be explicit.

The result is a bounded subsystem paper: nonlinear enough to model non-affine relationships, mathematically conservative about what that implies, and explicit about every place where information, determinism, authority, or evidence can be lost.

---

## Claim-status vocabulary

This document uses the Nexus project-wide status vocabulary exactly:

`CANONICAL`, `IMPLEMENTED`, `VERIFIED`, `PARTIALLY IMPLEMENTED`, `ACTIVE DEVELOPMENT`, `PROPOSED`, `DESIGN TARGET`, `EXPERIMENTAL`, `RESEARCH HYPOTHESIS`, `APPLICATION-SPECIFIC`, `HISTORICAL/SUPERSEDED`, `INFERRED`.

A Tier-2 subsystem paper does not promote itself into Tier-0 canon. `CANONICAL` is used only for contracts already established by the current Nexus architecture. `VERIFIED` is reserved for standard mathematics, direct derivations, or specific executed artifacts identified in this document.

---

# 1. Architectural Role and Scope

## 1.1 Why a nonlinear extension exists

HTLA can express heterogeneous state and arbitrary **linear** mappings between labeled components. That is sufficient for projection, mixing, dimension-changing linear transforms, label-aware similarity, and blockwise approximation. It is not sufficient, by itself, for every useful decision boundary or state transform.

A finite composition of purely linear maps remains linear. If

\[
A:\mathcal H_0\to\mathcal H_1
\]

and

\[
B:\mathcal H_1\to\mathcal H_2
\]

are linear, then

\[
B(A(x))=(BA)x
\]

is still one linear map. Additional depth alone does not create nonlinear expressive capacity.

HTNLA therefore introduces nonlinear maps **without discarding the label structure that HTLA made explicit**. It answers questions such as:

1. How can a target label apply a nonlinear transformation while still receiving dimensionally heterogeneous source components?
2. How can different target labels use different activation or competition rules?
3. What information is destroyed by a nonlinear or sparse step?
4. When can a layer be reversed exactly, approximately, partially, or not at all?
5. How should hard selection interact with deterministic replay?
6. How are learned nonlinear representations versioned against HVD state and derived ANN indexes?
7. Which performance and biological analogies are hypotheses rather than established properties?

Conceptually:

```text
heterogeneous labeled state
          |
          v
        HTLA
 typed block-linear substrate
          |
          v
        HTNLA
  nonlinear target maps
          |
          +--> optional residual maps
          |
          +--> optional k-WTA / competition
          |
          +--> reconstruction-status contract
          |
          v
  transformed labeled state
```

HTNLA is therefore a **nonlinear transformation layer**, not a replacement for HTLA, HVD, TMS, Cyrae, HIGC, THDE, QMT, HTCE, or TUCR.

## 1.2 What HTNLA owns

Within this paper, HTNLA owns the mathematical and software semantics of:

- dimensionally typed nonlinear layer maps over labeled direct sums;
- target-specific activation functions;
- optional typed residual maps;
- optional deterministic k-WTA sparsification;
- local differential/Jacobian structure where the maps are differentiable;
- reconstruction method classification;
- the mapping from reconstruction evidence to permissible epistemic outcomes;
- model-generation metadata required for transformed-state reproducibility;
- validation obligations for nonlinear learned representations.

It does **not** own:

- HVD identity;
- TMS physical realization;
- HDF5 durable archival policy;
- HIGC constitutional admissibility;
- THDE temporal evolution authority;
- QMT continuity judgments;
- Cyrae reward or remediation-causality construction;
- HTCE candidate-field ownership;
- ANN/HNSW truth or identity semantics;
- phenomenology or consciousness claims.

Thus:

```text
nonlinear transform != authority
nonlinear similarity != truth
nonlinear reconstruction != continuity proof
learned representation != HVD identity
```

## 1.3 HTNLA inherits HTLA's typed state boundary

Let source labels be \(S\) and target labels be \(T\). Define

\[
\mathcal H_S=\bigoplus_{s\in S}\mathbb R^{p_s},
\qquad
\mathcal H_T=\bigoplus_{t\in T}\mathbb R^{q_t}.
\]

An input is

\[
x=(x_s)_{s\in S},
\qquad
x_s\in\mathbb R^{p_s}.
\]

Different labels may have different dimensions. Equality of dimension does not imply equality of semantics.

The key inherited rule is:

```text
equal dimension != equal label meaning
```

and:

```text
cross-label interaction requires an explicit map
```

HTNLA adds nonlinear behavior **after or around** those typed maps; it does not erase the typing discipline.

## 1.4 Name retention versus mathematical precision

The historical acronym HTNLA is retained because it is already embedded in the Nexus corpus and its interface naming. The term "Algebra" should therefore be understood as a project name, not as a claim that the nonlinear layer family forms an algebra under ordinary operator addition and multiplication.

The precise description used throughout this paper is:

> **HTNLA is a parameterized family of labeled nonlinear maps built over the HTLA block-linear substrate.**

Where useful, finite compositions of these maps may be treated categorically as composable morphisms between labeled state objects. That structural viewpoint does not imply a linear operator algebra.

---

# 2. Relationship to Prior Art

HTNLA's novelty must be scoped narrowly. Its constituent mathematical and machine-learning ideas all have substantial prior art.

## 2.1 Relation-specific and heterogeneous graph networks

Relational Graph Convolutional Networks (R-GCNs) use relation-specific transformations in multi-relational graphs. Heterogeneous Graph Transformer (HGT) uses node- and edge-type-dependent parameters and attention mechanisms. These architectures demonstrate that **typed transformations are established neural-network practice**.

HTNLA is not equivalent to a graph network. Its state object is an HTLA direct sum, not a graph adjacency structure, and a label is not automatically a graph node or relation type. Nevertheless, the structural comparison is important: a paper cannot claim that "different learned maps for different semantic types" is novel by itself.

HTNLA's narrower distinction is that label identity, heterogeneous component dimension, block geometry, reconstruction semantics, and quinary epistemic outcomes are all part of one declared interface.

## 2.2 Mixture-of-Experts and conditional computation

Sparse Mixture-of-Experts (MoE) architectures conditionally route inputs through a subset of expert networks. They are relevant because they separate **total parameter capacity** from **active computation**.

HTNLA k-WTA is not synonymous with MoE routing. k-WTA may operate on:

- coordinates within one target component;
- label-level scores;
- candidate routes;
- modules or experts.

Only the latter two are close to conditional expert routing. Coordinate sparsity can leave all dense block multiplications intact, so its complexity implications differ sharply from MoE execution sparsity.

## 2.3 Invertible neural networks and normalizing flows

RealNVP, Glow, invertible residual networks, and related flow models provide the correct precedent for claims about exact reversibility. These architectures do not assume that generic nonlinear layers are invertible; they **construct** layers with explicit bijective structure and track the conditions required for exact inversion.

SurVAE Flows is particularly relevant conceptually because it treats bijective, surjective, and otherwise lossy transformations differently rather than forcing every reverse path into one undifferentiated "inverse" operation.

HTNLA adopts the same epistemic discipline at the subsystem level:

```text
reconstruction method != proof of unique recovery
```

## 2.4 Winner-take-all and sparse representation

Winner-take-all mechanisms and sparse coding predate HTNLA. WTA autoencoders and expand-and-sparsify models demonstrate that top-k selection can create sparse representations with useful properties under stated assumptions.

Those results do not establish that arbitrary learned HTNLA layers:

- preserve concentration of measure;
- improve retrieval;
- improve training stability;
- reduce dense matrix multiplication to \(O(D\log D)\);
- reduce energy by a fixed percentage.

Those remain configuration- and workload-dependent empirical or theorem-specific questions.

## 2.5 Universal approximation

Classical universal-approximation theorems establish density properties for certain network families under explicit assumptions on activation functions, domain, width, or depth. HTNLA can contain ordinary feed-forward architectures as special cases under some block configurations.

Therefore the defensible statement is:

```text
some HTNLA configurations may fall inside theorem-covered
universal-approximation families
```

not:

```text
every finite HTNLA configuration is a universal approximator
```

A fixed few-layer, hard-sparse, block-constrained network requires its own approximation analysis.

## 2.6 Reward-modulated plasticity as analogy, not ownership

Reward-modulated STDP literature provides precedent for a functional pattern in which locally accumulated eligibility is later modulated by a delayed scalar signal. Izhikevich (2007), Legenstein, Pecevski and Maass (2008), and Frémaux, Sprekeler and Gerstner (2010) are appropriate references for that general computational analogy.

They do not validate arbitrary constants, sigmoid offsets, "dopamine" thresholds, "serotonin" attention equations, or "GABA" penalties merely because the variables are biologically named.

## 2.7 Scoped contribution

The defensible contribution is the assembly:

```text
HTLA labeled direct-sum state
        +
typed source->target block maps
        +
per-target nonlinear maps
        +
optional deterministic sparsification
        +
explicit reconstruction-method taxonomy
        +
EXACT / AMBIGUOUS / UNKNOWN / IMPOSSIBLE output contract
        +
HVD/TMS model-generation discipline
```

Individual ingredients are prior art. The subsystem contribution is their integration into the Nexus representation and epistemic contract.

---

# 3. Formal Model

## 3.1 Source and target geometry

Let \(S\) and \(T\) be finite ordered label sets. Associate dimensions

\[
p_s\in\mathbb N,\qquad s\in S
\]

and

\[
q_t\in\mathbb N,\qquad t\in T.
\]

Then

\[
\mathcal H_S=\bigoplus_{s\in S}\mathbb R^{p_s},
\qquad
\mathcal H_T=\bigoplus_{t\in T}\mathbb R^{q_t}.
\]

The ordering is part of any flattened storage or serialization ABI. It does not change the abstract direct-sum object, but it does determine offsets in a concrete dense representation.

## 3.2 Coupling relation

Let

\[
E\subseteq T\times S
\]

be the configured coupling relation. A pair \((t,s)\in E\) means that source label \(s\) is permitted to contribute to target label \(t\).

For each permitted pair,

\[
W_{t,s}\in\mathbb R^{q_t\times p_s}.
\]

The use of \(E\) makes topology explicit. If a relationship is not configured, no block is invented.

```text
absent coupling != unknown coupling
```

An unresolved mapping should be represented as unresolved metadata, not silently converted into a zero block if that would change semantics.

## 3.3 Single HTNLA layer

For input

\[
x=(x_s)_{s\in S},
\qquad
x_s\in\mathbb R^{p_s},
\]

define the target preactivation

\[
\boxed{
z_t=b_t+\sum_{s:(t,s)\in E}W_{t,s}x_s+r_t
}
\]

where

\[
b_t,r_t\in\mathbb R^{q_t}.
\]

The term \(b_t\) is a target bias. The term \(r_t\) is an optional external or residual injection whose provenance and dimensions must be explicit.

A target-specific nonlinear map

\[
\phi_t:\mathbb R^{q_t}\to\mathbb R^{q_t}
\]

then produces

\[
\boxed{y_t=\phi_t(z_t)}.
\]

Where configured, a deterministic competition operator is applied:

\[
\boxed{y_t\leftarrow K_{k_t}(y_t)}
\]

where \(K_{k_t}\) denotes the target's k-WTA rule.

The complete layer is therefore a map

\[
F:\mathcal H_S\to\mathcal H_T.
\]

## 3.4 Multi-layer form

Let layer \(k\) map \(\mathcal H_{L_k}\) to \(\mathcal H_{L_{k+1}}\). In compact notation,

\[
\boxed{
H^{(k+1)}=\sigma^{(k)}\!\left(M^{(k)}H^{(k)}+b^{(k)}\right)
}
\]

where \(M^{(k)}\) is an HTLA block operator and \(\sigma^{(k)}\) is the collection of target nonlinearities and configured selection operators.

A network is a composition

\[
F=F_{K-1}\circ\cdots\circ F_1\circ F_0.
\]

Composition is well-defined only when the target label geometry of one layer matches the source geometry expected by the next, or an explicit adapter is inserted.

## 3.5 Residual form

The Nexus canonical residual form is

\[
\boxed{
H^{(k+1)}=R^{(k)}H^{(k)}+\sigma^{(k)}\!\left(M^{(k)}H^{(k)}+b^{(k)}\right)
}
\]

with

\[
R^{(k)}:\mathcal H_{L_k}\to\mathcal H_{L_{k+1}}.
\]

The residual map is **not automatically identity**. If labels or dimensions differ across layers, \(R^{(k)}\) must contain explicit compatible blocks.

Thus:

```text
residual connection != implicit shape coercion
```

## 3.6 Why HTNLA is not an operator algebra

Let

\[
F_1(H)=\sigma(M_1H)
\]

and

\[
F_2(H)=\sigma(M_2H).
\]

In general,

\[
F_1(H)+F_2(H)\neq \sigma((M_1+M_2)H).
\]

The nonlinear activation does not distribute over ordinary operator addition. The parameterized family is therefore not a vector space of operators under the standard linear operations, and the historical phrase "graded nonlinear algebra" is `HISTORICAL/SUPERSEDED`.

A more accurate structural statement is:

> Objects are labeled finite-dimensional state spaces; well-typed HTNLA maps are morphisms; finite compositions remain well-typed nonlinear maps.

This is sufficient for compositional reasoning without making an unsupported algebraic claim.

## 3.7 Labels remain types after nonlinearity

The nonlinear step does not erase semantic typing. Even when two target components happen to share the same dimension,

\[
q_{t_1}=q_{t_2},
\]

there is no automatic identification

\[
\mathbb R^{q_{t_1}}\equiv\mathbb R^{q_{t_2}}
\]

at the semantic layer.

An explicit cross-label mapping is still required.

---

# 4. Differential Structure, Activations, and Local Stability

## 4.1 Componentwise differentiable case

Suppose each \(\phi_t\) is differentiable at \(z_t\). Let

\[
D\phi_t(z_t)\in\mathbb R^{q_t\times q_t}
\]

be its Jacobian. For elementwise activations this matrix is diagonal.

The block Jacobian of the HTNLA layer is

\[
\boxed{
J_{t,s}(x)=D\phi_t(z_t)W_{t,s}
}
\]

for \((t,s)\in E\), before any hard k-WTA step.

This equation is useful because it preserves the label structure of backpropagation and local sensitivity. It also shows immediately that a nonlinear activation can suppress directions even when \(W_{t,s}\) itself is full rank.

## 4.2 Residual Jacobian

For

\[
F(x)=Rx+\sigma(Mx+b),
\]

the Jacobian is

\[
J_F(x)=R+D\sigma(Mx+b)M.
\]

This does not prove convergence or stability. It simply supplies the local differential object on which conditioning, local inversion, contraction, or control analyses can be based.

## 4.3 Lipschitz bound

Suppose \(\sigma\) is Lipschitz with constant \(L_\sigma\) under a declared compatible norm. Then

\[
\|\sigma(u)-\sigma(v)\|\le L_\sigma\|u-v\|.
\]

For

\[
F(x)=\sigma(Mx+b),
\]

one obtains the direct bound

\[
\boxed{
\|F(x)-F(y)\|\le L_\sigma\|M\|\,\|x-y\|
}
\]

and for the residual form,

\[
\boxed{
\|F(x)-F(y)\|
\le
(\|R\|+L_\sigma\|M\|)\|x-y\|.
}
\]

These are **sensitivity bounds**, not a theorem that training converges or that the network is Lyapunov stable.

A contraction claim requires an actual condition such as

\[
\|R\|+L_\sigma\|M\|<1
\]

under the chosen norm and mapping domain. Without such a condition, "residual connections guarantee stability" is not justified.

## 4.4 Local invertibility

For a smooth map between equal-dimensional Euclidean spaces, a nonsingular Jacobian at a point supports local invertibility in a neighborhood under the inverse-function theorem.

For HTNLA, the practical implication is:

```text
local nonsingular Jacobian
        ->
possible local inverse
```

not:

```text
local nonsingular Jacobian
        ->
global exact inverse
```

Global inversion additionally depends on domain restrictions and global injectivity.

## 4.5 Activation taxonomy

The principal activation cases are:

- **Identity - bijective.** It preserves whatever injectivity already exists in the affine precursor.
- **Leaky ReLU with slope \(a>0\) - bijective on \(\mathbb R\) coordinatewise.** An exact coordinate inverse exists, although the full layer still depends on block geometry.
- **tanh - bijective from \(\mathbb R\) to \((-1,1)\).** `artanh` is the mathematical inverse on the open range; finite-precision recovery may be ill-conditioned near saturation.
- **Logistic sigmoid - bijective from \(\mathbb R\) to \((0,1)\).** The same formal-versus-numerical distinction applies.
- **ReLU - non-injective.** All negative preactivations collapse to zero.
- **Hard clipping - non-injective outside its unsaturated interior.** Saturated values lose magnitude information.
- **GELU / Swish - no globally tractable bijection is assumed.** Treat inversion as restricted-domain or numerical unless separately proved.
- **Hard k-WTA - non-injective.** Discarded coordinates are not recoverable from output alone.

The historical claim that "tanh makes binding non-invertible" was too crude. Tanh itself is invertible on its range. Information loss may instead arise from a non-injective preceding map, dimensional compression, approximate binding, quantization, clipping, missing bias metadata, or later hard sparsification.

## 4.6 Hard k-WTA breaks ordinary differentiability

Hard k-WTA changes support when score orderings cross. At such boundaries the operator is discontinuous in its discrete support-selection map and is not ordinarily differentiable as a global smooth activation.

Within a region where the winning support is fixed and no ties occur, k-WTA behaves like multiplication by a constant diagonal mask:

\[
K_k(y)=D_My,
\]

where \(D_M\) has ones on retained coordinates and zeros elsewhere.

Locally within that fixed-support region,

\[
J_{K_k}=D_M.
\]

At support-change boundaries this local Jacobian description is insufficient. Any use of straight-through estimators, soft top-k relaxations, or differentiable sorting is `APPLICATION-SPECIFIC` and must be named as such.

---

# 5. Reconstruction and Epistemic Semantics

## 5.1 Exact recovery requires injectivity of the composite path

Consider

\[
F=K\circ\phi\circ A,
\]

where \(A\) is an affine or block-affine map, \(\phi\) a nonlinear activation, and \(K\) an optional sparsifier.

If any stage is many-to-one over the reachable domain, then the composite can be many-to-one.

If

\[
F(x_1)=F(x_2)
\]

for

\[
x_1\neq x_2,
\]

there is no unique inverse over that domain.

This is the central mathematical rule behind the HTNLA reconstruction contract.

## 5.2 Reconstruction method and epistemic outcome are different axes

HTNLA retains five reconstruction classes:

1. **Exact inverse**
2. **Pseudoinverse / regularized linear estimate**
3. **Partial unbinding**
4. **Iterative or resonator reconstruction**
5. **Explicit unresolved or information-loss result**

These are **methods or guarantee classes**. They do not replace the canonical quinary epistemic outcomes:

- `EXACT`
- `AMBIGUOUS`
- `UNKNOWN`
- `IMPOSSIBLE`

The mapping is intentionally not one-to-one.

The mapping is:

- **Exact inverse.** A unique preimage is established under declared assumptions. The permissible result is `EXACT`; `IMPOSSIBLE` is also possible when the requested output is proved outside the map's range.
- **Pseudoinverse / regularized estimate.** A least-squares or minimum-norm representative is selected. The result is usually `AMBIGUOUS`; it may be `EXACT` only with independent proof of uniqueness.
- **Partial unbinding.** Some coordinates, labels, or factors are recoverable. Proved subcomponents may be `EXACT`, while the remainder is `AMBIGUOUS` or `UNKNOWN`.
- **Iterative / resonator search.** Candidate preimages are searched or optimized. Any quinary outcome is possible depending on certification: unique solution -> `EXACT`; multiple viable solutions -> `AMBIGUOUS`; unresolved search -> `UNKNOWN`; proved absence -> `IMPOSSIBLE`.
- **Explicit unresolved/loss.** Information or provenance is insufficient. The result is `AMBIGUOUS`, `UNKNOWN`, or `IMPOSSIBLE`; never silently `EXACT`.

The governing law is:

```text
algorithm returned a vector != original state uniquely recovered
```

## 5.3 Pseudoinverse is a linear concept

For a linear map \(A\), the Moore-Penrose pseudoinverse \(A^+\) supplies a least-squares/minimum-norm solution under standard conditions. If \(A\) is not injective, however,

\[
\hat x=A^+y
\]

need not be the original \(x\).

For a generic nonlinear HTNLA map, the word "pseudoinverse" should therefore be reserved for a linear or linearized segment, or for a specifically defined generalized inverse construction. An optimizer minimizing nonlinear reconstruction error is not automatically a Moore-Penrose pseudoinverse.

## 5.4 Iterative reconstruction

Given observed target state \(y\), one possible reconstruction problem is

\[
\hat x
=
\arg\min_x
\left[
\frac12\|F(x)-y\|^2+\lambda\mathcal R(x)
\right],
\]

where \(\mathcal R\) encodes application-specific priors or constraints.

For a differentiable map before hard support changes,

\[
x^{(m+1)}=x^{(m)}-\eta\nabla_x\mathcal L(x^{(m)}).
\]

This procedure can produce a candidate. It does not establish uniqueness unless the objective and feasible set provide that guarantee.

A successful numerical fit may therefore still be `AMBIGUOUS` if multiple source states produce the same target.

## 5.5 Worked example: compression plus hard sparsity

Suppose

\[
x_{text}\in\mathbb R^{256},
\qquad
x_{image}\in\mathbb R^{768}.
\]

The joint source therefore contains 1024 real degrees of freedom before any source-side constraints are imposed.

Let

\[
z_{fusion}
=
W_{fusion,text}x_{text}
+
W_{fusion,image}x_{image}
+b
\in\mathbb R^{512}.
\]

Even before a nonlinear activation, an arbitrary mapping from the full 1024-dimensional source into a 512-dimensional linear target cannot be injective over the whole source space.

Now apply a nonlinearity and retain only 64 coordinates:

\[
y=K_{64}(\phi(z_{fusion})).
\]

The final output has undergone both dimensional compression and hard information deletion.

Without additional restrictions or side information, the correct reconstruction statement is not:

```text
approximately invertible
```

but:

```text
multiple source states may be compatible with the same output
```

which generally requires `AMBIGUOUS` or `UNKNOWN` status depending on what can be proved.

## 5.6 ReLU witness

For scalar ReLU,

\[
\operatorname{ReLU}(-1)=\operatorname{ReLU}(-9)=0.
\]

Thus ReLU is non-injective.

The executed reference test in this paper confirms the vector witness:

```text
relu([-1, 2]) = [0, 2]
relu([-9, 2]) = [0, 2]
```

No reconstruction procedure can determine from the output alone which negative first coordinate was present.

## 5.7 k-WTA witness

Let

```text
v1 = [10, 9,  0.5, 0.4]
v2 = [10, 9, -7.0, 0.1]
```

For top-2-by-magnitude k-WTA,

```text
K_2(v1) = [10, 9, 0, 0]
K_2(v2) = [10, 9, 0, 0]
```

The discarded coordinates differ substantially, yet the sparse outputs are identical. Hard k-WTA is therefore many-to-one.

---

# 6. Binding and the Quinary Reference Interface

## 6.1 HTNLA does not replace canonical binding

The deterministic Nexus v4 quinary binding operation remains the authoritative reference binding contract.

For the reference quinary alphabet

\[
\mathcal Q=\{-2,-1,0,+1,+2\},
\]

binding is intentionally information-losing. HTLA's current reference paper defines coordinate-level recovery outcomes as:

- `EXACT`
- `AMBIGUOUS`
- `UNKNOWN`
- `IMPOSSIBLE`

HTNLA must preserve those semantics rather than introducing a parallel notion of "soft exactness."

## 6.2 Historical soft binding is not canonical

Earlier HTLA/HTNLA drafts used constructions such as

\[
\operatorname{bind}(H,K)=\tanh(H\circledast K+b).
\]

That formulation is `HISTORICAL/SUPERSEDED` as the Nexus reference binding rule.

This does not mean circular convolution or tanh are invalid mathematics. It means that the current reference geometry prefers a deterministic quinary operation whose information loss can be classified mechanically.

## 6.3 Differentiable surrogates are allowed only as surrogates

An application may define a differentiable training surrogate

\[
B_\theta(x,y)
=
\psi_\theta(P_\theta(x,y))
\]

for gradient-based learning.

Such a surrogate must be tagged `APPLICATION-SPECIFIC` or `EXPERIMENTAL` and evaluated against the deterministic reference when semantic compatibility matters.

Required reporting includes:

```text
reference binding result
surrogate result
agreement/disagreement condition
reference unbind status
surrogate reconstruction status
```

The surrogate does not gain authority merely because it is easier to differentiate.

## 6.4 Missingness is not zero

The same epistemic rule used elsewhere in Nexus applies here:

```text
UNKNOWN != 0
AMBIGUOUS != approximate EXACT
IMPOSSIBLE != low confidence
```

A nonlinear layer that loses a coordinate must not fill it with a numeric zero and then treat that value as an observation of zero.

---

# 7. k-WTA, Structural Sparsity, and Complexity

## 7.1 Deterministic k-WTA definition

For \(v\in\mathbb R^d\) and integer \(1\le k\le d\), define a top-k index set

\[
I_k(v)=\operatorname{TopK}(|v|,k)
\]

under a declared deterministic tie rule.

Then

\[
(K_k(v))_i=
\begin{cases}
v_i,&i\in I_k(v),\\
0,&i\notin I_k(v).
\end{cases}
\]

The reference implementation in this paper resolves equal magnitudes by lower coordinate index.

If deterministic replay matters, tie behavior is part of the state-transition contract.

## 7.2 Dense block-affine cost

For coupling relation \(E\subseteq T\times S\), a dense block multiplication has arithmetic cost proportional to

\[
\boxed{
C_{block}=\Theta\!\left(\sum_{(t,s)\in E}q_tp_s\right).
}
\]

This is more informative than a blanket \(O(D^2)\) statement because it retains the actual label topology and heterogeneous dimensions.

If every source communicates with every target and total source/target dimensions scale together, the sum may scale quadratically in total dimension.

## 7.3 Post-activation sparsity does not erase prior work

The path

```text
x --dense block multiplication--> z --activation--> y --kWTA--> sparse y
```

still paid for the dense multiplication that produced \(z\).

Therefore:

```text
post-activation zeros != retroactive compute savings
```

A fixed retention fraction \(\rho\in(0,1)\) can reduce **later** sparse-aware work by a constant factor if later kernels actually exploit sparse input.

Because

\[
\rho D=\Theta(D)
\]

for constant \(\rho\), this does not by itself change the asymptotic class.

The historical claim

```text
70% sparsity => O(D log D)
```

is `HISTORICAL/SUPERSEDED`.

## 7.4 When asymptotic savings are real

Asymptotic improvement can come from actual structure.

Suppose there are \(L\) labels, each component has dimension at most \(n\), and each target label receives from at most \(c\) source labels for constant \(c\). Then

\[
|E|=O(L)
\]

and

\[
C_{block}=O(Ln^2).
\]

If total dimension is

\[
D=Ln,
\]

then

\[
C_{block}=O(Dn).
\]

For bounded \(n\), this is linear in total dimension \(D\).

Here the saving arises from **bounded-degree block topology**, not from post-hoc coordinate zeros.

Other legitimate sources of subquadratic cost include:

- FFT-compatible circulant or convolutional blocks;
- low-rank factors;
- sparse matrices with sparse kernels;
- conditional route activation;
- approximate structured transforms.

Each requires its own cost model.

## 7.5 Structural vacuum in the quinary reference geometry

The current Nexus quinary reference geometry uses

\[
d=1024,
\qquad
K_{wall}=307,
\]

so its active count satisfies

\[
\|A\|_0\le307.
\]

That implies at least approximately 70.02% structural vacuum in that **specific reference representation**.

This is not equivalent to claiming that every continuous HTNLA hidden layer must retain exactly 30% of its coordinates.

The distinction is:

```text
quinary reference occupancy constraint
        !=
universal neural-layer sparsity law
```

An HTNLA layer may choose a different \(k_t\), no k-WTA at all, or an entirely different sparse mechanism depending on the application.

## 7.6 Concentration claims

The source research considered whether k-WTA preserves concentration or quasi-orthogonality. Such a theorem depends on the input distribution, block maps, activation, support-selection rule, normalization, and correlation structure.

No general theorem in the supplied material establishes:

```text
arbitrary HTNLA + hard kWTA
        ->
preserved concentration of measure
```

Therefore that claim remains `RESEARCH HYPOTHESIS`.

A valid future theorem must state an explicit random model and bound the transformed distribution actually produced by the configured HTNLA layer.

---

# 8. Learning, Gradients, and Adaptation

## 8.1 Blockwise gradient structure

Let a scalar loss be \(\mathcal L\). Before any hard support discontinuity, define the target preactivation gradient

\[
g_t=\nabla_{z_t}\mathcal L\in\mathbb R^{q_t}.
\]

For

\[
z_t=b_t+\sum_sW_{t,s}x_s,
\]

the block gradient is

\[
\boxed{
\frac{\partial\mathcal L}{\partial W_{t,s}}=g_tx_s^T.
}
\]

Its shape is

\[
q_t\times p_s,
\]

exactly matching the typed block geometry.

This is an important implementation invariant: heterogeneous labels do not require padding or cross-label averaging to compute gradients.

## 8.2 Backpropagation to source components

The source gradient accumulates from every target that receives from \(s\):

\[
\boxed{
\nabla_{x_s}\mathcal L
=
\sum_{t:(t,s)\in E}W_{t,s}^Tg_t.
}
\]

Again, the coupling graph is explicit.

## 8.3 Hard k-WTA and training

If hard k-WTA is present, ordinary gradients are well-defined only away from support changes under a fixed active mask. A training system must state which mechanism it uses:

- hard mask with subgradient-like treatment;
- straight-through estimator;
- soft top-k relaxation;
- differentiable sorting/selection;
- alternating discrete/continuous optimization;
- no gradient through the selector.

No one choice is part of core HTNLA.

## 8.4 Optional modulatory learning signal

A generic software modulation rule can be written

\[
E_{t,s}^{(k+1)}
=
\lambda_EE_{t,s}^{(k)}
+
G_{t,s}^{(k)},
\]

followed by

\[
\Delta W_{t,s}^{(k)}
=
\eta\,m_k\,E_{t,s}^{(k)},
\]

where:

- \(E_{t,s}\) is an eligibility-like state;
- \(G_{t,s}\) is a local update contribution such as \(g_tx_s^T\);
- \(m_k\) is an external scalar modulation signal.

This is a **Level-1 computational mechanism**. Calling \(m_k\) "dopamine" would make it a Level-2 functional analogy at most and requires explicit scoping.

### Important Nexus temporal-causality constraint

HTNLA does not manufacture a valid reward-prediction error merely by subtracting two contemporaneous scalars.

If \(m_k\) is claimed to be a remediation RPE, its producer must satisfy the temporal/provenance contract established elsewhere in Nexus: a pre-action prediction, explicit action binding, post-action observation, sufficient observability, and valid temporal lineage.

Thus:

```text
HTNLA may consume a modulation signal
        !=
HTNLA establishes that the signal is causally valid RPE
```

## 8.5 Dynamic label adaptation is a schema operation

Historical prototypes attempted to average differently sized label vectors. That contradicts the direct-sum premise.

A new label or new component dimension must therefore arise through an explicit schema transition such as:

\[
P_{new\leftarrow s}:\mathbb R^{p_s}\to\mathbb R^{q_{new}}.
\]

The transition should record:

```text
source label
new label
source dimension
new dimension
projection / initialization method
trigger evidence
model generation
provenance
```

No cross-label arithmetic is legal merely because two components are stored in the same HVD.

## 8.6 Regularization

Standard regularizers may be applied blockwise, for example

\[
\mathcal L_{reg}
=
\lambda_1\sum_{t,s}\|W_{t,s}\|_1
+
\lambda_2\sum_{t,s}\|W_{t,s}\|_F^2.
\]

This is ordinary optimization machinery. It does not constitute a measured "energy conservation law."

Any hardware energy claim requires telemetry such as joules per query, joules per training step, or power-time integration under a specified device and workload.

---

# 9. HVD, TMS, HDF5, and ANN Integration

## 9.1 Architectural ownership

HTNLA is a transform subsystem. It does not own the active database.

The current Nexus ownership boundary remains:

```text
HVD   = logical cognitive database semantics
TMS   = mandatory live state / storage substrate
HDF5  = durable long-term persistence
HTNLA = nonlinear transform semantics
ANN   = derived retrieval acceleration
```

HTNLA parameters that affect authoritative behavior must therefore be represented as versioned HVD/TMS state rather than hidden process-local variables.

## 9.2 Model generation is part of state interpretation

Let

\[
\theta_g
\]

denote the parameter generation for an HTNLA model. A transformed representation should be interpreted as

\[
y=F_{\theta_g}(x).
\]

The same raw state transformed under a different generation

\[
F_{\theta_{g+1}}(x)
\]

may occupy a different geometry.

Therefore a transformed record should not be stored without enough metadata to identify the model generation that produced it.

A minimum conceptual descriptor is:

```text
model_id
model_generation
input schema version
output schema version
activation configuration
k-WTA configuration
block parameter digest
training/provenance reference
```

## 9.3 Index consistency

If an ANN/HNSW index stores transformed vectors

\[
F_{\theta_g}(x_i),
\]

then queries must be transformed under a representation compatible with that index.

Using

\[
F_{\theta_{g+1}}(q)
\]

against an index built under \(\theta_g\) can invalidate distance semantics even when every individual vector is numerically well formed.

This creates an explicit consistency rule:

```text
query transform generation
        must be compatible with
index representation generation
```

A model change may therefore require:

- index rebuild;
- dual-generation serving;
- migration/re-encoding;
- compatibility bridge;
- fail-closed rejection.

## 9.4 ANN/HNSW remains derived

A nonlinear transform may be useful before ANN indexing or retrieval, but it does not change the epistemic status of ANN.

```text
nearest neighbor after HTNLA transform
        !=
identity proof
```

and:

```text
high recall on a benchmark
        !=
constitutional admissibility
```

HNSW and related indexes remain derived acceleration structures.

## 9.5 TMS persistence path

HTNLA parameter mutations that are part of live authoritative state should follow ordinary TMS realization mechanics rather than inventing a separate database:

```text
authorized parameter/state mutation
          |
          v
         WAL
          |
          v
      Memtable
          |
          v
 immutable generations / SSTables
          |
          v
 compaction / reconsolidation
```

Whether a training step is itself authorized to produce such a mutation is a separate control question.

The mathematical subsystem does not grant mutation authority.

## 9.6 Durable persistence

Stable parameter generations and required model metadata may be included in the durable HDF5 persistence representation according to the broader Nexus persistence policy.

HDF5 is not reduced here to a "snapshot-only" role. It is the durable long-term persistence tier. Snapshotting, archival flush, restoration, and rehydration are mechanisms within that role.

## 9.7 Compaction is not automatically training

Historical HTNLA drafts proposed deferring expensive nonlinear work or training to database compaction. That may be a useful implementation experiment, but it is **not** a canonical property of compaction.

Database compaction owns storage maintenance. If a system chooses to attach learned reconsolidation or re-encoding to compaction, it must define:

```text
trigger
input generation
output generation
failure semantics
rollback
index invalidation
provenance
mutation authority
```

Without that contract, "compaction trains the nonlinear model" is only `PROPOSED`.

## 9.8 Ephemeral HVDs and counterfactual parameter states

An ephemeral HVD can host a candidate HTNLA state or model generation for counterfactual evaluation without mutating the authoritative HVD.

For example:

```text
authoritative model theta_0
          |
          +--> candidate theta_1 in ephemeral HVD D_1
          +--> candidate theta_2 in ephemeral HVD D_2
          +--> candidate theta_3 in ephemeral HVD D_3
```

Each candidate can be evaluated for task performance, HIGC admissibility, THDE transition implications, resource cost, or other criteria.

Selection still does not imply enactment:

```text
candidate model selected != authoritative model promoted
```

Promotion remains externally authorized.

---

# 10. Reference Implementation and Executed Validation

## 10.1 Scope of the reference code

The implementation below deliberately does less than the historical prototype. It verifies the core subsystem contract:

- labeled heterogeneous vectors;
- dimensionally typed blocks;
- target-specific nonlinearities;
- residual maps outside the nonlinear branch;
- deterministic k-WTA;
- fail-fast shape checking;
- exact coordinate inversion for a bijective activation example;
- explicit witnesses for non-injective activations.

It does **not** claim production performance, distributed training, durable database integration, learned inversion, biological fidelity, or benchmark superiority.

## 10.2 Executed reference implementation

```python
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Mapping, Optional
import numpy as np

Array = np.ndarray
Activation = Callable[[Array], Array]


def identity(x: Array) -> Array:
    return np.asarray(x, dtype=float)


def relu(x: Array) -> Array:
    return np.maximum(np.asarray(x, dtype=float), 0.0)


def leaky_relu(x: Array, slope: float = 0.1) -> Array:
    if not (0.0 < slope <= 1.0):
        raise ValueError("slope must lie in (0, 1].")
    x = np.asarray(x, dtype=float)
    return np.where(x >= 0.0, x, slope * x)


def leaky_relu_inverse(y: Array, slope: float = 0.1) -> Array:
    if not (0.0 < slope <= 1.0):
        raise ValueError("slope must lie in (0, 1].")
    y = np.asarray(y, dtype=float)
    return np.where(y >= 0.0, y, y / slope)


def k_wta(x: Array, k: int) -> Array:
    """Keep exactly k entries by absolute magnitude; ties favor lower index."""
    x = np.asarray(x, dtype=float)
    if x.ndim != 1:
        raise ValueError("k_wta expects a 1-D vector.")
    if not (1 <= k <= x.size):
        raise ValueError("k must satisfy 1 <= k <= len(x).")

    order = np.lexsort((np.arange(x.size), -np.abs(x)))
    keep = order[:k]
    out = np.zeros_like(x)
    out[keep] = x[keep]
    return out


@dataclass(frozen=True)
class LabeledVector:
    components: Mapping[str, Array]

    def checked(self) -> "LabeledVector":
        out: dict[str, Array] = {}
        for label, value in self.components.items():
            arr = np.asarray(value, dtype=float)
            if arr.ndim != 1:
                raise ValueError(f"{label}: component must be a 1-D vector.")
            out[label] = arr
        return LabeledVector(out)


@dataclass
class NonlinearBlockOperator:
    blocks: Mapping[str, Mapping[str, Array]]
    biases: Mapping[str, Array]
    activations: Mapping[str, Activation]
    residual_blocks: Optional[Mapping[str, Mapping[str, Array]]] = None
    winners: Optional[Mapping[str, int]] = None

    def apply(self, x: LabeledVector) -> LabeledVector:
        x = x.checked()
        out: dict[str, Array] = {}

        for target, by_source in self.blocks.items():
            if target not in self.biases or target not in self.activations:
                raise KeyError(f"{target}: missing bias or activation.")

            z = np.asarray(self.biases[target], dtype=float).copy()
            if z.ndim != 1:
                raise ValueError(f"{target}: bias must be 1-D.")

            target_dim = z.size

            for source, W in by_source.items():
                if source not in x.components:
                    raise KeyError(f"missing source label {source!r}")

                W = np.asarray(W, dtype=float)
                xs = x.components[source]
                expected = (target_dim, xs.size)

                if W.shape != expected:
                    raise ValueError(
                        f"block {target}<-{source} has shape {W.shape}, "
                        f"expected {expected}"
                    )

                z += W @ xs

            y = np.asarray(self.activations[target](z), dtype=float)
            if y.shape != (target_dim,):
                raise ValueError(
                    f"{target}: activation changed target-vector shape"
                )

            if self.residual_blocks and target in self.residual_blocks:
                r = np.zeros(target_dim, dtype=float)
                for source, R in self.residual_blocks[target].items():
                    if source not in x.components:
                        raise KeyError(
                            f"missing residual source label {source!r}"
                        )

                    R = np.asarray(R, dtype=float)
                    xs = x.components[source]
                    expected = (target_dim, xs.size)

                    if R.shape != expected:
                        raise ValueError(
                            f"residual block {target}<-{source} "
                            f"has shape {R.shape}, expected {expected}"
                        )

                    r += R @ xs

                y = r + y

            if self.winners and target in self.winners:
                y = k_wta(y, self.winners[target])

            out[target] = y

        return LabeledVector(out)
```

## 10.3 Heterogeneous-dimension fixture

The executed fixture uses:

```text
source:
    text   : R^3
    vision : R^5

target:
    semantic : R^4
    control  : R^2
```

with a residual map from `text -> semantic` and top-2 k-WTA on `semantic`.

Executed output:

```text
HETEROGENEOUS FORWARD CHECK
{'semantic': (4,), 'control': (2,)}
semantic_nonzero = 2
semantic = [3.47728498 0.         4.37847313 0.        ]
control = [0.99143319 0.99954503]
```

This verifies the intended heterogeneous label contract for the tested fixture.

## 10.4 Malformed block rejection

A deliberately malformed block of shape `(4,4)` was supplied for a source label of dimension `3`.

Executed result:

```text
MALFORMED SHAPE CHECK
ValueError: block semantic<-text has shape (4, 4), expected (4, 3)
```

The implementation therefore fails closed on that dimensional mismatch.

## 10.5 Exact activation inverse example

For leaky ReLU with positive slope \(0.1\), the coordinatewise inverse was executed on

```text
[-2.0, -0.25, 0.0, 0.5, 3.0]
```

and returned:

```text
LEAKY-RELU INVERSE CHECK
max_abs_error = 0.0
```

This verifies the activation's exact inverse for the tested floating-point values. It does not prove that an arbitrary full HTNLA layer containing that activation is globally invertible.

## 10.6 ReLU non-injectivity

Executed result:

```text
RELU NON-INJECTIVITY WITNESS
outputs_equal = True
output = [0.0, 2.0]
```

Distinct source vectors therefore produced the same output.

## 10.7 k-WTA non-injectivity

Executed result:

```text
KWTA NON-INJECTIVITY WITNESS
outputs_equal = True
output = [10.0, 9.0, 0.0, 0.0]
```

Again, distinct inputs produced the same sparse output.

## 10.8 Deterministic tie rule

For

```text
[5.0, -5.0, 1.0, 0.0]
```

with `k=1`, equal absolute magnitude occurs at indices 0 and 1. The reference rule chooses the lower coordinate index:

```text
KWTA TIE CHECK
k=1 output = [5.0, 0.0, 0.0, 0.0]
```

Deterministic tie handling is therefore part of the executable reference contract.

---

# 11. Validation and Falsification Program

HTNLA should be evaluated by decomposing its claims rather than asking whether "nonlinearity works" in the abstract.

## 11.1 Primary empirical hypothesis

A properly scoped empirical hypothesis is:

> **RESEARCH HYPOTHESIS:** For tasks whose relevant decision or retrieval geometry is not adequately represented by a matched linear HTLA baseline, a trained HTNLA configuration can improve at least one preregistered task metric under a controlled accuracy-efficiency trade-off.

No percentage is attached until measured.

## 11.2 Required baselines

At minimum, compare:

1. matched linear HTLA block model;
2. HTNLA without k-WTA;
3. HTNLA with k-WTA;
4. structurally block-sparse HTNLA;
5. optional invertible-profile HTNLA;
6. parameter- or compute-matched conventional nonlinear network;
7. graph-typed or MoE baseline when those analogies are actually relevant.

## 11.3 Required ablations

Required ablations are:

- **Linear vs nonlinear.** Ask whether nonlinearity itself helps. Report task metric, seeds, dataset split, and uncertainty.
- **Activation family.** Ask whether benefit is activation-specific. Compare ReLU, leaky ReLU, smooth alternatives, and an invertible profile where relevant.
- **k-WTA on/off.** Ask whether hard sparsity helps. Report task result, reconstruction-status distribution, and actual sparse-kernel utilization.
- **k sweep.** Measure the full quality/sparsity frontier rather than one selected point.
- **Block topology.** Ask whether speedup is caused by structural sparsity. Report \(|E|\), block dimensions, FLOPs, and wall time.
- **Residual map.** Ask whether residual geometry improves optimization. Report training curves, conditioning, and final task metric.
- **Inversion class.** Test whether returned `EXACT/AMBIGUOUS/UNKNOWN/IMPOSSIBLE` status matches inverse ground truth.
- **Model-generation change.** Test whether index/query consistency survives migration, dual-generation serving, or rebuild.
- **Surrogate binding.** Test whether a differentiable surrogate preserves deterministic reference behavior; report the quinary agreement distribution.

## 11.4 Metrics

Permissible metrics include:

- Recall@K, MRR, NDCG, classification accuracy, F-score, MSE, NLL, or another task-defined metric;
- p50/p95/p99 latency under specified hardware and batch conditions;
- throughput;
- peak memory and parameter bytes;
- measured sparse-kernel utilization;
- fraction of active coordinates and blocks;
- reconstruction error under a declared reconstruction method;
- calibration of epistemic recovery state against known inverse ground truth;
- joules/query or joules/training step from actual telemetry.

Undefined metrics such as "cognitive fidelity," "Binding Score," "Neural Dynamics Fidelity," or \(\Phi\) are not admissible merely because they appeared in historical drafts.

## 11.5 Falsification examples

The following observations would falsify common HTNLA claims:

- If matched HTLA performs equally well or better across preregistered nonlinear tasks, the claimed task advantage is not supported.
- If k-WTA produces zeros but dense kernels still dominate runtime, a compute-efficiency claim based on sparsity is falsified.
- If reconstruction is labeled `EXACT` for known many-to-one maps, the epistemic contract is violated.
- If a model generation changes while the ANN index remains stale and retrieval degrades, generation-independent index semantics are falsified.
- If a "dopamine" scalar uses no temporally valid reward prediction error but is described as such, the causal interpretation is invalid even if training numerically improves.

---

# 12. Failure Modes and Adversarial Cases

## 12.1 Silent dimension coercion

**Failure:** pad or truncate components implicitly so matrix multiplication succeeds.

**Risk:** a type error becomes a numeric value.

**Rule:** all dimension changes require explicit named transforms.

## 12.2 Hidden model drift

**Failure:** transform queries with a new model against an old transformed index.

**Risk:** retrieval geometry changes without version awareness.

**Rule:** model generation and representation generation are coupled metadata.

## 12.3 Sparsity theater

**Failure:** report 70% zeros while performing dense matrix multiplication, dense memory transfer, and dense communication.

**Risk:** representation sparsity is mistaken for realized compute savings.

**Rule:** measure executed sparse kernels and end-to-end cost.

## 12.4 False inversion

**Failure:** an optimizer returns one candidate and code labels it the recovered original.

**Risk:** ambiguity is erased.

**Rule:** a candidate reconstruction remains `AMBIGUOUS` unless uniqueness is independently established.

## 12.5 k-WTA ties

**Failure:** top-k uses nondeterministic tie behavior.

**Risk:** replay diverges across platforms or runs.

**Rule:** tie-breaking must be deterministic if deterministic replay is a requirement.

## 12.6 Missingness collapsed into zero

**Failure:** coordinates pruned or made unrecoverable are returned as observed zero.

**Risk:** epistemic loss masquerades as data.

**Rule:** recovery status travels alongside any candidate value.

## 12.7 Biologically named variables gain undeserved authority

**Failure:** scalar software variables are described as literal dopamine, serotonin, GABA, or conscious state.

**Risk:** functional analogy becomes biological or phenomenological claim.

**Rule:** apply the Nexus three-level distinction.

## 12.8 Counterfactual model self-promotion

**Failure:** an ephemeral HVD candidate model selects itself as authoritative because its score improved.

**Risk:** planning becomes unauthorized history.

**Rule:** external promotion authority remains mandatory.

---

# 13. Research Extensions

Everything in this section is non-load-bearing unless promoted by separate evidence.

## 13.1 Explicit invertible profile

**Status: PROPOSED / ACTIVE DEVELOPMENT**

A restricted HTNLA profile could require:

- equal total source and target dimension where exact global bijection is needed;
- invertible affine/block transforms;
- bijective activations;
- no hard information-destroying k-WTA;
- explicit log-determinant/Jacobian tracking where density modeling is relevant.

This would make exact inversion an architectural mode rather than a post-hoc hope.

## 13.2 Sparse conditional routing

**Status: RESEARCH HYPOTHESIS**

Instead of applying dense blocks and sparsifying afterward, a router could activate only a bounded set of source-target blocks per input. This may create genuine compute savings if routing cost, communication, and sparse kernels are accounted for.

The relevant metric is active computation, not logical sparsity alone.

## 13.3 Nonlinear retrieval geometry

**Status: RESEARCH HYPOTHESIS**

A trained HTNLA transform may improve retrieval for a specific task by reshaping representation geometry. This does not imply that HNSW becomes "manifold aware" automatically.

Any claim must compare:

```text
raw-space index
transformed-space index
query transform generation
index generation
recall / latency / memory
```

and both indexed items and queries must be transformed consistently.

## 13.4 Equivariant target maps

**Status: RESEARCH HYPOTHESIS**

If a label carries a known group action, one may constrain blocks and nonlinearities to preserve equivariance. Labels alone do not define a gauge group or representation; those structures must be declared separately.

## 13.5 Continuous-depth HTNLA

**Status: RESEARCH HYPOTHESIS**

A time-dependent nonlinear labeled state may be modeled by

\[
\frac{dH}{dt}=f_\theta(H,t)
\]

with an HTLA/HTNLA-compatible labeled vector field. This requires explicit regularity conditions, numerical integration semantics, and a reason continuous depth is useful for the target workload.

## 13.6 Reward-modulated adaptation

**Status: APPLICATION-SPECIFIC / RESEARCH HYPOTHESIS**

Eligibility traces and external modulatory signals may be useful for some adaptive systems. The biological names remain analogy only, and any remediation-RPE interpretation requires the temporal-causality contract described elsewhere in Nexus.

## 13.7 Quantum-assisted nonlinear processing

**Status: RESEARCH HYPOTHESIS**

Closed-system quantum evolution is linear and unitary. Generic ReLU, sigmoid, top-k, or k-WTA on amplitudes cannot simply be inserted as deterministic unitary gates.

Potential research mechanisms include:

- measurement back-action;
- ancilla-mediated nonlinear effective maps;
- postselection;
- repeat-until-success constructions;
- multi-copy estimation of nonlinear state functions;
- hybrid quantum-classical pipelines.

QSVT remains a powerful linear-operator singular-value transformation framework; it does not establish an HTNLA-specific nonlinear quantum primitive or speedup.

## 13.8 Dynamic label birth and retirement

**Status: RESEARCH HYPOTHESIS**

A time-varying label set

\[
L(t)
\]

may be useful for adaptive systems, but label birth is a schema/identity event, not merely a tensor resize. Any implementation must define namespace ownership, migration, model generation, and durable provenance.

---

# 14. Claim-Status Audit

The audit is intentionally written as a claim ledger rather than a compact table so that long mathematical statements remain readable in ordinary document layouts.

- **HTLA direct-sum substrate** - `CANONICAL`. Established by current Nexus/HTLA architecture
- **Canonical target preactivation \(z_t=b_t+\sum_sW_{t,s}x_s+r_t\)** - `CANONICAL`. Nexus monograph §6
- **Target nonlinearity \(y_t=\phi_t(z_t)\)** - `CANONICAL`. Nexus monograph §6
- **Optional k-WTA** - `CANONICAL as supported operator form; use is configuration-specific`. Nexus monograph/reference geometry
- **Multilayer form \(H^{(k+1)}=\sigma^{(k)}(M^{(k)}H^{(k)}+b^{(k)})\)** - `CANONICAL`. Nexus monograph §6
- **Residual form with explicit \(R^{(k)}\)** - `CANONICAL`. Nexus monograph §6
- **HTNLA is a graded nonlinear algebra** - `HISTORICAL/SUPERSEDED`. Ordinary closure under operator addition does not hold
- **HTNLA as family/category of typed nonlinear maps** - `PROPOSED / mathematically coherent`. Direct structural formulation
- **Block Jacobian \(J_{t,s}=D\phi_tW_{t,s}\)** - `VERIFIED`. Direct chain-rule derivation before hard selection
- **Lipschitz sensitivity bound** - `VERIFIED`. Direct norm inequality under stated assumptions
- **Leaky ReLU with positive slope is coordinatewise bijective** - `VERIFIED`. Direct inverse formula; executed test
- **tanh is bijective \(\mathbb R\to(-1,1)\)** - `VERIFIED`. Standard analysis
- **ReLU is non-injective** - `VERIFIED`. Direct counterexample; executed witness
- **Hard k-WTA is non-injective** - `VERIFIED`. Direct counterexample; executed witness
- **Five reconstruction classes** - `CANONICAL`. Current Nexus §6 semantics
- **`EXACT/AMBIGUOUS/UNKNOWN/IMPOSSIBLE` as authoritative recovery outcomes** - `CANONICAL`. Current quinary reference contract
- **Pseudoinverse output proves original state** - `HISTORICAL/SUPERSEDED if implied`. Least-squares/minimum-norm solution need not equal origin
- **Iterative reconstruction can always produce exact inverse** - `HISTORICAL/SUPERSEDED`. Optimization does not guarantee uniqueness
- **Deterministic quinary binding is authoritative reference** - `CANONICAL`. Current Nexus reference geometry
- **Circular-convolution-plus-tanh as canonical binding** - `HISTORICAL/SUPERSEDED`. Replaced by quinary reference contract
- **Fixed 70% k-WTA changes dense \(O(D^2)\) to \(O(D\log D)\)** - `HISTORICAL/SUPERSEDED`. Fixed fractional sparsity changes constants only unless realization changes
- **Bounded-degree block topology can reduce asymptotic block cost** - `VERIFIED under stated assumptions`. Direct operation-count derivation
- **k-WTA preserves concentration for arbitrary HTNLA** - `RESEARCH HYPOTHESIS`. No general theorem supplied
- **k-WTA improves retrieval or stability** - `RESEARCH HYPOTHESIS`. Requires matched ablation
- **20-50% recall improvement** - `HISTORICAL/SUPERSEDED`. No supporting experiment in source corpus
- **Fixed energy-conservation percentage** - `HISTORICAL/SUPERSEDED`. Requires hardware telemetry; old value is a design motif only
- **HTNLA universal approximation for every fixed configuration** - `HISTORICAL/SUPERSEDED`. UAT hypotheses are architecture-specific
- **Some HTNLA subclasses can instantiate theorem-covered feed-forward families** - `INFERRED`. Follows when configuration satisfies theorem assumptions
- **Reward-modulated eligibility rule as computational mechanism** - `APPLICATION-SPECIFIC`. Valid software pattern; biology only functional analogy
- **HTNLA itself produces causally valid remediation RPE** - `NOT CLAIMED`. Causal RPE belongs to temporal/provenance subsystem
- **HNSW after nonlinear transform automatically improves recall** - `RESEARCH HYPOTHESIS`. Requires consistent index/query generations and benchmark
- **ANN/HNSW establishes identity/truth** - `HISTORICAL/SUPERSEDED if implied`. Derived acceleration only
- **Compaction must train/reconsolidate HTNLA models** - `PROPOSED only`. Not a canonical database obligation
- **HDF5 is durable long-term persistence** - `CANONICAL`. Current Nexus architecture
- **Executed heterogeneous-dimension forward fixture** - `VERIFIED`. This paper's deterministic NumPy run
- **Executed malformed-shape rejection** - `VERIFIED`. This paper's negative test
- **Executed deterministic k-WTA tie rule** - `VERIFIED`. This paper's deterministic NumPy run
- **Generic nonlinear map can be directly block-encoded as unitary** - `HISTORICAL/SUPERSEDED`. Quantum evolution/unitary processing is linear; nonlinear effects need extra mechanisms
- **Quantum-assisted HTNLA** - `RESEARCH HYPOTHESIS`. Requires explicit circuit/resource model
- **Identity-transfer / phenomenal-continuity guarantees from HTNLA** - `EXCLUDED`. Outside subsystem scope
---

# 15. HTNLA Engineering Laws

1. **Labels are types, not offsets.**
2. **Equal dimension does not imply semantic compatibility.**
3. **Every cross-label contribution requires an explicit dimensionally valid block.**
4. **Nonlinearity does not erase source/target type information.**
5. **HTNLA is a family of nonlinear maps, not a generic graded algebra.**
6. **A residual path is an explicit map, not an implicit shape cast.**
7. **Exact inversion requires injectivity of the relevant composite path.**
8. **A returned candidate is not proof of unique recovery.**
9. **Pseudoinverse means least-squares/minimum-norm semantics, not recovered history.**
10. **Hard k-WTA is information-losing unless discarded state is preserved elsewhere.**
11. **k-WTA tie behavior must be deterministic when deterministic replay is required.**
12. **Post-activation zeros do not retroactively reduce dense computation.**
13. **Asymptotic speedup must come from realized structure, not a sparsity percentage.**
14. **UNKNOWN is not zero.**
15. **AMBIGUOUS is not approximate EXACT.**
16. **A differentiable binding surrogate is not the canonical binding authority.**
17. **A model generation is part of the interpretation of transformed state.**
18. **An ANN index must be representation-generation compatible with its query transform.**
19. **ANN similarity never becomes identity, truth, admissibility, or authorization.**
20. **HTNLA may consume control signals; it does not acquire the authority of their producer.**
21. **A biologically named variable is a software variable unless stronger evidence exists.**
22. **Training success is not a continuity proof.**
23. **Compaction is not automatically model training.**
24. **Candidate model selection is not promotion authority.**
25. **Every empirical advantage must survive a matched baseline and ablation.**

---

# 16. Minimal Expert Mental Model

The compact model is:

```text
HTLA gives HTNLA typed heterogeneous state.

For each target label:
    gather only declared source blocks
    build a dimensionally valid preactivation
    apply the target's nonlinear map
    optionally apply deterministic competition
    retain the model generation and provenance

If reconstruction is requested:
    determine what was mathematically preserved
    choose a reconstruction method
    return an epistemic result
    never turn information loss into exactness

If the transform feeds ANN/HNSW:
    bind the index to the representation generation
    treat ANN as derived acceleration only

If parameters change:
    persist through the authoritative TMS path
    migrate/rebuild derived representations as required
    promote counterfactual candidates only through external authority
```

The governing chain is:

```text
valid label geometry
        ->
well-typed block map
        ->
explicit nonlinearity
        ->
explicit information loss
        ->
explicit reconstruction status
        ->
versioned transformed state
```

---

# 17. Conclusion

HTNLA remains worth keeping, but for a more precise reason than the original drafts suggested.

Its value is not that nonlinear activation is new, that winner-take-all automatically makes high-dimensional computation cheap, that a few sparse layers are universally expressive, or that a learned transform confers cognitive or biological properties. Those claims are either established prior art, mathematically false in their historical form, or unsupported by the available evidence.

The useful subsystem is narrower and stronger.

HTNLA gives Project Nexus a disciplined way to apply nonlinear transformations to heterogeneous labeled state **without surrendering the type system created by HTLA**. It makes the target-specific nonlinear map explicit. It makes residual geometry explicit. It makes sparsification explicit. Most importantly, it makes the loss of recoverability explicit.

That last property is load-bearing. In a cognitive database architecture, a many-to-one operation cannot be allowed to manufacture apparent certainty merely because an optimizer can produce a plausible vector. The five reconstruction classes and the four authoritative quinary outcomes force the implementation to distinguish exact inverse, best-fit estimate, partial recovery, unresolved search, ambiguity, unknown state, and proven impossibility.

The same discipline extends into HVD and TMS. A nonlinear representation has a model generation. An ANN index built over that representation has a representation generation. A parameter mutation belongs on the authoritative live-state path. Durable model state belongs in the durable persistence tier. Ephemeral candidate models can be evaluated without becoming history. Selection does not become promotion. Similarity does not become identity.

The resulting subsystem can be summarized in one rule:

```text
nonlinearity may increase expressive capacity;
it does not reduce the obligation to represent what the system knows,
what it lost, what it inferred, and what it is authorized to change.
```

That is the version of HTNLA that can safely serve as the Nexus S9 Tier-2 subsystem paper.

---

# Appendix A. ASCII Formula Sheet

```text
STATE SPACES

H_S = direct_sum_{s in S} R^(p_s)
H_T = direct_sum_{t in T} R^(q_t)

COUPLING

E subseteq T x S
W_(t,s) in R^(q_t x p_s)

SINGLE TARGET

z_t = b_t + sum_{s:(t,s) in E} W_(t,s) x_s + r_t
y_t = phi_t(z_t)
y_t <- kWTA_t(y_t)        [optional]

MULTILAYER

H^(k+1) = sigma^(k)(M^(k) H^(k) + b^(k))

RESIDUAL

H^(k+1) = R^(k) H^(k)
          + sigma^(k)(M^(k) H^(k) + b^(k))

JACOBIAN BLOCK

J_(t,s)(x) = D phi_t(z_t) W_(t,s)

LIPSCHITZ BOUND

||F(x)-F(y)|| <= L_sigma ||M|| ||x-y||

RESIDUAL BOUND

||F(x)-F(y)|| <= (||R|| + L_sigma ||M||) ||x-y||

BLOCK GRADIENT

dL/dW_(t,s) = g_t x_s^T

SOURCE GRADIENT

grad_(x_s) L = sum_{t:(t,s) in E} W_(t,s)^T g_t

ITERATIVE RECONSTRUCTION

x_hat = argmin_x [ 0.5 ||F(x)-y||^2 + lambda R(x) ]

BLOCK COST

C_block = Theta(sum_{(t,s) in E} q_t p_s)

BOUNDED-DEGREE CASE

|E| = O(L)
C_block = O(L n^2)
D = L n
C_block = O(D n)

QUINARY RECOVERY OUTCOMES

EXACT
AMBIGUOUS
UNKNOWN
IMPOSSIBLE

CORE DISTINCTIONS

candidate reconstruction != unique inverse
post-activation sparsity != retroactive compute savings
similarity != identity
UNKNOWN != 0
selected candidate != authorized promotion
```

---

# Appendix B. Implementation Checklist

Before an HTNLA implementation is treated as conforming, verify:

- [ ] every source and target label has an explicit dimension;
- [ ] every block shape matches `(target_dim, source_dim)`;
- [ ] ordered label sequences determine concrete flattening offsets;
- [ ] missing labels fail explicitly or use a declared typed missingness policy;
- [ ] residual maps are explicit and dimensionally checked;
- [ ] activation functions are versioned by target label;
- [ ] hard k-WTA has deterministic tie handling;
- [ ] k-WTA support metadata is retained when partial reconstruction requires it;
- [ ] exact inverse claims include domain and injectivity conditions;
- [ ] pseudoinverse outputs are not labeled exact without uniqueness proof;
- [ ] iterative reconstruction reports uncertainty and stopping conditions;
- [ ] quinary `EXACT/AMBIGUOUS/UNKNOWN/IMPOSSIBLE` semantics remain authoritative;
- [ ] differentiable binding surrogates cannot override canonical quinary binding;
- [ ] model generation is stored with transformed state or derivable from provenance;
- [ ] ANN index generation is compatible with query transform generation;
- [ ] model changes define index invalidation/migration behavior;
- [ ] authoritative parameter mutations follow TMS persistence semantics;
- [ ] durable model state participates in HDF5 long-term persistence policy;
- [ ] no unmeasured recall/latency/energy number is presented as achieved;
- [ ] no biological or phenomenological claim is inferred from software variable names;
- [ ] counterfactual model candidates cannot self-promote.

---

# References

1. Schlichtkrull, M., Kipf, T. N., Bloem, P., van den Berg, R., Titov, I., & Welling, M. (2018). *Modeling Relational Data with Graph Convolutional Networks*. ESWC 2018. arXiv:1703.06103.
2. Hu, Z., Dong, Y., Wang, K., & Sun, Y. (2020). *Heterogeneous Graph Transformer*. WWW 2020. arXiv:2003.01332.
3. Dinh, L., Sohl-Dickstein, J., & Bengio, S. (2017). *Density Estimation using Real NVP*. ICLR 2017. arXiv:1605.08803.
4. Kingma, D. P., & Dhariwal, P. (2018). *Glow: Generative Flow with Invertible 1x1 Convolutions*. NeurIPS 2018.
5. Nielsen, D., Jaini, P., Hoogeboom, E., Winther, O., & Welling, M. (2020). *SurVAE Flows: Surjections to Bridge the Gap between VAEs and Flows*. NeurIPS 2020. arXiv:2007.02731.
6. Makhzani, A., & Frey, B. (2015). *Winner-Take-All Autoencoders*. NeurIPS 2015.
7. Dasgupta, S., & Tosh, C. (2020). *Expressivity of Expand-and-Sparsify Representations*. arXiv:2006.03741.
8. Cybenko, G. (1989). *Approximation by Superpositions of a Sigmoidal Function*. Mathematics of Control, Signals and Systems, 2, 303-314.
9. Baykal, C., Dikkala, N., Panigrahy, R., Rashtchian, C., & Wang, X. (2022). *A Theoretical View on Sparsely Activated Networks*. arXiv:2208.04461.
10. Izhikevich, E. M. (2007). *Solving the Distal Reward Problem through Linkage of STDP and Dopamine Signaling*. Cerebral Cortex, 17(10), 2443-2452.
11. Legenstein, R., Pecevski, D., & Maass, W. (2008). *A Learning Theory for Reward-Modulated Spike-Timing-Dependent Plasticity with Application to Biofeedback*. PLoS Computational Biology, 4(10), e1000180.
12. Frémaux, N., Sprekeler, H., & Gerstner, W. (2010). *Functional Requirements for Reward-Modulated Spike-Timing-Dependent Plasticity*. Journal of Neuroscience, 30(40), 13326-13337.
13. Gilyén, A., Su, Y., Low, G. H., & Wiebe, N. (2019). *Quantum Singular Value Transformation and Beyond: Exponential Improvements for Quantum Matrix Arithmetics*. STOC 2019. arXiv:1806.01838.
14. Project Nexus 4. *Canonical Technical Monograph*, Part III, §§5-7. Internal Tier-0 architectural source, 2026-08-31 reference edition.
15. Project Nexus 4. *Hypervector Linear Transdimensional Algebra (HTLA): Labeled Direct-Sum Calculus, Recoverability Contracts, and Quinary Reference Semantics*. Tier-2 S8 replacement candidate, 2026-08-31.

---

## Source-reconciliation note

This rewrite reconciles four supplied HTNLA source classes:

1. the historical/lossless HTNLA blueprint, retained as a record of the original design direction;
2. the corrected HTNLA v2 draft, which already removes several overclaims;
3. the deep-research dossier, which audits novelty, invertibility, sparsity, biology, quantum claims, and reference code;
4. the rigorous recast report, which supplies the strongest adversarial mathematical treatment.

Where those sources conflict, this paper follows the current Nexus monograph and rewritten HTLA Tier-2 paper for architecture and reference semantics, uses the research dossier/recast for corrections, and preserves historical claims only when they remain useful as explicitly labeled `HISTORICAL/SUPERSEDED` context.
