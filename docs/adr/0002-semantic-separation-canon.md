# ADR-0002: Canonical Semantic Separation Law

- **Status:** ACCEPTED
- **Date:** 2026-10-11
- **Decision scope:** framework-wide

## Context

Rheo-Chasmar deliberately separates identity, state, trajectory, memory,
evidence, retrieval similarity, truth-status, constitutional admissibility,
homeostatic desirability, authority, cognitive pressure, and committed action.

Multiple historical documents already contain partial forms of this principle,
including “identity is not state,” “history is not identity,” “memory is not
identity,” ANN/similarity-not-truth warnings, HIGC's non-compensatory
admissibility semantics, and the separation of Cyrae regulation from outward
actuation.

As the architecture grows, these distinctions require one normative rule.

## Decision

Adopt the following as a canonical framework invariant:

> Identity is not state.  
> State is not history.  
> History is not memory.  
> Memory is not evidence.  
> Evidence is not similarity.  
> Similarity is not truth.  
> Truth is not admissibility.  
> Admissibility is not desirability.  
> Desirability is not authority.  
> Cognitive pressure is not action.

No subsystem may use an implicit semantic cast between these categories.

Cross-domain transformations must be explicit, named, provenance-aware,
testable operations with declared failure semantics.

The normative specification is
`../architecture/semantic-separation-invariants.md`.

The supporting formalization and proof obligations are
`../mathematics/semantic-separation-theorems.md`.

## Consequences

1. HVD/ANN/HTLA similarity cannot become truth or evidence by threshold alone.
2. TMS/HDF5 retention cannot become identity or complete history by storage
   presence alone.
3. HIGC admissibility cannot be replaced by a utility/risk/reward score.
4. Cyrae desirability or pressure cannot create authority or direct actuation.
5. Maera/CA fluency, confidence, or orchestration cannot create permission.
6. QMT must adjudicate continuity using explicit continuity rules rather than
   snapshot equality.
7. THDE may use history without turning history into identity.
8. Application profiles must retain separate authority gates for consequential
   actions.

## Supersession rule

Future work may refine the formal domains and morphisms, but any proposal that
collapses two canonical categories requires an explicit ADR that demonstrates
why the distinction no longer applies. Silent collapse is prohibited.
