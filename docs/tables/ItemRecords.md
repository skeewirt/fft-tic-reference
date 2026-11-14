# ItemRecords

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Rows:** 261 records of 12 bytes
- **Keyed by:** item id
- **Read by:** [Item_GetRecord](../functions/Item_GetRecord.md)
- **Row layout:** [ItemRecord](../structs/ItemRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The item records the executable keeps for equipment and chemist data: ids 0..255 in one block, ids 256..260 in a second block of five. Item_GetRecord is the only code that addresses them.

## Behavior

- V: ids below 0x100 return the first block + 12 * id; ids 0x100 and above return the second block + 12 * (id - 256).
- V: there is no upper bound check in Item_GetRecord.

## Open questions

None recorded.
