# ANN index persistence and snapshots

- Per-collection, per-label ANN indexes are saved at:
  - <dbfile>.<collection>.<label>.ann (some backends emit .npz)
- A registry file lists label/dim info:
  - <dbfile>.<collection>.ann_registry.json
- On cold start, the DB attempts to load indexes from these files; if missing or invalid, it rebuilds from storage.

Snapshot/restore:
- HDF5Storage.create_snapshot(path) creates an atomic copy of the current DB file
- HDF5Storage.restore_from(path) atomically restores from a snapshot
- Use these for backups or point-in-time recovery

