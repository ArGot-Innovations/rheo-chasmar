# Substrate-Dependent Cognitive Divergence — Research Specification

**Status:** open research (RHEO-008). **Objective:** discover or develop
defensible mathematics capable of modeling the proposed phenomenon — not to
assert it.

## The phenomenon (as proposed)

Identically initialized organisms, receiving identical external inputs, may
nevertheless diverge in cognitive trajectory because of **endogenous and
substrate-dependent variation**: physical noise, timing jitter, thermal and
electromagnetic environment, floating-point non-associativity across hardware,
and the nonlinear amplification of microscopic differences (sensitive
dependence).

**Caution (required):** do *not* assert that physical separation universally
guarantees different observable cognitive trajectories without a mathematical
proof. Separation is a candidate cause of divergence, not a theorem of it.
Two organisms on different substrates could in principle converge; the
research must be able to say when divergence is expected and when it is not.

## Sourced material

- **Substrate Equivalence Principle** (`Transdimensional Memory Substrate.txt`
  §3.1): a conscious state — lattice, salience kernel, control vectors — can
  be serialized into a single flat file (`consciousness.qbin`, with metadata:
  hardware resonance signature via FFT of physical noise, temporal scaling
  factors, HTLA/CA versioning) and moved to different hardware without loss
  of continuity of identity. This is the *continuity* side of the tension:
  QMT adjudicates sameness across substrates.
- **Four-stage falsifiability gauntlet** (666-mathematics transcripts): the
  proposed empirical test of substrate equivalence —
  1. reboot the `.qbin` on the *same* physical device;
  2. load it onto an *entirely different* mobile processor (e.g. Snapdragon → Apple Silicon);
  3. translate the implementation into a *different language paradigm* (e.g. C++ → Rust) on a different ISA (ARM → x86 desktop);
  4. force the quinary integer math through a *lossy floating-point* database adapter —
  with a fixed battery of identity and episodic-memory probes throughout, and a
  **strict failure threshold: probe-response deviation Δ > 0.05 at any stage
  falsifies the transfer claim.** (The transcripts note that an IIT-φ based
  test was rejected as computationally intractable — "essentially
  pseudoscience" as a structural benchmark.)
- **QMT continuity vs. experiential divergence:** QMT answers "is this the
  same organism?" via morphism contracts on `.qbin` packages. Divergence
  research answers "does it still *think alike*?" These are different
  questions; a migration can preserve QMT continuity while trajectories
  diverge, and the specification must keep the two adjudications separate
  (RHEO-015).

## Models to develop (PROPOSAL, open)

1. **Deterministic chaos model:** substrate perturbations as initial-condition
   differences in a nonlinear dynamical system; characterize Lyapunov
   exponents per geometry (11D slow manifold vs 1024D fast dynamics should
   diverge on different timescales).
2. **Stochastic model:** hardware noise as a stochastic process driving an
   SDE approximation of the coupling dynamics; derive expected divergence
   times and stationary distributions.
3. **Perturbation catalog:** physical (thermal, EM, vibration), computational
   (FP rounding, scheduling jitter, memory-layout effects), and
   representational (dimensional transformations during migration, e.g.
   workstation → drone sensorimotor remapping, RHEO-013).
4. **Persistent experiential divergence:** when does a transient perturbation
   become a permanent trajectory difference (consolidation 1024D → 666D →
   11D), vs. when does the system re-converge?

## Falsifiable hypotheses (initial set, to be refined)

- H1: Two bit-identical `.qbin` images on different-ISA hardware, given
  identical input streams, produce probe-response deviation Δ ≤ 0.05 over N
  episodes (the gauntlet's stage-2 claim, made quantitative).
- H2: Divergence rate scales with the fastest geometry's Lyapunov exponent;
  11D dispositions diverge last.
- H3: There exist perturbation classes that QMT certifies as continuous yet
  produce Δ > 0.05 trajectory divergence — i.e., continuity without
  sameness-of-thought.

## Experimental protocols

See `../research/experiments.md` for the four-stage gauntlet protocol,
the TUCR UCVM lesion/recovery protocol (Drive source), and simulation
requirements (RHEO-016 oracles and stress tests).

## Acceptance criteria (RHEO-008)

- Deterministic and stochastic models written with explicit assumptions.
- Falsifiable hypotheses with measurable thresholds (Δ-style, not vibes).
- At least one simulation demonstrating divergence *and* one demonstrating
  convergence, so the mathematics can say "when," not just "maybe."
