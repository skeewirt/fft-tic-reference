# InputBindingBuild

- **Kind:** flow
- **Area:** [Input](../areas/input.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the UIKeyAssign rows become the live bindings of the input module and how a binding is read each frame.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [InputModule_Init](../functions/InputModule_Init.md) | V | Sets the context mask to 0x15. |
| <a id="2"></a>2 | [InputRows_Rebuild](../functions/InputRows_Rebuild.md) | V | Called every frame by UI_FrameUpdate; picks the pad layout (0 or 1) from a byte of g_CharaRenderMgr. |
| <a id="3"></a>3 | [InputRows_ApplyPadLayout](../functions/InputRows_ApplyPadLayout.md) | V | Copies the pad column of the layout and the long-press flag into each row's pad binding. |
| <a id="4"></a>4 | [InputRows_ApplyKeyBindings](../functions/InputRows_ApplyKeyBindings.md) | V | Builds the two key bindings with modifier and long-press flags. |
| <a id="5"></a>5 | [Input_UpdateActionRow](../functions/Input_UpdateActionRow.md) | V | Each frame, per row: reads the pad button and the two keys and writes value, pressed, released, held and repeat. |
| <a id="6"></a>6 | [InputKey_ReadBinding](../functions/InputKey_ReadBinding.md) | V | Reads one key or mouse binding and applies the modifier flags; the long-press flag is applied in step 5. |

## Notes

Glyph text for an action is built separately by InputGlyph_AppendPadButton from the same rows.

## Open questions

? what the layout byte of g_CharaRenderMgr is.
