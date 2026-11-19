# InputModule

- **Kind:** structure
- **Area:** [Input](../areas/input.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The UI input module (g_InputModule): device state, the 256 action rows and the binding settings. Only the fields read for the key-assignment table are listed.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by |
|---|---|---|---|---|---|
| <a id="device_state"></a>`0x8` | device_state | `bytes` | V | A copy of the device state. |  |
| <a id="key_states"></a>`0x240` | key_states | `uint32[]` | V | Key states at +576 + 4 * key code; bit 0 = down. Keys 16, 17 and 18 (Shift, Ctrl, Alt) are read directly at +640, +644 and +648 (InputKey_ReadBinding). |  |
| <a id="action_rows"></a>`0x550` | action_rows | `InputActionRow[256]` | V | The action rows at +1360, 48 bytes each; the row index is the UIKeyAssign key. |  |
| <a id="bindings_changed"></a>`0x3568` | bindings_changed | `uint8` | V | Set to 1 by InputRows_ApplyPadLayout (+13672). | [InputRows_ApplyPadLayout](../functions/InputRows_ApplyPadLayout.md) |
| <a id="input_mode"></a>`0x3580` | input_mode | `uint8` | V | 0 = pad, 1 = keyboard (+13696): InputGlyph_AppendPadButton and the guide bar pick glyphs by it. |  |
| <a id="context_mask"></a>`0x3598` | context_mask | `uint32` | V | Active input contexts (+13720), written once with 0x15 by InputModule_Init (registry InputContext). | [InputModule_Init](../functions/InputModule_Init.md) |
| <a id="pad_layout"></a>`0x359C` | pad_layout | `uint8` | V | Pad layout number (+13724) given to InputRows_ApplyPadLayout: 0 or 1 in practice. | [InputRows_ApplyPadLayout](../functions/InputRows_ApplyPadLayout.md), [InputRows_Rebuild](../functions/InputRows_Rebuild.md) |
| <a id="glyph_set"></a>`0x359D` | glyph_set | `uint8` | V | Byte at +13725: when it changes InputRows_Rebuild swaps the keyboard glyph set. |  |
| <a id="rebuilt_flag_a"></a>`0x359F` | rebuilt_flag_a | `uint8` | V | Set to 1 by InputRows_Rebuild (+13727); its reader was not followed. |  |
| <a id="rebuilt_flag_b"></a>`0x35A2` | rebuilt_flag_b | `uint8` | V | Set to 1 by InputRows_Rebuild (+13730); its reader was not followed. |  |

## Behavior

- V: InputRows_Rebuild is called by UI_FrameUpdate; it rebuilds the pad and key bindings of every row.

## Notes

Offsets in decimal as the code uses them: +576, +640, +1360, +13672, +13696, +13720, +13724, +13725, +13727, +13730. Row layout: struct InputActionRow.

## Open questions

? the other fields.
