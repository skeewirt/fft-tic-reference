# SDFFontRenderer_GlyphIndex

- **Address:** `0x1403A9474`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `unsigned __int16 SDFFontRenderer_GlyphIndex(SDFFontRenderer *r, const unsigned char *utf8)`
- **Callers:** GUITextNode_Draw (0x1403EADDC), sub_1403A9A9C (0x1403A9ABA)
- **Callees:** sub_1403BF9D4 (UTF-8 decode)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps the UTF-8 character at the pointer to the glyph slot of the current font: decodes the code point and looks it up in the font's 65536-entry u16 table; 0 means 'no glyph'.

## Behavior

- V: font = r + 8 * (u32 r+9540) + 64 (the active font slot set by GUITextNode_SetRenderScale); returns 0 when r+189 (renderer ready) is 0. Otherwise it decodes one UTF-8 sequence with sub_1403BF9D4 (up to 6 bytes; a code point above 0xFFFF becomes 9632 = U+25A0) and returns u16 table[codepoint] where table = *(font + 184).
- V: the returned slot indexes the 32-byte glyph records at *(font + 208) used by SDFFontRenderer_EmitGlyph (+8 x offset, +12 y offset, +16 advance, +24..30 atlas x, y, w, h as u16, +20 / +28 / +30 other fields); the atlas size reciprocal is *(font + 224).
- V: sub_1403A9A9C (the advance query used by layout) calls it and returns (scaleX * rec+16, scaleY * rec+20) for the glyph, zero when the glyph is 0.

## Referenced by

- Called by: [SDFFont_GetAdvance](SDFFont_GetAdvance.md)

## Notes

The name is ours (IDB: sub_1403A9474). Called once per glyph. A code point with table entry 0 is silently not drawn. The .fnt-derived table and records are described in docs/reference/fonts.md.

## Open questions

? why rec+20 is multiplied by the y scale in sub_1403A9A9C (it looks like a vertical advance / line term).
