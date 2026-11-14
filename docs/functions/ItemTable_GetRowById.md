# ItemTable_GetRowById

- **Address:** `0x1402B889C`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `void *ItemTable_GetRowById(uint16_t item_id)`
- **Callers:** sub_140109134, sub_140109F0C, BattleMsg_ResolveEntry, sub_1402C80D8
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the Item-en row for an item id through the shared NXD table interface, or null when the row is absent.

## Behavior

- V: the resource object is at 0x143CDA2E8 and the table interface at 0x143CD9CD0.
- V: the table is opened once and the pointer is cached; a failed open returns null.
- V: the row is looked up by the id and the returned entry is advanced by its own header offset.
- V: the final pointer is the row payload, not the table header.
- V: an id with no row returns null; the callers then fall back to a default name.
- V: the four callers are the item name, item help and battle-message text paths.
- I: the table is nxd table 45 (Item-en), which is why the callers use it for names and help.
- ?: the row layout past the header; it belongs to the item text records, not to this accessor.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [BattleMsg_ResolveEntry](BattleMsg_ResolveEntry.md)
- Reads tables: [Item](../tables/Item.md)

## Notes

Whole function read (141 bytes). The cached table pointer and the null path are explicit in the body.

## Open questions

None recorded.
