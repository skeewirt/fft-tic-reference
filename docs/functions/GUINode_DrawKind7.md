# GUINode_DrawKind7

- **Address:** `0x1403EC794`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void __fastcall GUINode_DrawKind7(UIRenderer *r, ComponentCtx *ctx, GUINode *n)`
- **Callers:** GUINode_DrawChildren (node kind 7)
- **Callees:** GUIWidget_FindResourceByName, UIImage_ResolvePart, GUILayer_UpdateActiveFlag, sub_1403E96A4, Matrix2x3_Multiply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draw hook for runtime node kind 7: one quad of node size, textured when the node names an image part, flat otherwise; it also asks for the offscreen flag of the context when no part is found.

## Behavior

- V: nothing happens unless n+204 (visible) is set and n+145 (hidden) is clear.
- V: when the dword n+216 is non-zero the image resource named by the key at n+208 is looked up in the widget and the part UIImage_ResolvePart(resource, n+224) resolved; the call GUILayer_UpdateActiveFlag(r, ctx, part == 0) follows (a no-op unless the renderer byte r+606626 and the context byte ctx+412 are set).
- V: the matrix is the node matrix (n+160) times ctx+504, the size is n+64 x n+68, the corner colours are n+236 and n+240 multiplied byte-wise with ctx+540 and the node colour at n+196 (via +160+36), the two floats n+228 / n+232 and the flag n+244 (mode 2) go to sub_1403E96A4.
- V: sub_1403E96A4 chooses between three emitters (sub_1403E1DB0 when mode bit 0 is set, sub_1403E2278 for a part with a texture or a positive float, else sub_1403E153C) and then increments the draw counter r+606592 once, so every visible kind 7 node counts as a draw.

## State touched

- Calls: [GUIWidget_FindResourceByName](GUIWidget_FindResourceByName.md), [UIImage_ResolvePart](UIImage_ResolvePart.md), [GUILayer_UpdateActiveFlag](GUILayer_UpdateActiveFlag.md), [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Notes

The name is ours (IDB: sub_1403EC794). The two floats and the corner colours are read from the node record without a name.

## Open questions

? What the three emitters of sub_1403E96A4 draw (a plain, a textured and a rounded variant?). ? A kind 7 node was not present in the Job Tree frame read live.
