# ErrandStateIsSpreadOverFiveStores

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Errands](../areas/errands.md)
- **Affects:** [Errand_LoadRecord](../functions/Errand_LoadRecord.md), [Errand_IsAvailable](../functions/Errand_IsAvailable.md), [Errand_IsOffered](../functions/Errand_IsOffered.md), [Errand_BuildBoardEntry](../functions/Errand_BuildBoardEntry.md), [Errand_BuildBoard](../functions/Errand_BuildBoard.md), [Errand_Start](../functions/Errand_Start.md), [Errand_ApplyResult](../functions/Errand_ApplyResult.md), [Errand_Recall](../functions/Errand_Recall.md), [DateBits_Store9](../functions/DateBits_Store9.md), [sub_1402CCEE0](../functions/sub_1402CCEE0.md), [sub_14039DA58](../functions/sub_14039DA58.md), [sub_14033FB84](../functions/sub_14033FB84.md), [g_ErrandDelay](../globals/g_ErrandDelay.md), [g_ErrandFinishDay](../globals/g_ErrandFinishDay.md), [g_ErrandNewFlags](../globals/g_ErrandNewFlags.md), [g_ErrandActive](../globals/g_ErrandActive.md), [g_ErrandBoardList](../globals/g_ErrandBoardList.md), [ErrandActiveSlot](../structs/ErrandActiveSlot.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

An errand is an index 0..95 into five stores: its 23-byte record, a 4-bit state nibble in the event variables (864 + id), a delay byte, 9 bits of finish date and two new flags, plus the eight active slots that name it by a byte. The tavern board walks the 96 indices and lists those available in the current town.

## Behavior

- V: the state nibble: 0x02 dispatched (Errand_Start, cleared by the result and the recall), 0x04 succeeded (Errand_ApplyResult at grade 0; Errand_IsAvailable's prerequisite), 0x08 set by Errand_Start.
- V: the delay byte's low 6 bits are days before the errand is offered again: 0x60 after a grade 1 result, 0x90 after grade 2; one day = min(d, 32) - 1.
- V: g_ErrandFinishDay holds 9 bits per errand (day 5, month 4): 96 x 9 bits are its 108 bytes.
- V: bounds: 96 in the board and town loops, 160 nibbles (864..1023; 1024 and up trap), the slot's errand byte (255), the board entry's 11-bit id, 128 board entries, 8 slots.

## Open questions

? who reads event variables 960..1023.
