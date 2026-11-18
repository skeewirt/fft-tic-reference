# UIMenuFunction_OnInput

- **Address:** `0x1402AB4D8`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIMenuFunction_OnInput(UIFFTOMenuFunctionBase *part, uint8 *input)`
- **Callers:** UIAddonFFTOTitle input (0x1401C410C)
- **Callees:** TitleMenu_MoveCursor

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The shared menu input of the `UIFFTOMenuFunctionBase` part (the title menu's part at +48).

## Behavior

- V: reads the same bytes as the list input: +13640 / +13644 and +13642 / +13646 call part vtable +16 (delta -1 / +1; a no-op for the title), +13641 / +13645 and +13643 / +13647 call part vtable +24 (TitleMenu_MoveCursor by an indirect call, -1 / +1); then 0x1400F1278(input).

## State touched

- Calls: [TitleMenu_MoveCursor](TitleMenu_MoveCursor.md)

## Referenced by

- Observed behaviours: [ListGadgetInputPath](../behaviors/ListGadgetInputPath.md)

## Open questions

None recorded.
