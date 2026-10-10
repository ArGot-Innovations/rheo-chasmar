# Nine-Coupling Dynamics — Research Scaffold

**Status:** open research (RHEO-005). The nine directional coupling
relationships come from the 2026-10-10 design discussion. **No source
derives them; no coupling operator is verified.** Everything below is a
research scaffold: assumptions, candidate formalisms, and open questions.

## The relationships (design discussion, verbatim)

The three geometries interact through nine directional couplings. These are
**not** nine organisms or nine independent copies of the cognitive
architecture — they are relationships within one organism:

| From ↓ / To → | 11D | 666D | 1024D |
|---|---|---|---|
| **11D** | 11→11 | 11→666 | 11→1024 |
| **666D** | 666→11 | 666→666 | 666→1024 |
| **1024D** | 1024→11 | 1024→666 | 1024→1024 |

Intended semantics (from the design discussion):

- **Self-couplings** (11→11, 666→666, 1024→1024): within-geometry dynamics —
  slow foundational drift, competence consolidation, rapid situated updating.
- **Downward** (11→666, 11→1024, 666→1024): dispositions and competence
  shaping anticipation and action. Foundational vigilance biases what the
  organism is ready to see; learned strategies bias immediate decisions.
- **Upward** (1024→666, 666→11, 1024→11): experience feeding back —
  exceptional situated events restructuring competence, and competence over
  time shifting foundations.

## Scaffold (from the architecture spec, not a result)

The architecture spec proposes the research scaffold:

```
X_j(t+1) = Φ_j( X_j(t), COMPOSE_i( C_{i→j}(X_i(t), X_j(t)) ), E_t, S_t, M_t )
```

where X_j is the state of geometry j, C_{i→j} the coupling operator,
E_t external inputs, S_t substrate state, M_t memory retrieval. **Every
symbol on the right-hand side except X_j(t) is undefined.** In particular:

- The **spaces** each C_{i→j} maps between are undefined (dimensional
  mismatch: 11 vs 666 vs 1024).
- **COMPOSE** (how multiple incoming couplings combine) is undefined.
- **Φ_j** (the within-geometry update) is undefined.
- Continuity, stability, and invariants are unproven.

## Assumptions (explicit, to be tested)

1. **One organism.** Couplings are intra-organism relationships, never
   inter-organism channels.
2. **Geometry-aware, state-dependent, multiscale.** Each C_{i→j} may be
   nonlinear; none is assumed to be a scalar or dense matrix.
3. **Bidirectional causality with feedback.** Upward and downward paths both
   exist; feedback loops are expected and must be analyzed for stability,
   not assumed stable.
4. **Causal timing.** Couplings have latencies; 1024D→666D consolidation is
   slower than 1024D→1024D reaction. Timing is part of the specification.

## Candidate mathematical areas (PROPOSAL, not adopted)

- Nonlinear dynamical systems / coupled oscillators for self-couplings.
- Multiscale coupling (heterogeneous timescales) for upward/downward paths.
- Adaptive state spaces and structure-preserving maps for dimensional
  mismatch (how does an 11-vector influence a 666-fractal?).
- Contraction analysis / Lyapunov methods for stability criteria — as
  *candidate* tools, with no claim they apply.

## What must be defined before implementation (RHEO-005)

Operators, admissible composition, state-transition semantics, stability
criteria, invariants (what is conserved across a coupling step), measurable
behavior (what an experiment would observe), and uncertainty handling.

## Acceptance criteria

- All nine C_{i→j} given explicit domains, codomains, and candidate forms.
- Stability criteria stated and tied to falsifiable simulations.
- The taxi emergency and biscuits-and-gravy traces (RHEO-012) expressed as
  nine-coupling activation sequences.
