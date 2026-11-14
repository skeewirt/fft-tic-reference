# GUINode_DrawKind5

- **Address:** `0x1403EBFA0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char __fastcall GUINode_DrawKind5(UIRenderer *r, ComponentCtx *ctx, GUINode *n)`
- **Callers:** GUINode_DrawChildren (node kind 5)
- **Callees:** GUIWidget_FindResourceByName, UIImage_ResolvePart, GUILayer_UpdateActiveFlag, UIDraw_QuadFromTexelRect, sub_1403DFE34, sub_1403F183C, Matrix2x3_Multiply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draw hook for runtime node kind 5: draws a string of characters (digits, a space, other characters) from one image part, each with its own advance; the draw counter makes it consume a layer slot.

## Behavior

- V: returns without drawing when n+204 (visible) is 0 or n+145 (hidden) is set, when the image resource named by the key at n+208 is not found in the widget (GUIWidget_FindResourceByName(ctx+488, n+208)), when the part UIImage_ResolvePart(resource, int16 n+312) is null or has no texture, or when the string length (n+288) is not positive.
- V: after those gates it calls GUILayer_UpdateActiveFlag(r, ctx, 0) and increments the draw counter r+606592 once (before any quad), so the node counts as a draw of the current layer even if its quads were empty.
- V: the string is the std::string at n+272 (the pointer is n+272 itself when the capacity n+296 is below 16, else the heap pointer stored there); per character the advance is the int16 n+314 for '0'..'9', n+318 for a space and n+316 for any other character; a non-positive value falls back to the part width divided by 1 (2 when the part byte +35 is set); the sum of the advances is the string width used to place the quads.
- V: the quads go through UIDraw_QuadFromTexelRect or sub_1403DFE34 (flat quad; which of the two is chosen was not read), with the node matrix (n+160) times the context matrix (ctx+504) and the colour ctx+540 times the node colour; sub_1403F183C places the characters (not read).

## State touched

- Calls: [GUIWidget_FindResourceByName](GUIWidget_FindResourceByName.md), [UIImage_ResolvePart](UIImage_ResolvePart.md), [GUILayer_UpdateActiveFlag](GUILayer_UpdateActiveFlag.md), [UIDraw_QuadFromTexelRect](UIDraw_QuadFromTexelRect.md), [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Notes

The name is ours (IDB: sub_1403EBFA0). The node kind is the one GUINode_DrawChildren dispatches as 5; the file-side meaning (a number string node?) is I, from the digit / space / other advances.

## Open questions

? The placement maths (sub_1403F183C) and the fade or clamp the +316 / +318 advances feed. ? A kind 5 node was not present in the Job Tree frame read live.
