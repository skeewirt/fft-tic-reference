# ListGadgetInputPath

- **Kind:** observed behaviour
- **Scope:** why a list cursor moves only when the screen calls the list input
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [UIListGadget_OnInput](../functions/UIListGadget_OnInput.md), [UIListGadget_IsAnimating](../functions/UIListGadget_IsAnimating.md), [UIAddonFFTOConfig_OnInput](../functions/UIAddonFFTOConfig_OnInput.md), [UIMenuFunction_OnInput](../functions/UIMenuFunction_OnInput.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A list gadget's cursor moves by pad or keyboard only when the screen's input handler calls the list's own input; the Left / Right branches of the settings screen return before that call.

## Behavior

- V: the settings input ends with `if (!UIListGadget_IsAnimating(list)) UIListGadget_OnInput(list, input)` when no value list is open and the row list takes input.
- V (seen live 2026-11-13): a screen of this class whose input handler lacked the call left the cursor on row 1 for Down and pad DOWN.
- V: the shared menu input of the `UIFFTOMenuFunctionBase` part reads the same input bytes: +13640 / +13644 and +13642 / +13646 call part vtable +16 (delta -1 / +1), +13641 / +13645 and +13643 / +13647 call part vtable +24 (the title's TitleMenu_MoveCursor); then 0x1400F1278(input).
- V: UIListGadget_IsAnimating is true while a 'Show', 'Slide_left' or 'Slide_right' state runs; GUINode_PlayState sets the state's running byte.

## Open questions

None recorded.
