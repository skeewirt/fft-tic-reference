# GUITextNode_Draw

- **Address:** `0x1403EA0B0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUITextNode_Draw(GUIDrawCtx *ctx, GUIDrawState *st, GUITextNode *node)`
- **Callers:** UI draw pass (virtual)
- **Callees:** GUIFontTable_GetSetRow, sub_1403EE35C, GUIFontRenderer_UploadPalette, sub_1403A94C8, UITable_GetRow, SDFFontRenderer_EmitGlyph

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one text node: builds the shader palette from the node's UIFontSet row and colours, then emits glyph quads (and the shadow pass) through SDFFontRenderer.

## Behavior

- V: row = GUIFontTable_GetSetRow(node+300); the 80-byte row is copied into the palette block and its four colour slots (+8, +16, +28, +40) are blended with the node's colours (node +264..+292) by sub_1403EE35C and the draw alpha.
- V: the block goes to GUIFontRenderer_UploadPalette (sub_1403EDEA4); each glyph is emitted by sub_1403A94C8 with the scale set by GUITextNode_SetRenderScale.
- V (TEXT PLACEMENT, decoded 2026-10-28; Draw does NOT lay anything out, it only reads what GUITextNode_Layout stored): the node holds a glyph vector at +328 (36-byte records: +0 x, +4 y, +8 width, +12 size multiplier f, +20 char, +24 line index) and a line vector at +360 (24-byte records: +0 x, +4 y, +8 width, +12 height, +16 x-squeeze, +20 flag). Per glyph Draw computes the pen y as line.y + rec.y + (UIFontType row +8 / 64) * size * rec.f, then the pen x as line.x + rec.x (lines 429-492 of the pseudocode: v77 = line+4 + rec+4, v78 = rec+0 + line+0, v92 = (row27[+8] * 1/64) * (size * rec.f) + v77), and maps (x, y) through the node matrix (node+160 times the draw state +504). SDFFontRenderer_EmitGlyph then places the quad at pen + (glyph.x0, glyph.y0) * size/64 (y0 is relative to the baseline), so the pen y IS the baseline.
- V (live read of the Job Tree digit node, 2026-10-28, ReadProcessMemory only): the node is W 18 x H 20, size 23, node+252/+256/+260 = 4 / 2 / 1; its line record is (x 0.0, y -3.0, width 13.80, height 23.0, squeeze 1.0, flag 0) and its single glyph '8' (56) is (x 0, y 0, width 13.80, f 1.0). So line.y = H - size = 20 - 23 = -3 exactly as the rule below predicts.
- V (VERTICAL RULE; GUITextNode_Layout -> sub_1403DDED8 / sub_1403DE4D0): inside the node (origin = top-left of the node box, layout px) a line's y starts at the running cursor (node-local 0 for the first line; each finished line adds size + int16 node+308, where size = int16 node+304 and NOT the font's line height); the line record height is size. After all lines are built sub_1403DE4D0 adds an offset to every line.y with content = last.y + last.height and H = int32 node+68: node+256 = 0 top: +0; 1 middle: +(H - content) / 2; 2 bottom: +(H - content); 3 distribute: +(H - content) / (nLines - 1) * i, and a single line gets (H - content) / 2. The offset is negative when the text is taller than the box (size 23 in H 20 gives -3 for bottom, -1.5 for middle). Baseline in node-local y = verticalOffset + (UIFontType.Unknown8 / 64) * size  (for one line, f = 1).
- V (font term): the 'row +8' read by Draw (line 484-489) and sub_1403DDED8 is the in-memory row of nxd table 27 (UIFontType) as a raw record [DLCFlags +0][FontPath string offset +4][Unknown8 +8][UnknownC +12][Unknown10 +16][Unknown14 +20] (live: rows are 24 bytes, e.g. Jura = 0, 0x2xx, 56.0, 1.0, 1.0, 0.0). So the factor is Unknown8 / 64 = 56/64 = 0.875 for Jura SemiBold (type 6), 50/64 for Zilvertype (5), 55/64 for Bunyan (0), the nominal 'size' number and NOT the .fnt ascent (Jura ascent 62, descent 14, line height 76). The row offsets GUITextNode_Layout uses (+12 / +16 / +20 as the f multiplier, the alternate f and the 'size multiplier') are therefore UnknownC / Unknown10 / Unknown14 (1.0, 1.0, 0.0), one dword later than that page labels them; f = UnknownC = 1.0 for every row, and UnknownC * ... never changes the baseline (the f terms cancel: Layout adds K*size*(1 - f), Draw adds K*size*f).
- V (HORIZONTAL RULE; sub_1403DDED8): line.x = 0 for node+252 = 0 (left) and for 4 (auto: becomes left unless the soft-wrap flag st+88 set by GUITextNode_WrapLine (sub_1403DE608) is on, in which case it is justified; without it, right only if layout+122, which is always 0), (W - lineWidth) / 2 for 1 (centre), W - lineWidth for 2 (right), 3 = distribute (extra space / (glyphs - 1) between glyphs); lineWidth = max(rec.x + rec.width) of the line, W = int32 node+64. Glyph rec.x = pen cursor + kerning; the pen advances by advance * (size / 64) * f (the .fnt advance in metric units), so rec.width = advance * size/64. Overflow node+260 = 2 (shrink): when lineWidth > W every glyph x and width is multiplied by W / lineWidth (stored as line+16 and applied again by Draw to the glyph scale x), lineWidth becomes W; = 3 sets the line flag only (not traced); 0 / 1 do nothing here.
- V (UIB mapping, GUINode_BuildFromFile type 3): text block dwords: +64 text id, +68 string offset, +72 int16 size (-> +304), +76/+77/+78 bold / italic / (+313 flag), +80 int16 -> +306, +84 int16 -> +308 (line spacing), +88 -> node+256 vertical, +92 -> node+252 horizontal, +96 -> node+260 overflow. So the quoted metrics list [1073, 70422, 1, 0, 0, 2, 4, 1] (text id, string offset, bold byte, +306, +308, VERTICAL 2, HORIZONTAL 4, OVERFLOW 1; the size 23 sits in the dword between) means: vertical = bottom, horizontal = auto (left), overflow 1. TextLv [1072, 70118, 1, 0, 0, 2, 4, 2] = bottom, auto/left, overflow 2 (shrink to fit).
- V (test cases, layout px from the node top, font Jura SemiBold, H 20 for both boxes): TextLv size 20: line.y = 20 - 20 = 0, baseline = 0 + 0.875 * 20 = 17.5. TextLvNum size 23: line.y = 20 - 23 = -3 (live), baseline = -3 + 0.875 * 23 = 17.125. The studio's baseline-middle shortcut (centre at origin.y + size / 2, baseline 24/64 * size below it) is origin.y + 0.875 * size = 17.5 / 20.125, so it agrees for the prefix (offset 0 because size = H) and puts the digit 3.0 layout px too low, i.e. 2.0 screen px at scale 2/3.
- V (EARLY-OUT GATES, disassembly of the entry, 2026-10-31): the function returns without drawing unless, in order, byte node+0xCC is non-zero, byte node+0x91 is zero, the string size qword at node+0xE8 is non-zero and sub_1403DBA94(font table, font set) returns true; r15 = node for the whole body (so r15 still names the node at SDFFontRenderer_EmitGlyph entry), r14 = ctx and rbx = st. Draw is therefore called for nodes it skips; 'Draw was called' is not evidence of drawing.
- I: the node-local origin of (x, y) is the node's top-left corner (the node matrix at node+160 carries position and pivot; not decoded). Draw's right-edge fade (line 433-442: alpha falls off when a glyph's x passes W - size/2, for lines whose flag byte is set) was read but not exercised, so it is ? for these nodes.

## State touched

- Calls: [GUIFontTable_GetSetRow](GUIFontTable_GetSetRow.md), [GUIFontRenderer_UploadPalette](GUIFontRenderer_UploadPalette.md), [UITable_GetRow](UITable_GetRow.md), [SDFFontRenderer_EmitGlyph](SDFFontRenderer_EmitGlyph.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md), [g_GUIFontTable](../globals/g_GUIFontTable.md), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Appears in flows: [BattleMessageBanner](../flows/BattleMessageBanner.md)
- Called by: [GUINode_DrawChildren](GUINode_DrawChildren.md)
- Observed behaviours: [TextNodeDrawGate](../behaviors/TextNodeDrawGate.md)

## Notes

Placement formula (node-local layout px, one line): baseline_y = voff + Unknown8/64 * size with voff = 0, (H - size) / 2 or (H - size) for node+256 = 0, 1 or 2, H = node+68, size = int16 node+304; left_x = 0 (node+252 = 0 or 4), (W - w) / 2 (1), W - w (2). Measured by the owner: the retail digit sits about 1.25 screen px above the studio's baseline-middle; the rule gives 3.0 layout px = 2.0 screen px at scale 2/3 (live line.y = -3.0 confirms the 3.0), so either the retail estimate is low or the node scale is not exactly 2/3: not resolved. The font's own ascent / descent / line height are not used by placement at all (only the glyph quad offsets y0 / x0 from the .fnt are).

## Open questions

Where the node matrix (node+160) gets its translation (position minus pivot, scale +80/+84) is not traced. Overflow mode 3 and the line flag byte (line+20) are not traced.
