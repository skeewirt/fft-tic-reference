# ItemMenuListWordMarkOverlapsLargeIds

- **Kind:** observed behaviour
- **Scope:** engine (shop and equip list)
- **Area:** [Items and shops](../areas/items.md)
- **Affects:** [g_MenuList](../globals/g_MenuList.md), [MenuListWord](../structs/MenuListWord.md), [Shop_BuildItemList](../functions/Shop_BuildItemList.md), [Inventory_BuildEquipList](../functions/Inventory_BuildEquipList.md), [ShopEntry_Fill](../functions/ShopEntry_Fill.md), [sub_140332C54](../functions/sub_140332C54.md), [sub_140332C8C](../functions/sub_140332C8C.md), [sub_14036A994](../functions/sub_14036A994.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A shop or equip list word holds the item id in its low bits and the 'cannot equip' mark in bit 14; an item id can be up to 15 bits wide, so for an id of 16,384 and above the id's own bit 14 and the mark are the same bit.

## Behavior

- V: a list word is the item id, with 0x4000 ORed in when the unit cannot equip the item and the list is built in mode 1; the list ends at 0xFFFF.
- V (disassembly): the game's own equip functions refuse a word with bits above 14 set, so an item id is at most 0x7FFF and bit 15 of a list word is never set by an id; bit 14 is the id's own for ids from 16,384.
- I: an id of 16,384 or more and an id below 16,384 with the mark are the same word, so a reader cannot tell them apart from the word alone; every stock reader that masks the word to an id first (steps 5 to 7 of ItemMenuListLifecycle) uses the stock mask 0x3FF or a wider one and then tests bit 14 of the original or of the loaded value.
- V (seen live, item ids above the stock range placed in the item table): ids up to 16,383 listed in the Outfitter Buy and Sell lists; ids 16,384, 20,000 and 32,000 did not appear in either, the cut being exactly at 0x4000.
- V (disassembly): ItemOrder_FilterList runs on g_MenuList right after the mode-1 builds and rewrites it in the saved order, so any per-row side data indexed by list position ends up on another row as soon as the saved order is not the id order; the mark of a row belongs to its id, not to its slot.

## Notes

The party hand word has its own layout (PartyHandWord): there bit 15 is the picked-or-bought-in-this-visit flag, never set on a list word.

## Open questions

? whether the mark was ever meant to be read by the Classic item pages for ids above 0x3FF.
