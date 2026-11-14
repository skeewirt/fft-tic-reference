# SaveDifficulty_Serialize

- **Address:** `0x1400C1A78`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveDifficulty_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFile_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the difficulty level.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `difficultyLevel`.
- V: used by SaveFile_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
