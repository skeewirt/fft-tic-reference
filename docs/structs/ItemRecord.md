# ItemRecord

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 12-byte record of an item (Item_GetRecord): icon, level, equipment slot bits, equipment category, attribute index, price and the story progress it is sold from. Ids 0..255 and 256..260 sit in two arrays.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by |
|---|---|---|---|---|---|
| <a id="icon_palette"></a>`0x0` | icon_palette | `uint8` | I | Palette row of the item icon (clamped to 15). |  |
| <a id="icon"></a>`0x1` | icon | `uint8` | I | Icon tile of the item. |  |
| <a id="level"></a>`0x2` | level | `uint8` | I | Level the item is offered from; compared with a unit level when the best equipment is picked. |  |
| <a id="slot_flags"></a>`0x3` | slot_flags | `uint8` | V | Equipment slot bits: 0x80 weapon, 0x40 shield, 0x20 head, 0x10 body, 0x08 accessory (which sub-record the code reads under each bit: V; the slot names: I); 0x02 skips the item in the best-equipment pick; bit 0x01 is tested by sub_14030BF04 (breakable equipment, I). |  |
| <a id="byte4"></a>`0x4` | byte4 | `uint8` | ? | No reader found near the record accessor. |  |
| <a id="equip_category"></a>`0x5` | equip_category | `uint8` | V | Equipment category: the bit index into the job's equipment flags that Item_CanUnitEquip reads; 19 puts a hand item into the shield slot (PartyUnit_ReloadEquipment). | [Item_CanUnitEquip](../functions/Item_CanUnitEquip.md), [Item_CanUnitEquipPreview](../functions/Item_CanUnitEquipPreview.md), [sub_14028B354](../functions/sub_14028B354.md) |
| <a id="byte6"></a>`0x6` | byte6 | `uint8` | ? | No reader found near the record accessor. |  |
| <a id="attribute"></a>`0x7` | attribute | `uint8` | V | Index of a 26-byte equipment attribute record; the five readers ignore values from 0x55 up. |  |
| <a id="price"></a>`0x8` | price | `uint16` | V | Price; Item_SellPrice (Item_SellPrice) returns half of it (at least 1). | [Item_SellPrice](../functions/Item_SellPrice.md), [ShopEntry_Fill](../functions/ShopEntry_Fill.md), [sub_140287D9C](../functions/sub_140287D9C.md), [sub_14028B354](../functions/sub_14028B354.md), [sub_1402EEC2C](../functions/sub_1402EEC2C.md) |
| <a id="shop_progress"></a>`0xA` | shop_progress | `uint8` | V | The item is listed in a shop only while this is not above event variable 111 (Shop_BuildItemList); I: story progress. | [Shop_BuildItemList](../functions/Shop_BuildItemList.md), [sub_14028B510](../functions/sub_14028B510.md) |
| <a id="byte11"></a>`0xB` | byte11 | `uint8` | ? | No reader found near the record accessor. |  |

## Behavior

- V: the item's category (and so which sub-record it has) is not in the record: Item_FindCategoryIndex derives it from the item id (first-id thresholds).

## Referenced by

- Described by tables: [ItemRecords](../tables/ItemRecords.md)
- Indexed by registries: [ItemCategories](../registries/ItemCategories.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
