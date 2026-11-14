# GUINode_DrawKind8

- **Address:** `0x1403ECA88`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall GUINode_DrawKind8(UIRenderer *r, ComponentCtx *ctx, GUINode *n)`
- **Callers:** GUINode_DrawChildren (node kind 8)
- **Callees:** GUILayer_UpdateActiveFlag, GUILayer_Select, Matrix2x3_Multiply, sub_1403F1CFC, sub_1403DF9E0, sub_1403DFCF0, sub_1403E4FEC, sub_1403E30E0, sub_1403E40EC, sub_1403E3BBC, sub_1403E3828, sub_1403E4AE8, sub_1403E4688, sub_1403ECA24, sub_1403E9344

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draw hook for runtime node kind 8: a chain of segments built from a vector of 552-byte elements (n+216 .. n+224) drawn as strips; unlike the other node draws it can re-select the layer in the middle of the node.

## Behavior

- V: nothing happens unless n+204 (visible) is set and n+145 (hidden) is clear, and the element vector holds at least two elements (the element count is (n+224 - n+216) / 552 and one less when the byte n+276 is 0).
- V: GUILayer_UpdateActiveFlag(r, ctx, int16 n+272 == 0) runs first; the node matrix (n+160) times ctx+504 and the colours n+240 / n+244 multiplied with ctx+540 are prepared; when the renderer byte r+606625 and sub_1403F1CFC(n) are set the node is drawn as one flat quad through sub_1403DF9E0 of size n+64 x n+68.
- V: otherwise each element pair is emitted through sub_1403DFCF0 / sub_1403E4FEC (strip with a width) and the corner helpers sub_1403E30E0 / sub_1403E40EC / sub_1403E3BBC / sub_1403E3828 / sub_1403E4AE8 / sub_1403E4688 / sub_1403ECA24; when the end is reached and the byte n+336 is 2, 3 or 4 the function calls GUILayer_Select(r, ctx), i.e. it opens a NEW layer record of the current context at that point (a slot boundary inside one node; the other node draws never do this).
- V: at the end the draw counter r+606592 is incremented once when the byte n+336 is 0.

## State touched

- Calls: [GUILayer_UpdateActiveFlag](GUILayer_UpdateActiveFlag.md), [GUILayer_Select](GUILayer_Select.md), [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Notes

The name is ours (IDB: sub_1403ECA88). Only the control flow that touches layers and the draw counter was read; the geometry (a ribbon or trail node?) is I at best and was not decoded. A kind 8 node was not present in the Job Tree frame read live.

## Open questions

? What the node is in the UIB (a ribbon, trail or polyline); what n+336 (values 0, 2, 3, 4) selects. ? Whether the GUILayer_Select in the middle is reached on screens other than the battle UI.
