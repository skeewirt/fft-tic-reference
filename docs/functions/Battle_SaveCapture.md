# Battle_SaveCapture

- **Address:** `0x1402CDBC4`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void Battle_SaveCapture(int mode)`
- **Callers:** sub_140210AF0
- **Callees:** SceneVar_Read, memmove, sub_140302D60, sub_140243A60, sub_1401D46B0, sub_14002630C, sub_140226C2C, sub_14030D740, Battle_SnapshotLiveState, sub_140327004, SaveWork_CopyErrandState, sub_140304BEC, sub_1402CD788, sub_14041FAE0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Captures the battle state into the autosave battle payload: the scene variables, the five memory blocks A..E, the live item and unit state and the item order record.

## Behavior

- V: it stores the mode argument in the save manager field at 0x141D3B9C8+? and reads the scene variables it needs.
- V: the five memory blocks it copies are the event-script buffer at 0x140D3CD50, the second block at 0x140D3F950, the map cell block at 0x140D8DCB0, the nine scene-task slots at 0x14114B150 and the current action block at 0x1418716A0.
- V: the block copies are memmove calls with the sizes 0x2800, 0x6EE, 0x5E8, 0xBB8 and 0x28 bytes respectively.
- V: Battle_SnapshotLiveState captures the item stores and the unit save table under the same call.
- V: SaveWork_CopyErrandState copies the errand and status state into the payload.
- V: sub_140327004 copies the item order record in the capture direction.
- V: the routine writes 127 fields in all and is the only producer of the battle payload.
- I: the sparse copy is a memory capture rather than a field-by-field serialiser, because whole buffers are moved verbatim.
- ?: the mode argument meaning; only its store was seen.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [sub_140243A60](sub_140243A60.md), [Battle_SnapshotLiveState](Battle_SnapshotLiveState.md), [sub_140327004](sub_140327004.md), [SaveWork_CopyErrandState](SaveWork_CopyErrandState.md)
- Reads: [g_CurrentActionBlock](../globals/g_CurrentActionBlock.md)

## Referenced by

- Observed behaviours: [EventIdRowOfTheCurrentEventIsReadWithoutANullTestWhenSkipping](../behaviors/EventIdRowOfTheCurrentEventIsReadWithoutANullTestWhenSkipping.md), [ResumedBattleRestoresUnitRecordsWithoutUnpack](../behaviors/ResumedBattleRestoresUnitRecordsWithoutUnpack.md), [ScenarioWordLinksRecordsByATenBitKeyAndLivesInTheBattleCapture](../behaviors/ScenarioWordLinksRecordsByATenBitKeyAndLivesInTheBattleCapture.md), [StatusLoopsInflictCopyAndBattleTableLifetime](../behaviors/StatusLoopsInflictCopyAndBattleTableLifetime.md), [TheAiHandlesSixteenUnitsOnTheField](../behaviors/TheAiHandlesSixteenUnitsOnTheField.md), [TrackedDateCountersAreCopiedBySixteenByteMovesInFiveSequences](../behaviors/TrackedDateCountersAreCopiedBySixteenByteMovesInFiveSequences.md)

## Notes

Whole function read (2561 bytes). It captures five blocks of fixed sizes.

## Open questions

None recorded.
