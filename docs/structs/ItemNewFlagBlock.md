# ItemNewFlagBlock

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 1007 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The block at g_ItemNewFlags: the shop new-item flags first, then the four Poachers' Den (poach) arrays. The last poach byte is at +0x3EE; g_InventoryCounts begins at +0x3F0, one byte later. The save serialises the five parts from this base and the code addresses the poach parts by literal offsets from it.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="shop_new"></a>`0x0` | shop_new | `uint8[261][2]` | V | Two flag bytes per item id 0..260. One plane is cleared when the item is first sold and the other when it is first obtained (I: the shop badges). |
| <a id="poach_item_num"></a>`0x20A` | poach_item_num | `uint8[97]` | V | Poach stock count per poach item id; the reader in sub_1400D6FB0 stops at 96. |
| <a id="poach_item_get_order"></a>`0x26B` | poach_item_get_order | `uint8[97]` | V | Obtain order of the poach items, read by sub_1401ABE14. |
| <a id="poach_item_sort"></a>`0x2CC` | poach_item_sort | `uint8[97]` | V | Sort position used by the poach list. |
| <a id="poach_item_new"></a>`0x32D` | poach_item_new | `uint8[97][2]` | V | Two flag bytes per poach item, set to the pair 0x01 0x01 at a new game; the last byte is +0x3EE. |

## Behavior

- V: the shop/poach serialiser writes five descriptors from this base: 261 flag pairs at 0, then the 97-byte count, obtain-order and sort arrays at 522, 619 and 716, then the 97 flag pairs at 813.
- V: the save work pack and unpack copy the whole 1007-byte block, and every poach reader and writer uses its literal offset from this base.
- V: the new-game reset writes the shop flag pairs to the pair 0x01 0x01, then clears the three 97-byte poach arrays and sets the 97 poach flag pairs to the same value.
- V: only 272 bytes separate the Poachers' Den stock from this base (0x1411A7700 to 0x1411A7810), so the 261-byte den array cannot grow in place either.

## Referenced by

- Global instances: [g_ItemNewFlags](../globals/g_ItemNewFlags.md)

## Notes

V: the save and poach functions.

## Open questions

? whether the two shop flag planes mean "new in this shop" and "new to the party" as inferred from the clear sites; no code names them. ? the byte at +0x3EF between the last poach flag pair and the inventory counts; no reader and no save field names it.
