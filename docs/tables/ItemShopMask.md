# ItemShopMask

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x14067F890`
- **Rows:** 256 rows of 2 bytes
- **Keyed by:** item id 0..0xFF
- **Read by:** [Shop_BuildItemList](../functions/Shop_BuildItemList.md), [sub_14028B510](../functions/sub_14028B510.md)
- **Held in:** [g_ItemShopMask](../globals/g_ItemShopMask.md)
- **Row layout:** [ItemShopMaskRow](../structs/ItemShopMaskRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which shops sell which item: a mask word whose bit for shop s is 0x8000 >> s. A constant table in read-only data; no code writes it and it is never saved.

## Behavior

- V: shop = town shop index (I).

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
