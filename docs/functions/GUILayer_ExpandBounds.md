# GUILayer_ExpandBounds

- **Address:** `0x1403E75DC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUILayer_ExpandBounds(UIRenderer *r, int layerIndex)`
- **Callers:** GUICore_CommitFrame (once per slot 0..count - 1, after GUILayer_Flush), sub_1403D64F4
- **Callees:** UIBlur_TapCount, GUILayer_BoundsAdd32, roundf

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The last step that fixes a layer's float rectangle (layer+208..+220): the union of the quad bounds drawn into the slot (the dirty rectangle) grown by the blur reach of the slot's effects and by 16 pixels, clamped to the target. The layer-order part rotates the order values of layers that share a layer id.

## Behavior

- V: input = the slot's dirty rectangle, four ints at r + 512 * i + 41824 (x0, y0, x1, y1), filled by GUILayer_Flush from the quad bounds and cleared every frame by GUIRenderer_ResetFrame. When it is empty (x0 >= x1 or y0 >= y1) the rectangle of the layer is not written (it keeps the default (0, 0, W, H) of GUILayer_ResetRecord; such a slot has no command and is never used).
- V: radius R = 0, then max with: the float layer+500 when the layer kind dword layer+28 is 1 (whole-layer blur group); layer+188 when the drop-shadow byte layer+177 is set; layer+204 when the glow byte layer+178 is set; layer+180 when the single-float byte layer+176 is set (layer = r + 303480 + 592 * i, the record minus 24 bytes). The three radii in the record are the pixel values GUILayer_BuildRecord wrote (UIB radius x min scale); a group whose flag is clear is ignored even when its stale radius value is large.
- V: R <= 0 adds nothing. Otherwise the pad P (pixels, added to every edge with saturation, GUILayer_BoundsAdd32) is f * UIBlur_TapCount(R / f, 1 / 255) with f = 1 for R <= 3.2, 2 for <= 6.4, 4 for <= 12.8, 8 for <= 25.6, 16 for <= 51.2 and 32 above (the sigma argument is R, R x 0.5, 0.25, 0.125, 0.0625, 0.03125). With a float32 model of GaussianKernel_Build: R 0.667 -> 3, 0.8 -> 3, 1.0 -> 4, 2.0 -> 6, 2.667 -> 8, 4.0 -> 12, 6.0 -> 16, 6.667 -> 20, 10 -> 28.
- V: when the byte layer+486 (the +178 context group) is set each padded edge e is replaced by round((e - W x sx) x k + e) (x edges: W = r+184, sx = float layer+504, y edges: H = r+188, sy = float layer+508), k = float layer+520 + 1, and then clamped so that it is never inside the original dirty rectangle (not exercised by the Job Tree: read in the code only).
- V: then every edge grows by 16 pixels (saturating), and each edge is clamped into [0, W] (x) and [0, H] (y) with W = r+184, H = r+188; the result is stored as floats (x0, y0, x1 - x0, y1 - y0) at layer+208..+220. A rectangle entirely off the target collapses to a zero width or height (live: layers with x0 = x1 = 0).
- V (live 2026-10-30, 26 + 40 layers of two Job Tree frames): the integer rectangle that GUILayer_PackAtlasRect later derives from the float rectangle ((int)x, (int)y, (int)(x + w), (int)(y + h), layer+240..+252) equals the rule above applied to the dirty rectangle for every used layer (dirty (620, 475, 625, 485), radius 0.667 single float -> pad 3 + 16 -> (601, 456, 644, 504); dirty (834, 395, 935, 409), glow radius 2.667 -> pad 8 + 16 -> (810, 371, 959, 433); a shadow radius 2.0 -> pad 6).
- V: layer ids: when the slot's layer id (r + 512 * i + 41840) is non-zero, the newest record whose id has the same high word and a larger low word is searched; if it is a later slot j > i, the order dwords (layer+12) of the slots i..j are rotated so that slot j takes the order of slot i and the slots i..j-1 move up by one (higher ids keep their place after compositing). The Job Tree frames have no layer id (all ids 0).

## State touched

- Calls: [UIBlur_TapCount](UIBlur_TapCount.md), [GUILayer_BoundsAdd32](GUILayer_BoundsAdd32.md)
- Reads: [GUILayer.layer_kind](../structs/GUILayer.md#layer_kind), [GUILayer.effect_flags](../structs/GUILayer.md#effect_flags), [GUILayer.shadow_radius](../structs/GUILayer.md#shadow_radius), [GUILayer.glow_radius](../structs/GUILayer.md#glow_radius), [GUILayer.single_radius](../structs/GUILayer.md#single_radius), [GUILayer.blur_radius](../structs/GUILayer.md#blur_radius)
- Writes: [GUILayer.rect](../structs/GUILayer.md#rect)

## Referenced by

- Called by: [GUICore_CommitFrame](GUICore_CommitFrame.md)
- Observed behaviours: [JobTreeLayerList](../behaviors/JobTreeLayerList.md)

## Notes

Glow radius 4.0 falls in the (<= 6.4) class: f = 2, pad 12. The atlas margin of GUILayer_PackAtlasRect looks at radii above 3.2 of +500, +180 and +188 and not at the glow radius +204 (as read in that function; the two functions use different subsets). The rule is the one a software renderer needs to reproduce layer rectangles: see the behavior JobTreeLayerList.

## Open questions

The blur pass itself (shader and weights) is not decoded (?). The +486 scaling branch was not exercised (?).
