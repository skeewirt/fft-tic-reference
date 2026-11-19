# InputRows_Rebuild

- **Address:** `0x1400F1720`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `void InputRows_Rebuild(void *inputModule)`
- **Callers:** UI_FrameUpdate
- **Callees:** sub_1403DB748, sub_1403DAF0C, sub_1400F1A84, sub_1400F1B58, sub_1400F2344

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds the input module's action bindings after a change of the pad / keyboard glyph set or the button layout.

## Behavior

- V: sets the pad layout number at input module +13724 from a flag byte of g_CharaRenderMgr (+13493 != 0), swaps the keyboard glyph set when the byte at +13725 changed, then calls InputRows_ApplyPadLayout with that layout, InputRows_ApplyKeyBindings and (unless input module +2608 is 14) sub_1400F2344.
- V: sets the bytes at +13727 and +13730 to 1.
- V: because the layout number is a truth value, only pad layouts 0 and 1 are ever selected; the layout 2 columns of UIKeyAssign (pad_layout_2 and pad_long_press_2) are dead in the stock code.

## State touched

- Calls: [InputRows_ApplyPadLayout](InputRows_ApplyPadLayout.md), [InputRows_ApplyKeyBindings](InputRows_ApplyKeyBindings.md)
- Reads: [g_InputModule](../globals/g_InputModule.md)
- Writes: [InputModule.pad_layout](../structs/InputModule.md#pad_layout)

## Referenced by

- Appears in flows: [InputBindingBuild](../flows/InputBindingBuild.md)

## Notes

Name is ours.

## Open questions

? what g_CharaRenderMgr +13493 is: no instruction writes it with that displacement (it is read here and by sub_1400EC678).
