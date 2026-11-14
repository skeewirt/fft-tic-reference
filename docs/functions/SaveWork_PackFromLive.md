# SaveWork_PackFromLive

- **Address:** `0x140218F78`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveWork_PackFromLive(int timestamp, uint8_t job, uint8_t level)`
- **Callers:** SaveWork_PackFromParty (tail jump at 0x14021B0E3)
- **Callees:** PreviewUnit_BuildRecord, SceneVar_Read, sub_140218C50, sub_1402CD168

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the save work copy (`g_SaveWorkCurrent`, 40164 bytes) from the live game state: slot summary, four preview sprite records, the 54 live 600-byte unit records and the other tables.

## Behavior

- V (J9, decompile): writes the summary at slot +256..+290: job (+274, from the argument), level (+275), month/day, location (+278, SceneVar 49), version, language, game-cleared, difficulty, new-game-plus, main progress, play time.
- V: builds four 32-byte sprite records (+292..+419) via PreviewUnit_BuildRecord: the first unit whose marker byte is 1..3, then present units in slots 50..53.
- V: copies the 54 unit records of 600 bytes to work +1304 + 600*n and the 160-byte `g_UnitJobFlags` block (146 bytes used) to +38604.
- V (J9): chk_sum (+420..+435) and the pad byte +287 are not written (0xFF in the owner's saves).

## State touched

- Calls: [PreviewUnit_BuildRecord](PreviewUnit_BuildRecord.md), [SceneVar_Read](SceneVar_Read.md), [sub_1402CD168](sub_1402CD168.md)
- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Called by: [SaveWork_PackFromParty](SaveWork_PackFromParty.md)
- Observed behaviours: [BattleForkDeterminism](../behaviors/BattleForkDeterminism.md), [CheckpointCopyHoldsTheLiveUnitRecords](../behaviors/CheckpointCopyHoldsTheLiveUnitRecords.md)

## Notes

The only caller is the tail jump from SaveWork_PackFromParty, which covers all 5 pack paths; a post-pack hook there writes the class fallback (J9 H1). J7 proposed this name.

## Open questions

None recorded.
