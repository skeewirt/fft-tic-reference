# sub_1400C3DBC

- **Address:** `0x1400C3DBC`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `bool sub_1400C3DBC(SaveDataManager *manager)`
- **Callers:** `sub_1400C3B84` (flush), `sub_1400C480C` (world save) — 2 sites
- **Callees:** `sub_1400C3140` (queue one entry), `sub_140033A18`, `sub_1400C3084`, `sub_1400C6378`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Walks the resume name-to-record map and queues every dirty record as a container entry, erasing each record as it goes.

## Behavior

- V: the map is the per-group dedupe map: a record is keyed by entry name and holds the buffer and its dirty state.
- V: each dirty record is handed to the entry writer, which seals it and queues it under its name.
- V: the record is erased after queueing, so the map only holds entries that still have to be written.
- V: it returns whether anything was queued, which the world-save caller uses to decide whether to kick a write at all.
- V: two call sites: the per-frame flush and the world-map save.
- I: erasing on queue is why a name can be recaptured later without a duplicate entry in the same container.
- ?: what the three helper calls do; only the map walk and the queue were read.

## State touched

- Calls: [sub_1400C3140](sub_1400C3140.md)

## Referenced by

- Called by: [sub_1400C3B84](sub_1400C3B84.md), [sub_1400C480C](sub_1400C480C.md)

## Notes

The "queue everything that is ready" half of the resume writer; `sub_1400C4198` is the "prepare one record" half.

## Open questions

None recorded.
