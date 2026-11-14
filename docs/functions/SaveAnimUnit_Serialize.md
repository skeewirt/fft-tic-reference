# SaveAnimUnit_Serialize

- **Address:** `0x1400B7970`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveAnimUnit_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveSummary_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes one animated unit's state: animation work id, unit id, colour and colour offset, flags and animation sequence.

## Behavior

- V: builds 6 descriptors and runs FieldSchema_Run over them.
- V: field names: `iAnimWorkID_`, `iUnitID_`, `iColor_`, `iColorOfs_`, `iFlags_`, `iAnimSeq_`.
- V: used by SaveSummary_Serialize.
- I: used for the unit shown in the save summary.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveSummary_Serialize](SaveSummary_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
