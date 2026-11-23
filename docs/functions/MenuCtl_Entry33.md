# MenuCtl_Entry33

- **Address:** `0x14037680C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MenuCtl_Entry33(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 33; pushed by MenuCtl_Entry43 (row kind 2))
- **Callees:** sub_1403769CC, HelpMessage_Open, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of a list (table index 33): confirm opens the entry's page (kind 34).

## Behavior

- V: cancel sets dword 0 to 0; confirm (list not empty and not busy) sets dword 0 to 1 and dword 0 of 0x1437A62B0; the help action opens HelpMessage_Open(own record dword 1 + 4096), which is 4237 when index 43 pushed it (it stores 141 there).
- V: after the close it pops; a choice stores the cursor in 0x140D49660 and in dword 2 of 0x1437A62B0 and calls sub_1403769CC with the entry id from the shared list buffer g_ErrandBoardList (masked with 0x7FF; several list builders fill that buffer, it is not errand data), which pushes kind 34; a cancel re-opens the screen below.

## State touched

- Calls: [HelpMessage_Open](HelpMessage_Open.md), [Input_TestAction](Input_TestAction.md)

## Open questions

None recorded.
