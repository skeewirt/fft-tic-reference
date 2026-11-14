# SaveOpenedFlag_Serialize

- **Address:** `0x1400BFA84`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveOpenedFlag_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveItemOpened_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes an exists/opened flag pair.

## Behavior

- V: builds 2 descriptors and runs FieldSchema_Run over them.
- V: field names: `is_exist`, `is_opened`.
- V: used by SaveItemOpened_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveItemOpened_Serialize](SaveItemOpened_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
