# g_ItemShopMask

- **Kind:** global
- **Address:** `0x14067F890`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint8[512]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which shops sell which item: two bytes per item id 0..0xFF, a mask word whose bit for shop s is 0x8000 >> s. A constant table in read-only data; no code writes it and it is never saved.

## Behavior

- V: the pair is read high byte first: shop 0 is bit 7 of the first byte, shop 7 its bit 0, shop 8 bit 7 of the second byte and shop 14 its bit 1. The second byte's bit 0 is slot 15.
- V: only 15 shops are read (0..14). Slot 15 is set on 253 of the 256 stock ids and no reader tests it.
- V: three functions read the table: Shop_BuildItemList (with the shop bound of 15), sub_14028B510 (the new-item notice) and sub_140344B68 (the new-arrival list).
- V: over the 256 stock ids the shops hold 107, 116, 116, 116, 116, 116, 105, 95, 95, 130, 95, 49, 130, 95 and 130 ids; ids 0, 254 and 255 carry no bit at all.
- V: the table lies in the read-only data section, so a shop's stock cannot be changed in place; Shop_BuildItemList is the single function that turns the bits into the displayed list.

## Referenced by

- Described by tables: [ItemShopMask](../tables/ItemShopMask.md)

## Open questions

? the meaning of slot 15: it is set on every valid id, which suggests a data-tool validity marker rather than a shop.
