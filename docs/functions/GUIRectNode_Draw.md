# GUIRectNode_Draw

- **Address:** `0x1403EC4B0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIRectNode_Draw(UIRenderer *r, DrawCtx *ctx, GUINode *rect)`
- **Callers:** GUINode_DrawChildren
- **Callees:** sub_1403E6440, Matrix2x3_Multiply, sub_1403E00AC, sub_1403E0824

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws a Rect node (runtime kind 6): one quad with a colour per corner.

## Behavior

- V: skipped when node+204 (visible) is 0 or node+145 (hidden) is set; otherwise sub_1403E6440(r, ctx, 1) selects the plain-colour pipeline state and the node's matrix (node+160) is multiplied with the context matrix (ctx+504).
- V: the node colour (node+196, the fill with alpha x opacity) is multiplied per channel with the context colour (ctx+540), and each of the four corner colours (node+208 / +212 / +216 / +220) with that product, /255 each; the quad is node+64 x node+68 in size and goes to sub_1403E00AC (or sub_1403E0824 when node byte +224 is set) with the four vertex colours; node byte +225 adds the outline flag.

## State touched

- Calls: [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Notes

The studio's chrome renderer (game_chrome.js) follows this: corner colour x fill colour (alpha x opacity), Gouraud across the quad, premultiplied-over blending, GPU pixel-centre coverage.

## Open questions

The difference between sub_1403E00AC and sub_1403E0824 (the node's +224 flag) (?).
