# Errand_ConfirmDialogInput

- **Address:** `0x1402EDCC0`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `char __fastcall Errand_ConfirmDialogInput(int *control)`
- **Callers:** Table entry only (0x140681400 index 10); ClassicMenu_RunScreenStack reaches it through the table
- **Callees:** Input_TestAction, Input_RepeatDirection, sub_1402D541C, sub_1401D80A8, sub_1402EE37C, EventVar_Read, Errand_BuildBoard, sub_14036CB1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame input handler of a two-choice confirmation dialog in the errand screens: moves the choice, then on confirm tests the errand list with `sub_1402EE37C` (I: that an errand is free) and that the player has enough gil.

## Behavior

- V: it is entry 10 of the classic menu input table at 0x140681400 (registry ClassicMenuControllers; Tavern_TopInput is entry 5, Errand_BoardInput entry 7).
- V: nothing happens while bit 0x100 of the dialog's window record flags is set (the window record index is `control[1]`).
- V: state `control[3]` 3 and 1 wait for a confirm or cancel action; state 1 first plays message 47328 and moves to 3; state 3 pops two control levels and rebuilds the board with `Errand_BuildBoard`.
- V: in state 0 a direction repeat (`Input_RepeatDirection`) flips the choice in `control[2]`, moves the cursor record by 16 per choice and plays sound 3.
- V: confirm with choice 0 scans indexes 0..0x31 with `sub_1402EE37C`; none found: message 47138, state 1; otherwise when gil (`EventVar_Read(44)`) is below `dword_140D49460`, message 47121 and state 3; otherwise it pops two levels and calls `sub_14036CB1C`.
- V: cancel, or confirm on choice 1, plays sound 2 or 1, pops two levels and rebuilds the board.
- I: the dialog is the errand dispatch confirmation (rests on `Errand_BuildBoard`, the gil test and the message ids); `dword_140D49460` is the fee.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [Input_RepeatDirection](Input_RepeatDirection.md), [sub_1401D80A8](sub_1401D80A8.md), [EventVar_Read](EventVar_Read.md), [Errand_BuildBoard](Errand_BuildBoard.md)

## Notes

Whole body read; action ids 0x1A and 0x1B are confirm and cancel by use. The scan bound in the code is 0x32 (50), so the last index is 0x31; the table address 0x140681400 is the pointer table listing this function at index 10 (reached by data reference, not in the body).

## Open questions

What `sub_1402EE37C` tests for each index.
