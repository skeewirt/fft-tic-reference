# SaveUwasaMouke_Serialize

- **Address:** `0x1400C0270`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveUwasaMouke_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWorldMap_Serialize
- **Callees:** FieldSchema_Run, SaveMenuNewB_Serialize, SaveMenuNewC_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the rumor and Mouke menu records (`uwasa` and `mouke`).

## Behavior

- V: builds 2 descriptors and runs FieldSchema_Run over them.
- V: field names: `uwasa`, `mouke`.
- V: its nested records use SaveMenuNewB_Serialize, SaveMenuNewC_Serialize.
- V: used by SaveWorldMap_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveMenuNewB_Serialize](SaveMenuNewB_Serialize.md), [SaveMenuNewC_Serialize](SaveMenuNewC_Serialize.md)

## Referenced by

- Called by: [SaveWorldMap_Serialize](SaveWorldMap_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
