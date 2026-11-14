# Item_SellPrice

- **Address:** `0x1402874A8`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int Item_SellPrice(uint16_t id)`
- **Callers:** Inventory_AddWithOverflow, Inventory_SellOverflow, ShopEntry_Fill, sub_1402D5FE4, sub_14036C468 (five direct sites)
- **Callees:** Item_GetRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the gil a shop pays for one unit of an item: half its record price, with a floor of one.

## Behavior

- V: A zero id returns zero without touching the record table.
- V: It masks the id to ten bits (0x3FF) and reads the price word at record +8.
- V: It halves the price and raises a zero result to one, so a priced item never sells for nothing.
- V: It calls the record accessor only and has five direct callers.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md)
- Reads: [ItemRecord.price](../structs/ItemRecord.md#price)

## Referenced by

- Called by: [Inventory_AddWithOverflow](Inventory_AddWithOverflow.md), [Inventory_SellOverflow](Inventory_SellOverflow.md), [ShopEntry_Fill](ShopEntry_Fill.md), [sub_1402D5FE4](sub_1402D5FE4.md), [sub_14036C468](sub_14036C468.md)

## Notes

- V: whole body read.

## Open questions

None recorded.
