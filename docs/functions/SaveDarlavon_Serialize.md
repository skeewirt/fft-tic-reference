# SaveDarlavon_Serialize

- **Address:** `0x1400BFC68`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveDarlavon_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveUnitJobInfo_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the Darlavon opened flag and an arrival flag.

## Behavior

- V: builds 2 descriptors and runs FieldSchema_Run over them.
- V: field names: `darlavon_opened_flag`, `is_arrival`.
- V: used by SaveUnitJobInfo_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveUnitJobInfo_Serialize](SaveUnitJobInfo_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
