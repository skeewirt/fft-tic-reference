# SDFFont_GetKerning

- **Address:** `0x1403A9114`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `float *SDFFont_GetKerning(SDFFontRenderer *R, float out[2], unsigned __int16 leftCp, unsigned __int16 rightCp)`
- **Callers:** GUITextNode_PlaceGlyph
- **Callees:** sub_1403BA2D4 (AdditionalKerning_Lookup)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Kerning pair lookup: returns (x, y) kerning for a left / right code point pair of the current font, from the font's own kerning rows plus the second .ker table.

## Behavior

- V: font = qword at R + 8 * dword(R + 9540) + 64. gidR = u16 font[23][rightCp], gidL = u16 font[23][leftCp] (code point -> glyph id table).
- V: glyph record = font[26] + 32 * gidL; when its u16 +2 (row count) is 0 the result row is zero. Otherwise a binary search over the rows at font[27] + 12 * (dword +4): row.first (u16 +0) >= gidR stops, then gidR < row u16 +2 goes left; the hit row supplies qword +0 and dword +8, the x / y values (float at +4 and dword +8).
- V: when font[25] (the .ker table object) is non-null: sub_1403BA2D4(font[25], tmp, gidL, gidR) is looked up and ADDED: x += tmp.x, y += tmp.y. out = (x, y).

## State touched

- Calls: [AdditionalKerning_Lookup](AdditionalKerning_Lookup.md)

## Notes

Name proposed (IDB: sub_1403A9114); matches docs/reference/fonts.md 'Kerning tables'. The row order note (u16 +0 is the last gid, +2 the first, per live check) is in fonts.md.

## Open questions

? as in fonts.md: the exact .ker file offsets (every shipped .ker is 40 bytes, zero records).
