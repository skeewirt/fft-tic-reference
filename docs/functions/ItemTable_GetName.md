# ItemTable_GetName

- **Address:** `0x1402B892C`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `char *ItemTable_GetName(unsigned int itemId)`
- **Callers:** ItemCell_BindIconAndName (sub_14029BEC4), BattleMsg_BuildArgs, sub_140142014, sub_140153CA0, sub_1401961DC, sub_14029DA78, sub_14029E140
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow (sub_1403D2FD8)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the display name of an item from its Item-en row (nxd table 45), or null when the row is missing.

## Behavior

- V: loads table 45 lazily through NxdRegistry_Find into the cache shared with ItemTable_GetRow (`qword_143CDA2E8`) and reads the row with NxdTable_GetRowById(itemId).
- V: returns the string of the first string column (row offset at +4) when it is not empty, else the string the offset at +8 points to (both relative to row +4).
- V: null when the table or the row is missing; a negative entry key resolves to the shared empty row.
- I: the first column is Name (the live row of key 51 gives 'Rod'); the fallback column is not identified.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Appears in flows: [ItemNameToScreen](../flows/ItemNameToScreen.md)
- Called by: [BattleMsg_BuildArgs](BattleMsg_BuildArgs.md), [ItemCell_BindIconAndName](ItemCell_BindIconAndName.md), [sub_140142014](sub_140142014.md), [sub_140153CA0](sub_140153CA0.md)

## Notes

An inlined copy of ItemTable_GetRow with the name selection added.

## Open questions

? which column the fallback offset (+8) names.
