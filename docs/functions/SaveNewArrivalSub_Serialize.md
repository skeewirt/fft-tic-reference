# SaveNewArrivalSub_Serialize

- **Address:** `0x1400C1E40`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveNewArrivalSub_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveLibrary_Serialize
- **Callees:** FieldSchema_Run, SaveNewFlags_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes a new-arrival entry with a sub-key.

## Behavior

- V: builds 2 descriptors and runs FieldSchema_Run over them.
- V: field names: `new_arrival`, `sub_key`.
- V: its nested records use SaveNewFlags_Serialize.
- V: used by SaveLibrary_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveNewFlags_Serialize](SaveNewFlags_Serialize.md)

## Referenced by

- Called by: [SaveLibrary_Serialize](SaveLibrary_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
