# UIAddon_OnEventBase

- **Address:** `0x1401D1F7C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAddon_OnEventBase(UIAddon *addon, int *event, void *a3)`
- **Callers:** every add-on's event handler (UIAddonFFTOConfig_OnEvent, UIAddonFFTOTitle_OnEvent)
- **Callees:** UIAddon_CanTakeInput

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Base event handler every add-on's own handler calls first.

## Behavior

- V: event 1 = input: when the add-on's id is not in the input exclusivity list (`g_CharaRenderMgr` +43600, index +44632), byte +47 is clear (the compare at 0x1401D2176) and vtable slot 3 says yes, it calls vtable +96 (slot 12) with `g_InputModule` + 8 and sets widget +77 from `uiaddon.nxd` byte 29.
- V: event 4 calls vtable +112 (slot 14, the per-frame update); 5 (shown) sets widget +78 from `uiaddon.nxd` byte 30 and calls +48; 6 (hidden) clears the focus and the cursor target, then +72; 7 answers whether the add-on is busy (+43); 0xC focuses a node; 13 releases a list.
- V: writers of +47 in the title code (their addresses are other functions, not in this body): UIAddonFFTOTitlePlaymode vtable slot 17 (0 at 0x1401C5674) and 0x1401C60E4 (1 at 0x1401C6172). I: +47 = takes no input.

## State touched

- Calls: [UIAddon_CanTakeInput](UIAddon_CanTakeInput.md)

## Referenced by

- Called by: [UIAddonFFTOConfig_OnEvent](UIAddonFFTOConfig_OnEvent.md)
- Observed behaviours: [TitleBackdropAndInputFlag](../behaviors/TitleBackdropAndInputFlag.md), [UIAddonBaseEventRouting](../behaviors/UIAddonBaseEventRouting.md)

## Open questions

None recorded.
