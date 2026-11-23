# MenuCtl_Entry26

- **Address:** `0x140371B2C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MenuCtl_Entry26(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 26; built by sub_140371984)
- **Callees:** sub_140371CAC, HelpMessage_Open, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of a list (table index 26): confirm opens the page of the entry (sub_140371CAC), the help action opens the list's help.

## Behavior

- V: cancel sets dword 0 to 0 and clears dword 1 of 0x142FF9E74; the help action opens HelpMessage_Open(4127); confirm (list not empty) sets dword 0 to 1; both start the close.
- V: after the close it pops; a choice stores the cursor in 0x140D49640 and calls sub_140371CAC with the entry id from the shared list buffer g_ErrandBoardList (masked with 0x7FF; several list builders fill that buffer, it is not errand data), which pushes kind 27; a cancel re-opens the screen below.

## State touched

- Calls: [HelpMessage_Open](HelpMessage_Open.md), [Input_TestAction](Input_TestAction.md)

## Open questions

None recorded.
