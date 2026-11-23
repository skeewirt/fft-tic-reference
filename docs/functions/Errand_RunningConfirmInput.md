# Errand_RunningConfirmInput

- **Address:** `0x140371790`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char Errand_RunningConfirmInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 19)
- **Callees:** Errand_BuildActiveList, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Two-row confirm for a running errand (table index 19): the first row sets a bit in the active errand's record and prints a notice.

## Behavior

- V: state is record dword 6: 0 asks, nonzero waits for a confirm or cancel to dismiss the notice.
- V: up and down toggle dword 5 and the cursor; confirm with dword 5 equal to 0 prints text id 47134, sets mask 0x2 of the byte at g_ErrandActive + 9 x errand index (record dword 4) and marks three windows busy; confirm with 1 selected only leaves.
- V: leaving lowers the window counters (2, 2 and 4), pops and calls Errand_BuildActiveList.
- ?: what the mask 0x2 in the active record means to the errand code (a recall or an abandon mark are both possible).

## State touched

- Calls: [Errand_BuildActiveList](Errand_BuildActiveList.md), [Input_TestAction](Input_TestAction.md)

## Open questions

None recorded.
