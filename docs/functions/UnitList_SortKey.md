# UnitList_SortKey

- **Address:** `0x14028AEFC`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int UnitList_SortKey(const uint8_t *saveRecord, int keyKind, ...)`
- **Callers:** UnitList_Compare
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_1401F08BC, sub_1402607C0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the value a party unit list is sorted by for one sort mode (key kind 0..18), read from the unit's save record.

## Behavior

- V: key kind 2 (the 'job' sort) reads the Job row (table 46) of the record's job word (+36): the sort_order column (+0x38) when it is not negative, else the job id itself.
- V: key kinds 0 and 3 return the word at record +44, kind 1 the word at +0, kind 4 +38, 5 +40, 6 +12, 7 +16, 8 +18, 9 +22, 10 +24, 11 +28, 12 +30, 13 the byte at +373, 14 the byte at +371; any other kind below 15 returns 0.
- V: kind 15 returns 5 when the record's word at +44 equals the party leader's id or an event-provided id; otherwise the result depends on the battle-mode globals and the word at +44 being below 0x32 (a 0 / 1 flag). Kind 16 returns the same kind of 0 / 1 flag for the word at +44 below 0x32. Kinds 17 and 18 return 0 or the byte at +372 plus 1.
- I: the words at +44 and +36 are the unit's level and job (the +36 word is the job word other sheets read as party +36); the meaning of the other offsets was not named.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [UnitList_Compare](UnitList_Compare.md)
- Observed behaviours: [SortOrderColumnsOfJobAndAbilityTables](../behaviors/SortOrderColumnsOfJobAndAbilityTables.md)

## Notes

Name is ours (executable database: sub_14028AEFC). Only key kind 2's use of the Job sort_order column was read to the end; the other kinds are listed by the record offset they return.

## Open questions

? the meaning of key kinds 15..18 and of the record bytes +371..+373.
