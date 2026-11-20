# ShopEntry_Fill

- **Address:** `0x14036B2D0`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `void ShopEntry_Fill(ShopEntry *entry, int index, int mode)`
- **Callers:** ShopList_BuildEntries (sub_14036B18C), sub_14036B5D0
- **Callees:** ShopEntry_InitFromList (sub_14028B65C), Item_GetRecord, Item_SellPrice, NxdRegistry_Find, NxdTable_GetRowById, sub_140284998, sub_140199BC8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the 40-byte shop list entry of list index `index`: id and counts (ShopEntry_InitFromList), price, flags; then stores it in the list gadget.

## Behavior

- V: price (entry +24) = Item_SellPrice(id) when mode == 1, else the record price Item_GetRecord(id & 0x3FF) +8.
- V: mode 1: entry +32 = Item-en row byte +44 != 0; entry +28 = number of party units wearing the item with byte +359 set.
- V: mode 2: entry +12 / +16 grow by one for each of the 5 words at 0x14184A680 + 10 * (selected unit) equal to the id; entry +35 is set when the selected slot's equipment word has bit 15 and its id is not this entry's id (see the last bullet).
- V: entry +33 = g_ItemNewFlags[2 * id] for ids up to 0x104, else 0; entry +34 = bit 14 of the list word (cannot equip).
- V: the cannot-equip byte (entry +0x22) is bit 14 of the list word: the word is sign-extended at 0x14036B450, shifted right by 14 at 0x14036B459, ANDed with the constant 1 at 0x14036B45C, and stored at 0x14036B45F.
- V: the selected-slot byte (entry +0x23) is not the list word's bit 15: it tests the selected unit's equipment word at 0x14036B4A9-0x14036B4B4, where the sign branch at 0x14036B4AC reads bit 15, the mask at 0x14036B4AE keeps the id, and the mismatch is stored at 0x14036B4BB.

## State touched

- Calls: [ShopEntry_InitFromList](ShopEntry_InitFromList.md), [Item_GetRecord](Item_GetRecord.md), [Item_SellPrice](Item_SellPrice.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)
- Reads: [MenuListWord.cannot_equip](../structs/MenuListWord.md#cannot_equip), [ShopEntry.item_id](../structs/ShopEntry.md#item_id), [ItemRecord.price](../structs/ItemRecord.md#price), [g_ItemNewFlags](../globals/g_ItemNewFlags.md)
- Writes: [ShopEntry.cannot_equip](../structs/ShopEntry.md#cannot_equip), [ShopEntry.price](../structs/ShopEntry.md#price), [ShopEntry.new_flag](../structs/ShopEntry.md#new_flag)

## Referenced by

- Appears in flows: [ItemMenuListLifecycle](../flows/ItemMenuListLifecycle.md)
- Called by: [ShopList_BuildEntries](ShopList_BuildEntries.md), [sub_14036B5D0](sub_14036B5D0.md)
- Observed behaviours: [ItemDisplayInShopAndEquipPanels](../behaviors/ItemDisplayInShopAndEquipPanels.md), [ItemMenuListWordMarkOverlapsLargeIds](../behaviors/ItemMenuListWordMarkOverlapsLargeIds.md), [ItemRowGrammarBytesAndGates](../behaviors/ItemRowGrammarBytesAndGates.md), [MenuListFlagFlow](../behaviors/MenuListFlagFlow.md)

## Notes

The price shown and charged for a new item is its exe record price (verified in the game: 1,200 shown and charged for item 300).

## Open questions

None recorded.
