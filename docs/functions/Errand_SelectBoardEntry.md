# Errand_SelectBoardEntry

- **Address:** `0x1402ED7E0`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `int64_t Errand_SelectBoardEntry(int errand)`
- **Callers:** Errand_BoardInput
- **Callees:** sub_1402D541C, Errand_LoadRecord, WorldMenu_AllocWindowRecord, sub_140379CCC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the detail of a board errand: the tavern keeper's line, the record, and the legacy message window.

## Behavior

- V: picks a chance from g_ErrandDelay[errand] (10 with neither of the top two bits, 20 with bit 0x40, 40 for a negative byte) and rolls the random generator: under the chance the keeper says message 47116 with 0xD000 + errand as its argument, else message 0xB879 + errand.
- V: loads the record (Errand_LoadRecord) and opens a message window with message 0x8800 + errand (sub_140379CCC).

## State touched

- Calls: [Errand_LoadRecord](Errand_LoadRecord.md), [WorldMenu_AllocWindowRecord](WorldMenu_AllocWindowRecord.md)
- Reads: [g_ErrandDelay](../globals/g_ErrandDelay.md)

## Referenced by

- Called by: [Errand_BoardInput](Errand_BoardInput.md)

## Notes

Name is ours (was sub_1402ED7E0).

## Open questions

? which banks hold the per-errand messages 0xB879 + id and 0x8800 + id and how many entries they have.
