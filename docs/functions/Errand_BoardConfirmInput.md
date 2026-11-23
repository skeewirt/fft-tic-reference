# Errand_BoardConfirmInput

- **Address:** `0x1402ED9C8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char Errand_BoardConfirmInput(int64_t record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 9)
- **Callees:** Errand_BuildBoard, Input_TestAction, sub_1402D541C, sub_1402EDB48

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Confirm step of an errand window (table index 9): cancel returns to the board, confirm opens the next window (kind 10).

## Behavior

- V: ignored while the window named by record dword 1 is busy (mask 0x100).
- V: cancel (action 0x1B) plays cue 2, lowers the window counters, pops and calls Errand_BuildBoard.
- V: confirm (0x1A) plays cue 1; when the word 0x140D49438 is nonzero it sets the first message cell to 47126 minus one if the word 0x140D4943A is nonzero, otherwise, when the second word is nonzero, it sets the cell to 47127 (else it is unchanged). It stores the sum of the two words in 0x140D49460, prints text id 47119 or 47120 (by whether the sum is nonzero), builds a window (sub_1402EDB48) and pushes kind 10.

## State touched

- Calls: [Errand_BuildBoard](Errand_BuildBoard.md), [Input_TestAction](Input_TestAction.md)

## Open questions

? what the two words at 0x140D49438 and 0x140D4943A count.
