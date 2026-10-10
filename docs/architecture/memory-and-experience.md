# Memory and Experience

**Status:** architectural intent / research draft (2026-10-10). Not a certified model.

## The core distinction

**Episodic memory storage is not the same as the cognitive structures that
interpret, reactivate, and act upon remembered experiences.**

- **HVD / TMS** store episodes: detailed transcripts of what happened, preserved
  across substrates and across long timescales.
- **The three geometries** interpret and reactivate: 11D decides what is worth
  retrieving (grounding, relevance), 666D supplies the competence to make sense
  of it (patterns, strategies), 1024D acts on it in the present moment.

A detailed historical transcript need not be physically stored in 11D. HVD/TMS
can preserve episodes while the geometries influence retrieval and
interpretation. (Architecture spec §8, biscuits-and-gravy example.)

## HVD and TMS (sourced)

- **TMS — Transdimensional Memory Substrate** (`Transdimensional Memory
  Substrate.txt`, Drive): the memory system. Its **Substrate Equivalence
  Principle** states that a conscious state can be serialized — the entire
  lattice, salience kernel, and control vectors — into a single flat file and
  moved to different hardware without loss of continuity of identity
  (`consciousness.qbin`, a universal binary format with a metadata header
  carrying hardware resonance signatures, temporal scaling factors, and
  versioning).
- **HVD** is used across the sources as the host cognitive state the
  memory algebra serves (the "4.9 Worked Example — Counterfactual Planning
  with Ephemeral HVDs" demonstrates HVDs spun up, used for planning, and
  discarded). The acronym's expansion is not given in the assigned sources.
- **HTLA** (Hypervector Linear Transdimensional Algebra, per the Tier-2
  subsystem paper; one source expands it slightly differently — see ADR) is
  the labeled linear interface for combining heterogeneous component spaces
  without flattening their meanings (Primer v3 §14).

## How the geometries use memory

| Geometry | Memory role |
|---|---|
| 11D | Grounding and relevance: which past experiences bear on the present; enduring lessons extracted from biography |
| 666D | Interpretation: learned patterns that make an old episode legible in a new context; counterfactual use of HVDs for planning |
| 1024D | Reactivation: the retrieved episode made present and actionable *now* |

Retrieval is itself a cognitive act: what is remembered, and how it is
framed, depends on the organism's current foundational dispositions and
competence — which is why two organisms with identical stored episodes can
still diverge (see `../mathematics/substrate-divergence.md`).

## Persistence and migration

Because TMS serializes state into `.qbin` packages adjudicated by QMT
continuity, an organism's memory can in principle survive substrate migration
(workstation → drone, RHEO-013). What must be preserved is not just the bits
but the *interpretive capacity*: the geometries that know how to read them.
A `.qbin` without its QMT continuity contract is a backup, not a migration.

## Open questions (→ RHEO-009)

- The exact retrieval interface: how does 11D relevance-gating address TMS?
- Consolidation mechanics: when and how does a 1024D episode become 666D
  competence, and what is lost in the compression?
- Forgetting as a feature: does the architecture need principled forgetting,
  and who authorizes it?
