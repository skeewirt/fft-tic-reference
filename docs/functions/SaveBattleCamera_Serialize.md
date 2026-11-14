# SaveBattleCamera_Serialize

- **Address:** `0x1400C24CC`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveBattleCamera_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFile_Serialize
- **Callees:** FieldSchema_Run, SaveCameraSettings_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the battle camera reserve record.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `m_battle_camera_reserve`.
- V: its nested records use SaveCameraSettings_Serialize.
- V: used by SaveFile_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveCameraSettings_Serialize](SaveCameraSettings_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
