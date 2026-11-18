# GUINode_UpdateColourAndMatrix

- **Address:** `0x1403EFF08`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUINode_UpdateColourAndMatrix(GUINode *node, char force)`
- **Callers:** GUINode_UpdateSubtree (sub_1403F08C0) for every child and for the node itself; a dozen screen code paths call it directly (GuideBar_Layout, sub_14015CB04, sub_1401F36A0, sub_1402AD0DC, sub_1402EE84C, sub_1403F2FDC)
- **Callees:** sub_1403D9570 (named colour lookup), GUINode_BuildLocalMatrix (sub_1403F0270), Matrix2x3_Multiply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-node update that every node of every kind goes through each frame: resolves the node colour, multiplies it (and the opacity) with the parent's, derives the visible flag (+204) and, when the node is dirty, rebuilds the node's 2x3 matrix at +160 and the accumulated scale / rotation / sort order at +184..+200.

## Behavior

- V (colour source): id = node+96. When bit 30 (0x40000000) is set the colour is looked up by name through sub_1403D9570(palette object qword_143CDAA60, id & 0xBFFFFFFF) (a std::map by name hash, falling back to a linear search of UITable 20 rows by name; -1 on a miss). When id is nonzero without bit 30 it indexes the palette's dword vector (palette+40; out of range = sub_1403D9570(palette, 0)). When id = 0 the node's own colour dword node+100 (RGBA bytes) is used. Call the result C.
- V (colour x parent, integer, truncating): with a parent P = node+24: node+196 = C.r * P.r / 255, +197 = P.g * C.g / 255, +198 = P.b * C.b / 255 (unsigned integer divide each, so (a*b)/255 truncates), and node+199 (alpha) = (int)((float)(P.a * C.a / 255) * node+108), where node+108 is the node's own opacity float; the (int) is a truncating float-to-int and only the low byte is stored. P.a (parent+199) already contains the parent's opacity, so opacity multiplies down the tree through the alpha byte, not through a separate float. Without a parent: +196/+197/+198 = C.r/g/b, +199 = (int)((float)C.a * node+108).
- V (visible flag): node+204 = node+144 (enabled) != 0 && node+153 != 0 && alpha (+199) != 0 && (no parent || parent+204 != 0).
- V (colour percent): when any of the bytes node+104 / +105 / +106 is not 100, each of R, G, B is replaced by clamp(c * pct / 100, 0, 255) using the colour computed above (integer divide by 100, clamp to 255 then to >= 0). Alpha is not touched. The percent bytes default to 100, so for ordinary nodes this block is skipped.
- V (matrix, only when force != 0 or (visible and node+149 dirty): ; then +149 is cleared): local matrix = GUINode_BuildLocalMatrix (sub_1403F0270) into node+160; with a parent it becomes Matrix2x3_Multiply(node+160, node+160, parent+160) (local applied first, then the parent's world matrix). Then the accumulators: +184 = parent+184 * node+80, +188 = parent+188 * node+84 (accumulated scale x / y), +192 = parent+192 + node+88 (accumulated rotation), +200 = parent+200 + node+92 (accumulated sort order). Without a parent +184/+188/+192/+200 are copies of node+80/+84/+88/+92.
- V (tail): node+205 = node+151; the word at node+150 (two flag bytes, +150 and +151) is cleared. (+150 makes GUINode_ApplyAnimChannels skip the node.)
- I: nothing here snaps or rounds the matrix: translation is the float sum of integer position and pivot (see GUINode_BuildLocalMatrix); the only integer steps are the colour byte divides above.

## State touched

- Calls: [GUINode_BuildLocalMatrix](GUINode_BuildLocalMatrix.md), [Matrix2x3_Multiply](Matrix2x3_Multiply.md)

## Referenced by

- Called by: [GUINode_UpdateSubtree](GUINode_UpdateSubtree.md), [GuideBar_Layout](GuideBar_Layout.md), [GuideBar_LayoutRow](GuideBar_LayoutRow.md), [sub_14013DD70](sub_14013DD70.md)
- Observed behaviours: [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Notes

The name is ours (IDB: sub_1403EFF08). Field map used here (node = runtime GUINode): +24 parent, +52 kind, +56/+60 position (int), +64/+68 size (int), +72/+76 pivot (int), +80/+84 scale (float), +88 rotation (float, radians), +92 sort order (int), +96 colour id, +100 own colour RGBA, +104..+106 colour percent, +108 opacity (float), +144 enabled, +149 dirty, +153 flag, +160 matrix (6 floats), +184..+200 accumulators, +196..+199 final RGBA, +204 visible, +208 first child, +32 next sibling, +40 previous sibling.

## Open questions

What node+153 and +151 / +205 mean; what the palette (UITable 20) colours are; whether (int) of an alpha above 255 can occur (opacity > 1 would wrap the byte).
