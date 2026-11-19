# InputRows_ApplyPadLayout

- **Address:** `0x1400F1A84`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `void InputRows_ApplyPadLayout(void *inputModule, int layout)`
- **Callers:** sub_1400F1720 (InputRows_Rebuild)
- **Callees:** UITable_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies one of the three pad-button columns of the key-assignment table into the pad binding of every action row.

## Behavior

- V: stores the layout number (0..2) at input module +13724.
- V: for each UIKeyAssign row 1..255 it clears the 16-byte pad binding at input module +1360 + 48 * row, then sets its first dword to the row's pad_layout_0 (+4), pad_layout_1 (+8) or pad_layout_2 (+0xC) column for layout 0, 1 or 2, with flag 0x10000 added when the matching pad_long_press_0 / _1 / _2 byte (+0x20 / +0x21 / +0x22) is set.
- V: sets the input module's 'bindings changed' byte (+13672) to 1.
- V: this answers the open question of Input_UpdateActionRow: the pad column is chosen by the layout argument; the only caller passes 0 or 1 (see InputRows_Rebuild), so layout 2 is read here but never selected.

## State touched

- Calls: [UITable_GetRow](UITable_GetRow.md)
- Reads: [g_InputModule](../globals/g_InputModule.md)
- Writes: [InputActionRow.binding](../structs/InputActionRow.md#binding), [InputModule.pad_layout](../structs/InputModule.md#pad_layout), [InputModule.bindings_changed](../structs/InputModule.md#bindings_changed)

## Referenced by

- Appears in flows: [InputBindingBuild](../flows/InputBindingBuild.md)
- Called by: [InputRows_Rebuild](InputRows_Rebuild.md)
- Observed behaviours: [KeyLongPress](../behaviors/KeyLongPress.md)

## Notes

Name is ours. Binding flag 0x10000 on a pad binding is the long press tested by Input_UpdateActionRow.

## Open questions

? what the layout argument stands for beyond the byte of g_CharaRenderMgr that InputRows_Rebuild passes (the Enhanced-mode set being layout 1 is I, from the fast-forward rows existing only there).
