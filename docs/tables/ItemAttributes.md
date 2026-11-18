# ItemAttributes

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x14080FEA0`
- **Rows:** 85 rows of 26 bytes
- **Keyed by:** the attribute index of the item record (values from 0x55 up are ignored)
- **Read by:** [Item_BuildAttributeLines](../functions/Item_BuildAttributeLines.md), [sub_1400FA7AC](../functions/sub_1400FA7AC.md), [sub_1402779EC](../functions/sub_1402779EC.md), [sub_140286C8C](../functions/sub_140286C8C.md), [sub_140396984](../functions/sub_140396984.md)
- **Held in:** [g_ItemAttributeTable](../globals/g_ItemAttributeTable.md)
- **Row layout:** [ItemAttributeRow](../structs/ItemAttributeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Equipment attribute records: stat, move and jump bonuses, status groups and elements an item adds to its wearer.

## Behavior

- V: five readers apply a record when a unit equipment is summed.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: meaning of flag25
