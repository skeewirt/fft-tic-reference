# ShopEntry

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One entry of a shop item list (buy, sell or equip), built per list index by ShopEntry_Fill from word_141811470 and drawn by ShopItemList_DrawRow.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="item_id"></a>`0x0` | item_id | `uint32` | V | The list word masked with 0x3FF (ShopEntry_InitFromList). | [ShopEntry_Fill](../functions/ShopEntry_Fill.md), [ShopItemList_FillRow](../functions/ShopItemList_FillRow.md) | [ShopEntry_InitFromList](../functions/ShopEntry_InitFromList.md) |
| <a id="list_index"></a>`0x8` | list_index | `int32` | V | Index into word_141811470. |  |  |
| <a id="equipped"></a>`0xC` | equipped | `int32` | V | Item_CountEquippedByParty of the list word; the equip mode adds the selected unit's matching equipment words. |  | [ShopEntry_InitFromList](../functions/ShopEntry_InitFromList.md) |
| <a id="owned"></a>`0x10` | owned | `int32` | V | Item_CountTotal of the list word; 99 or more shows the count in red outside the sell mode. | [ShopItemList_DrawRow](../functions/ShopItemList_DrawRow.md) | [ShopEntry_InitFromList](../functions/ShopEntry_InitFromList.md) |
| <a id="price"></a>`0x18` | price | `int32` | V | Buy and equip modes: the item record price (Item_GetRecord +8); sell mode: Item_SellPrice. Red when the party's gil (scene variable 44) is lower. | [ShopItemList_DrawRow](../functions/ShopItemList_DrawRow.md) | [ShopEntry_Fill](../functions/ShopEntry_Fill.md) |
| <a id="worn_marked"></a>`0x1C` | worn_marked | `int32` | V | Sell mode: party units wearing the item with unit byte +359 set. |  |  |
| <a id="sell_grey"></a>`0x20` | sell_grey | `uint8` | V | Sell mode: Item-en row byte +44 is not 0; greys the row. |  |  |
| <a id="new_flag"></a>`0x21` | new_flag | `uint8` | V | g_ItemNewFlags[2 * id] for ids up to 0x104, else 0. |  | [ShopEntry_Fill](../functions/ShopEntry_Fill.md) |
| <a id="cannot_equip"></a>`0x22` | cannot_equip | `uint8` | V | Bit 14 of the list word. |  | [ShopEntry_Fill](../functions/ShopEntry_Fill.md) |
| <a id="selected_slot_item"></a>`0x23` | selected_slot_item | `uint8` | V | Equip mode: the selected unit's slot word has bit 15 set and its id (word & 0x3FF) is not this entry's id, i.e. the slot holds a different item that this session changed (ShopEntry_Fill 0x14036B4A9-0x14036B4BB). |  |  |

## Notes

Detail and evidence: ShopEntry_Fill, ShopEntry_InitFromList, ShopItemList_DrawRow. The entry is 40 bytes on the stack, one per displayed list index; it is never saved, and the shared menu list it indexes is rebuilt per screen open.

## Open questions

None recorded.
