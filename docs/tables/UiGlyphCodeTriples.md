# UiGlyphCodeTriples

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x140680DB0`
- **Rows:** 73 rows of 3 bytes
- **Keyed by:** row index
- **Row layout:** [GlyphCodeTripleRow](../structs/GlyphCodeTripleRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Scan list used to turn a character code 1..72 into a glyph slot (row index). Verdict: engine-data.

## Behavior

- V: the loop breaks at the first row that contains the code; code not found gives row 73, which is then replaced by 0
- V: with a language record that is not Japanese, row 71 is replaced by row 72

## Notes

Our names. Tags: V.

## Open questions

- ?: why each code is repeated three times
