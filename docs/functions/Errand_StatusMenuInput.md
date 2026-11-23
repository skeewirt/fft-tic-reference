# Errand_StatusMenuInput

- **Address:** `0x140377530`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t Errand_StatusMenuInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 37; built by sub_140377118)
- **Callees:** MenuCtl_ListCursorStep, sub_140378C74, HelpMessage_Open

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of a two-row menu (table index 37): the first row opens one list and the second row opens another (kind 41, the errand finish list).

## Behavior

- V: it first copies the three globals at 0x141856700 to 08 like index 28.
- V: the help action opens HelpMessage_Open(4186 + row kind); cancel pops, clears 0x140D49668 and re-opens the screen below; confirm stores the row in 0x140D49668 and runs a builder: row kind 0 a list builder (kind 38, I), row kind 1 sub_140378C74 (pushes kind 41).
- V: otherwise it moves the cursor with MenuCtl_ListCursorStep (the row cursor is 16 pixels a row from -26).
- I: the errand name rests on the kinds it leads to (40 reads g_ErrandActive, 42 reads g_ErrandFinishDay).

## State touched

- Calls: [MenuCtl_ListCursorStep](MenuCtl_ListCursorStep.md), [HelpMessage_Open](HelpMessage_Open.md)

## Open questions

None recorded.
