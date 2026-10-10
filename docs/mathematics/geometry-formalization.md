# Geometry Formalization — Research Scaffold

**Status:** open research (RHEO-003). This document collects what the sources
actually establish about the three geometries, states the formalization goals,
and lists what remains undefined. **Nothing here is a certified mathematical
model.** Proposals are labeled PROPOSAL; sourced facts are labeled SOURCED.

## What the sources establish (SOURCED)

- **1024-D:** The Primer v3 (§14) states: "A 1024-dimensional reference HSL has
  been used and verified in bounded implementation work… That number is
  important as a reference geometry. It should not automatically become a
  universal law of all future Rheo realizations." The 666-mathematics
  transcripts describe a 1024-dimensional memory array with quinary bit-plane
  algebra (three 64-bit integer arrays: sign plane + two magnitude planes,
  one-hot hardware mask intercepting illegal magnitude-3 states) and a
  K-winner-take-all gate enforcing ~30% activation (307 of 1024; see the
  "Why 307" source).
- **666-D:** The historical HSL research describes 666 dimensions as the
  symmetric pairwise interactions among 36 cognitive primitives:
  36 × 37 / 2 = 666 (630 off-diagonal pairs + 36 diagonal self-interactions).
  The 36 primitives are a *stipulated design choice* (18 macro sectors), not a
  discovered law. See `../adr/0001-hsl-fractal-reconciliation.md`.
- **11-D:** The Identity monograph's only 11-dimensional object is a
  *superseded* continuous controller model (Cyrae ODE control vector), marked
  HISTORICAL / SUPERSEDED. It must not be cited as the 11D lattice.
- **The 11/666/1024 three-geometry doctrine, the fractal framing of 666D, and
  the nine couplings come from the 2026-10-10 design discussion**, documented
  in `../architecture/three-geometry-cognitive-architecture.md`. They do not
  appear in the Drive sources.

## Formalization targets

For each geometry G ∈ {11D lattice, 666D fractal, 1024D lattice}, define:

1. **State space:** the set X_G and its structure (vector space? manifold?
   combinatorial complex?). PROPOSAL: treat 11D and 1024D as real vector
   spaces ℝ¹¹, ℝ¹⁰²⁴ with quinary/discrete structure where the sources require
   it; treat 666D per the ADR outcome (currently unresolved between
   symmetric-matrix coordinates and fractal construction).
2. **Topology and metric:** what "nearness" means in each geometry, and
   whether the three topologies are comparable.
3. **Fractal structure (666D):** fractal dimension, scaling law, and the
   construction that generates the fractal from infancy initialization.
   OPEN — no source gives this; the design discussion asserts "fractal"
   without a construction.
4. **Infancy initialization:** the initial state x_G(0) for each geometry,
   including the role of the historical G0 boot sequence (music-seeded 666D
   weights) if retained.
5. **Adaptation rates:** formalize "11D rarely / 666D via consolidation /
   1024D rapidly" as distinct update operators with distinct timescales, not
   merely different learning rates on identical structures.

## Explicit non-goals

- Do not present the scaffold equation from the architecture spec as a result.
- Do not silently substitute (-∞, +∞) for (±∞, ±∞). See
  `neutral-weight-domain.md`.
- Do not conflate the historical 666D symmetric-matrix lattice with the
  proposed 666D fractal until the ADR resolves their relationship.

## Acceptance criteria (RHEO-003)

- Coordinate charts, topology, and metric written for all three geometries.
- Fractal construction for 666D either specified or explicitly deferred with
  experiments proposed.
- Infancy initialization specified per geometry.
- All definitions traceable to sources or labeled as new proposals.
