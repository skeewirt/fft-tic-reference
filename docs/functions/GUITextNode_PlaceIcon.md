# GUITextNode_PlaceIcon

- **Address:** `0x1403DDC38`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUITextNode_PlaceIcon(GUITextLayout *layout, GUITextLayoutState *st, unsigned int iconKey)`
- **Callers:** sub_1403DD3A0 (tag handler, tag 0xE104)
- **Callees:** UITable_GetRow, sub_1403DB6B8, SDFFontRenderer-side shear helper sub_1403A942C (SDFFont_ItalicShearWidth), sub_1401CBD68 (glyph vector grow), sub_1403DA594, sub_1403DA918, sub_14006635C (reference vector grow), GUITextNode_WrapLine

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Places an inline icon (an Icon table image) in the text flow as a glyph record of width size * f with char 0, requests its texture slot, and wraps the line when it does not fit.

## Behavior

- V (arguments): iconKey (a3) = the low 16 bits (sign-extended) of the code point that follows the tag, taken only when the code point is in plane 15 (code point & 0xF0000 == 0xF0000), else 0. The call is made from sub_1403DD3A0 (the in-string tag handler) for tag code 0xE104 (the branch of the 0xE100..0xE104 group where the decompile subtracts 0xE100 three times and compares the result to 1). Nothing happens when iconKey is 0 or UITable_GetRow(118, iconKey) (the Icon table, see Icon_FormatPath) returns null.
- V (locals): xe = st+56 (x extra, per-glyph spacing), W = (float)(int32 node+64), w = (float)(int16 node+304) * st+52 (f) = icon width, slot = sub_1403DB6B8(g_GUIFontSlots, iconKey) (texture slot id of the icon: keys 50..71 and 1100..1265 go through the two range helpers sub_1403DB420 / sub_1403DB5B4, other keys through a name lookup sub_1403DB140 / sub_1403DB280).
- V (x): off = 0; if st+64 != 0 (not the first glyph of the line) off = xe, and when the renderer shear (R+9524, R = qword_143CDA098 + 37944) > 0 and the last glyph record's italic byte (+29) is set, off += S * last.f with S = SDFFont_ItalicShearWidth. x = off + st+36 (pen).
- V (glyph record, 36 bytes): +0 x, +4 y = st+48, +8 width = w, +12 f = st+52, +16 dword slot id, +20 u16 char = 0 (this is what marks an icon record; GUITextNode_WrapLine never breaks next to one), +22 u16 ordinal = glyph count before the append, +24 u16 line index = current line count, +26 byte colour index (st[67 + st+84], 0 when st+84 = 0), +27..+31 = 0 (so bold and italic are off), +32 byte st+89.
- V (reference list): a 16-byte entry is appended to the second vector at layout+64 (allocator +64, begin +72, end +80, cap +88): dword +0 iconKey, dword +4 slot, dword +8 = Icon row dword +12 (UnknownC), dword +12 = 0. If the slot record (sub_1403DA594(slots, slot)) exists and its refcount (+80) is exactly 1, entry +4 is replaced by the handle returned by sub_1403DA918 (a texture slot acquire / load request using the slot's path at +56). GUITextNode_Layout moves this vector out at the start of each layout and releases entry +4 and +12 (sub_1403DA30C) when it ends.
- V (pen): st+64 += 1; st+36 += off + w.
- V (wrap): when node+260 = 0 and x + w > W it calls GUITextNode_WrapLine(layout, st).

## State touched

- Calls: [UITable_GetRow](UITable_GetRow.md), [SDFFont_ItalicShearWidth](SDFFont_ItalicShearWidth.md), [GUITextNode_WrapLine](GUITextNode_WrapLine.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [GUITextNode_HandleTag](GUITextNode_HandleTag.md)

## Notes

The name is ours (IDB: sub_1403DDC38). The icon's height is not stored; the bounds code (GUITextNode_ComputeBounds) uses size * f for every record. Not exercised by plain upright text.

## Open questions

? the exact tag byte sequence for 0xE104 in the UI strings and which Icon rows are used inline (the key range / the Icon table's row dword +12). ? how GUITextNode_Draw renders a char-0 record (reads +16 slot?). ? the semantics of sub_1403DB6B8 / sub_1403DA594 / sub_1403DA918 were only skimmed (slot lookup, refcount check, load request). ? the tag number 0xE104 was derived from the decompiled subtraction chain, not checked against a string.
