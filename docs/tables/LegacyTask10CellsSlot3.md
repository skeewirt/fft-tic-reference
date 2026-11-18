# LegacyTask10CellsSlot3

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x140900020`
- **Rows:** 24 rows of 12 bytes
- **Keyed by:** cell index
- **Row layout:** [UiSpriteCell](../structs/UiSpriteCell.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sprite cell list of the legacy scene task 10, language 0, variant 3. Verdict: designer-data.

## Behavior

- V: 16 slots in memory order language x 4 + variant; slot 0 holds 28 cells (0x150 bytes), the other 15 hold 24 cells (0x120 bytes); the reader picks the variant from two page flags and the language from the text language (verified for all 16 addresses)
- V: sub_140399A64 (0x140399A64): picks the cell slot by text language (0..3) and the page variant (0..3) from two page flags

## Notes

Our names. Tags: V reader, I variant meaning.

## Open questions

- ?: what the four variants (two page flags) are
