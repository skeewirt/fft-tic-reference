# GUINineGridNode_Draw

- **Address:** `0x1403EAF9C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINineGridNode_Draw(UIRenderer *r, DrawCtx *ctx, GUINode *node)`
- **Callers:** GUINode_DrawChildren
- **Callees:** UIImage_ResolvePart, sub_1403E0AC0, UIImage_DrawTiled, Matrix2x3_Multiply, sub_1403E6440

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws a Ninegrid node (runtime kind 4): the node's part cut into 3 x 3 cells by the node's own borders and drawn into the node box.

## Behavior

- V: skipped when node+204 (visible) is 0 or node+145 (hidden) is set; the part is resolved with UIImage_ResolvePart(.., node+224) and the node colour (node+196) is multiplied with the context colour (ctx+540) like every image draw.
- V: the borders come from node+228 (left), +232 (top), +236 (right), +240 (bottom) in layout px; when left + right exceeds the node width (node+64) or top + bottom the node height (node+68) the pair is shrunk proportionally (left = left * width / (left + right) and so on).
- V: the source cells use the borders times k texels, k = 1 + the part's double-resolution byte (part+35); the corner cells are drawn with sub_1403E0AC0 (stretched quad); the edge cells switch on node+244: 2 -> UIImage_DrawTiled (plain tiling), 3 -> UIImage_DrawTiled with the mirrored flag; the other values (0 stretch, 1) were not read in the 27 KB body (I: a stretched quad).

## State touched

- Calls: [UIImage_ResolvePart](UIImage_ResolvePart.md), [UIImage_DrawTiled](UIImage_DrawTiled.md), [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Notes

The studio draws the chip, badge and name plate with these borders (labels.json nine); the plate's 24 + 20 = 44 texels leave a zero-width middle, drawn as the single boundary column.

## Open questions

The degenerate middle cell (zero source width) was not traced in the 27 KB function; the studio stretches the boundary column (I). Part+35 is assumed 0 for the job tree atlases (the borders fit the 22 x 22 and 44 x 48 parts at 1:1).
