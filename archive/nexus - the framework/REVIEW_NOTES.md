# Review notes — project_nexus_v4_reference.py

## Verified against your uploaded files
- Source hash matched your verification report exactly (`03f8913c8f1f...`)
- `--self-test`: pass
- Full demo (seed 2026): every nominal and stress number reproduced exactly
- Output snapshot: byte-identical SHA-256 to your uploaded `.qbin`, on a different Python (3.12.3 vs 3.13.5) and NumPy (2.4.4 vs 2.3.5) than your original run

## Changes made (all additive, no cycle-math touched)

1. **Calibration fingerprint.** `save_snapshot` now hashes every numerical
   calibration constant (LAMBDA, W_C/W_E/W_R/W_N, BIAS, K0, GAMMA_M, salience
   gains, etc.) into the manifest. `restore_snapshot` checks it and raises
   `ValueError` on mismatch instead of silently running old state through
   different dynamics. This closes the gap between the module docstring's
   claim ("versioned here so they cannot be silently changed") and what was
   actually checked — previously, nothing was.

2. **Memory-array length check.** `restore_snapshot` now validates that
   `memory_sign`/`memory_mag1`/`memory_mag2` row counts match the manifest's
   memory list before indexing, with a clear `ValueError` instead of an
   obscure `IndexError` on a malformed snapshot.

3. **Negative self-tests.** Added four tests that previously didn't exist:
   - `InvariantGuard` actually rejects a controller state pushed outside the
     `[0,1]` cube (previously only ever tested on legitimate cycles)
   - `InvariantGuard` actually rejects a swapped Value Anchor
   - `restore_snapshot` actually rejects a tampered checksum
   - `restore_snapshot` actually rejects a calibration-fingerprint mismatch

## Confirmed side effect (expected, not a bug)
Your original `project_nexus_demo_snapshot.qbin` predates the fingerprint
field. Loading it with this reviewed version correctly raises
`ValueError: snapshot calibration fingerprint does not match...` — that's
the new check doing its job on a snapshot it can't verify, not a break.

## What this review does not claim
Same scope as your own report's section 10: this confirms code correctness
and closes two specific integrity gaps. It says nothing about long-horizon
stability, cross-BLAS/architecture determinism, parameter calibration
validity, or anything about cognition/consciousness.
