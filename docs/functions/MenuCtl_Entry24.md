# MenuCtl_Entry24

- **Address:** `0x140374304`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MenuCtl_Entry24(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 24; built by sub_1403741C4)
- **Callees:** sub_140374484, HelpMessage_Open, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of a list (table index 24): confirm opens the detail page (kind 25), the help action opens the list's help.

## Behavior

- V: cancel sets record dword 0 to 0 and clears dword 0 of 0x142FF9E74; confirm (list not empty, dword 12 nonzero) sets dword 0 to 1; both start the close.
- V: the help action opens HelpMessage_Open(4184).
- V: after the close it pops; a choice stores the cursor in 0x140D49638 and calls sub_140374484 with the entry id from the shared list buffer g_ErrandBoardList (masked with 0x7FF; several list builders fill that buffer, it is not errand data), which pushes kind 25; a cancel re-opens the screen below.

## State touched

- Calls: [HelpMessage_Open](HelpMessage_Open.md), [Input_TestAction](Input_TestAction.md)

## Open questions

None recorded.
