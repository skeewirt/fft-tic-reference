# Battle_RestoreSceneVars

- **Address:** `0x1402CE5C8`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void Battle_RestoreSceneVars(void)`
- **Callers:** sub_140210AF0
- **Callees:** SceneVar_Write, Battle_SnapshotLiveState, sub_140226C2C, sub_1400FF76C, memmove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Puts a saved battle's scene state back from the battle snapshot region: seven scene variables, the live stores, the battle unit table, the look queue and the look pool.

## Behavior

- V: writes scene variables 50, 51, 46, 47, 35, 36 and 39 from the dwords at 0x1408167A8..0x1408167C0 (46, 47, 35 and 36 masked with 0xF) through SceneVar_Write.
- V: calls Battle_SnapshotLiveState(byte_14089BC68, 1), copies 0x2A00 bytes from 0x140898134 to g_PreviewUnitTable (the 21 battle units) and calls sub_140226C2C.
- V: the Battle_SnapshotLiveState(..., 1) call puts the live unit save records (0x7E90 bytes into g_UnitSaveData) and the item stores back from the snapshot; I: for a battle resumed from an autosave this is where the live unit records come from, since Save_ResumeCheckpoint does not run SaveWork_UnpackToLive when the payload part count is not 0 (seen live 2026-11-09: no unpack hook call during a cold battle resume).
- V: copies byte +1 of every battle unit into the 21-byte table at 0x143791D50.
- V: copies the look queue: dword_140897B84 to dword_141853C08, then 520 bytes from 0x140897BB0 to g_LookQueueCount (the count and the 16 entries; four unrolled rounds of 128 bytes and one qword), then five dwords and a 16-byte value of the load state (0x141856700..0x141856930).
- V (2026-11-09): the 16-byte value is g_BattleEntrySource (from 0x140897DB8): the battle key dword the entries and their OverrideEntryData rows are fetched by, and the entry base pointer of the saving process.
- V: copies the 15 look pool records (0x2FA8A bytes) from g_SnapshotLookPool to g_LookPool, then calls sub_1400FF76C when qword_143CD9DE0 is set.
- I: every source lies in the battle snapshot region (g_SaveBattleSnapshot) that sub_1402181EC fills from a resume payload (668,112 bytes), so the pool records come back with the sprite bytes the saved battle had.

## State touched

- Calls: [SceneVar_Write](SceneVar_Write.md), [Battle_SnapshotLiveState](Battle_SnapshotLiveState.md)
- Reads: [g_SnapshotLookPool](../globals/g_SnapshotLookPool.md)
- Writes: [g_LookPool](../globals/g_LookPool.md), [g_LookQueueCount](../globals/g_LookQueueCount.md), [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md), [g_BattleEntrySource](../globals/g_BattleEntrySource.md)

## Referenced by

- Appears in flows: [BattleResumeRestoresTheLooks](../flows/BattleResumeRestoresTheLooks.md)
- Called by: [sub_140210AF0](sub_140210AF0.md)
- Observed behaviours: [EventIdRowOfTheCurrentEventIsReadWithoutANullTestWhenSkipping](../behaviors/EventIdRowOfTheCurrentEventIsReadWithoutANullTestWhenSkipping.md), [LookPoolOfFifteenIsWiredIntoFixedSlots](../behaviors/LookPoolOfFifteenIsWiredIntoFixedSlots.md), [ResumeLoadsTheLookStateTwice](../behaviors/ResumeLoadsTheLookStateTwice.md), [ResumedBattleRestoresUnitRecordsWithoutUnpack](../behaviors/ResumedBattleRestoresUnitRecordsWithoutUnpack.md)

## Notes

Whole function read (2026-11-08), written from scratch; the earlier sheet did not list the queue and pool copies. Structures: LookQueueEntry, LookPoolRecord.

## Open questions

? whether a resumed load consumes the restored queue entries (their unit pointers are absolute addresses of the saving process, and the exe is built with a dynamic base) or queues the units anew.
