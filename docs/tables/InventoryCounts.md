# InventoryCounts

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable memory (saved with the game)
- **Rows:** 261 entries of 1 byte
- **Held in:** [g_InventoryCounts](../globals/g_InventoryCounts.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The party's inventory: one count per item id 0..260, saved with the game. Written by Inventory_AddCount, Inventory_AddWithOverflow, Inventory_ReturnItem, the starting items and the event and battle code.

## Open questions

None recorded.
