# ItemCategoryTypes

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** Executable
- **Address:** `0x14067FB78`
- **Rows:** 14 rows of 4 bytes
- **Keyed by:** category index 0..13
- **Read by:** [Battle_ResolveAction](../functions/Battle_ResolveAction.md), [Item_CategoryFirstId](../functions/Item_CategoryFirstId.md), [sub_1402B8DA0](../functions/sub_1402B8DA0.md), [sub_1402B8D3C](../functions/sub_1402B8D3C.md), [sub_1402B8E04](../functions/sub_1402B8E04.md), [Item_GetEquipPalette](../functions/Item_GetEquipPalette.md), [sub_1402B8CD4](../functions/sub_1402B8CD4.md), [sub_1402B8C74](../functions/sub_1402B8C74.md)
- **Row layout:** [ItemCategoryTypeRow](../structs/ItemCategoryTypeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Record kind of each category: which sub-record table an item of the category has.

## Behavior

- V: eight readers.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
