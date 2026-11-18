# LegacyCursorRowsLang0

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408FB632`
- **Rows:** about 33 rows of 24 bytes
- **Keyed by:** row index
- **Read by:** [ClassicCursorRows_Select](../functions/ClassicCursorRows_Select.md)
- **Row layout:** [LegacyCursorRowsLang0Row](../structs/LegacyCursorRowsLang0Row.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Cursor row table of a legacy menu, language 0 variant: 24-byte rows holding the cursor x, y and a key; the candidate address is the third halfword of the first row (base + 4). Verdict: designer-data.

## Behavior

- V: reader addresses rows as base + 24 x index with base 0x1408FB62E; 0x320 bytes before the other-language block
- V: ClassicCursorRows_Select (0x14036E28C): picks this block for text language 0 (base 0x1408FB62E) and 0x1408FB94E for the others; reads three halfwords of 24-byte row [index] and updates a cursor

## Notes

Our names. Tags: V reader, ? fields.

## Open questions

- ?: which menu uses it
- ?: exact row count
