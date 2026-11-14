# Input_UpdateActionRow

- **Address:** `0x1400EFF18`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `void Input_UpdateActionRow(InputRows *rows, uint32 action)`
- **Callers:** sub_1400EFB50 (all 256 rows each frame, row 57 first)
- **Callees:** UITable_GetRow, sub_1400F02BC, sub_1400F06AC, sub_1400F0870

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame refresh of one action row: reads the pad button and the two keys bound to the action and writes their value, pressed, released, held and repeat bytes.

## Behavior

- V: the row is live only when UIKeyAssign (UI table 25) has a row for the action and the input module's context mask (dword +13720) has the row's context bit: 1 by default, 2 when the table row's byte +42 is set, plus 4 when byte +43 is set. Otherwise the pad binding's state bytes are zeroed.
- V: pad binding (first 16 bytes): sub_1400F02BC reads the bound button (binding dword at +0) and returns its value, a 'pressed' flag taken from the pad's newly-pressed mask and a 'held' flag from its down mask; the row stores value at +8 and +9, pressed at +10, held at +12 and +13, released at +11 (the previous value was non-zero and it is no longer held) and the repeat flag at +14; the press time (the UI clock in ms) goes to +4 when the value rises from 0.
- V: binding flag 0x10000 (bit 16, read with a bit test, so the constant itself is not in the body) turns the binding into a long press: pressed / held are reported only after 1000 ms down; flag 0x20000 (bit 17, same) into a short press reported on release within 1000 ms.
- V: the two key bindings (at +16 and +32) are read by sub_1400F06AC and stored the same way (value +8 / +9, pressed +10, released +11, held +12, repeat +14).
- V: pad button ids in sub_1400F02BC: 9..12 the four d-pad bits, 13..16 bits 4..7, 17 bit 8, 18 bit 11, 21 bit 10, 22 bit 13, 23 bit 15, 24 bit 14 of the pad mask, 19 / 20 the two triggers, 1..8 stick directions; id 30 is bit 4 reported only while action 89 is held; id 45 a two-button chord.
- V: the pad mask is built by sub_140020350 from the XInput buttons: bits 0..3 d-pad, bit 4 Y, 5 A, 6 X, 7 B, 8 LB, 11 RB, 10 left stick, 13 right stick, 14 Back, 15 Start, 9 / 12 the triggers past a threshold. So button id 18 is RB, 13 is Y, 15 is X.

## State touched

- Calls: [UITable_GetRow](UITable_GetRow.md)
- Writes: [InputActionRow.value](../structs/InputActionRow.md#value), [InputActionRow.pressed](../structs/InputActionRow.md#pressed), [InputActionRow.released](../structs/InputActionRow.md#released), [InputActionRow.held](../structs/InputActionRow.md#held), [InputActionRow.repeat](../structs/InputActionRow.md#repeat), [InputActionRow.press_time](../structs/InputActionRow.md#press_time)

## Notes

Key codes below 160 index a per-key state array (Windows virtual-key numbers: 17 Ctrl, 16 Shift, 53 the 5 key); 160..164 are the five mouse buttons (164 = the fifth).

## Open questions

? Which UIKeyAssign pad column (three layouts) the binding builder copies for the current button layout.
