# UnitList_Compare

- **Address:** `0x14028ADF8`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int UnitList_Compare(const uint8_t *a, const uint8_t *b, int keyKind, char favoriteFirst)`
- **Callers:** sub_140285C30
- **Callees:** UnitList_SortKey, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Compares two party units for the unit list sort by one key kind: the sign is negated for a row of table 44 whose byte +6 is 0.

## Behavior

- V: with the last argument set, a unit whose record byte +112 has bit 2 sorts before one without it (both set: equal).
- V: the keys of both units come from UnitList_SortKey; key kind 17 falls back to kind 14 when the two keys are equal and not 1.
- V: the result is the difference (key of b - key of a), negated unless the table-44 row of the key kind has byte +6 non-zero; a missing table or row gives the negated difference (smaller key first).
- I: bit 2 of the record byte +112 is the unit-list 'favourite' flag, because the unit list screen has a favourite toggle and this is the only per-unit bit the sort puts first.

## State touched

- Calls: [UnitList_SortKey](UnitList_SortKey.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Observed behaviours: [SortOrderColumnsOfJobAndAbilityTables](../behaviors/SortOrderColumnsOfJobAndAbilityTables.md)

## Notes

Name is ours (executable database: sub_14028ADF8). Table 44 is the sort-mode table; its byte +6 chooses ascending (0) or descending order.

## Open questions

? the sort-mode table's name and its other columns.
