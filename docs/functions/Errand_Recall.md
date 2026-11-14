# Errand_Recall

- **Address:** `0x1402EE1C8`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `int64_t Errand_Recall(void)`
- **Callers:** Errand_BoardInput
- **Callees:** sub_1401A1D28, EventVar_Read, EventVar_Write, sub_14019DC5C, Errand_LoadRecord, Errand_BuildBoardEntry, sub_1401A1AE4, sub_1402D541C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Calls off the dispatched errand selected on the board: its units come back and the errand is offered again.

## Behavior

- V: takes the selected board entry (sub_1401A1D28) and its errand (+0x138); does nothing for a negative one.
- V: finds the active slot whose errand byte equals it, clears the away byte (+0x11E of the g_UnitSaveData record of each of the slot's units below 0x36), moves the later slots down by 9 bytes and lowers g_ErrandActiveCount.
- V: clears bit 0x02 of the errand state nibble (EventVar_Write(864 + errand, value & 0xFFFD)), reloads the record (Errand_LoadRecord), rebuilds the entry with Errand_BuildBoardEntry and hands it to the board widget (sub_1401A1AE4), then sets the screen state (sub_1402D541C).

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [EventVar_Write](EventVar_Write.md), [Errand_LoadRecord](Errand_LoadRecord.md), [Errand_BuildBoardEntry](Errand_BuildBoardEntry.md)
- Reads: [g_ErrandActive](../globals/g_ErrandActive.md), [g_ErrandActiveCount](../globals/g_ErrandActiveCount.md)
- Writes: [g_ErrandActive](../globals/g_ErrandActive.md), [g_ErrandActiveCount](../globals/g_ErrandActiveCount.md)

## Referenced by

- Called by: [Errand_BoardInput](Errand_BoardInput.md)
- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)

## Notes

Name is ours (was sub_1402EE1C8). Whole function read.

## Open questions

None recorded.
