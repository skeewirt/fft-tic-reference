# GUITextNode_HandleTag

- **Address:** `0x1403DD3A0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool GUITextNode_HandleTag(GUITextLayout *layout, GUITextLayoutState *st)`
- **Callers:** GUITextNode_Layout
- **Callees:** GUITextNode_FinishLine, GUITextNode_PlaceIcon, UITable_GetRow, sub_1400796D0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Executes one in-string control code of a text node (newline, alignment, colour push / pop, size, spacing, icon, soft-hyphen suppression); returns 1 when it was a known code, 0 otherwise.

## Behavior

- V: the code is the dword at st+60. 10 (line feed): GUITextNode_FinishLine. 0xE000 / 0xE001: ++ / -- of byte st+86; 0xE002 / 0xE003: ++ / -- of byte st+87 (nesting counters; their effect in PlaceGlyph, probably bold / italic, was not re-read here: I).
- V (alignment, byte st+85): 0xE004 sets 0, 0xE006 sets 1, 0xE008 sets 2, 0xE00A sets 4; each first calls GUITextNode_FinishLine when the current line has glyphs (st+64 != 0). The odd codes 0xE005, 0xE007, 0xE009, 0xE00B finish the line and restore st+85 = the node's default alignment (byte node+252).
- V (colour, st+84 = stack depth, st+68.. = stack bytes): 0xE00C reads one parameter code point (plane-15 low 16 bits, else 0, sign-extended in the int): a negative value pops (--st+84), otherwise pushes the byte at st[68 + depth] and ++st+84. 0xE00D pops. 0xE00E sets byte st+89 = 1 and 0xE00F sets it to 0 (the flag copied to byte +32 of every glyph record, see PlaceIcon). 0xE010 sets byte st+90 = 1 (soft-hyphen suppress, read by WrapLine).
- V (spacing, offsets): 0xE100 reads a parameter, v = the node font set row (UITable_GetRow(27, st+32)) float +16 when byte g_GUIFontTable+40 is set else +12 (1.0 if no row), and sets st+52 (glyph multiplier f) = param * v / 256. 0xE101 reads two parameters: first * 0.0625 is stored in st+44 and added to the pen st+36, the second * 0.0625 (factor from a register, I) is stored in st+48. 0xE102: one parameter * 0.0625 into st+44 and added to st+36. 0xE103: one parameter * 0.0625 into st+48. 0xE104: one parameter -> GUITextNode_PlaceIcon(layout, st, iconKey).
- V: a parameter is the code point that follows the tag in the string, taken only when (cp & 0xF0000) == 0xF0000 and then its low 16 bits, else 0. The string pointers st+8 (previous) and st+16 (next) are advanced by the decoder sub_1400796D0.
- V: unknown codes return 0 (the caller then treats the code as a printable glyph).

## State touched

- Calls: [GUITextNode_FinishLine](GUITextNode_FinishLine.md), [GUITextNode_PlaceIcon](GUITextNode_PlaceIcon.md), [UITable_GetRow](UITable_GetRow.md)
- Reads: [g_GUIFontTable](../globals/g_GUIFontTable.md)

## Notes

The name is ours (IDB: sub_1403DD3A0). Corrects the sheets GUITextNode_PlaceIcon / WrapLine only by adding the full code map: the icon tag is 0xE104 (V here). The mapping of 0xE004.. to alignment names (left / centre / right ...) is I: values 0, 1, 2, 4 are the node alignment enum, which GUITextNode_FinishLine uses.

## Open questions

? the glyph-level effect of st+86 / +87 (PlaceGlyph not re-read). ? the multiplier constant for 0xE101's second parameter. ? exact meaning of st+44 (probably the left margin of the current line).
