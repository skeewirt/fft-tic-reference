# UIAgent_DetachAddon

- **Address:** `0x1401D183C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIAgent_DetachAddon(UIAgent *agent, UIAddon *addon)`
- **Callers:** UIAgentFFTOSystem_FreeAddons
- **Callees:** UIAddonFFTOConfig_OnClose

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Removes an add-on from its agent's list, hides it and calls its slot 5.

## Behavior

- V: removes it from the list (+16 / +24); unless +44 / +45 are set: +44 = 1, `UIAddon_Hide(addon, 0)`, then the add-on's vtable +40 (slot 5, an indirect call; for General Options its on-close handler).

## State touched

- Calls: [UIAddonFFTOConfig_OnClose](UIAddonFFTOConfig_OnClose.md)
- Reads: [UIAgentBase.addons_begin](../structs/UIAgentBase.md#addons_begin), [UIAgentBase.addons_end](../structs/UIAgentBase.md#addons_end)
- Writes: [UIAgentBase.addons_end](../structs/UIAgentBase.md#addons_end)

## Referenced by

- Appears in flows: [GeneralOptionsOpenAndClose](../flows/GeneralOptionsOpenAndClose.md), [UIAgentLifecycle](../flows/UIAgentLifecycle.md)
- Called by: [Boot_CloseUI](Boot_CloseUI.md), [Boot_Update](Boot_Update.md), [Movie_Start](Movie_Start.md), [OpeningTask_10](OpeningTask_10.md), [UIAgentFFTOSystem_FreeAddons](UIAgentFFTOSystem_FreeAddons.md), [UISaveLoad_StateSourcePick](UISaveLoad_StateSourcePick.md), [sub_1401839E4](sub_1401839E4.md)

## Open questions

None recorded.
