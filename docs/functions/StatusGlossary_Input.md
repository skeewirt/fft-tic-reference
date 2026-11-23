# StatusGlossary_Input

- **Address:** `0x14036E360`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int16 StatusGlossary_Input(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 56)
- **Callees:** HelpMessage_Open, ClassicCursorRows_Select, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of a page of rows linked by direction (table index 56): moves between rows by a link table and shows each row's help text.

## Behavior

- V: each row has a 24-byte entry in a per-language table (two tables, chosen by the language); the qword at +8 holds a text base and its bytes +10 to +13 are four neighbour row numbers; a direction press moves the cursor to the neighbour when it differs from the current row and plays cue 3.
- I: the four checks of Input_RepeatDirection() map to the four neighbour bytes in the order +10, +11, +12, +13; which direction each is was not decoded.
- V: confirm opens HelpMessage_Open with the row's text id: the pointer at the entry's +0 is read as a signed 16-bit value v and the row is accepted when (unsigned 16-bit)(v + 1) is above 1, so both -1 and 0 block it; row 11 is always accepted; a null pointer uses the base alone.
- V: the text id is the base plus v; for the base 24576 it is the base plus byte 0x140D4CA13, and plus 164 instead when that byte is 0xA1 and the low nibble of byte 0x140D4CAFE is 8 or more.
- V: cancel lowers the window counters, pops, restores 0x140D49ABC from record dword 3 and calls WorldMenu_RunTopOpenHook.

## State touched

- Calls: [HelpMessage_Open](HelpMessage_Open.md), [ClassicCursorRows_Select](ClassicCursorRows_Select.md), [Input_TestAction](Input_TestAction.md)

## Open questions

None recorded.
