# SaveSlot_WriteFromLive

- **Address:** `0x1400C4420`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveSlot_WriteFromLive(int64_t mgr, int slot, int situation)`
- **Callers:** sub_140183C38
- **Callees:** SaveWork_PackFromParty, SceneVar_Read, Str_Format, UIText_Get, sub_1400C3140, sub_140034C64, memmove, memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes one save slot: packs the live state into the work copy and copies it into the 50-slot RAM cache.

## Behavior

- V (decompile): `Src = &g_SaveWorkCurrent; memset(Src, 0xFF, 0x9CE4); SaveWork_PackFromParty(slot); Src[282] = situation; Src[284..285] = SceneVar 39`.
- V: `memmove(g_SaveSlotCache + 40164 * slot, Src, 0x9CE4)` (0x9CE4 = 40164).
- V: when situation == 1 it also queues a `resume_enma%02d_world.sav` entry (battle resume).

## State touched

- Calls: [SaveWork_PackFromParty](SaveWork_PackFromParty.md), [SceneVar_Read](SceneVar_Read.md), [Str_Format](Str_Format.md), [UIText_Get](UIText_Get.md), [sub_1400C3140](sub_1400C3140.md), [sub_140034C64](sub_140034C64.md)

## Referenced by

- Appears in flows: [AutoSaveWrite](../flows/AutoSaveWrite.md)
- Called by: [sub_140183C38](sub_140183C38.md)
- Observed behaviours: [BattleForkDeterminism](../behaviors/BattleForkDeterminism.md), [EventIdRowOfTheCurrentEventIsReadWithoutANullTestWhenSkipping](../behaviors/EventIdRowOfTheCurrentEventIsReadWithoutANullTestWhenSkipping.md)
- Reads file formats: [BattleResumeImage](../formats/BattleResumeImage.md)

## Notes

The cache is written to the file by SaveSlots_StoreToFile.

## Open questions

None recorded.
