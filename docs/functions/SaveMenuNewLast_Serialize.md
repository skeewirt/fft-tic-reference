# SaveMenuNewLast_Serialize

- **Address:** `0x1400BFF98`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveMenuNewLast_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWorldMap_Serialize
- **Callees:** FieldSchema_Run, SaveNewFlags_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes a menu's new-entry flags and the last selected menu index.

## Behavior

- V: builds 2 descriptors and runs FieldSchema_Run over them.
- V: field names: `menu_new`, `last_menu_index`.
- V: its nested records use SaveNewFlags_Serialize.
- V: used by SaveWorldMap_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveNewFlags_Serialize](SaveNewFlags_Serialize.md)

## Referenced by

- Called by: [SaveWorldMap_Serialize](SaveWorldMap_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
