# Errand_FinishListInput

- **Address:** `0x140378E10`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char Errand_FinishListInput(_DWORD *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 41; built by sub_140378C74)
- **Callees:** sub_140378FA4, HelpMessage_Open

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of a list (table index 41): confirm opens the entry's page (kind 42).

## Behavior

- V: cancel sets dword 0 to 0 and starts the close; confirm (list not empty) sets it to 1; the help action opens HelpMessage_Open(4187).
- V: after the close it pops; a choice stores the cursor in 0x140D49680 and calls sub_140378FA4 with the entry id from the shared list buffer g_ErrandBoardList (masked with 0x7FF; several list builders fill that buffer, it is not errand data), which pushes kind 42; a cancel marks the window named by the record's dword 12 busy and re-opens the screen below.
- I: the errand name rests on the page it opens (kind 42 reads g_ErrandFinishDay).

## State touched

- Calls: [HelpMessage_Open](HelpMessage_Open.md)

## Open questions

None recorded.
