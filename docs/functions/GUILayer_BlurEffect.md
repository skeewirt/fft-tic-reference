# GUILayer_BlurEffect

- **Address:** `0x1403B6640`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void GUILayer_BlurEffect(UILayer *layer, __int64 a2, __int64 a3, __int64 a4, float *renderSize)`
- **Callers:** GUILayer_Composite
- **Callees:** UIBlur_Run, sub_1403AC620, sub_1403ABEDC, sub_1403B5664, GUILayer_BlitFinal

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Whole-layer blur (the effect with radius at layer+500): copies the layer region, blurs it with UIBlur_Run and blits the result.

## Behavior

- V: runs only when |layer+500| > 0; copies the layer rectangle (+208..+220) into target 27 (sub_1403AC620 / sub_1403ABEDC), builds the normalised clamp rectangle with half-pixel insets, calls UIBlur_Run(radius = |+500|, ..., 59, ...), then sub_1403B5664 and GUILayer_BlitFinal.

## State touched

- Calls: [UIBlur_Run](UIBlur_Run.md), [GUILayer_BlitFinal](GUILayer_BlitFinal.md)
- Reads: [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo), [GUILayer.sort_hi](../structs/GUILayer.md#sort_hi), [GUILayer.rect](../structs/GUILayer.md#rect), [Renderer.targets_by_type](../structs/Renderer.md#targets_by_type), [g_RenderDevice](../globals/g_RenderDevice.md), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key)

## Referenced by

- Called by: [GUILayer_Composite](GUILayer_Composite.md)

## Notes

Not the component glow (that is GUILayer_GlowPass).

## Open questions

None recorded.
