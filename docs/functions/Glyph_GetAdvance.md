# Glyph_GetAdvance

- **Address:** `0x140331E60`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `unsigned char Glyph_GetAdvance(int glyphIndex)`
- **Callers:** sub_140220710, sub_140220EA0, EventMessage_Task (two sites)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the pixel advance of a message glyph.

## Behavior

- V: the answer is byte [glyphIndex] of the glyph advance width table (0x140683C50, 2912 entries).
- V: for glyph indexes 2416..2447 that also pass a second test on the index (a row and column split of the index), the answer comes from the 32-byte exception table at 0x140683A28 instead.
- ?: which of the 32 exception glyphs the second test lets through.

## Referenced by

- Reads tables: [GlyphAdvanceWidths](../tables/GlyphAdvanceWidths.md)

## Notes

Read in full (one small function). The main table is addressed relative to the image base, so its absolute address does not appear in the body.

## Open questions

?: what the exception glyphs are (all 32 have the advance 10).
