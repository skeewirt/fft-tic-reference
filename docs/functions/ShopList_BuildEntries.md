# ShopList_BuildEntries

- **Address:** `0x14036B18C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ShopList_BuildEntries(int count, int mode, char a3, char a4)`
- **Callers:** sub_14036A9D8 (the buy screen, after Shop_BuildItemList), sub_1402D7640, sub_14036B53C, sub_14036B71C, sub_14036C49C
- **Callees:** ItemOrder_FilterList, sub_140286228, sub_1402A3230, ShopEntry_Fill (sub_14036B2D0), sub_1401983E4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the entries of the shop's item list from word_141811470: orders the list, sizes the list gadget and fills one entry per id (ShopEntry_Fill).

## Behavior

- V: the list is reordered with ItemOrder_FilterList (saved item order of the current group) or sub_140286228 (a sort mode), which returns the count.
- V: sub_1402A3230 is called on the list gadget (manager +320 -> +112, +88) with that count (I: sizes the list); then ShopEntry_Fill(entry, i, mode) runs for every index.
- V: both order paths rewrite the list in place (filter at 0x14036B1EB, sorter at 0x14036B218) and neither masks the entries it writes back.

## State touched

- Calls: [ItemOrder_FilterList](ItemOrder_FilterList.md), [sub_140286228](sub_140286228.md), [ShopEntry_Fill](ShopEntry_Fill.md)

## Referenced by

- Called by: [sub_1402D7640](sub_1402D7640.md), [sub_14036A9D8](sub_14036A9D8.md), [sub_14036B71C](sub_14036B71C.md), [sub_14036C49C](sub_14036C49C.md)

## Notes

The ordering step keeps only ids its stores know.

## Open questions

I: mode 1 = sell, 2 = equip (from ShopEntry_Fill's branches).
