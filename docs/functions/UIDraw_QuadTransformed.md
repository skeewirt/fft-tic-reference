# UIDraw_QuadTransformed

- **Address:** `0x1403E0B80`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 UIDraw_QuadTransformed(UIRenderer *r, float xform[6], int rect[4], GUIFontSlot *part, float uv[8], unsigned tintRGBA, unsigned layer)`
- **Callers:** UIDraw_QuadFromTexelRect (sole code caller; UIImage_DrawTiled has its own vertex emitter)
- **Callees:** UIDraw_SetStateFromSlot, UIRender_QueueImageDraw, UIRender_AccumulateQuadBounds

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Emits one image quad: the rectangle rect = (x0, y0, x1, y1) mapped through the 2x3 matrix, with given UVs and one colour, as 4 vertices of 24 bytes.

## Behavior

- V: returns without drawing when x0 == x1 or y0 == y1 (empty rectangle). Otherwise UIDraw_SetStateFromSlot(r, .., part) and UIRender_QueueImageDraw(renderer global +37936, 4 vertices, ..) reserve the vertices.
- V (positions, float, no rounding or snapping): X = m0*x + m2*y + tx, Y = m1*x + m3*y + ty for the corners in the order (x0,y0), (x0,y1), (x1,y1), (x1,y0), where the sums are formed as (m0*x + m2*y) + tx with the integer rect values converted to float first.
- V (vertex, 24 bytes): +0 X, +4 Y, +8 z = 0.0, +12..+15 the colour bytes of tintRGBA exactly as passed (no multiply here), +16 u, +20 v. UVs by vertex: (uv[0], uv[1]) at (x0,y0), (uv[4], uv[5]) at (x0,y1), (uv[6], uv[7]) at (x1,y1), (uv[2], uv[3]) at (x1,y0), so uv[] = [u0 v0, u1 v0, u0 v1, u1 v1] as UIDraw_QuadFromTexelRect builds it.
- V: the four transformed points are then passed to UIRender_AccumulateQuadBounds.

## State touched

- Calls: [UIDraw_SetStateFromSlot](UIDraw_SetStateFromSlot.md), [UIRender_QueueImageDraw](UIRender_QueueImageDraw.md), [UIRender_AccumulateQuadBounds](UIRender_AccumulateQuadBounds.md)
- Reads: [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [UIDraw_QuadFromTexelRect](UIDraw_QuadFromTexelRect.md)

## Notes

The name is ours (IDB: sub_1403E0B80). 8555 hits per 4 s (the same count as UIDraw_QuadFromTexelRect: every plain quad goes through both). The caller passes the node matrix (node+160 combined with the draw state matrix) as xform, so the on-screen position of an image / nine-grid cell is the matrix of GUINode_BuildLocalMatrix times the parent chain, applied to the integer rectangle, with no pixel snapping; any snapping would have to happen in the vertex shader or the camera matrix.

## Open questions

The vertex colour semantics beyond 'tintRGBA bytes copied' (premultiplication, which byte order) belong to the shader.
