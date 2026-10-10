# The Neutral-Weight Domain — Research Scaffold

**Status:** open research (RHEO-004). The notation below is preserved exactly
as specified in the 2026-10-10 design discussion. **Its mathematical meaning
is undefined.** This document defines the research program, not the answer.

## The notation (exact)

```
(±∞, ±∞)
```

This is **not** the conventional interval (-∞, +∞). Do not silently substitute
one for the other. The pair structure — two signed infinities — is load-bearing
and must survive formalization.

**Corpus check:** the notation `(±∞, ±∞)` occurs nowhere in the Drive sources
(verified by search over all retrieved text sources). It is an innovation of
the design discussion. No source gives it algebraic rules.

## What "neutral weight" must mean (research program)

A complete definition must cover all five of the following. Each is currently
open:

1. **Neutrality.** In what sense is the weight "neutral"? Candidate readings
   (PROPOSAL, not adopted): a weight that contributes no bias to a decision;
   a weight that marks "no information" as distinct from "zero information"
   (compare the Identity monograph's HIGC discipline: "refuses to evaluate a
   missing fact as an implicit neutral scalar"); a fixed point of the
   coupling operators. These readings are not equivalent; choosing among them
   is RHEO-004's central task.
2. **Representation.** How the pair of signed infinities is represented in a
   finite machine. The infinities cannot be stored literally; whatever finite
   encoding is chosen must preserve the pair structure and the distinction
   from (-∞, +∞).
3. **Algebraic operations.** Addition, scaling, composition: what is
   (±∞, ±∞) + (±∞, ±∞)? What is its interaction with finite weights? Any
   proposed algebra must state its axioms and check them — *not* inherit the
   extended-real arithmetic by default, since the pair structure may demand
   different rules (e.g., independent saturation of each component).
4. **Computational approximation.** How couplings compute with neutral weights
   in practice: saturation thresholds, symbolic markers vs. large finite
   values, and where the approximation breaks.
5. **Numerical stability.** Proof or empirical demonstration that neutral
   weights do not inject NaNs, overflow cascades, or silent bias into the
   nine-coupling dynamics.

## Constraints on any proposed definition

- Must preserve the exact notation `(±∞, ±∞)` — no silent reinterpretation.
- Must distinguish neutrality from zero, from "unknown," and from the
  conventional infinite interval.
- Must be compatible with the quinary/discrete arithmetic the sources use
  elsewhere (bit-plane algebra, KWTA gating), or explain the boundary.

## Acceptance criteria (RHEO-004)

- Algebraic meaning, identity/neutrality element behavior, and singularity
  handling written and checked.
- Finite representation specified; numerically safe computation demonstrated
  (property tests, RHEO-016).
- Explicit statement of which candidate reading of "neutrality" was adopted
  and why the others were rejected.
