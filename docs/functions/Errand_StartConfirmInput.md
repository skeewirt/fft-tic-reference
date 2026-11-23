# Errand_StartConfirmInput

- **Address:** `0x14036A650`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char Errand_StartConfirmInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 13)
- **Callees:** Errand_Start, Errand_BuildBoard, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Two-row confirm of the errand start (table index 13): the first row calls Errand_Start.

## Behavior

- V: up and down toggle record dword 2 and move the cursor 16 pixels; confirm with row 1 selected only leaves, with row 0 selected it calls Errand_Start; cancel only leaves.
- V: leaving lowers the window counters (by 2, 2 and 4), pops, sets 0x140D49420 to 1 and calls Errand_BuildBoard.

## State touched

- Calls: [Errand_Start](Errand_Start.md), [Errand_BuildBoard](Errand_BuildBoard.md), [Input_TestAction](Input_TestAction.md)

## Notes

Pushed by sub_14036A294.

## Open questions

None recorded.
