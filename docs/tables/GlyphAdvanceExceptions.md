# GlyphAdvanceExceptions

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** Executable
- **Address:** `0x140683A28`
- **Rows:** 32 rows of 1 bytes
- **Keyed by:** glyph index minus 2416 (glyphs 2416..2447)
- **Row layout:** [GlyphAdvance](../structs/GlyphAdvance.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Advance widths of the 32 glyphs 2416..2447, an exception list that Glyph_GetAdvance consults before the main table. All 32 values are 10. Verdict: engine-data.

## Behavior

- V: Glyph_GetAdvance returns this table's byte for glyph indexes 2416..2447 when a second test on the index (a row and column split of the index) also passes; otherwise the main width table answers
- V: the 32-entry extent is the reader's own bound (index minus 2416 below 0x20); other data follows up to the main width table
- ?: what the second test selects (which of the 32 glyphs really use the exception)

## Notes

Our names. Found beside the table at 0x140683A00; tags V extent and reader, ? second test.

## Open questions

None recorded.
