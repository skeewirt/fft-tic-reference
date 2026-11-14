# ItemCell_SetItem

- **Address:** `0x14029ADE4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ItemCell_SetItem(void *ctx, ItemCellParts *parts, int itemId, char showEmpty)`
- **Callers:** ShopItemList_FillRow (sub_1402A3578), sub_14029643C
- **Callees:** ItemIcon_FormatSmallPath (sub_1400FC14C), ItemCell_BindIconAndName (sub_14029BEC4)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills an item cell (icon image and name text) for an item id: formats the small item icon path and hands it with the id to ItemCell_BindIconAndName.

## Behavior

- V: formats the icon path into a 260-byte buffer with ItemIcon_FormatSmallPath(itemId), then calls ItemCell_BindIconAndName(ctx, parts, itemId, path, showEmpty).

## State touched

- Calls: [ItemIcon_FormatSmallPath](ItemIcon_FormatSmallPath.md), [ItemCell_BindIconAndName](ItemCell_BindIconAndName.md)

## Referenced by

- Called by: [ShopItemList_FillRow](ShopItemList_FillRow.md), [sub_14029643C](sub_14029643C.md)

## Open questions

None recorded.
