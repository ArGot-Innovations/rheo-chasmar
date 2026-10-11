# HDF5 Storage Layout

This document provides a schematic overview of the physical data layout within the `hvd_database.h5` file. Understanding this structure is useful for debugging, direct data inspection, and appreciating how the database organizes collections and their associated data.

The HDF5 file is organized hierarchically, with top-level groups representing different collections.

```text
/ (root)
|
+-- collection_A/
|   |
|   +-- vectors/
|   |   |
|   |   +-- vector_id_1/
|   |   |   |
|   |   |   +-- visual (dataset: float32, shape=(D1,))
|   |   |   +-- audio (dataset: float32, shape=(D2,))
|   |   |
|   |   +-- vector_id_2/
|   |       |
|   |       +-- text (dataset: float32, shape=(D3,))
|   |       ...
|   |
|   +-- metadata (dataset: string, shape=(N,))
|   |   (A JSON string array storing metadata for N vectors)
|   |
|   +-- tombstones (dataset: string, shape=(M,))
|       (An array of vector IDs marked for deletion)
|
+-- collection_B/
    |
    ... (Structure is repeated for each collection)
```

## Key Components Explained

- **/ (root)**: The root of the HDF5 file.

- **`collection_A/`**: A top-level **group** representing a single, namespaced collection within the database.

- **`vectors/`**: A subgroup containing all the hypervector data for the collection.

- **`vector_id_1/`**: A group where the key is the unique ID of a hypervector record. This group holds all the vector components for that record.

- **`visual` (dataset)**: An HDF5 **dataset** containing the raw NumPy array for a single component of the hypervector. The dataset is named after the component key (e.g., "visual", "audio", "text").

- **`metadata` (dataset)**: A single, contiguous dataset within the collection's group. It stores the metadata for all vectors in the collection as a large array of JSON strings. This design is optimized for efficient batch reading.

- **`tombstones` (dataset)**: A dataset containing a list of vector IDs that have been "soft-deleted." These IDs are ignored during searches and are physically removed from the file only during a full index rebuild.


## TMS storage engine configuration (optional)

If you choose the Transdimensional Memory Substrate (TMS) backend (`database.backend: "tms"`), the storage layer switches from the HDF5 layout described above to an LSM-style design with a Write-Ahead Log (WAL), memtables, and SSTables. You configure this in `config.yaml` under `database.tms`.

- See `docs/configuration.md` → “When using the TMS backend (`database.backend: "tms"`)” for the full set of fields and tuning notes.

- Common fields:
  - `database.tms.wal_keep_last` — keep N most recent WAL segments in-place after rotation (default 2).
  - `database.tms.wal_archive_dir` — optional directory to move older WAL segments (disabled by default).
  - `database.tms.compaction_interval_seconds` — background compaction cadence (seconds). If omitted, engine default is used.
  - `database.tms.cleanup_jitter_ms` — optional small random delay for background cleanup sweeps (default 0).

Example snippet:

```yaml
database:
  backend: "tms"
  tms_path: "./tms_store"
  tms:
    wal_keep_last: 2
    wal_archive_dir: "./wal_archive"
    cleanup_jitter_ms: 0
```

Notes:

- Values set in `config.yaml` take precedence over environment variables `TMS_WAL_KEEP_LAST`, `TMS_WAL_ARCHIVE_DIR`, `TMS_COMPACTION_INTERVAL_SECONDS`, and `TMS_CLEANUP_JITTER_MS`.
- Deletion hardening: SSTable file unlink uses a small retry with exponential backoff to tolerate transient races around iterator unpinning. Tunables: `TMS_UNLINK_RETRY_ATTEMPTS` (default 5) and `TMS_UNLINK_RETRY_INITIAL_MS` (default 10ms).
- Iterator safety: When compacting, files currently pinned by readers are orphaned and removed after the last unpin or during background sweeps; this prevents use-after-close.
- Archival is best-effort and never blocks a successful flush.
