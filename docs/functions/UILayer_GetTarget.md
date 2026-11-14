# UILayer_GetTarget

- **Address:** `0x1403B0838`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 UILayer_GetTarget(UILayer *layer)`
- **Callers:** GUILayer_Composite, GUILayer_ApplyEffects, GUILayer_BlurEffect, UILayer_FillConstants, UIRender_PrepareLayers, GUILayer_PackAtlasRect, GUILayer_CopyOffsetRegion, UIRender_ResolveBase, UIRender_DrawOverlayQuads, UIRender_DrawLetterbox, UIRender_SubmitFrame, others
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the render target object a layer draws into: its own (layer+584) or else the renderer's current target.

## Behavior

- V: layer+584 when non-zero; otherwise index = byte g_Renderer+13754: 0xFF returns 0, else the qword g_Renderer + 8 * index + 6560.

## State touched

- Reads: [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [GUILayer_ApplyEffects](GUILayer_ApplyEffects.md), [GUILayer_CopyOffsetRegion](GUILayer_CopyOffsetRegion.md), [UICommand_ExecuteBatches](UICommand_ExecuteBatches.md), [UILayer_FillConstants](UILayer_FillConstants.md), [UIRender_DrawLetterbox](UIRender_DrawLetterbox.md), [UIRender_DrawOverlayQuads](UIRender_DrawOverlayQuads.md), [UIRender_PrepareLayers](UIRender_PrepareLayers.md), [UIRender_ResolveBase](UIRender_ResolveBase.md)
- Observed behaviours: [LayerAtlasPlacement](../behaviors/LayerAtlasPlacement.md)

## Notes

The name is ours (IDB: sub_1403B0838). The target object has u16 width / height at +20 / +22 and a byte at +86 that selects the per-target slot tables (g_Renderer + 512 * byte + 24224 ..) used everywhere in the layer passes.

## Open questions

None recorded.
