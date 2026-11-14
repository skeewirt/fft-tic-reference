# ItemOrderLists

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The ten saved item order lists: 16-bit words in static storage, no header and no length word. Five item-menu lists (A0..A4) sit in scattered arrays reached through one pointer table; five equip and obtain-order lists (B0..B3 and B4) form one contiguous block. The save carries A as five copies and B as one 1010-byte copy.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="item_user_sort"></a>`0x8A6C` | item_user_sort | `uint16[141]` | V | Item-menu order, group 0 (weapons and shields). Live at 0x1407B2550, 282 bytes; 139 stock ids can enter it, so two entries are spare. |
| <a id="item_user_sort2"></a>`0x8B86` | item_user_sort2 | `uint16[30]` | V | Item-menu order, head. Live at 0x1407B2678, 60 bytes; 29 stock ids, one spare. |
| <a id="item_user_sort3"></a>`0x8BC2` | item_user_sort3 | `uint16[38]` | V | Item-menu order, body. Live at 0x1407B24B0, 76 bytes; 37 stock ids, one spare. |
| <a id="item_user_sort4"></a>`0x8C0E` | item_user_sort4 | `uint16[34]` | V | Item-menu order, accessory. Live at 0x1407B2500, 68 bytes; 33 stock ids, one spare. |
| <a id="item_user_sort5"></a>`0x8C52` | item_user_sort5 | `uint16[21]` | V | Item-menu order, thrown weapons. Live at 0x1407B26B8, 42 bytes; six stock ids, fifteen spare. |
| <a id="equip_user_sort_hand"></a>`0x8C7C` | equip_user_sort_hand | `uint16[141]` | V | Equip-screen order for the hand, with the same membership as the first item-menu list. Live at 0x141874540. |
| <a id="equip_user_sort_head"></a>`0x8D96` | equip_user_sort_head | `uint16[30]` | V | Equip-screen order for the head. Live at 0x14187465A. |
| <a id="equip_user_sort_armor"></a>`0x8DD2` | equip_user_sort_armor | `uint16[38]` | V | Equip-screen order for the body. Live at 0x141874696. |
| <a id="equip_user_sort_accessory"></a>`0x8E1E` | equip_user_sort_accessory | `uint16[34]` | V | Equip-screen order for the accessory slot. Live at 0x1418746E2. |
| <a id="item_get_order_sort"></a>`0x8E62` | item_get_order_sort | `uint16[262]` | V | Obtain order, the only list with the whole id range as its membership. Live at 0x141874726, 524 bytes; 258 stock ids, four spare. |

## Behavior

- V: the end of every list is a word equal to 0xFF (255) or at least 0x105 (261). Ids 0..254 and 256..260 are therefore storable and only 255 is not, although 0xFFFF is the terminator of the separate menu list.
- V: no list stores a length. The initialiser writes the 0xFF terminator into all ten, zeroes the whole B block from a zeroed 1010-byte template and then rewrites six of the eight sort-field byte lists.
- V: the five A lists are reached through the pointer table at 0x14067F498 (a second table at 0x140689C38 holds the same five pointers); the B lists through the table at 0x14067FA90, and the obtain-order list starts 0x1E6 bytes into the block.
- V: the membership writers insert a newly owned id at index 0 and shift the tail right with no capacity check. A3 ends flush against the mode-1 sort bytes and A1 has only two spare words before A4, so one word too many changes a neighbour rather than a spare entry.
- V: the save pack writes A0..A4 as five fixed-size copies at 0x8A6C, 0x8B86, 0x8BC2, 0x8C0E and 0x8C52, and the whole B block as one 1010-byte copy at 0x8C7C; the load and the repair pass read the same six.
- V: a second syncer (sub_14039684C) maintains the same lists from the inventory snapshot instead of the live counts, and reaches the obtain-order writer by a tail jump.
- I: the stock id counts (139, 29, 37, 33, 6 and 258) leave 2, 1, 1, 1, 15 and 4 spare, so a stock save cannot exercise the insert-without-capacity path.

## Referenced by

- Observed behaviours: [OrderInsideItemGroup](../behaviors/OrderInsideItemGroup.md)

## Notes

V: the list table, the save copies, the initialiser and the adjacency, with the sheets of the eleven writers and copiers.

## Open questions

? the purpose of the 12-byte table at 0x1407B26F0 that the initialiser writes next to the lists; no order-list function reads it.
