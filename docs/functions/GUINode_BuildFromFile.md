# GUINode_BuildFromFile

- **Address:** `0x1403F5A80`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_BuildFromFile(GUIBuildCtx *ctx, FileNode *src, GUINode *dst)`
- **Callers:** UIB loader (not traced)
- **Callees:** GUINode_SetPosition, sub_1403EF6B4, sub_1403EF704, UIName_Key

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies a UIB file node into its runtime GUINode (position, size, pivot, colours, then the type-specific block).

## Behavior

- V: file node +8/+12 origin -> GUINode_SetPosition (runtime +56/+60); +0x44/+0x48 size; +0x1C/+0x20 pivot (runtime +72/+76); +0x50 byte flag.
- V: type 3 (Text): data block = src + *(int*)(src+0x4C) (= +0xB0 in the file): block+64 dword text id -> runtime +248; block+72 int16 size -> +304; block+80 int16 -> +306; block+84 int16 -> +308; block+76/+77/+78 bytes -> +311/+312/+313; src+0x70 (dword index 28) font-set key -> runtime +300. (Colours and alignment are set in other parts of the same function: not mapped here.)
- V: font-set keys in ffto_job_tree.uib: TextBoardJobName Title 60, TextLv/TextLvNum 51; TextBoardJobLv Title/TextLv 98.
- V (Ninegrid, file type 4, runtime kind 4): runtime +224 = the part index (texture reference +8), +228 / +232 / +236 / +240 = the four border ints at data block +0x68 (left, top, right, bottom, layout px), +244 = the fill type from block +0x78 (copied as 0 / 1 / 2 / 3 into +244; 2 and 3 are drawn with UIImage_DrawTiled, 3 with mirrored odd cells), +248 = the byte at block +0x7C. Job tree values: chip BG (10, 8, 10, 8), badge NineGrid00 (10, 10, 10, 10), name plate NineGrid02 (24, 0, 20, 0), all fill type 0.
- V (Rect, file type 6, runtime kind 6): the data block (header +0x4C = its offset) holds the fill RGBA at +8, the outline at +0xC, the opacity (float) at +0x10, the visible flag at +0x20 and the four corner colours (TL, TR, BL, BR) at +0x40..+0x4C; the loader copies the four corner dwords (block dwords 16..19) to runtime +208 / +212 / +216 / +220 and the node colour (fill with alpha x opacity) lands at +196. The same +0x20 byte is the visible flag of a Reference (header +0xC0); runtime +204 mirrors it (live: BGBlur's Rect00 and the Tab / MainTab rects with flag 0 read visible 0 and colour 0).
- V (live read of 12 level boards, debugger, read-only): runtime node layout: +24 parent, +32 next sibling, +48 object id, +52 kind (1 layer, 3 text, 4 ninegrid, 12 component reference), +56/+60 position (int32), +64/+68 size (int32), +72/+76 pivot (int32), +80/+84 scale (float), first child +208; a component object embeds its own geometry node at +272 (its children start at +480). Live TextBoardJobLv root: pos (0,-2) size 40x24 pivot (20,12) although the file says 40x20; its Title text node is 14x24 (file 14x20): sizes and the root are re-fitted after the build (the code that does it was not located; the font line height gives the same 24).
- V (file type -> runtime kind, from the switch): 7 -> 7 (ellipse), 8 -> 8 (bezier), 9 -> 13 (collision), 10 (the default branch) -> 12 (component reference), 11 -> 10, 13 -> 9 (Mask); each branch returns when the node's runtime kind (+52) is not the one it expects.
- V (Mask, file type 13, runtime kind 9; how it is used, from a live backtrace of the title text draw): ComponentEffects_Collect finds the Mask node in the component's property block, resolves the component it names and ComponentLayer_Begin draws that component (TextBoard01) into a separate layer through ComponentLayer_DrawMaskComponent; the mask node supplies the placement (its position, size and scale feed ComponentDrawContext_ComputeMatrix). V: the node's own name key is stored at +216, a second name key from the string at header +0xA0 at +248 (live and file: 'TextBoard01' for TextMask/MaskNode00), and +264 / +288 are refreshed from the key's table row; when the data block's count (block +0x44) is positive the first entry's name replaces +216 and its int goes to +232. The kind 9 node itself has no draw in GUINode_DrawChildren (the dispatch ignores it), so it is a name binding: MainTab_BindNodes finds the Title text node of the component this name selects.
- V (file type 11 -> runtime kind 10): one name key, taken from the string at header +0x74 + its offset, is stored at +208 (the kind-10 draw, sub_1403ED7D0, looks it up in the widget's resource vector).

## State touched

- Calls: [GUINode_SetPosition](GUINode_SetPosition.md), [UIName_Key](UIName_Key.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GUINode_LoadTree](GUINode_LoadTree.md)

## Notes

Also the target of state keyframes (sub_1403F6FC0 applies per-property records to the same runtime fields).

## Open questions

Other node types (Image, Layer, Collision, kind 10) are branches of the same function and are only partly documented here; what the kind 10 resource is called in the file format.
