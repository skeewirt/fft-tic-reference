# SaveMenuNewA_Serialize

- **Address:** `0x1400BFEC8`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveMenuNewA_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWorldMap_Serialize
- **Callees:** FieldSchema_Run, SaveIsNew_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes one menu's new-entry marker (`menu_new`).

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `menu_new`.
- V: its nested records use SaveIsNew_Serialize.
- V: used by SaveWorldMap_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveIsNew_Serialize](SaveIsNew_Serialize.md)

## Referenced by

- Called by: [SaveWorldMap_Serialize](SaveWorldMap_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
