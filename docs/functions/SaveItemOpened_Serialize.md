# SaveItemOpened_Serialize

- **Address:** `0x1400BFB98`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveItemOpened_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveGameFlow_Serialize
- **Callees:** FieldSchema_Run, SaveOpenedFlag_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes an item entry that wraps an exists/opened flag pair.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `item`.
- V: its nested records use SaveOpenedFlag_Serialize.
- V: used by SaveGameFlow_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveOpenedFlag_Serialize](SaveOpenedFlag_Serialize.md)

## Referenced by

- Called by: [SaveGameFlow_Serialize](SaveGameFlow_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
