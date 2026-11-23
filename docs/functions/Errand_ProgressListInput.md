# Errand_ProgressListInput

- **Address:** `0x140377D28`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t Errand_ProgressListInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 38)
- **Callees:** sub_140377E9C, MenuCtl_ListCursorStep, HelpMessage_Open

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of a list of entries (table index 38): confirm opens the next list through sub_140377E9C (kind 39).

## Behavior

- V: the help action opens HelpMessage_Open(4186); cancel clears 0x140D49670, lowers the window counters (4, 1 and 5), pops and re-opens the screen below.
- V: confirm stores the row in 0x140D49670, lowers the counters, pops and calls sub_140377E9C with the row kind (record dword 13 + row), which pushes kind 39.
- V: otherwise the row cursor moves (MenuCtl_ListCursorStep).
- I: the errand name rests on the kinds it leads to (39, then 40 with g_ErrandActive).

## State touched

- Calls: [MenuCtl_ListCursorStep](MenuCtl_ListCursorStep.md), [HelpMessage_Open](HelpMessage_Open.md)

## Open questions

None recorded.
