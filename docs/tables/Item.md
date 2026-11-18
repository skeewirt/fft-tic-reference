# Item

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** NXD file
- **NXD table id:** 45
- **Keyed by:** item id
- **Read by:** [ItemTable_GetRow](../functions/ItemTable_GetRow.md), [ItemTable_GetRowById](../functions/ItemTable_GetRowById.md), [NxdTable_GetRowById](../functions/NxdTable_GetRowById.md), [UIText_ResolveCategoryRow](../functions/UIText_ResolveCategoryRow.md)
- **Row layout:** [NxdDataItemRow](../structs/NxdDataItemRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The item rows (the Item-en table), read through ItemTable_GetRow and ItemTable_GetRowById and used by the text resolver for the category 'Item'. The item records the game keeps in the executable are a separate table.

## Behavior

- V: ItemTable_GetRow caches table 45 (0x2D); UIText_ResolveCategoryRow sends the category 'Item' to the same id.

## Notes

NXD tables are loaded through the shared registry (NxdRegistry_Find by table id) and read with NxdTable_GetRowById or a key lookup; the file format is described by the NXD format records.

## Open questions

None recorded.
