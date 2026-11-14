# SDFFont_GetAdvance

- **Address:** `0x1403A9A9C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `float *SDFFont_GetAdvance(__int64 renderer, float *out, unsigned __int8 *glyphChar)`
- **Callers:** GUITextNode_PlaceGlyph (x2), sub_1403DF09C
- **Callees:** SDFFontRenderer_GlyphIndex

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the scaled advance (x, y) of one character: per-axis renderer scale times the glyph record advance, or (0, 0) when the font is unavailable or the glyph is missing.

## Behavior

- V: font slot = dword at renderer+9540; glyph index v6 = SDFFontRenderer_GlyphIndex(renderer, glyphChar).
- V: valid only if byte renderer+189 != 0 AND v6 != 0; otherwise out = (0.0, 0.0).
- V: glyph record address = the qword at +208 of the font object (the font object is the qword at renderer + 8*slot + 64) plus 32*v6 (32-byte records, array pointer at font+208).
- V: out[0] = *(float*)(renderer+9500) * *(float*)(rec+16); out[1] = *(float*)(renderer+9504) * *(float*)(rec+20). So x advance is rec+16 with x scale +9500, y advance rec+20 with y scale +9504 (separate scales per axis).
- V: returns the out pointer. Xrefs: GUITextNode_PlaceGlyph (two sites 0x1403DD85A, 0x1403DD8D0), sub_1403DF09C, plus data refs at 0x143D40180 / 0x143D4018C.
- I: the advance is the only kerning-like quantity read here: no pair kerning is applied in this function.

## State touched

- Calls: [SDFFontRenderer_GlyphIndex](SDFFontRenderer_GlyphIndex.md)

## Notes

Pairs with the layout code that steps the pen by this advance. Scale +9500/+9504 are the same fields the EmitGlyph sheet calls separate x and y scales.

## Open questions

? whether rec+16 / rec+20 are pre-multiplied by atlas size or in em units (values not sampled).
