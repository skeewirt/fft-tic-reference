# PoachTable_GetRowById

- **Address:** `0x1402B8A78`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `void *PoachTable_GetRowById(uint16_t poach_id)`
- **Callers:** BattleMsg_ResolveEntry
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the PoachItem-en row for a poach type through the shared NXD table interface.

## Behavior

- V: the resource object is at 0x143CDA880 and the table interface at 0x143CD9CD0.
- V: the table is opened once, cached, and the row is looked up by the id.
- V: the entry is advanced by eight bytes plus its own header offset before it is returned.
- V: a failed open or a missing row returns null.
- V: the only caller is the event message builder, which needs the poach name for a message.
- I: the table id is 0xEC (PoachItem-en) for this accessor.
- ?: whether the +8 advance is the payload start of every row or specific to this table.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [BattleMsg_ResolveEntry](BattleMsg_ResolveEntry.md)
- Reads tables: [PoachItem](../tables/PoachItem.md)

## Notes

Whole function read (135 bytes).

## Open questions

None recorded.
