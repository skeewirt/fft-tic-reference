# ConfigSettings_Serialize

- **Address:** `0x1400C4C78`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void ConfigSettings_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** ConfigFile_Serialize
- **Callees:** FieldSchema_Run, ConfigVolume_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the game's option settings: resolution, screen mode and brightness, depth of field, speaker and subtitle visibility, text and voice language, sound, camera reversal, cursor behaviour, auto equip, button and key assignment, v-sync, event auto-advance and more.

## Behavior

- V: builds 26 descriptors and runs FieldSchema_Run over them.
- V: field names: `resolution`, `screenMode`, `screenBrightness`, `enableDof`, `visibleSpeaker`, `textLang`, `voiceLang`, `visibleSituationSubtitles`, `sound`, `reverseCameraHorizontal`, `reverseCameraVertical`, `enableDeactivePlay`, `cursorMoveType`, `enableCursorClip`, `enableAutoBestEquip`, `buttonAssign`, `buttonType`, `keyAssign`, `keyCustomize`, `enableRemoveMonsterForce`, `forwardEnabledType`, `enableVSync`, `platform`, `enableEventKeepAuto`, `enableSaveMenuCursor`, `enableEveryBattleCastMessage`.
- V: its nested records use ConfigVolume_Serialize.
- V: used by ConfigFile_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [ConfigVolume_Serialize](ConfigVolume_Serialize.md)

## Referenced by

- Called by: [ConfigFile_Serialize](ConfigFile_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
