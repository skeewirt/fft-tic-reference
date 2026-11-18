# ItemCategoryFirstIds

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x1406804E0`
- **Rows:** 14 rows of 2 bytes
- **Keyed by:** category index 0..13
- **Read by:** [Item_CategoryFirstId](../functions/Item_CategoryFirstId.md), [Item_FindCategoryIndex](../functions/Item_FindCategoryIndex.md)
- **Row layout:** [ItemCategoryFirstIdRow](../structs/ItemCategoryFirstIdRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

First item id of every category: Item_FindCategoryIndex returns the last category whose first id is not above the item id (entries 1..12 are compared).

## Behavior

- V: ids 0xFE, 0xFF and above 0x104 are rejected before the lookup, so category 13 is unreachable.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
