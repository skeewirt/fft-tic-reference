# ScenarioSetup_ApplyRecord

- **Address:** `0x1402FB7C8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int ScenarioSetup_ApplyRecord(void)`
- **Callers:** sub_14020E578 (the scene entry; it turns refresh state 2 into 3 before the call, so every scene start rebuilds), sub_1402357C4, EventUnitBlock_RunTask (one event instruction)
- **Callees:** SceneVar_Read, SceneVar_Write, NxdRegistry_Find, NxdTable_GetRowById, NxdTable_GetEntryCount, NxdTable_GetLeafCount3, NxdTable_GetEntryByKeys3, NxdEntry_GetRow, SaveWork_UnpackToLive_Repair, EventChain_Find, sub_140257384, sub_140326080

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

At a scene start, applies the scenario setup record of the scene's event to the scene variables and rebuilds the per-event word table; in the mid-event refresh it only re-reads two scene bytes through the event's link.

## Behavior

- V: when the refresh state word (0x140D408F4) is 2 (set by one event instruction in EventUnitBlock_RunTask and by sub_1402357C4, each while scene variable 508 is 0, right before they call this function), it clears the scene bytes 0x140C6AD7A / 0x140C6AD76, reads g_BattleMapWords[var 39], and when the word is non-zero searches the records for the event number (w & 0xFF) + ((w >> 2) & 0x300) and copies that record's bytes +13 / +14 into them; nothing else is done (the table is not rebuilt).
- V: otherwise: clears scene variables 112..143, sets 509, moves var 39 on to the next event when variable 100 asks for it (with fixed jumps 90 -> 116, 298 -> 328, 740 / 742 -> 678), then rebuilds the words: for every record up to the first whose event number is 0 (bound 887, an immediate loaded into a register that also bounds the next search) it stores byte +18 + (byte +19 << 10), OR byte +20 << 8, at words[the record's event number].
- V: after the loop it writes words 401..404 and 400 as constants (400 and 404 depend on scene variable 510).
- V: then it searches the records for the scene's event (var 39, or the resume copy when the resume flag is 1); no record: variables 48 and 39 are set to 0 and it returns.
- V: with a record it reads the fields into scene variables: map byte +2 -> 51 (event 93 keeps 51), +3 nibbles -> 48 / 35, +4 -> 36, +7 or +15 -> 50, +9 / +11 -> 53 / 54 and their count -> 52, +17 -> 511, the two scene bytes +13 / +14, and collects the scene's characters from the EnhancedBattleEvent rows of the key at +22 (it returns before writing variable 51 when that key has no row, has 16 or more entries, or the list reaches 512 words).
- V: event numbers are read sign-extended from 16 bits in every search.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [SceneVar_Write](SceneVar_Write.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdTable_GetEntryCount](NxdTable_GetEntryCount.md), [NxdTable_GetLeafCount3](NxdTable_GetLeafCount3.md), [NxdTable_GetEntryByKeys3](NxdTable_GetEntryByKeys3.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [SaveWork_UnpackToLive_Repair](SaveWork_UnpackToLive_Repair.md), [EventChain_Find](EventChain_Find.md)
- Reads: [g_UnitSaveData](../globals/g_UnitSaveData.md)

## Referenced by

- Observed behaviours: [PlayerDeploymentAreaTableHasSevenHundredSixtyEightRows](../behaviors/PlayerDeploymentAreaTableHasSevenHundredSixtyEightRows.md), [ScenarioSetupRecordFeedsTheBattleSceneVariables](../behaviors/ScenarioSetupRecordFeedsTheBattleSceneVariables.md), [ScenarioWordLinksRecordsByATenBitKeyAndLivesInTheBattleCapture](../behaviors/ScenarioWordLinksRecordsByATenBitKeyAndLivesInTheBattleCapture.md)

## Notes

Read: the whole decompilation and the three loops in the disassembly; the character list collected from EnhancedBattleEvent only as far as its bounds. An older sheet under the address name described this function as the filler of a save snapshot block; that was wrong.

## Open questions

?: what the flag bits 8, 9 and 12..15 of the word mean to the battle functions that test them; what the scene bytes 0x140C6AD7A / 0x140C6AD76 select.
