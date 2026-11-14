# CMesId_GetText

- **Address:** `0x1400FCB2C`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `const char *CMesId_GetText(unsigned int id)`
- **Callers:** BattleMsg_TextFromDescriptor (one site), BattleMsg_ResolveEntry (two sites)
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the text of one row of NXD table 172 (0xAC, the C_Mes_Id_Sample table) and caches the table pointer.

## Behavior

- V: the table pointer is cached in qword_143CDA340; when it is empty the function finds table 172 with NxdRegistry_Find(g_NxdRegistry, 172).
- V: the row is fetched by key with the generic table row lookup (NxdTable_GetRowById then NxdEntry_GetRow); a missing table or a missing row returns null.
- V: a row whose key is negative resolves to a shared empty row, which is returned instead of null.
- V: table 172 is the English C_Mes_Id_Sample table: keys 2000..23025, 1734 rows, of which keys 10000..10171 are 172 rows; key 10098 holds '<string=lstr0>' and key 10512 does not exist.
- V: the executable's own text-tag resolver names table 172 'C_Mes_Id_Sample', so the table name is the game's; the function name is ours.
- V: three direct call sites in two functions.
- I: the row key is the message id BattleMsg_IdFromDescriptor produces; keys 2000..23025 match 1000 * kind + index for the kinds that function accepts.
- ?: why the 172-row block at 10000 exists beside the 1000-wide blocks, and when the cache is invalidated.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [BattleMsg_ResolveEntry](BattleMsg_ResolveEntry.md), [BattleMsg_TextFromDescriptor](BattleMsg_TextFromDescriptor.md)
- Reads tables: [C_Mes_Id_Sample](../tables/C_Mes_Id_Sample.md)

## Notes

The name is ours (IDB: sub_1400FCB2C). Read in full (about 134 bytes) while tracing the item battle message. The row lookup that follows the registry find is NxdTable_GetRowById plus NxdEntry_GetRow.

## Open questions

The invalidation rule for the cached table pointer; whether a missing row is expected or always an error; what the row text tags <string=lstrN> / <num=...> expand to.
