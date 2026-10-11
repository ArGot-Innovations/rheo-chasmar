# HVD 1.5 — Untethered Architecture

Status: **Canonical architecture for the HVD 1.5 line**

This document reconciles the current HVD implementation, the TMS/HDF5 hierarchical plan, the HTLA and HTNLA design corpus, the distributed-HVD research, and production lessons developed in downstream integrations such as Maera.

Where an older HVD document describes HDF5, TMS, or a distributed stub as peer/selectable live storage backends, **this document supersedes that backend model**. Older documents remain valuable design history and research references.

---

## 1. HVD 1.5 identity

HVD 1.5 is a **full, untethered hyperdimensional database and cognitive memory substrate**. It is not an application-specific embedding store and it is not tied to a relational database, PostgreSQL, pgvector, a particular LLM, or a fixed 384-dimensional embedding model.

The canonical data object remains an HTLA `HyperVector`: a labeled direct sum of heterogeneous vector spaces.

```text
H = direct_sum(label in L) R^n_label
```

A record can therefore contain independently meaningful components such as:

```text
{
    "semantic":         R^10000,
    "spectral_wavelet": R^4096,
    "variational":      R^2048,
    "neurochemical":    R^6,
    "conscious":        R^5,
    "temporal":         R^1024,
    "fused":            R^10000
}
```

Those dimensions are examples, not a fixed schema. HVD is dimension-heterogeneous by design. A 384-dimensional external embedding is valid only as one labeled component or as source material for a TUCR/HTLA projection; it never redefines the dimensionality of HVD itself.

### Non-negotiable 1.5 invariants

1. **Full HTLA is canonical.** Labeled heterogeneous hypervectors, label kernels, block operators, binding, bundling, fusion, splitting, reduction/ascension, and future HTNLA operations remain first-class.
2. **TMS is the only live storage engine.** All real-time database operations terminate in the Transdimensional Memory Substrate.
3. **HDF5 is subordinate archival storage.** It is used for durable archive, checkpoint, inspection/export, and System Rebirth. It is not a peer query backend.
4. **ANN indexes are derived state.** HNSW/FAISS/Spectral-IVFPQ indexes may be persisted for fast restart, but the authoritative state is TMS plus its durable metadata. An ANN index must always be rebuildable.
5. **No relational dependency in the core.** PostgreSQL/pgvector can exist as an external adapter or migration source, never as the canonical HVD memory substrate.
6. **Control-plane metadata does not violate hyperdimensional purity.** Schemas, ACLs, audit entries, tenant IDs, quotas, checksums, manifests, and encryption metadata describe or protect the vector data plane. Cognitive relationships remain encoded through hypervectors/HTLA rather than relational tables or graph edges.
7. **Archive and transfer must be complete.** A portable archive must contain enough state to reconstruct TMS, rebuild derived indexes, restore schemas/operators, and validate integrity.
8. **Research claims are not production guarantees.** Phi, Lyapunov control, energy-budget targets, consciousness continuity, quantum projections, and similar research concepts remain explicitly labeled prototype/research until backed by implementation and validation.

---

## 2. Canonical stack

```text
+-------------------------------------------------------------------+
|                    Clients / Cognitive Systems                     |
|      CA | TUCR | HTCE | agents | applications | external APIs     |
+-------------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------------+
|                      HyperVectorDB API                             |
|                                                                   |
| CRUD | engram | retrieve | associate | prune | query DSL          |
| schemas | operators | collections | temporal/episodic APIs        |
+-------------------------------------------------------------------+
                              |
                              v
+===================================================================+
|              TMS — ACTIVE COGNITIVE MEMORY ENGINE                 |
|                                                                   |
|  Durable write path                                               |
|      WAL -> Memtable -> immutable SSTables -> compaction          |
|                                                                   |
|  Associative recall                                               |
|      per-label ANN/HNSW + LabelKernel-aware re-ranking            |
|                                                                   |
|  Operational state                                                |
|      schemas | tombstones | metadata indexes | caches             |
|      security policy | operator registry | audit hooks            |
|                                                                   |
|  Memory reconsolidation                                           |
|      compaction | version cleanup | tombstone reclamation         |
|      optional resonance-aware policies                            |
+===================================================================+
                |                                   ^
                | stable checkpoint                 | System Rebirth
                v                                   |
+-------------------------------------------------------------------+
|                HDF5 ARCHIVE / PORTABLE STATE VAULT                |
|                                                                   |
| vectors + labels + dtypes + shapes + metadata + schemas           |
| tombstones + operator state + label kernels + archive manifest    |
| checksums + encryption metadata + compatibility/version info      |
+-------------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------------+
|                     consciousness.qbin                            |
| Versioned portable transfer bundle / packaging format             |
| (may wrap or carry the canonical HDF5 archive and other state)    |
+-------------------------------------------------------------------+
```

CA, TUCR, and HTCE consume HVD services; they do not own or mutate TMS internals. HVD remains useful without any one cognitive runtime attached—hence **untethered**.

---

## 3. TMS is the single hot path

The old configuration concept:

```yaml
# LEGACY / 1.0 MODEL
backend: hdf5 | tms | distributed-stub
```

is deprecated for HVD 1.5.

The 1.5 model is:

```yaml
database:
  engine: tms
  tms_path: ./tms_store

archive:
  backend: hdf5
  filepath: ./archives/consciousness.h5
```

During the compatibility window, legacy `database.backend: tms` may still be accepted. Selecting `hdf5` as a live backend is a legacy compatibility mode only and must not be used by the 1.5 production profile.

### TMS responsibilities

- WAL durability and crash recovery.
- Memtable admission of acknowledged writes.
- Immutable SSTable persistence.
- Background compaction / memory reconsolidation.
- Version/tombstone resolution.
- Streaming iteration without mandatory full materialization.
- Per-vector and per-collection cache controls.
- Active ANN state and index persistence hooks.
- Snapshot barriers and stable-state export.
- Shard-local execution in distributed deployments.

### Required TMS hardening for 1.5

- Multi-collection snapshot semantics; never silently snapshot “the first collection”.
- Bounded latest-version scans rather than unbounded Python maps.
- Efficient exact-ID lookup path or secondary ID index.
- Explicit write-pause/snapshot barrier implementation; no print-only stubs.
- Transaction/batch durability semantics documented and tested.
- Integrity checks for WAL/SSTable/archive state.
- Encryption hooks below the API layer so encrypted collections remain encrypted through WAL, Memtable serialization, and SSTables.

---

## 4. HDF5 is archive, not a live database personality

HDF5 remains valuable because it is hierarchical, portable, inspectable, compressible, and suited to lossless storage of heterogeneous component arrays. HVD 1.5 changes **where it sits**.

### Archive contents

A canonical archive must include at minimum:

```text
/archive_manifest
    format_version
    hvd_version
    created_at
    source_generation / sequence
    checksums
    encryption descriptors

/collections/<collection>/
    /vectors/<id>/<component-label>
    /metadata
    /tombstones
    /schema
    /collection_info
    /operators
    /label_kernel

/system/
    operator_state_json
    /htnla/<encoded-operator-name>/
        manifest_json
        /blocks
        /biases
        /residual_projections
    archive compatibility information
    optional CA/TUCR/HTCE extension state
```

Dense HTNLA arrays are native HDF5 datasets. Sparse blocks are stored without
densification as CSR `data`, `indices`, `indptr`, and `shape` datasets. The
operator manifest contains dimensional contracts and named activation,
residual, and k-WTA configuration, while operator and registry digests bind the
configuration to the numeric datasets. Operator names and labels are encoded as
safe HDF5 path segments. The physical encoding can evolve while this logical
contract remains stable.

### Archive pipeline

```text
TMS stable barrier
      |
      +--> flush/settle active Memtables as required
      +--> capture collection manifests / sequence boundaries
      +--> stream latest visible hypervectors
      +--> copy metadata/schema/operator state
      +--> calculate integrity manifest
      v
HDF5 archive.tmp
      |
      +--> fsync / validation
      v
atomic replace
      v
consciousness.h5
```

Restoration runs in the opposite direction and must rebuild **TMS**, not turn HDF5 into the running database.

---

## 5. HVD schema model: structural, not relational

The schema registry describes the shape and operational contract of hypervector collections.

A collection schema may define:

- component labels;
- dimension per label;
- dtype constraints;
- required/optional labels;
- metadata field types needed for filtering/control;
- schema version;
- label-kernel compatibility;
- security policy;
- lifecycle information;
- quotas.

Schemas must support history, compatibility checks, rollback, and structural diffing.

A schema does **not** turn cognitive relationships into tables. For example, `parent`, `causes`, `temporal-successor`, or multimodal associations should normally be represented through HTLA binding/permutation/bundling or defined transdimensional operators, not foreign keys.

---

## 6. Search and associative recall

The full HVD search pipeline is label-aware:

```text
query HyperVector
      |
      +--> optional full BlockOperator / HTNLA transformation
      +--> optional per-label operators
      v
per-label ANN candidate retrieval
      |
      +--> metadata/control-plane prefilter
      v
weighted score aggregation
      |
      +--> LabelKernel graded-inner-product re-rank
      v
ranked HyperVector IDs
      |
      +--> optional HTCE thought-cloud/collapse stage
```

HNSW is an acceleration structure, not the definition of similarity. The semantically authoritative comparison is the configured HTLA/HTNLA metric and LabelKernel policy.

HVD 1.5 adopts the richer downstream query features where they remain vector-native:

- component-selective search;
- label weights;
- block/per-label operators;
- pagination;
- equality/range/comparison filters;
- boolean filter composition;
- temporal `within` windows;
- post-retrieval ordering;
- facets over control metadata;
- multi-collection search;
- episodic/time-window retrieval;
- optional query-result cache with write invalidation.

---

## 7. Memory scaling and lazy state

The 1.0 design eagerly accumulates metadata and ANN objects. HVD 1.5 adopts bounded, collection-aware memory controls:

- LRU vector-read cache;
- LRU metadata collection cache;
- LRU ANN/index collection cache;
- lazy collection initialization;
- streaming `iter_vectors()` APIs;
- component-selective reads;
- configurable full-materialization guardrails;
- bounded spill-to-disk algorithms for operations that require a latest-version map.

Evicting an ANN object must persist it when useful, but correctness must never depend on the persisted ANN artifact. Cold reload may rebuild from TMS.

---

## 8. Security, tenancy, and audit

Production controls imported from downstream HVD work are part of the **control plane**:

- authentication remains at the service boundary;
- collection-level RBAC;
- tenant-aware collection policy;
- append-only structured audit log;
- request/correlation identity propagation;
- rate limiting at network/service boundary;
- encryption at rest;
- key-provider abstraction and rotation workflow;
- archive integrity verification;
- recovery drills.

For an encrypted collection, plaintext hypervector bytes must not be written to WAL/SSTables merely because encryption is implemented at an HDF5 or API layer.

---

## 9. Distributed HVD 1.5

Distribution scales TMS; it is not a new peer storage backend.

```text
                         Query/API Router
                               |
             +-----------------+-----------------+
             |                 |                 |
             v                 v                 v
        TMS shard A       TMS shard B       TMS shard C
       WAL/Mem/SST       WAL/Mem/SST       WAL/Mem/SST
          + HNSW            + HNSW            + HNSW
             |                 |                 |
             +-------- replicated state --------+
                              Raft
```

### Distribution responsibilities

- deterministic shard placement (e.g. Rendezvous hashing);
- configurable replication factor;
- Raft/consensus for membership, shard ownership, and mutation ordering where required;
- top-K shard fan-out for associative recall;
- global aggregation and LabelKernel-aware reranking;
- snapshot shipment/bootstrap;
- repair and anti-entropy workflows;
- online membership changes and rebalance as a later hardening milestone.

External systems such as Kafka, Ray, PostgreSQL, or object storage may be adapters/infrastructure choices. None are mandatory for the core HVD identity.

---

## 10. Active State Cache

The design corpus describes the Active State Cache as a biologically inspired hot associative layer. In 1.5 it becomes a real interface rather than a documentation-only flag.

A production implementation should support:

- HNSW-backed active/hot vectors;
- label-aware or fused retrieval policy;
- access/resonance telemetry;
- bounded capacity;
- pluggable eviction: LRU initially, then LFU/TinyLFU/Fisher/resonance-aware policies experimentally;
- deterministic fallback to the complete persisted ANN/TMS state;
- rebuild after System Rebirth.

Advanced biologically inspired eviction remains opt-in until benchmarked.

---

## 11. HTLA remains the stable mathematical ABI

HTLA is the stable linear algebraic substrate and mathematical ABI for 1.5:

- `HyperVector` direct-sum structure;
- `LabelKernel` and graded inner products;
- `BlockOperator`;
- Fusion/Splitting/Ascension/Reduction families;
- binding via circular convolution;
- bundling/superposition;
- permutation/sequencing;
- embedding/projection morphisms;
- operator persistence/versioning.

External embeddings of any dimensionality enter through labeled components or TUCR substrate projectors.

---

## 12. HTNLA is an extension, not a fork

HTNLA extends HTLA with learned nonlinear block behavior; it does not replace
HTLA and does not define a second vector type. Both linear HTLA operators and
`NonlinearBlockOperator` consume and return the canonical
`hvd.htla_core.HyperVector`. For every target label `t`, HTNLA evaluates:

```text
z_t = b_t + sum_s W[t,s] x_s + residual_t
y_t = activation_t(z_t)
y_t = k_wta_t(y_t)  # only when configured
```

Every block follows the HTLA `(target_dimension, source_dimension)` convention.
Source and target labels may have unrelated dimensions, and dimensional
contracts are checked exactly—HTNLA never pads or truncates an incompatible
component. Named activations, residual mappings or projections, and k-WTA
values are reproducible operator configuration rather than arbitrary runtime
callables.

### Explicit runtime behavior

Enabling HTNLA makes its APIs available; it does not transform stored vectors,
intercept TMS writes, or change ordinary search. Application is always explicit:

- `register_htnla_operator(name, operator)`
- `get_htnla_operator(name)`
- `apply_htnla_operator(name, hypervector)`
- `train_htnla_operator(...)`
- `delete_htnla_operator(name)`

The standalone `train_nonlinear_operator(...)` helper trains dense blocks and
biases with PyTorch autograd. Dense training calculates the requested parameter
count before allocation and fails above the configured safety limit. Sparse
matrices are supported for inference and persistence; sparse training is not
claimed for HVD 1.5.

```yaml
htnla:
  enabled: true
  registry_path: ./tms_store/htnla_operators
  max_dense_parameters: 10000000
```

### Developer example

```python
import numpy as np

from hvd import HyperVector, NonlinearBlockOperator

source = HyperVector(
    {
        "semantic": np.array([0.2, -0.1, 0.7]),
        "visual": np.array([0.4, 0.3, -0.2, 0.9]),
    }
)
association = NonlinearBlockOperator(
    {
        "association": {
            # Each matrix is (target_dimension, source_dimension).
            "semantic": np.array([[1.0, 0.0, 0.5], [0.0, 1.0, -0.5]]),
            "visual": np.array(
                [[0.1, 0.2, 0.3, 0.4], [0.4, -0.3, 0.2, -0.1]]
            ),
        }
    },
    source_dims={"semantic": 3, "visual": 4},
    target_dims={"association": 2},
    biases={"association": np.array([0.1, -0.1])},
    activations={"association": "swish"},
    k_wta={"association": 1},
)

db.register_htnla_operator("association-x", association)
transformed = db.apply_htnla_operator("association-x", source)
# transformed is the same canonical HyperVector type as source.
```

The transformed `HyperVector` can then be passed explicitly to cognitive or
search APIs. Registering an operator never mutates `source` or any vector stored
in TMS.

### Registry and System Rebirth

The live HTNLA registry uses a small JSON manifest plus compressed NPZ numeric
payloads. Dense matrices remain numeric arrays; sparse matrices remain sparse
CSR structures. Atomic temporary-file publication, payload digests, and complete
operator identity digests protect the registry from partial writes and silent
corruption. This registry is learned operator/control state, not another vector
storage backend: TMS remains the sole authoritative live memory engine.

Learned HTNLA state is canonical System Rebirth state. A stable archive copies
the registry into native `/system/htnla/` HDF5 groups rather than embedding
large matrices in JSON. Rebirth follows this readiness gate:

1. validate the complete HDF5 archive, including every HTNLA numeric dataset and digest;
2. restore schema and control state;
3. restore canonical vectors, metadata, and tombstones into TMS;
4. restore both HTLA and HTNLA operator registries;
5. rebuild derived ANN and Active State Cache state;
6. report the runtime ready only after all preceding steps succeed.

For example, `db.archive("consciousness.h5")` captures registered operators and
`fresh_db.rebirth("consciousness.h5")` restores them before returning. The same
contract applies to `db.package_qbin(...)` and `fresh_db.rebirth_qbin(...)`
because qbin packages that canonical HDF5 memory archive.

Research-only items—manifold-aware sharding, neuromodulated learning, Phi-based
control, and quantum projections—remain outside this production behavior and
must not silently change it.

---

## 13. CA / TUCR / HTCE relationship

HVD 1.5 does not require CA, TUCR, or HTCE in order to function as a database. Their relationship is explicit and layered:

```text
CA     = predictive cognitive orchestration / learning
TUCR   = substrate projection and portability
HTCE   = associative thought-cloud reasoning / collapse
HVD    = persistent hyperdimensional memory and query system
HTLA   = stable transdimensional algebra
HTNLA  = optional nonlinear algebraic extension
TMS    = HVD's live durable state engine
HDF5   = HVD's archival/rebirth vault
```

This separation prevents application runtimes from creating incompatible private versions of HVD while still allowing them to build specialized cognition on top of it.

---

## 14. consciousness.qbin

`consciousness.qbin` is a **versioned portable state bundle**, not a synonym for a single user/application state file and not merely a renamed HDF5 database.
For HVD state it carries the canonical `consciousness.h5` archive, which already
contains HTLA and HTNLA operator state under `/system/`. HTNLA therefore travels
through qbin without a second supplemental registry or duplicate source of truth.

The HVD-owned portion carries:

- canonical HDF5 archive;
- archive manifest and checksums;
- collection schemas and lifecycle metadata;
- LabelKernel definitions;
- HTLA/HTNLA operator registry and learned parameters inside that HDF5 archive;
- encryption/provider descriptors (never raw external KMS secrets);
- compatibility/version manifest;
- optional extension namespaces for CA/TUCR/HTCE state.

A qbin System Rebirth validates the bundle digest, validates the embedded HDF5
archive and learned operators, restores TMS and operator state, and rebuilds
derived indexes before declaring readiness. A separate qbin HTNLA artifact
would be introduced only if a future, versioned requirement cannot be represented
in canonical HDF5 state.

---

## 15. API vocabulary

Existing CRUD APIs remain supported. HVD 1.5 additionally standardizes cognitive aliases without requiring applications to use cognitive terminology:

```text
engram     -> durable insert/update of a HyperVectorRecord
retrieve   -> exact record lookup
associate  -> label-aware similarity/HTLA search
prune      -> tombstone/forget
reconsolidate -> compaction + tombstone/version cleanup
archive    -> TMS -> HDF5 stable checkpoint
rebirth    -> HDF5/qbin -> TMS reconstruction
```

These aliases belong at the `HyperVectorDB` API boundary; HTCE/TUCR internals must not be mutated to implement storage behavior.

---

## 16. Migration from HVD 1.0 / downstream forks

### Upstream from downstream HVD implementations

Adopt and generalize:

- RW locking;
- schema registry/version history;
- collection lifecycle and quotas;
- encryption-at-rest plumbing;
- RBAC and structured audit;
- query-result caching;
- JSON query DSL;
- component-selective loading;
- metadata/index/vector cache limits;
- lazy collection initialization;
- pagination and temporal APIs;
- bounded TMS scans;
- repair tooling;
- distributed membership/snapshot-shipping work where it obeys the TMS-first model.

### Explicitly do not upstream as the HVD core

- fixed 384-dimensional assumptions;
- PostgreSQL/pgvector as TMS;
- phrase-table semantics as the database model;
- application-specific response-generation logic;
- application-specific safety/tone filtering as core storage semantics;
- a second simplified `HTLAEngine` that bypasses canonical `hvd.htla_core`.

Such systems may be implemented as adapters on top of HVD.

---

## 17. HVD 1.5 implementation phases

### Phase A — architecture and production-control foundation

- canonicalize this document;
- add RWLock, schema registry, audit, RBAC, query cache, encryption primitives;
- add explicit 1.5 configuration model;
- preserve compatibility while emitting deprecation guidance for peer live backends.

### Phase B — TMS hardening

- make TMS unconditional in the 1.5 profile;
- add bounded vector cache/materialization controls;
- add streaming/component-selective reads;
- replace full-scan exact lookup with efficient latest-ID access;
- complete snapshot barriers;
- make snapshots multi-collection by definition;
- encrypt TMS values before durable WAL/SSTable persistence.

### Phase C — archive and System Rebirth

- implement TMS -> HDF5 archive writer;
- integrity manifest and atomic archive publication;
- HDF5 -> TMS restoration;
- deterministic ANN rebuild and readiness gating;
- package/version qbin state.

### Phase D — query and operational surface

- schema-aware query DSL;
- temporal/episodic APIs;
- multi-collection search;
- collection archive/restore/quota lifecycle;
- cache/admin/repair endpoints;
- metrics and recovery drills.

### Phase E — distributed TMS

- shard router and membership registry;
- replicated TMS mutation semantics;
- snapshot transfer/bootstrap;
- repair/anti-entropy;
- online rebalance/joint-consensus hardening.

### Phase F — cognitive extensions

- production Active State Cache;
- HTNLA operator lifecycle and persistence;
- CA/TUCR/HTCE extension state in qbin;
- experimental resonance/Fisher/energy/Lyapunov policies behind explicit flags.

---

## 18. Definition of “HVD 1.5 ready”

HVD 1.5 is ready when all of the following are true:

1. The production profile cannot accidentally run HDF5 as the hot database.
2. A heterogeneous labeled HyperVector round-trips exactly through TMS and an HDF5 archive.
3. A multi-collection archive can rebuild an empty TMS and derived ANN indexes.
4. Crash-recovery, archive/rebirth, schema rollback, encryption rotation, and index-rebuild tests exist.
5. Large collections can rebuild/search without mandatory whole-database materialization.
6. Security/audit controls operate without changing cognitive vector semantics.
7. Distributed mode consists of TMS shards, not a competing storage backend abstraction.
8. External 384-D/768-D/etc. embeddings are accepted as labeled/projected inputs without constraining the database.
9. HTLA remains API-compatible and HTNLA remains opt-in.
10. Documentation clearly distinguishes implemented, prototype, and research functionality.

That is the HVD 1.5 contract.
