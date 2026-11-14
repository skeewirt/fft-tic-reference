# UIRender_SubmitFrame

- **Address:** `0x1403B9844`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void UIRender_SubmitFrame(__int64 ui, __int64 a2)`
- **Callers:** none direct (probably a virtual call of the UI renderer)
- **Callees:** UIRender_ResolveBase, UIRender_DrawOverlayQuads, GUILayer_Composite, UIContext_SortCommands, UICommandRing_Flush, UICommandRing_Reset, UIRender_DrawLetterbox, sub_14003F7C0, sub_14003E120

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

End-of-frame UI submission: composites every prepared layer, sorts the commands of all 32 contexts, merges them into one stream and executes it.

## Behavior

- V: runs only when a2 == 0. Calls UIRender_ResolveBase and UIRender_DrawOverlayQuads, then for the layers whose page changes (layer+16) with +492, +179 and +79 == 0 and +28 != 2 emits one clear-style command (type 19) per atlas texture of the page (sort key ((page & 0x3F | targetByte << 18) << 25) | 0x1AB01D80000, flag word 2 when the renderer option bit is set).
- V: maps 7 command buffers (ui+8464..8584) and calls GUILayer_Composite for each of the active layers (first call with flag 1, cleared once a layer has +76 set), then repeats the per-page loop with key 0x1AB01DFFC00 and flag word 1.
- V: sorts the 32 contexts with UIContext_SortCommands and k-way merges them by key into one region at the end of the ring (ring+192, count ring+208), then UICommandRing_Flush, UICommandRing_Reset and UIRender_DrawLetterbox.
- V: the call order in the function is UIRender_ResolveBase, UIRender_DrawOverlayQuads, GUILayer_Composite once per layer (the layer effect passes, among them the +177 shadow, are packed into the contexts' command lists inside it), UIContext_SortCommands, UICommandRing_Flush, UICommandRing_Reset, UIRender_DrawLetterbox.
- I: the effect commands are therefore recorded before UICommandRing_Flush replays the UI draws, so the sampler state they are packed with is whatever the context holds at that moment (the default words from RenderContext_ResetFrame for slot 14; see GUILayer_BlurShadowPass). Basis: the call order above and the live trace on that sheet.
- I: sort key layout (shifts and masks read from the helpers, all keys are 64-bit): bits 10..18 = layer order (+12), bits 19..24 = the pass constant (const >> 9 & 0x3F: 7 copy 0x6AC00E00, 14 base 0x6AC01C00, 16 / 59 the +177 blur 0x6AC02000 / 0x6AC07600), bits 25..30 = atlas page (+16), bit 43 and up = render target byte. Commands therefore execute grouped per target, then per atlas page, then per pass, then by layer order.

## State touched

- Calls: [UIRender_ResolveBase](UIRender_ResolveBase.md), [UIRender_DrawOverlayQuads](UIRender_DrawOverlayQuads.md), [GUILayer_Composite](GUILayer_Composite.md), [UIContext_SortCommands](UIContext_SortCommands.md), [UICommandRing_Flush](UICommandRing_Flush.md), [UICommandRing_Reset](UICommandRing_Reset.md), [UIRender_DrawLetterbox](UIRender_DrawLetterbox.md)
- Reads: [Renderer.targets_by_type](../structs/Renderer.md#targets_by_type), [UIManager.layer_quad_buffer](../structs/UIManager.md#layer_quad_buffer), [g_RenderDevice](../globals/g_RenderDevice.md), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key), [UIManager.layer_quad_mapped](../structs/UIManager.md#layer_quad_mapped)

## Referenced by

- Appears in flows: [FrameUiSubmission](../flows/FrameUiSubmission.md), [UiLayerComposite](../flows/UiLayerComposite.md)
- Observed behaviours: [LayerCompositeOrder](../behaviors/LayerCompositeOrder.md)

## Notes

The name is ours (IDB: sub_1403B9844). The key layout and the command type meanings (19, 4, 5) are inferred; the loops themselves were read in full. This is the function the Job Tree frame goes through every frame.

## Open questions

Exact semantics of the type-19 commands (barrier / discard of the page textures, I); the second loop's key 0x1AB01DFFC00.
