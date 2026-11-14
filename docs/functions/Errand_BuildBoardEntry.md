# Errand_BuildBoardEntry

- **Address:** `0x1402EE0F0`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `bool Errand_BuildBoardEntry(BoardEntry *entry, int errand)`
- **Callers:** Errand_BuildBoard, Errand_Recall
- **Callees:** EventVar_Read, Errand_IsAvailable

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decides whether an errand that is not dispatched goes on the tavern board and fills its board entry.

## Behavior

- V: sets entry +0x144 to -1, then reads the errand state nibble EventVar_Read(864 + errand): with 0x02 or 0x04 set it returns 0 (dispatched or already completed).
- V: returns 0 when the low 6 bits of the errand delay byte g_ErrandDelay[errand] are not 0 (days left before it is offered again).
- V: returns 0 unless Errand_IsAvailable(errand, dword_140D493E8 + 1) (the town the party is in, plus 1).
- V: fills the entry: +0x13C = bit 0x08 of the nibble, +0x150 / +0x154 = words 6 and 7 of g_ErrandRow (the fewest and most days), three unit slots of 0x68 bytes from +0x60 set to -1, +0x138 = the errand, +0x148 = the first new flag g_ErrandNewFlags[2 * errand] when the errand byte is below 0x60 and not negative (else 0); returns 1.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [Errand_IsAvailable](Errand_IsAvailable.md)
- Reads: [g_ErrandDelay](../globals/g_ErrandDelay.md), [g_ErrandNewFlags](../globals/g_ErrandNewFlags.md)

## Referenced by

- Called by: [Errand_BuildBoard](Errand_BuildBoard.md), [Errand_Recall](Errand_Recall.md)
- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md)

## Notes

Named before this sheet. The new-flag read indexes with the low byte of the errand (an id of 0x100 and up would pass the test). The caller has loaded g_ErrandRow for the errand before.

## Open questions

? what bit 0x08 of the nibble means on the board (Errand_Start sets it with 0x02).
