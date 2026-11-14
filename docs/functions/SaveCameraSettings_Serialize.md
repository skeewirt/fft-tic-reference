# SaveCameraSettings_Serialize

- **Address:** `0x1400C23B8`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveCameraSettings_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveBattleCamera_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes two camera settings (`m_zoom` and `m_fukan`).

## Behavior

- V: builds 2 descriptors and runs FieldSchema_Run over them.
- V: field names: `m_zoom`, `m_fukan`.
- V: used by SaveBattleCamera_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveBattleCamera_Serialize](SaveBattleCamera_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
