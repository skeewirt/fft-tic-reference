# GUILayerXform_Recompute

- **Address:** `0x1403F8A20`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 sub_1403F8A20(GUILayerXform *t)`
- **Callers:** GUILayerXform_MapPointFloat, GUILayerXform_MapPointInt, sub_1403F8D2C, GUICore_DrawWidget, GUICore_CommitFrame, sub_1403D6234, sub_14015AB34, sub_140175F58
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Recomputes a GUI layer transform (one of the window-to-UI layers at GUICore + 216 + 144 * index): a letterbox fit of the UI size into the viewport, as a forward matrix, an inverse matrix and the scale. The return value is unused.

## Behavior

- V: inputs: +0 / +4 ints = the UI (design) size w / h; +8 / +12 floats = layer scale multipliers; +16 / +20 ints = an extra offset added to the viewport centre; +24 / +28 ints = the viewport width W / height H; +32 / +36 / +40 / +44 ints = the viewport rectangle (left, top, right, bottom). GUICore's per-frame update fills them: +24 / +28 = right - left, bottom - top and +32.. = the rectangle.
- V: fit scale f = W / w when w * H >= h * W, else H / h (the smaller of the two ratios, integer cross-multiplied); sx = (+8) * f, sy = (+12) * f; the viewport centre cx = (+16) + (left + right) / 2 and cy = (+20) + (top + bottom) / 2 (integer halves).
- V: outputs (floats): +48..+68 = the viewport-local forward matrix [sx, 0, 0, sy, tx, ty] with tx = cx - (w / 2) * sx - left and ty = cy - (h / 2) * sy - top; +72..+92 = the inverse [1/sx, 0, 0, 1/sy, w/2 - cx/sx, h/2 - cy/sy] of the window-absolute transform; +96..+116 = the window-absolute forward matrix [sx, 0, 0, sy, cx - (w/2) * sx, cy - (h/2) * sy]; +120 / +124 = sx / sy; the dirty byte +128 is cleared. The zero entries are computed as products with 0.0.
- V: consumers: GUILayerXform_MapPointInt / GUILayerXform_MapPointFloat map a window point to UI coordinates with the +72 inverse; sub_1403F8D2C maps a UI point to window pixels with the +96 matrix; GUICore_DrawWidget copies +48..+71 and +120 / +124 into the root draw context (ctx+504 and ctx+528 / +532); sub_14015AB34 and sub_140175F58 read the lengths of the +72..+84 rows (1 / scale); GUICore_CommitFrame recomputes a dirty transform before drawing the outside bars (only for transforms whose +132 dword is 1); sub_1403D6234 refills the viewport fields.
- V: the callers either test the dirty byte +128 first (MapPoint*, sub_1403F8D2C, GUICore_DrawWidget, GUICore_CommitFrame, sub_14015AB34, sub_140175F58) or, like sub_1403D6234, set it to 1 and call directly.

## Referenced by

- Called by: [GUICore_BeginFrame](GUICore_BeginFrame.md)

## Notes

Proposed name: GUILayerXform_Recompute. Worked check: UI size 1920 x 1080 in a 1280 x 720 viewport at (0, 0): f = 2/3, tx = 640 - 960 * 2/3 = 0, sx = sy = 0.6667. The scan that listed this function as writing component fields +100 / +104 / +116 / +120 is a coincidence of offsets: here they are the layer transform's own floats (+100 = 0.0 zero term, +104 = 0.0, +116 = ty0, +120 = sx), not component properties.

## Open questions

? what +16 / +20 are (set outside this function; their values were not read). ? why the inverse (+72..+92) is built from the window-absolute matrix while the viewport-local matrix (+48) is the one drawn with. ? what +132 (set to 1 by sub_1403D6234, read by GUICore_CommitFrame to draw the outside bars) is exactly.
