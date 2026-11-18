# CharGridOrder

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x1406847B0`
- **Rows:** 97 rows of 1 bytes
- **Keyed by:** grid cell 0..96 (cursor index)
- **Row layout:** [CharGridCell](../structs/CharGridCell.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which symbol each cell of the 97-cell character selection grid shows. Verdict: designer-data.

## Behavior

- V: sub_1403325E4 (task that opens a selection grid): for each of 97 cells stores table[i] + 0xBFFF (0xC000 plus the zero-based symbol) into the cell word list
- V: OpeningTask_7: reads the symbol under the cursor cell (cursor index word)
- V: 97 loop bound in the builder; all values distinct and 1..97 (checked on the bytes); candidate begins exactly at base + 2912 of the glyph table

## Notes

Our names. Tags: V layout, I that it is a name or text-entry grid.

## Open questions

- ?: which screen shows the grid (the readers are the opening-sequence tasks)
