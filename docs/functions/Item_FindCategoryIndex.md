# Item_FindCategoryIndex

- **Address:** `0x1402B8BCC`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int32_t Item_FindCategoryIndex(uint16_t itemId)`
- **Callers:** Item_CategoryFirstId, six item sub-record accessors (sub_1402B8C74 .. Item_GetEquipPalette), Item_IsInCategory, sub_1403099B0 (9 call references)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns an item id into its category index: the number of leading entries of the 14-word first-id array (`g_ItemCategoryFirstId`) that are <= the id.

## Behavior

- V (decompile): ids above 0xFD are rejected unless they are 0x100..0x104 (0xFE and 0xFF are rejected); a rejected id returns -1.
- V: scans the word array from entry 1 (0x1406804E2) while id >= entry, counting; returns -1 if the scan runs off the end (0x1406804FC).
- V (J8): the index is then mapped by `g_ItemCategoryType` (index -> type 0..9) in the callers.

## Referenced by

- Called by: [Battle_ResolveAction](Battle_ResolveAction.md), [Item_CategoryFirstId](Item_CategoryFirstId.md), [Item_GetEquipPalette](Item_GetEquipPalette.md), [Item_IsInCategory](Item_IsInCategory.md), [sub_1402B8C74](sub_1402B8C74.md), [sub_1402B8CD4](sub_1402B8CD4.md), [sub_1402B8D3C](sub_1402B8D3C.md), [sub_1402B8DA0](sub_1402B8DA0.md), [sub_1402B8E04](sub_1402B8E04.md), [sub_1403099B0](sub_1403099B0.md)
- Observed behaviours: [ItemIdSpace](../behaviors/ItemIdSpace.md)
- Resolves registries: [ItemCategories](../registries/ItemCategories.md)

## Notes

J8: the category map is hand-aligned with the item id ranges; each sub-record table starts exactly where the previous one ends, so a relocation moves them as one block.
- Reading of the code:
  - V: ids above 0xFD that are not 0x100..0x104 return -1 (so 0xFE and 0xFF never have a category).
  - V: otherwise counts the 13 category first-ids from entry 1 on (g_ItemCategoryFirstId + 2 .. + 28) while the id is at least the entry; reaching the end returns -1, so category 13 is unreachable.
  - V: stock first-ids give categories 0..12 = ids 0x00, 0x7A, 0x80, 0x90, 0xAC, 0xD0, 0xF0, 0x100, 0x102 (empty), 0x102 (empty), 0x102, 0x103, 0x104.
  - V: leaf; leaves rcx, r9, r10 untouched, which its callers rely on (Item_GetEquipPalette reuses cx, Item_IsInCategory keeps its category in r9).

## Open questions

None recorded.
