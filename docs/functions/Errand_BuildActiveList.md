# Errand_BuildActiveList

- **Address:** `0x140370F38`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `int64_t Errand_BuildActiveList(void)`
- **Callers:** sub_140371790
- **Callees:** sub_140379F3C, sub_140379DF0, Input_ActionBit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the board list with the errands that are away (dispatched and not yet back) for the legacy list window.

## Behavior

- V: for each active slot whose flag byte has no 0x04: the board list entry = errand byte - 0x3000, the word list entry 8 when the slot's flag has 0x02, else 0 (the index is range-checked against 0x80 entries); the slot index goes into the window's row table.
- V: then sets up the list window (sub_140379F3C, sub_140379DF0) with at most 6 visible rows.

## State touched

- Reads: [g_ErrandActive](../globals/g_ErrandActive.md), [g_ErrandActiveCount](../globals/g_ErrandActiveCount.md)
- Writes: [g_ErrandBoardList](../globals/g_ErrandBoardList.md)

## Referenced by

- Called by: [Errand_RunningConfirmInput](Errand_RunningConfirmInput.md)

## Notes

Name is ours (was sub_140370F38).

## Open questions

None recorded.
