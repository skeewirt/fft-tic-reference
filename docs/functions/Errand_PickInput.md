# Errand_PickInput

- **Address:** `0x14036A190`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char Errand_PickInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 12)
- **Callees:** sub_14036A294, Errand_BuildBoard, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Choice step of an errand window (table index 12): collects a cancel or a pick, then returns to the board or paints the next board.

## Behavior

- V: while the message window object is busy or record dword 0 is 0 it reads input: cancel sets dword 0 to -1 and 0x140D49420 to 1, confirm sets it to 1 and stores the picked number (word at 0x140D498D4) in 0x140D49424; both start the close of the window.
- V: after the close it pops two levels; a pick calls sub_14036A294 (the board painter, which pushes kind 13), a cancel calls Errand_BuildBoard.

## State touched

- Calls: [sub_14036A294](sub_14036A294.md), [Errand_BuildBoard](Errand_BuildBoard.md), [Input_TestAction](Input_TestAction.md)

## Open questions

None recorded.
