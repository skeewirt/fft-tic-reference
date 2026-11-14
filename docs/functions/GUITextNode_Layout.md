# GUITextNode_Layout

- **Address:** `0x1403DCF90`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GUITextNode_Layout(GUITextLayout *layout, GUITextNode *node)`
- **Callers:** sub_1403F1234 (call at 0x1403F12B7)
- **Callees:** GUIFontTable_GetSetRow, GUIFontSet_FontTypeForLanguage, sub_1403DBD60, GUITextNode_SetRenderScale, sub_1403DD3A0, sub_1403DD780, sub_1403DE4D0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Lays out one text node: resolves its font from the node's UIFontSet id and the game language, sets the glyph scale, then walks the string (colour/size tags) placing glyphs.

## Behavior

- V: reads the UIFontSet key from node+300 and fetches the 80-byte row with GUIFontTable_GetSetRow (the singleton at qword_143CDAA48).
- V: the UIFontType id comes from GUIFontSet_FontTypeForLanguage(row); if it is >= 18 or the font slot table qword_143CDA288[16*id+145] is 0 the node is not drawn.
- V: per-type floats come from the UIFontType table via UITable_GetRow(27, typeId): +12 (UnknownC; +16 = Unknown10 instead when qword_143CDAA48+40 is set) is stored in the layout state as the per-glyph multiplier f, +20 (Unknown14) is the size multiplier. The nominal size Unknown8 (+8) is not read here (GUITextNode_FinishLine reads it for the baseline term).
- V (corrected 2026-10-28 by the GUITextNode_PlaceGlyph decode): size * UIFontType.Unknown14 + int16 node+306 is NOT the glyph size; it is the per-glyph x spacing stored at st+56 and added to each glyph's x from the second glyph on (the second term is 0 unless the node's data block sets it; forced to 0 for node+315 and a non-Japanese language). The glyph size is int16 node+304 (render scale = size / 64). Live: the Job Tree title and the chip prefix show no extra spacing.
- V: calls GUITextNode_SetRenderScale, then loops sub_1403D8510 / sub_1403DD3A0 (tag handling; 0xE104 places an inline icon via GUITextNode_PlaceIcon) / GUITextNode_PlaceGlyph over the string, then GUITextNode_AlignVertical; it also resets the glyph / line vectors and the bounds, sets the language flags layout+120..124 (Korean maps alignment 4 to 0), moves out and finally releases the icon reference vector at layout+64, and writes layout+96 (1 or 3, 2 when the font is unusable).

## State touched

- Calls: [GUIFontTable_GetSetRow](GUIFontTable_GetSetRow.md), [GUIFontSet_FontTypeForLanguage](GUIFontSet_FontTypeForLanguage.md), [GUITextNode_SetRenderScale](GUITextNode_SetRenderScale.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md), [g_GUIFontTable](../globals/g_GUIFontTable.md), [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Appears in flows: [BattleMessageBanner](../flows/BattleMessageBanner.md)
- Called by: [GUITextNode_UpdateLayout](GUITextNode_UpdateLayout.md)

## Notes

Text node runtime layout (V from sub_1403F0E24, sub_1403F5A80): +248 text id (UI-en key), +300 UIFontSet key, +304 int16 size, +306/+308 int16 extras, +310..+315 flags. See docs/reference/labels.md and fonts.md.

## Open questions

The SDF shader (SDFFontRenderer) that applies the UIFontSet threshold/outline parameters is not decompiled (?).
