# SaveIdPair_Serialize

- **Address:** `0x1400B8584`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveIdPair_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWalkRoute_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes a small record with a second id (`id2`).

## Behavior

- V: builds 2 descriptors and runs FieldSchema_Run over them.
- V: field names: `id2`.
- V: used by SaveWalkRoute_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveWalkRoute_Serialize](SaveWalkRoute_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
