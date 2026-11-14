# SaveUnitJobInfo_Serialize

- **Address:** `0x1400C14CC`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveUnitJobInfo_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFile_Serialize
- **Callees:** FieldSchema_Run, SaveDarlavon_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the unit job and guide record: the unit job, the info-guide flags and the skin colour offset.

## Behavior

- V: builds 3 descriptors and runs FieldSchema_Run over them.
- V: field names: `unit_job`, `info_guide`, `color_skin_offset`.
- V: its nested records use SaveDarlavon_Serialize.
- V: used by SaveFile_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveDarlavon_Serialize](SaveDarlavon_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
