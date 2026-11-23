# MenuCtl_Entry52

- **Address:** `0x140346428`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MenuCtl_Entry52(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 52)
- **Callees:** sub_1402841D0, sub_1402B52E4, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Yes or no step with a result (table index 52): confirm applies the number held in word 0x140D498D4 when it is below 512.

## Behavior

- V: while record dword 0 is 0 (or the message window is busy) it reads input: cancel sets dword 0 to -1, confirm sets it to 1, both start the close.
- V: after the close it pops; on a confirm with the held number below 512 it calls sub_1402841D0(number), sub_1402B52E4 and sets the redraw mask; then it calls WorldMenu_RunTopOpenHook.
- I: it is the screen opened by sub_14034637C, which pushes kind 52; ClassicMenu_HubStep calls that function.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md)

## Open questions

None recorded.
