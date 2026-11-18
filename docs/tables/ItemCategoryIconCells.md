# ItemCategoryIconCells

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x1407155B0`
- **Rows:** 40 rows of 2 bytes (rows 0..36 used)
- **Keyed by:** item record category byte (item record +5)
- **Read by:** [sub_140332CD0](../functions/sub_140332CD0.md)
- **Row layout:** [CategoryIconCell](../structs/CategoryIconCell.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Texture position of the category icon drawn beside each shop item row. Verdict: designer-data.

## Behavior

- V: sub_140332CD0 (shop row category text): reads the item's category byte, then table[2 x category] and table[2 x category + 1]
- V: two byte reads at base + 2 x category and +1; 0x58 bytes to the next symbol; the first row is 0, 0 and the last rows look unused
- V: rows 0..36 are used, rows 37..39 are zero padding, row 40 on is another object
- V: the callers are sub_140333974, sub_14036A9D8 and sub_14036C49C (the legacy screens); the Enhanced Outfitter Buy and Sell lists did not change when rows 1..8 were rewritten live

## Notes

Our names. Tags: V reader, I extent.

## Open questions

- ?: how many categories exist (rows 37..39 are padding; a category above 36 reads zero)
