# GlyphAdvanceWidths

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** Executable
- **Address:** `0x140683C50`
- **Rows:** 2912 rows of 1 bytes
- **Keyed by:** glyph index (message text code)
- **Read by:** [Glyph_GetAdvance](../functions/Glyph_GetAdvance.md)
- **Row layout:** [GlyphAdvance](../structs/GlyphAdvance.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Advance width of each message glyph (the proportional-font metrics of the legacy text drawer). Verdict: engine-data.

## Behavior

- V: Glyph_GetAdvance: returns table[glyph index], or the exception table byte for the 32 glyphs 2416..2447
- V: sub_1403325E4 and OpeningTask_7 read the table 0xB60 (2912) bytes after this address: that is the next table
- V: single reader reads byte [index]; the neighbouring reader addresses base + 2912 for the next table (0x1406847B0), so the extent is 2912 bytes; values 4..10

## Notes

Our names. Tags: V extent, V reader, I meaning.

## Open questions

- ?: whether the HD text path still uses these widths
