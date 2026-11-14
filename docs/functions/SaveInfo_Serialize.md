# SaveInfo_Serialize

- **Address:** `0x1400B83D8`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveInfo_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFile_Serialize
- **Callees:** FieldSchema_Run, SaveSummary_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the `info` section: a header, a checksum, the play time, and the slot summary.

## Behavior

- V: builds 3 descriptors and runs FieldSchema_Run over them.
- V: field names: `header`, `chk_sum`, `time`.
- V: its nested records use SaveSummary_Serialize.
- V: used by SaveFile_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveSummary_Serialize](SaveSummary_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
