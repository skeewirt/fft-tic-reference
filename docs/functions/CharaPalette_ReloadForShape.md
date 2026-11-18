# CharaPalette_ReloadForShape

- **Address:** `0x14026FB28`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int CharaPalette_ReloadForShape(void)`
- **Callers:** BattleLoad_StepFresh, sub_14030476C, sub_1401F2E4C, sub_14023A0B4
- **Callees:** GameData_ReadSectors, sub_14026E194, sub_14026E2C0, sub_14026E484, SceneUnit_BuildFromQueueEntry, sub_1402F3888, sub_1402F3A04

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step function that walks the look queue and, for each entry, loads its frame file, its sequence file and its classic sprite file, then builds the scene unit; returns 0 when the queue is done, 1 or 2 while work remains.

## Behavior

- V: the state is a pass (0 frame file, 1 sequence file, 2 sprite file and unit build), a step inside the pass and the entry index, all in the block at 0x140CE3240.
- V: pass 0 reads attribute byte 0 of the entry's sprite (table 0x673300 + 4 * sprite); when it is 5 or more and differs from the last one loaded it reads the file named by the row of that value in the table at 0x140785130 or its twin at 0x140785180.
- V: pass 1 does the same with attribute byte 1 and the tables at 0x140784610 and 0x1407845B0.
- V: pass 2 replaces a sprite above 170 by 1, scans the 15 look pool records for a byte +1 equal to it (a hit skips the file read), otherwise reads the classic file named by the table at 0x140784690 (language flag 0: 0x140784BE0) through GameData_ReadSectors.
- V: in step 2 of pass 2 it calls SceneUnit_BuildFromQueueEntry with the queue entry's fields and the file buffer, and then sub_14026E194 three times.
- V: after the sprite pass of an entry it moves to the next entry; it returns 0 when the entry index reaches the queue count.
- V: its step machine (0x140CE3240: pass, step, entry index; buffer 0x140CE3250) returns 0 once the entry index reaches g_LookQueueCount, 1 or 2 otherwise; its files are read with GameData_ReadSectors, which is synchronous (MemFile_Read; it clears the pending flag the high dword of qword_141856AB0 itself). The mid-battle join runs it once per frame until 0.
- V: load step 2 stores a queue word above 170 back as 1 (stock clamp) and tests the word against byte +1 of all 15 look pool records, claimed or not (the loop over 0x140D005A1 in steps of 0x32D6), reading no classic file when one matches; the scene unit is then built from whatever data the record its build uses holds. It passes the load queue entry's word +6 to SceneUnit_BuildFromQueueEntry as the sprite, so a scene unit's shape is the queue word.

## State touched

- Calls: [GameData_ReadSectors](GameData_ReadSectors.md), [SceneUnit_BuildFromQueueEntry](SceneUnit_BuildFromQueueEntry.md)

## Referenced by

- Called by: [BattleLoad_StepFresh](BattleLoad_StepFresh.md), [Battle_JoinUnitAndLoad](Battle_JoinUnitAndLoad.md), [sub_14030476C](sub_14030476C.md)
- Observed behaviours: [HdSheetAndClassicPaletteLoading](../behaviors/HdSheetAndClassicPaletteLoading.md), [LookPoolOfFifteenIsWiredIntoFixedSlots](../behaviors/LookPoolOfFifteenIsWiredIntoFixedSlots.md), [LookSlotsAlreadyInTheGame](../behaviors/LookSlotsAlreadyInTheGame.md), [MidBattleJoinLoadsLooks](../behaviors/MidBattleJoinLoadsLooks.md), [PoolRecordKeepsItsSpriteAcrossTheReset](../behaviors/PoolRecordKeepsItsSpriteAcrossTheReset.md), [SceneUnitShapeIsTheQueueWord](../behaviors/SceneUnitShapeIsTheQueueWord.md), [SpriteTablesCanLiveInBlocksOf1300Rows](../behaviors/SpriteTablesCanLiveInBlocksOf1300Rows.md)
- Reads tables: [SpriteClassicFilesByShape](../tables/SpriteClassicFilesByShape.md), [SpriteClassicFilesByShapeB](../tables/SpriteClassicFilesByShapeB.md), [SpriteLookAttributes](../tables/SpriteLookAttributes.md)

## Notes

The file tables are reached by lea of their addresses in the pass-2 branch (IDA: 0x14026FD5C, 0x14026FD69), the others the same way in passes 0 and 1. The sprite number is read as a 16-bit word from the queue entry, so the look pool and the file tables see the global number. The name was already in the IDB with the comment 'unstudied'; this sheet replaces it.

The pass-2 clamp loads 0xAA into ecx at 0x14026FD05 for a signed word compare (jump if less or equal): 170 itself passes and reads row 170, past the stock tables (the next table's row 0). LookQueue_Add already replaces 170 and up by 1, so in stock the clamp never fires.

The pass-2 hit test reads byte +1 of every pool record, claimed or not, so a sprite number names the same graphics for as long as any record holds it (the battle setup sub_140210AF0 clears +1 of all records at its start; LookPool_ResetForBattleLoad does not).

## Open questions

? the use of the two-value sub-step of pass 0 and 1 (counters at 0x140CE3240).
