# GUIQuad_EmitGouraud

- **Address:** `0x1403E00AC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIQuad_EmitGouraud(UIRenderer *r, const float m[6], const int rect[4], const uint8 colors[16], unsigned int sortKey, char flags)`
- **Callers:** GUIRectNode_Draw (0x1403EC766)
- **Callees:** UIRender_AppendCommand, UIRender_AccumulateQuadBounds, sub_1403B830C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Emits one coloured quad (the Rect node's draw): the rectangle pushed through a 2x3 matrix, four corner colours, drawn as four triangles around a centre vertex; optionally also an outline command.

## Behavior

- V (corners): rect = {x0, y0, x1, y1}; each corner is (X, Y) = (m0*x + m2*y + m4, m1*x + m3*y + m5) in float: c0 = (x0,y0), c1 = (x1,y0), c2 = (x0,y1), c3 = (x1,y1) (rect[2] is the right edge, rect[3] the bottom edge).
- V (colours): colors = 4 RGBA dwords in the order c0, c1, c2, c3. The centre vertex has the position ((c0 + c1 + c2 + c3 computed as ((c0+c1)+c2)+c3) * 0.25) and the per-channel colour (sum of the four bytes) >> 2 (integer, truncating; alpha included).
- V (geometry): a type-12 command with 12 vertices of 24 bytes (x, y, 0, RGBA at +12, zeros) allocated by UIRender_AppendCommand(r+37936 object, 12, sortKey, r+48): triangles (c0,c2,centre), (c2,c3,centre), (c3,c1,centre), (c1,c0,centre). So the colour varies linearly toward the centre, NOT as a bilinear gradient across a two-triangle quad.
- V (bounds): after the vertices UIRender_AccumulateQuadBounds(r, the four corner positions) updates the draw bounds.
- V (outline): when (flags & 2) a second command (sub_1403B830C, type 8) with 8 vertices is built from the four corner positions and the corner colours with alpha halved (alpha >> 1; R, G, B unchanged).

## State touched

- Calls: [UIRender_AppendCommand](UIRender_AppendCommand.md), [UIRender_AccumulateQuadBounds](UIRender_AccumulateQuadBounds.md)
- Reads: [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)

## Notes

The name is ours (IDB: sub_1403E00AC). Pixel-exact rule for a simulator: the interior of a Rect node with four different corner colours is a four-triangle fan with an integer-averaged centre colour; a single colour (all corners equal) is flat.

## Open questions

? Exact layout of the outline command (which vertex pairs) and the difference to sub_1403E0824 (the +224 variant).
