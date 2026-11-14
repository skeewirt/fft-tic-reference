# UIDraw_QuadFromTexelRect

- **Address:** `0x1403E0AC0`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 UIDraw_QuadFromTexelRect(UIRenderer *r, float xform[6], int rect[4], GUIFontSlot *part, int texelRect[4], unsigned tintRGBA, unsigned layer)`
- **Callers:** UIImageNode_Draw, GUITextNode_Draw, GUINineGridNode_Draw (15 sites), sub_1403EBFA0
- **Callees:** sub_1403DCA04, UIDraw_QuadTransformed

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Thunk-like helper for plain quads: converts a texel rectangle of a texture part into UVs and draws one quad with UIDraw_QuadTransformed.

## Behavior

- V: (w, h) = sub_1403DCA04(part) = the texture size read from the part's texture record as u16 at +136 / +138 (1, 1 when there is no texture).
- V: u0 = (float)texelRect[0] / (float)w, v0 = (float)texelRect[1] / h, u1 = (float)texelRect[2] / w, v1 = (float)texelRect[3] / h (so texelRect is x0, y0, x1, y1 in texels, plain division with no half-texel offset); passes the UV list [u0 v0, u1 v0, u0 v1, u1 v1] to UIDraw_QuadTransformed.

## State touched

- Calls: [UIDraw_QuadTransformed](UIDraw_QuadTransformed.md)

## Referenced by

- Called by: [GUINode_DrawKind5](GUINode_DrawKind5.md)

## Notes

The name is ours (IDB: sub_1403E0AC0). 8555 hits per 4 s. The nine-grid draw emits each of its up to 9 cells through this function, so each cell's UV is exactly texel / texture size with no inset.

## Open questions

Whether texelRect[2..3] are exclusive end coordinates (the arithmetic is the same either way).
