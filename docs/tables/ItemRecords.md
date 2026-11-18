# ItemRecords

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x14080EA90`
- **Rows:** 261 records of 12 bytes
- **Keyed by:** item id (ids 0..255 at this address, ids 256..260 in ItemRecordsHigh at 0x140680510)
- **Read by:** [Item_GetRecord](../functions/Item_GetRecord.md)
- **Row layout:** [ItemRecord](../structs/ItemRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The item records the executable keeps for equipment and chemist data. Item_GetRecord is the only code that addresses them.

## Behavior

- V: ids below 0x100 return the first block + 12 * id; ids 0x100 and above return the second block + 12 * (id - 256).
- V: there is no upper bound check in Item_GetRecord.
- I: the price word and the category thresholds of the sub-tables are aligned by hand with this table.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
