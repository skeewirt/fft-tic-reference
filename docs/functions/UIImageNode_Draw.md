# UIImageNode_Draw

- **Address:** `0x1403E9C48`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char UIImageNode_Draw(UIRenderer *r, GUIContext *ctx, GUINode *node)`
- **Callers:** GUI node draw dispatcher sub_1403E9A6C (kind 2)
- **Callees:** UIImage_ResolvePart, UIImage_DrawTiled, sub_1403E0AC0, UIDraw_SetStateFromSlot, sub_1403E6440, Matrix2x3_Multiply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one Image node: resolves its texture part, builds the node's colour, flips and draw state, then calls the draw routine its fill type selects.

## Behavior

- V: returns at once when node+204 (visible) is 0 or node+145 (hidden) is non-zero. The part (a GUIFontSlot record) comes from node+208 when set, else UIImage_ResolvePart (texture ref at node+232, part id node+248, node+252/+256).
- V: tint = node colour (node+160 block, +36 of it) multiplied per byte by the context colour (ctx+540); node size in node+64/+68; flip bytes node+268 (u) and +269 (v) swap the part rectangle corners, +270 forces slot byte 38.
- V: copies the node floats +272/+276/+280 (0.5, 0.2, 1.0 in every node read) and the part size * 0.00012207 (= 1/8192) into the renderer draw state at r+28 / +32 / +36 / +40.
- V: switch on fill type node+264: 0 (default) = plain quad (sub_1403E0AC0); 1 = call to sub_1403E0AC0 with a clamped inner rectangle; 2 = UIImage_DrawTiled without mirroring; 3 = UIImage_DrawTiled with mirroring (odd columns mirrored in u, odd rows in v). Increments r+606592 (draw counter).

## State touched

- Calls: [UIImage_ResolvePart](UIImage_ResolvePart.md), [UIImage_DrawTiled](UIImage_DrawTiled.md), [UIDraw_SetStateFromSlot](UIDraw_SetStateFromSlot.md), [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Referenced by

- Called by: [GUINode_DrawChildren](GUINode_DrawChildren.md)

## Notes

The Job Tree hover ring (UnitSelect/Image01) is fill type 3.

## Open questions

The inner-rectangle maths of fill type 1 was not studied (?).
