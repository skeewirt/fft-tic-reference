# g_CMesIdTable

- **Kind:** global
- **Address:** `0x143CDA340`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `ptr`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The cached result of the NXD registry lookup for table 172, the battle message text table. CMesId_GetText calls NxdRegistry_Find with id 172, keeps the result here and reads the message row by id; a missing row gives null.

## Behavior

- V: table 172 is the message table: keys 2000..23025, 1734 rows; key 10098's text is <string=lstr0> and key 10512 does not exist (extracted table data).
- V: the text function returns null when the row is missing (decompile).

## Referenced by

- Described by tables: [C_Mes_Id_Sample](../tables/C_Mes_Id_Sample.md)

## Notes

V: the lookup is NxdRegistry_Find(g_NxdRegistry, 172) and its result is kept in the qword. I: the first call fills it and later calls reuse it. ?: whether the cached pointer is the table object, a row or the row text.

## Open questions

? whether the cache holds the table object, a row or the row text; ? when the cache is invalidated on a table reload.
