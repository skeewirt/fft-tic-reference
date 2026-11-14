# SaveMenuNewC_Serialize

- **Address:** `0x1400C01A0`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveMenuNewC_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveUwasaMouke_Serialize
- **Callees:** FieldSchema_Run, SaveNewFlags_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes a third menu's new-entry flags (`menu_new`).

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `menu_new`.
- V: its nested records use SaveNewFlags_Serialize.
- V: used by SaveUwasaMouke_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveNewFlags_Serialize](SaveNewFlags_Serialize.md)

## Referenced by

- Called by: [SaveUwasaMouke_Serialize](SaveUwasaMouke_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
