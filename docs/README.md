# Rheo-Chasmar — Documentation

**Status:** research documentation, 2026-10-10. This tree holds the project's
migrated source research, architectural specifications, mathematical research
scaffolds, and the authoritative research backlog.

**Naming note.** The project was called **Project Nexus** (and Nexus 4) until
2026-10-09, when John renamed it **Rheo-Chasmar**. Older documents use the Nexus
name; they are preserved verbatim under `sources/original/` and are *not*
renamed. New documents use Rheo-Chasmar. Where both names appear, "Nexus/Rheo"
means the same continuing project.

## Layout

| Path | Contents |
|---|---|
| `sources/original/` | Source documents imported from Google Drive, byte-identical to the Drive copies (original filenames preserved) |
| `sources/provenance/` | Provenance ledger: Drive file IDs, timestamps, SHA-256 checksums, version/supersession notes |
| `architecture/` | Architectural specifications (design-discussion intent + sourced material) |
| `mathematics/` | Mathematical formalizations, proofs/countermodels, and research scaffolds; each document declares its own status |
| `research/` | `RESEARCH_BACKLOG.md` (authoritative task index, RHEO-001…RHEO-017), open research questions, experiment protocols |
| `adr/` | Architecture decision records |
| top-level PDFs/DOCXs/txt | 18 source files that could not pass the GitHub connector (binaries + 4 oversized texts), sorted in via local git 2026-10-11 — see `MANIFEST-github-blocked.txt` |

## How to read this tree

1. **Original research is never rewritten.** Files under `sources/original/` are
   historical records. Interpretations live in `architecture/`, `mathematics/`,
   and `adr/` — and must say which claims are sourced, which are proposed, and
   which are unresolved.
2. **Register discipline.** Following the Cognitive Metamorphic Primer v3:
   distinguish *design metaphor* (useful analogy), *formalism* (mathematical
   claim), and *engineering claim* (what is built and tested). A metaphor that
   is useful for thinking is not a proof.
3. **The three-geometry architecture** (11D lattice / 666D fractal / 1024D
   lattice, nine couplings, `(±∞, ±∞)` neutral weights) comes from the
   2026-10-10 design discussion, documented in
   `architecture/three-geometry-cognitive-architecture.md`. It is architectural
   intent, not a certified mathematical model. The older Drive sources do *not*
   contain this framing — see `adr/0001-hsl-fractal-reconciliation.md` for the
   evidence.

## Entry points

- Canonical semantic-separation law: `architecture/semantic-separation-invariants.md`
- Formal proof/countermodel support: `mathematics/semantic-separation-theorems.md`
- Decision record: `adr/0002-semantic-separation-canon.md`
- Start: `architecture/three-geometry-cognitive-architecture.md`
- Sources: `sources/provenance/SOURCE_INVENTORY.md`
- Open work: `research/RESEARCH_BACKLOG.md`
- Open questions: `research/research-questions.md`
- Decisions: `adr/0001-hsl-fractal-reconciliation.md`
