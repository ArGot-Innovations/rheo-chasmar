# ADR 0001 — Reconciling the Historical 666D Specification with the 666D Fractal

**Date:** 2026-10-10 · **Status:** OPEN (unresolved — evidence recorded, decision pending)

## Context

Two descriptions of "666 dimensions" exist in this project and they are not
obviously the same thing:

- **(H) Historical:** the HSL research describes 666 dimensions as the
  symmetric pairwise relationships among 36 cognitive primitives:
  36 × 37 / 2 = 666 (630 off-diagonal interaction pairs + 36 diagonal
  self-interactions). The 36 primitives are a stipulated design choice
  organized into 18 macro sectors — "pure engineering constraint," not a
  discovered law.
- **(F) Current:** the 2026-10-10 design discussion specifies a
  **666-dimensional fractal** as the geometry of developed competence
  (wisdom, contextual interpretation, generalization, anticipation).

A symmetric interaction matrix is not inherently a fractal. This ADR records
the evidence, the competing interpretations, and what would resolve them.
**No conflation is permitted in the meantime.**

## Evidence

### For (H): the combinatorial derivation (sourced)

`666-dimensional_math_for_mobile_minds_timestamps.txt` (Drive) gives the
derivation explicitly: a 36×36 symmetric matrix of primitive interactions;
symmetry halves the 1296 grid to 648; the 36 diagonal self-interactions must
be added back whole (648 + 18 = 666); general formula n(n+1)/2. The transcript
contains speech-to-text garbles ("12,296" for 1296, "124" for 1024); the final
formula is stated correctly. The same source contains an explicit numerology
rebuttal: the 666 is "purely combinatorial geometry… the literal inescapable
shape of the mathematical room they built," and stresses the 36 primitives
were *chosen*, not discovered.

### Against silently replacing (H) with (F)

- The word "fractal" appears **nowhere** in any retrieved Drive source
  (verified by search). The fractal framing originates entirely in the
  2026-10-10 design discussion.
- The nine coupling relationships likewise appear in no source.
- The Identity monograph's only 11-D object is a superseded controller model;
  the QMT paper treats dimension changes abstractly. Neither supports (F).

### A second framing conflict (sourced)

The HSL specification PDF (`Formal Specification & Implementation Plan for
the Hypercontext Salient Lattice (HSL).pdf`, Drive) never mentions 666, 36
primitives, or quinary encoding at all — it frames HSL as a graded Riemannian
product manifold with salience-weighted similarity and Fokker–Planck kernel
diffusion. So "HSL" currently names **two different mathematical objects**:
the 666-D combinatorial lattice (666-file) and the continuous manifold
(HSL PDF). The migration keeps these distinct; see terminology notes in
`../research/research-questions.md`.

### The G₀ terminology warning

The 666-transcripts use "G0 boot sequence" for the music-seeded initialization
of the 666 weights. The design discussion uses G₀ for constitutional
invariants. These are different concepts sharing a symbol; see
`../architecture/constitutional-identity-boundaries.md`.

## Competing interpretations

1. **Coordinates:** the 666 symmetric-matrix entries serve as coordinates
   (or parameters) of the fractal — the fractal is *built over* the
   interaction space. Requires: a fractal construction whose natural
   coordinate chart is the symmetric 36×36 matrix.
2. **Supersession:** the fractal replaces the symmetric-matrix lattice as the
   666D model; the historical derivation is retained as provenance but not as
   live mathematics. Requires: an explicit retirement statement and a
   migration path for anything built on (H).
3. **Layer separation:** (H) is the discrete memory algebra layer and (F) the
   competence/dynamics layer, both 666-dimensional by design coincidence or
   by construction. Requires: the coupling between layers to be specified
   (feeds RHEO-005).
4. **Rejection:** the fractal framing is withdrawn for lack of mathematical
   substance; 666D remains the combinatorial lattice. Requires: nothing but
   honesty.

Interpretation (1) is the design discussion's apparent intent ("investigate
whether the historical coupling representation can serve as coordinates,
parameters, or another structural component of the fractal model"), but intent
is not evidence. All four remain live.

## Unresolved questions

- What is the fractal *construction* (generator, scaling law, fractal
  dimension)? Without it, (F) is a label, not a model.
- Is there any principled reason the competence geometry has the *same*
  dimension count (666) as the historical interaction lattice, or is the
  number inherited for continuity?
- Which of the two HSL framings (combinatorial vs. manifold) does the
  current architecture actually build on?

## Proposed experiments

- E1: Formalize interpretation (1) far enough to state its fractal dimension
  and scaling; check consistency against the 36×37/2 counting.
- E2: Attempt to construct an explicit fractal over symmetric-matrix
  coordinates; document where the construction breaks, if it does.
- E3: Survey whether any retrieved source hints at self-similar structure in
  the 666D lattice (negative results count as results).

## Decision

**Pending.** This ADR stays OPEN until one interpretation is adopted with
evidence or the fractal framing is withdrawn. RHEO-002 tracks the work.
