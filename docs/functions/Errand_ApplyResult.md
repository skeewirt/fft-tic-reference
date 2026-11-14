# Errand_ApplyResult

- **Address:** `0x140370054`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `int64_t Errand_ApplyResult(ResultEntry *entry)`
- **Callers:** Errand_Finish
- **Callees:** Unit_BuildJobUnlockMask, EventVar_Read, EventVar_Write, DateBits_Store9, `sub_140278D5C`, Job_IdToIndex

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies a finished errand's result to the save: event flags, gil, loot, JP and the active list.

## Behavior

- V: clears 0x02 (dispatched) of the errand's state nibble (event variable 864 + the slot's errand byte) and sets 0x04 (succeeded) when g_ErrandGrade is 0.
- V: adds the pending gil to variable 44, capped at 99,999,999, and refreshes the displayed gil.
- V: for loot kind 1 or 2 sets the won treasure's variable (801 + index or 848 + index) to 1.
- V: for each party unit it clears the busy byte; if its JP gain is non-negative, the unit exists, its flag bit 0x20 is clear and its job is not 161 or 164, it adds the gain to both the unit's current and total JP of its job (16-bit values at +128 and +174, capped at 9999), recomputes the job level nibble and rebuilds the unlock mask into +47..49 with Unit_BuildJobUnlockMask.
- V: on success stores the date (event variables 46 / 47) as the errand's 9 bits of g_ErrandFinishDay (DateBits_Store9); with a treasure find also the treasure's date (0x1411A71E8 / 0x1411A7260).
- V: writes the errand's delay byte g_ErrandDelay[errand] = 0x60 when g_ErrandGrade is 1, 0x90 when it is 2.
- V: removes the active record by shifting later 9-byte records down and decrementing the active count.
- V: the JP / level index is Job_IdToIndex of the save record's job byte (+2, the record in rsi).

## State touched

- Calls: [Unit_BuildJobUnlockMask](Unit_BuildJobUnlockMask.md), [EventVar_Read](EventVar_Read.md), [EventVar_Write](EventVar_Write.md), [DateBits_Store9](DateBits_Store9.md), [Job_IdToIndex](Job_IdToIndex.md)

## Referenced by

- Called by: [Errand_Finish](Errand_Finish.md)
- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)

## Notes

This is where a unit's JP in each job is increased by errands (16-bit arrays at +128 and +174).

## Open questions

None recorded.
