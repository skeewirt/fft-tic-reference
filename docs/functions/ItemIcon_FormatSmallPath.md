# ItemIcon_FormatSmallPath

- **Address:** `0x1400FC14C`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int ItemIcon_FormatSmallPath(char *out, int itemId, int cap)`
- **Callers:** ItemCell_SetItem (sub_14029ADE4), sub_140142014, sub_14014D57C, sub_140153CA0
- **Callees:** Icon_FormatPath, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes the texture-parts path of an item's small icon: Icon row 13 ('equip_item_s/textureparts/ei_s_%03d_uitx') formatted with the item id.

## Behavior

- V: Icon_FormatPath(13, tmp, useParts = 1, 260) gives the texture-parts URI of 'ui/ffto/icon/equip_item_s/textureparts/ei_s_%03d_uitx' (the template is the Icon row's file path).
- V: then formats that template with the item id (0 when the id is negative) into `out`.
- V: the retail pack 0008 has ei_s_000 .. ei_s_260 only (.utexpt parts and .tex textures); a higher id names a file that does not exist.

## State touched

- Calls: [Icon_FormatPath](Icon_FormatPath.md), [Str_Format](Str_Format.md)

## Referenced by

- Appears in flows: [ItemNameToScreen](../flows/ItemNameToScreen.md)
- Called by: [ItemCell_SetItem](ItemCell_SetItem.md), [sub_140142014](sub_140142014.md), [sub_14014D57C](sub_14014D57C.md), [sub_140153CA0](sub_140153CA0.md)
- Observed behaviours: [ItemDisplayInShopAndEquipPanels](../behaviors/ItemDisplayInShopAndEquipPanels.md)
- Reads file formats: [ItemIconPath](../formats/ItemIconPath.md)

## Notes

No table field selects the icon: it is the item id. The record's icon / icon_palette bytes feed the classic icon path (ItemIcon_Set), not this one.

## Open questions

None recorded.
