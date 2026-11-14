# GUILayer_CopyOffsetRegion

- **Address:** `0x1403B6028`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char GUILayer_CopyOffsetRegion(UILayer *layer, unsigned char targetType)`
- **Callers:** GUILayer_Composite
- **Callees:** UILayer_GetTarget, UIBlur_CopyTarget

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Used when layer byte +487 is set: copies the layer's rectangle from target slot 30 into render target 26 (the first scratch), standing in for the effect ping-pong start.

## Behavior

- V: returns 0 at once when layer+487 is 0. Otherwise sets the sort key state+8 = ((layer+12 & 0x1FF | ((layer+16 & 0x3F | tt << 18) << 15) | 0x6AC00E00) << 10) with tt = 0 when targetType == 1 (the key is set again after the copy).
- V: rectangles are cast to int with truncation: dst = ((int)x, (int)y, (int)(x + w), (int)(y + h)) from floats +208 / +212 / +216 / +220; src = x' = (+232 - +224) + x, y' = (+236 - +228) + y, then ((int)x', (int)y', (int)(x' + w), (int)(y' + h)). (+224 / +228 = the atlas offset, +232 / +236 = the second atlas offset, both written by GUILayer_PackAtlasRect.)
- V: calls UIBlur_CopyTarget(blurObj = *(g_Renderer+37928), layer target, srcSlot 30, dstRT 26, filter index 2, srcRect = the shifted rectangle, flag = the destination rectangle). Returns 1.

## State touched

- Calls: [UILayer_GetTarget](UILayer_GetTarget.md), [UIBlur_CopyTarget](UIBlur_CopyTarget.md)
- Reads: [GUILayer.sort_lo](../structs/GUILayer.md#sort_lo), [GUILayer.sort_hi](../structs/GUILayer.md#sort_hi), [GUILayer.rect](../structs/GUILayer.md#rect), [GUILayer.atlas_offset](../structs/GUILayer.md#atlas_offset), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key)

## Referenced by

- Called by: [GUILayer_Composite](GUILayer_Composite.md)

## Notes

The name is ours (IDB: sub_1403B6028). The caller treats it as the replacement for GUILayer_ApplyEffects when +487 is set (see GUILayer_Composite). Rounding: truncation toward zero of float rectangle edges; the right edge is (int)(x + w), not (int)x + (int)w. Filter index 2 (UIBlur_CopyTarget digit 1) is not decoded.

## Open questions

What slot 30 holds; meaning of filter index 2.
