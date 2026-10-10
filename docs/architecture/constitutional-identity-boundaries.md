# Constitutional Identity Boundaries

**Status:** architectural intent / research draft (2026-10-10). Not a certified model.

## The distinction

Foundational cognition (11D) and constitutional identity are different things:

- **11D foundational cognition** = enduring dispositions, grounding, sensory
  foundations, role representation. It changes slowly, but it *can* change.
- **Constitutional identity** = obligations and invariants that *must not*
  change without breaking what the organism is. These are the hardest
  constraints in the system.

Not every Rheo organism must possess an assigned identity or develop an
identity-like self-concept. General-purpose organisms may evolve without one.
Some specialized organisms (security, safety-critical control) may require
immutable constitutional obligations. The architecture supports both.

## G₀ constitutional invariants

**Terminology warning — two usages exist and must not be conflated:**

1. **Historical usage (Drive sources):** "G0 boot sequence" — an initialization
   artifact described in the 666-dimensional mathematics transcripts: a 36-track
   experimental music album whose acoustic structure seeds initial weights
   across the 666 dimensions ("acoustic seating… it gives the mind its starting
   mass"). This is about *bootstrapping*, not obligation.
2. **Current usage (2026-10-10 design discussion):** **G₀ = the set of
   constitutional invariants** — the obligations that define the organism's
   non-negotiable bounds. This definition is new; the historical sources do not
   contain it.

When this tree says G₀, it means usage (2) unless stated otherwise.

G₀ invariants are the authority against which everything else is checked. They
do not learn, they do not adapt, and no amount of accumulated expertise
overrides them.

## Related authorities

| Concept | Role | Source |
|---|---|---|
| **G₀** | Constitutional invariants; immutable obligations | Design discussion (new definition) |
| **11D** | Foundational cognition; slow-changing dispositions | Design discussion |
| **HIGC** | Admissibility: is a state/action within bounds? Four states — ADMISSIBLE, BOUNDARY, OUTSIDE, UNRESOLVED (Identity monograph §"HIGC") | `Identity_Architecture_Canonical_Technical_Monograph.md` |
| **THDE** | Evolution authority: what may change and under what discipline | Named in sources; formal definition open (RHEO-010) |
| **QMT** | Continuity adjudication across state/substrate transformation via `.qbin` morphism packages | `QMT_qbin_Morphism_Theory_Tier2_Subsystem_Paper_2026-08-31.md` |
| **Accumulated expertise** | 666D competence; learned, revisable | Design discussion |
| **Preferences / dispositions** | Enduring but not immutable; 11D/666D | Design discussion |
| **Biography / episodic memory** | Stored in HVD/TMS; interpreted by the geometries, not stored in them | `Transdimensional Memory Substrate.txt` |

## Rules

1. **Do not equate enduring preferences with immutable constitutional
   requirements.** A preference that has lasted years is still a preference.
   Only G₀ is constitutional.
2. **11D is not G₀.** The architecture spec is explicit: 11D is "not synonymous
   with G₀ constitutional authority." Foundational dispositions inform
   judgment; they do not license violating invariants.
3. **Expertise never overrides constitution.** 666D competence, however deep,
   cannot authorize what G₀ forbids. This is the point of the taxi safety
   requirement: experimental cognitive adaptation must never bypass validated
   autonomous-driving controls.
4. **Identity is optional; obligations are not, where assigned.** An organism
   without an identity-like self-concept still obeys its G₀ if one is assigned.

## Open questions (→ RHEO-010)

- Formal definition of THDE's evolution authority and its interface to HIGC.
- The exact adjudication procedure QMT uses to certify continuity across a
  constitutional boundary check.
- Whether G₀ invariants are finitely enumerable per organism, and in what
  representation.
