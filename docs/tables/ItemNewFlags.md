# ItemNewFlags

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable memory (saved with the game)
- **Rows:** 261 rows of 2 entries of 1 byte
- **Held in:** [g_ItemNewFlags](../globals/g_ItemNewFlags.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Two flag bytes per item id 0..260, set at a new game; I: the shop 'new item' badges (byte 1 cleared when the item is first sold, byte 0 when it is first obtained). The first 522 bytes of a 1007-byte block whose tail holds the four Poachers' Den (poach) arrays; g_InventoryCounts begins one byte after it.

## Open questions

None recorded.
