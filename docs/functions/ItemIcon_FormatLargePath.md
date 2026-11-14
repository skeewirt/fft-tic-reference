# ItemIcon_FormatLargePath

- **Address:** `0x1400FC0D8`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int ItemIcon_FormatLargePath(char *out, int itemId, int cap)`
- **Callers:** EquipDetail_Refresh, sub_140109134
- **Callees:** Icon_FormatPath, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes the texture-parts path of an item's large icon: Icon row 12 ('equip_item/textureparts/ei_%03d_uitx') formatted with the item id.

## Behavior

- V: Icon_FormatPath(12, tmp, useParts = 1, 260), then the template formatted with the item id (0 when negative).
- V: the retail pack 0008 has ei_000 .. ei_260 only.

## State touched

- Calls: [Icon_FormatPath](Icon_FormatPath.md), [Str_Format](Str_Format.md)

## Referenced by

- Called by: [EquipDetail_Refresh](EquipDetail_Refresh.md)
- Observed behaviours: [ItemDisplayInShopAndEquipPanels](../behaviors/ItemDisplayInShopAndEquipPanels.md)
- Reads file formats: [ItemIconPath](../formats/ItemIconPath.md)

## Open questions

None recorded.
