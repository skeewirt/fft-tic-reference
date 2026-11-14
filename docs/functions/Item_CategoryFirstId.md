# Item_CategoryFirstId

- **Address:** `0x1402B8C0C`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `uint32_t Item_CategoryFirstId(uint16_t itemId)`
- **Callers:** the five sub-record accessors sub_1402B8C74, sub_1402B8CD4, sub_1402B8D3C, sub_1402B8DA0, sub_1402B8E04
- **Callees:** Item_FindCategoryIndex

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the first item id of the category (type) that contains the given id, so a caller can index a sub-record table from its start; 0 when the id is rejected.

## Behavior

- V (decompile): index = Item_FindCategoryIndex(id); -1 returns 0.
- V: otherwise `g_ItemCategoryFirstId[ g_ItemCategoryFirst[ g_ItemCategoryType[index] ] ]` (word, zero-extended).

## State touched

- Calls: [Item_FindCategoryIndex](Item_FindCategoryIndex.md)

## Referenced by

- Called by: [sub_1402B8C74](sub_1402B8C74.md), [sub_1402B8CD4](sub_1402B8CD4.md), [sub_1402B8D3C](sub_1402B8D3C.md), [sub_1402B8DA0](sub_1402B8DA0.md), [sub_1402B8E04](sub_1402B8E04.md)
- Resolves registries: [ItemCategories](../registries/ItemCategories.md)

## Notes

Data names applied in the same pass: g_ItemCategoryFirstId (0x1406804E0, 14 x u16), g_ItemCategoryType (0x14067FB78, 14 x u32), g_ItemCategoryFirst (0x14067FB38, 10 x u32), g_ItemRecords (0x14080EA90, 256 x 12), g_ItemRecordsHigh (0x140680510, 5 x 12).
- Category lookup read:
  - V: category -1 returns 0.
  - V: otherwise kind = g_ItemCategoryType[category] (u32, 0..9), first category of the kind = g_ItemCategoryFirst[kind], result = g_ItemCategoryFirstId[that category].
  - V: stock kinds by category: 0 0 1 2 2 3 4 5 5 6 7 7 8 9; first category per kind: 0 2 3 5 6 7 9 10 12 13.
  - V: preserves r9 and r10 for its callers (only rax, rcx, rdx, r8 are written).

## Open questions

None recorded.
