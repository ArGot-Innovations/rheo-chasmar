# Project Nexus v4.0 Verification Report

**Implementation:** `project_nexus_v4_reference.py`  
**Reference snapshot:** `project_nexus_demo_snapshot.qbin`  
**Verification date:** 2026-07-20 (America/Chicago)  
**Seed:** `2026`

## 1. Test environment

- Python: `3.13.5`
- NumPy: `2.3.5`
- Platform: `Linux 4.4.0 x86_64, glibc 2.41`
- Source size: `54,823 bytes`
- Snapshot size: `109,838 bytes`

## 2. Commands executed

```bash
python -m py_compile project_nexus_v4_reference.py
python project_nexus_v4_reference.py --self-test
python project_nexus_v4_reference.py \
  --seed 2026 \
  --snapshot project_nexus_v4_rerun_snapshot.qbin
```

## 3. Overall result

| Verification area | Result |
|---|---:|
| Python syntax compilation | PASS |
| Quinary dense/packed round trips | PASS |
| Active-mask and sign-vacuum invariants | PASS |
| HTNLA binding contract | PASS |
| Partial-inverse admissibility | PASS |
| Deterministic salience k-WTA | PASS |
| Inverse-bridge boundedness | PASS |
| All-vacuum edge case | PASS |
| Nominal warm-memory reconstruction | PASS |
| Hybrid-event fail-safe | PASS |
| Snapshot save/restore round trip | PASS |
| Seeded snapshot byte determinism | PASS |

Self-test console result:

```text
All Project Nexus v4.0 property tests passed.
```

## 4. Property-test coverage

The built-in deterministic suite exercised the following behaviors.

1. **Quinary serialization and canonicalization**
   - Twenty random dense vectors using values `{-2,-1,0,1,2}` were packed into the three bit planes.
   - Every vector passed invariant validation.
   - Every packed vector reconstructed exactly to the original dense vector.

2. **Binding and partial unbinding**
   - Twenty random constituent/binder pairs were bound.
   - Composite activity equaled the intersection of constituent and binder activity.
   - No sign bits remained outside the active plane.
   - Partial unbinding produced no impossible coordinates for valid composites.
   - The original constituent had zero admissible-set distance from its exact partial inverse.

3. **Deterministic k-WTA**
   - Two identical vectors given identical salience scores and `k=123` produced identical gated outputs.
   - Both outputs contained exactly 123 active coordinates.

4. **Inverse bridge**
   - The all-vacuum expected/observed case returned prediction error `0.0` without division errors.
   - RPE remained in `[-1,1]`.
   - Prediction error and novelty remained in `[0,1]`.
   - Twenty additional random cases satisfied the same bounds.

5. **Integrated runtime**
   - A corrupted composite completed all four TUCR stages.
   - The invariant guard passed.
   - Semantic cleanup accepted the intended attractor named `TARGET_A`.
   - A severity-1 hybrid shock activated the controller fail-safe.

6. **Persistence**
   - A runtime snapshot was saved and restored into a fresh runtime.
   - Controller state, salience state, Value Anchor, and warm-memory record names matched after restoration.

## 5. Nominal demonstration results

### Initial substrate

- Constituent `A` active coordinates: **484**
- Binder `B` active coordinates: **849**
- Expected bound composite active coordinates: **405**
- Base 666D spectral alpha: **-0.141983**
- Eigen-solver residual: **2.71e-03**

### TUCR trace

```text
integrate -> compete -> resonate -> transcend
```

### Inverse bridge

- Prediction error: **0.0425**
- Reward-prediction error: **-0.0064**
- Novelty: **0.7095**

### Salience k-WTA

- Active before gate: **389**
- Active after gate: **224**
- Coordinates pruned: **165**
- Resulting vacuum fraction: **78.1%**

### Partial inverse

- Exact coordinates: **763**
- Ambiguous coordinates: **86**
- Unknown coordinates: **175**
- Impossible coordinates: **0**

### Semantic cleanup and Maera

- Recovered memory: **`TARGET_A`**
- Action: **RENDER**
- Mode: **NOMINAL**
- Snap confidence: **0.822**
- Admissible-set distance: **0.101**
- Winner margin: **0.134**
- Cognitive resource `C_r`: **0.499**
- Invariant guard: **passed**

Exact output:

```text
[MAERA] action=RENDER mode=NOMINAL memory=TARGET_A k=224/1024 active=224 snap_conf=0.822 distance=0.101 margin=0.134 E=0.042 RPE=-0.006 N=0.709 Cr=0.499 guard=True
```

## 6. Hybrid stress-event results

Injected event:

- Name: **`PERIMETER_BREACH`**
- Severity: **1.0**

Controller response:

- Effective spectral alpha: **+0.9633**
- Spectral-friction penalty: **254.61**
- Allowed active coordinates: **1**
- Fail-safe: **triggered**
- Cognitive resource `C_r`: **0.274**
- Invariant guard: **passed**

Semantic/output response:

- Recovered memory: **none accepted**
- Action: **ABSTAIN**
- Mode: **SAFE_MODE**
- Active coordinates: **1**
- Candidate confidence: **0.765**
- Candidate distance: **0.164**
- Winner margin: **0.001**, below the acceptance margin

Exact output:

```text
[MAERA] action=ABSTAIN mode=SAFE_MODE memory=NONE k=1/1024 active=1 snap_conf=0.765 distance=0.164 margin=0.001 E=0.154 RPE=+0.003 N=0.710 Cr=0.274 guard=True
```

The important result is not merely that stress reduced activity. The runtime refused to convert a nearly tied cleanup candidate into an outward assertion. Maera abstained while the lower-level invariant guard still reported a structurally legal state.

## 7. Snapshot verification

### External file hashes

```text
03f8913c8f1f59b1507723c1cb1dc4039803db27fe39e8d2d4d11c51626aaa98  project_nexus_v4_reference.py
02a6cae04f106ba82847d5a2ed600651e99c56afb2d39a55a2453f94626e7eea  project_nexus_demo_snapshot.qbin
02a6cae04f106ba82847d5a2ed600651e99c56afb2d39a55a2453f94626e7eea  project_nexus_v4_rerun_snapshot.qbin
```

The original demonstration snapshot and the independently regenerated snapshot are **byte-for-byte identical**.

### Internal snapshot manifest

- Schema: `project-nexus-v4.0`
- HSL dimension: `1024`
- Coupling dimension: `666`
- Seed: `2026`
- Warm-memory records: `128`
- Internal canonical-state SHA-256: `68e6682c79edf155c49f74e17466dd08759e84f2d0aeb5eb75b34a7a9829d4f7`

### Stored array layout

- `controller_C`: `(11,) float64`
- `controller_dCdt`: `(11,) float64`
- `controller_scalars`: `(3,) float64`
- `salience_weights`: `(1024,) float64`
- `salience_previous_error`: `(1024,) float64`
- Value Anchor bit planes: three `(16,) uint64` arrays
- 666D coupling diagonal: `(666,) float64`
- Low-rank coupling basis: `(666,12) float64`
- Coupling strengths: `(12,) float64`
- Warm-memory bit planes: three `(128,16) uint64` arrays
- Manifest: UTF-8 JSON stored as `(7064,) uint8`

Only `TARGET_A` recorded a semantic-snap hit in this demonstration; all distractors remained at zero hits.

## 8. Saved post-stress state

The supplied snapshot was written after the nominal cycle and the hybrid stress cycle. Its saved controller values were:

```text
C = [
  0.5104240934, 0.4999583632, 0.4974365989,
  0.3136611204, 0.3642904936, 0.5592725399,
  0.5029206553, 0.5052040715, 0.7953713787,
  0.3859730414, 0.7908035622
]

C_r = 0.2744384266
B   = 0.5939476823
freeze_cycles = 1
```

## 9. What these results establish

The test run provides executable evidence that this implementation:

- Maintains the packed-quinary activity/sign invariants for the tested paths.
- Implements deterministic salience-based sparsification.
- Preserves the valid HTNLA partial-inverse relationship in randomized tests.
- Recovers a known attractor from a moderately corrupted bound representation.
- Transitions to a fail-safe state and abstains during the tested severity-1 event.
- Saves and restores its principal runtime state with checksum verification.
- Reproduces the seeded snapshot deterministically in the tested environment.

## 10. What these results do not establish

These are implementation/property tests, not empirical proof of general intelligence, consciousness, self-creation, universal stability, or production security. They do not yet establish:

- Long-horizon numerical stability over millions of cycles.
- Robustness over a broad distribution of seeds, corruption levels, and event sequences.
- Formal Lyapunov stability of the complete hybrid system.
- Cross-platform byte-identical snapshots under different NumPy, BLAS, CPU, or endian environments.
- Performance limits, memory scaling, concurrency safety, or real-time guarantees.
- Calibration validity of the current 11D coefficients, 666D spectral gains, or cleanup thresholds.
- Resistance to deliberately malformed snapshot archives beyond checksum/schema rejection.

Those require a larger falsification harness, parameter sweeps, long-run tests, mutation tests, profiling, and independent replication.
