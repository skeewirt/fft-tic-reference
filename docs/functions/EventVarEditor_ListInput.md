# EventVarEditor_ListInput

- **Address:** `0x14036DD60`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void EventVarEditor_ListInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 11)
- **Callees:** EventVarEditor_DrawPage, Input_TestAction, EventVar_Read, ClassicMenu_OpenNumberEntry (range 0..9999)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of the event variable editor list (table index 11): moves through the variables and opens the value editor.

## Behavior

- V: up and down move a row cursor (record dword 3, 16 pixels a row) with wrap.
- V: two page actions (0x1E and 0x1D) change the first variable (record dword 2) and redraw the page. In one direction 0x1E subtracts 100 (clamped to 0) and 0x1D subtracts 10 (0 wraps to 1020); in the other 0x1E adds 100 (clamped to 1020) and 0x1D adds 10 (1020 wraps to 0).
- V: confirm reads the variable at first + row, sets the shared number-entry words and pushes kind 48 with that variable number.
- V: cancel lowers the window counters, pops and re-opens the screen below.
- V (seen live): opened on the world map, the screen pushes kind 11 and its input runs (Down moves the row, A pushes the number entry kind 48, B cancels it, B again closes the editor) while nothing is drawn.

## State touched

- Calls: [EventVarEditor_DrawPage](EventVarEditor_DrawPage.md), [Input_TestAction](Input_TestAction.md), [EventVar_Read](EventVar_Read.md), [ClassicMenu_OpenNumberEntry](ClassicMenu_OpenNumberEntry.md)

## Open questions

None recorded.
