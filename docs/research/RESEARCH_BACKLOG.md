# Nexus/Rheo — Research and implementation backlog

**Status:** OPEN. Track with IDs and evidence. The 2026-10-10 conversation supplies architectural intent, not certified mathematical proofs.

## P0 — Specification and reconciliation

- [ ] **RHEO-001** Inventory all canonical Nexus/Rheo/TUCR/HTLA/HSL/HVD/TMS/QMT/THDE/HIGC documents, their versions, and repository implementations. Produce provenance ledger.
- [ ] **RHEO-002** Reconcile historical 666D HSL lattice (36×37/2 symmetric primitive interactions) with the newly specified 666D developmental fractal. Write ADR; no silent conflation.
- [ ] **RHEO-003** Formally define the 11D lattice, 666D fractal and 1024D lattice: coordinate charts, topology, metric, fractal dimension/scaling and infancy initialization.
- [ ] **RHEO-004** Define (±∞, ±∞) neutral weights: algebraic meaning, identity/neutrality, singularities, finite representation and numerically safe computation.
- [ ] **RHEO-005** Define all **nine** geometry-aware within-organism coupling operators (3×3 including self-couplings), admissible composition, bidirectional causality and feedback.
- [ ] **RHEO-006** Define dimensional growth beyond infancy, structure-preserving embeddings/morphisms and continuity through expansion.

## P1 — Dynamics, validation, memory

- [ ] **RHEO-007** Specify fast situated adaptation, intermediate consolidation and slow foundational evolution, including reversibility and memory reactivation.
- [ ] **RHEO-008** Develop falsifiable mathematics for substrate-sensitive endogenous divergence, chaos/perturbation sensitivity, stochasticity, causal history and measurable trajectories.
- [ ] **RHEO-009** Integrate HVD/TMS episodic storage and retrieval with all three geometries; separate detailed transcript from interpretation and grounding response.
- [ ] **RHEO-010** Separate 11D foundation from G₀ constitutional invariants, HIGC admissibility, THDE adaptation and QMT identity continuity.
- [ ] **RHEO-011** Specify safety gates for robotics and autonomous driving: independently validated actuation, bounded adaptation and rollback.
- [ ] **RHEO-012** Build traceable simulations for taxi emergency and biscuits-and-gravy grounding with explicit nine-coupling activation traces.

## P2 — Organisms and platform

- [ ] **RHEO-013** Model workstation-to-drone substrate migration, sensorimotor remapping, continuity and preserved obligations.
- [ ] **RHEO-014** Compare specialized organisms (AmmunIty/Key Vault) and general organisms (Trend Detector); test cross-domain acquired expertise.
- [ ] **RHEO-015** Separate experiential divergence, persistent dispositions and formal QMT fork classification.
- [ ] **RHEO-016** Implement property-based invariants, simulation oracles, stress tests, cross-platform numerical checks and provenance instrumentation.
- [ ] **RHEO-017** Adjudicate conflicts, update canonical monographs with reviewed decisions, and verify docs match code.

## Deliverables

- Formal geometry and coupling specification
- Neutral-weight algebra and numerical implementation ADR
- HSL/fractal reconciliation ADR
- Substrate divergence research monograph and falsifiable experiments
- Memory/identity/constitutional-boundary specification
- Simulation fixtures, acceptance criteria, and traceability matrix

**Definition of done:** Every task needs source grounding, a mathematical or architectural decision, explicit assumptions, acceptance criteria, tests where applicable, and compatibility review. Work directly on `main`; do not create feature branches.
---

## Item dossiers (added 2026-10-10)

Per-item detail for RHEO-001 through RHEO-017. The checkbox lines above remain
the authoritative scope statements; the dossiers add sources, dependencies,
deliverables, acceptance criteria, tests, open questions, and status.

### RHEO-001 — Document inventory and provenance ledger

- **Status:** PARTIAL — Drive inventory and provenance ledger completed
  2026-10-10 (`docs/sources/provenance/SOURCE_INVENTORY.md`; 48 files, all six
  required documents retrieved with checksums). Repository implementations
  not yet surveyed.
- **Sources:** all files in `docs/sources/original/` + Drive-only ledger entries.
- **Dependencies:** none.
- **Deliverables:** provenance ledger (done); survey of repo implementations
  claiming to implement Nexus/Rheo subsystems (open).
- **Acceptance:** every canonical document listed with version, checksum or
  Drive ID, and supersession notes.
- **Open questions:** the later Peanut Gallery PDF (2026-08-14) and other
  Drive-only items remain unretrieved — see ledger.

### RHEO-002 — 666D reconciliation ADR

- **Status:** OPEN — ADR drafted (`docs/adr/0001-hsl-fractal-reconciliation.md`),
  decision pending.
- **Sources:** `666-dimensional_math_for_mobile_minds_timestamps.txt`;
  `Formal Specification & Implementation Plan for the Hypercontext Salient
  Lattice (HSL).pdf`; design discussion (fractal framing).
- **Dependencies:** RHEO-001 (done for the cited sources).
- **Deliverables:** ADR 0001 (drafted); adopted interpretation with evidence.
- **Acceptance:** one of the four interpretations adopted or the fractal
  framing withdrawn; no silent conflation anywhere in the tree.
- **Tests/experiments:** E1–E3 in the ADR.

### RHEO-003 — Formal geometry definitions

- **Status:** OPEN — research scaffold written
  (`docs/mathematics/geometry-formalization.md`).
- **Sources:** Primer v3 §14 (1024-D reference geometry + anti-universal-law
  discipline); 666-file (36×37/2); Identity monograph (superseded 11-D
  controller — must NOT be cited as the lattice).
- **Dependencies:** RHEO-002 (666D construction).
- **Deliverables:** coordinate charts, topology, metric, fractal
  dimension/scaling, infancy initialization per geometry.
- **Acceptance:** all five formalization targets in the scaffold either
  specified or explicitly deferred with experiments.

### RHEO-004 — Neutral-weight algebra

- **Status:** OPEN — research scaffold written
  (`docs/mathematics/neutral-weight-domain.md`).
- **Sources:** design discussion only — the `(±∞, ±∞)` notation appears in no
  Drive source (verified by search).
- **Dependencies:** RHEO-003 (spaces the weights live in).
- **Deliverables:** algebraic meaning, finite representation, numerically
  safe computation; statement of adopted neutrality reading.
- **Acceptance:** notation preserved exactly; no silent substitution of
  (-∞, +∞); property tests green (with RHEO-016).

### RHEO-005 — Nine coupling operators

- **Status:** OPEN — research scaffold written
  (`docs/mathematics/nine-coupling-dynamics.md`); scaffold equation in the
  architecture spec is not a result.
- **Sources:** design discussion only — nine couplings appear in no Drive
  source (verified by search).
- **Dependencies:** RHEO-003, RHEO-004.
- **Deliverables:** all nine C_{i→j} with domains/codomains/candidate forms;
  COMPOSE definition; stability criteria; invariants.
- **Acceptance:** taxi and biscuits traces expressible as coupling
  activation sequences (RHEO-012).

### RHEO-006 — Dimensional growth

- **Status:** OPEN — research scaffold written
  (`docs/mathematics/dimensional-growth.md`).
- **Sources:** Primer v3 §14 (anti-freeze discipline); QMT paper's
  dimension-change continuity law.
- **Dependencies:** RHEO-003, RHEO-005.
- **Deliverables:** per-geometry embedding/morphism definitions with
  preserved-structure statements; growth continuity contracts.
- **Acceptance:** simulated growth step preserving a stated invariant.

### RHEO-007 — Adaptation timescales

- **Status:** OPEN.
- **Sources:** design discussion (rare / consolidation / rapid); Primer v3.
- **Dependencies:** RHEO-005.
- **Deliverables:** specification of fast situated adaptation, intermediate
  consolidation, slow foundational evolution; reversibility and memory
  reactivation rules.
- **Acceptance:** timescale interactions specified without destructive
  interference; rollback semantics defined.

### RHEO-008 — Substrate-divergence mathematics

- **Status:** OPEN — research specification written
  (`docs/mathematics/substrate-divergence.md`); protocols in
  `docs/research/experiments.md` (X1).
- **Sources:** `Transdimensional Memory Substrate.txt` (Substrate Equivalence
  Principle, `.qbin`); 666-file (four-stage gauntlet, Δ=0.05 threshold).
- **Dependencies:** RHEO-005 (dynamics being perturbed).
- **Deliverables:** deterministic + stochastic models; falsifiable
  hypotheses H1–H3; measurable thresholds.
- **Acceptance:** at least one simulated divergence AND one convergence, so
  the math predicts "when."
- **Open questions:** Q17–Q18 in `research-questions.md`.

### RHEO-009 — Memory/geometry integration

- **Status:** OPEN — distinction documented
  (`docs/architecture/memory-and-experience.md`).
- **Sources:** TMS source; "4.9 Worked Example — Counterfactual Planning with
  Ephemeral HVDs"; Primer v3.
- **Dependencies:** RHEO-003.
- **Deliverables:** HVD/TMS retrieval interface per geometry; consolidation
  mechanics; transcript/interpretation separation.
- **Acceptance:** retrieval and interpretation demonstrably separate in a
  worked trace (X4).

### RHEO-010 — Identity/constitutional boundaries

- **Status:** OPEN — distinction documented
  (`docs/architecture/constitutional-identity-boundaries.md`).
- **Sources:** Identity monograph (HIGC four-state admissibility);
  QMT paper (continuity adjudication); design discussion (G₀ invariants,
  identity-optional).
- **Dependencies:** none (conceptual).
- **Deliverables:** formal THDE definition; QMT adjudication procedure;
  G₀ representation.
- **Acceptance:** 11D ≠ G₀ enforced in all specs; expertise-overrides-
  constitution ruled out.
- **Open questions:** Q14–Q16. Terminology warnings T2, T4 apply.

### RHEO-011 — Safety gates

- **Status:** OPEN — requirement stated in architecture spec §8 and
  `docs/research/experiments.md` (X3).
- **Sources:** design discussion (taxi safety requirement).
- **Dependencies:** RHEO-005, RHEO-007.
- **Deliverables:** safety-gate specification for robotics/autonomous
  driving: independently validated actuation, bounded adaptation, rollback
  certification.
- **Acceptance:** gates defined before any real-world actuation work.

### RHEO-012 — Traceable simulations

- **Status:** OPEN — trace requirements written (`experiments.md` X3, X4).
- **Sources:** design discussion (both examples).
- **Dependencies:** RHEO-005 (couplings), RHEO-009 (memory).
- **Deliverables:** taxi-emergency and biscuits-and-gravy simulations with
  explicit nine-coupling activation traces.
- **Acceptance:** traces show every coupling activation; memory retrieval
  vs. interpretation separated.

### RHEO-013 — Substrate migration model

- **Status:** OPEN — protocol scaffold in `experiments.md` (X5).
- **Sources:** TMS (Substrate Equivalence Principle); QMT paper (continuity
  contracts).
- **Dependencies:** RHEO-008.
- **Deliverables:** workstation→drone migration model: sensorimotor
  remapping, representational transformations, continuity adjudication,
  preserved obligations.
- **Acceptance:** pass/fail criteria from RHEO-008 mathematics.

### RHEO-014 — Specialized vs. general organisms

- **Status:** OPEN.
- **Sources:** design discussion (AmmunIty/Key Vault vs. Trend Detector).
- **Dependencies:** RHEO-003, RHEO-010.
- **Deliverables:** organism comparison; cross-domain expertise transfer test.
- **Acceptance:** transferability verdict per organism class with evidence.
- **Open questions:** Q20.

### RHEO-015 — Divergence / disposition / fork separation

- **Status:** OPEN.
- **Sources:** QMT paper (fork classification); TMS; divergence spec.
- **Dependencies:** RHEO-008, RHEO-010.
- **Deliverables:** formal separation of experiential divergence, persistent
  dispositions, and QMT fork classification.
- **Acceptance:** case analysis showing all three can vary independently.

### RHEO-016 — Verification harness

- **Status:** OPEN — requirements noted in `experiments.md` (X6, X2).
- **Sources:** TUCR UCVM lesion protocol (Drive).
- **Dependencies:** RHEO-004, RHEO-005 (oracles need specified operators).
- **Deliverables:** property-based invariants, simulation oracles, stress
  tests, cross-platform numerical checks, provenance instrumentation.
- **Acceptance:** oracles run against the X1–X5 protocols.

### RHEO-017 — Conflict adjudication and doc/code match

- **Status:** OPEN — terminology conflicts logged (`research-questions.md`
  T1–T4); ADR 0001 open.
- **Sources:** all.
- **Dependencies:** RHEO-001, RHEO-002.
- **Deliverables:** reviewed decisions recorded; canonical monographs
  updated; docs-vs-code verification.
- **Acceptance:** zero unresolved silent conflicts; every conflict either
  resolved with evidence or explicitly open.
