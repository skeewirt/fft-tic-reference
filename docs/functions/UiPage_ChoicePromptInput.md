# UiPage_ChoicePromptInput

- **Address:** `0x14036FB14`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char __fastcall UiPage_ChoicePromptInput(int *page)`
- **Callers:** the page dispatcher through tbl_UiScreenInputSteps (0x140681400, index 15; the table is read by the dispatcher ClassicMenu_RunScreenStack, not by this body)
- **Callees:** Input_ActionBit, Input_TestAction, sub_1401D80A8, Input_RepeatDirection, WorldMenu_RunTopOpenHook, sub_14036FCB8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of a two-choice prompt page (entry 15 of tbl_UiScreenInputSteps, the page dispatcher's table at 0x140681400): moves a two-position cursor, and on confirm or cancel pops the page's records and either runs a follow-up or returns to the page below.

## Behavior

- V: `page[1]` is the window record index (a record of 14 dwords in `dword_140D4B9B0`); nothing happens while bit 0x100 of that record's first dword is set.
- V: when `page[5]` is above 0 it is cleared and the action bit of action 27 (cancel) is ORed into the pressed mask `dword_140D4CC18` first.
- V: cancel (action 27, mask 64): plays sound request `sub_1401D80A8(qword_143CD9DD8, 10, 2)`, then pops the page: `dword_140D4CA00 -= 2`, `--dword_140D4C974`, `dword_140D4C978 -= 3`, `--dword_140D8DBA0`, and calls `WorldMenu_RunTopOpenHook`, which runs the handler of the page now on top of the stack (it indexes by `dword_140D8DBA0`).
- V: when `Input_RepeatDirection` (the direction-with-repeat test; its arguments are not visible in the pseudocode, it is called twice) reports a press, `page[2]` is toggled (^= 1), the cursor sprite record `page[0]` gets y = window record dword 7 + 16 * `page[2]` + 14, and sound `(10, 3)` plays.
- V: confirm (action 26, mask 32): plays sound `(10, 1)`. With `page[2] == 0` it pops two pages' worth (`dword_140D4CA00 -= 2`, `--dword_140D4C974`, `dword_140D8DBA0 -= 2`, `dword_140D4C978 -= 3`), stores 0, 0, 1 in qwords 3072..3074 of the block at `off_14078D5D8`, and calls `sub_14036FCB8(page[4])`. With `page[2] != 0` it takes the same path as cancel.
- I: choice 0 is the affirmative one and `page[4]` is the follow-up argument (rests on the confirm path running a follow-up only for choice 0).
- ?: what `sub_14036FCB8` and the three qwords at `off_14078D5D8` + 0x6000 do (not read).

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [sub_1401D80A8](sub_1401D80A8.md), [Input_RepeatDirection](Input_RepeatDirection.md), [WorldMenu_RunTopOpenHook](WorldMenu_RunTopOpenHook.md)

## Notes

V: whole body read. The name is ours. The sound ids (10 with 1, 2, 3) are the constants the pseudocode shows.

## Open questions

?: which page uses this step and what the prompt asks.
