# InputRows_ApplyKeyBindings

- **Address:** `0x1400F1B58`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `void InputRows_ApplyKeyBindings(void *inputModule)`
- **Callers:** sub_1400F1720 (InputRows_Rebuild), sub_1400F2550
- **Callees:** UITable_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the two keyboard bindings of every action row from the key-assignment table: key code plus modifier and long-press flags.

## Behavior

- V: for each UIKeyAssign row 1..255 key binding 1 (input module +1360 + 48 * row + 16) = row key (+0x10) OR flags: 0x100000 when byte +0x2D is set, 0x10000 for key_ctrl (+0x24), 0x20000 for key_alt (+0x25), 0x40000 for key_shift (+0x23), 0x80000 for key_long_press (+0x26).
- V: key binding 2 (+32) = row key_2 (+0x14) with the same flags from +0x2D, +0x28 (key_2_ctrl), +0x29 (key_2_alt), +0x27 (key_2_shift) and +0x2C (key_2_long_press).
- V: the flags are read by InputKey_ReadBinding (modifiers 0x40000 Shift, 0x10000 Ctrl, 0x20000 Alt) and by Input_UpdateActionRow (0x80000 = long press).
- V: no instruction in the image tests binding bit 0x100000 (set from UIKeyAssign +0x2D); its reader was not found.

## State touched

- Calls: [UITable_GetRow](UITable_GetRow.md)
- Reads: [g_InputModule](../globals/g_InputModule.md)
- Writes: [InputActionRow.binding](../structs/InputActionRow.md#binding)

## Referenced by

- Appears in flows: [InputBindingBuild](../flows/InputBindingBuild.md)
- Called by: [InputRows_Rebuild](InputRows_Rebuild.md)
- Observed behaviours: [KeyLongPress](../behaviors/KeyLongPress.md)

## Notes

Name is ours. Rows 1..255 only: row 0 is never built.

## Open questions

? the reader of binding bit 0x100000.
