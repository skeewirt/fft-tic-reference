# SortOrderColumnsOfJobAndAbilityTables

- **Kind:** observed behaviour
- **Scope:** engine (job and ability lists)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [UnitList_SortKey](../functions/UnitList_SortKey.md), [UnitList_Compare](../functions/UnitList_Compare.md), [sub_14028A8B0](../functions/sub_14028A8B0.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The sort_order columns of the Job and Ability tables and the order keys the lists use.

## Behavior

- V: Job sort_order (+0x38) is the key of the unit list's 'job' sort mode (UnitList_SortKey kind 2); a negative value falls back to the unit's job id.
- V: Ability sort_order (+0x34) orders the abilities of a job-screen ability page ascending, 0 or a missing row counting as 999999, ties by ability id (sub_14028A8B0).
- V: UnitList_Compare negates the key difference unless byte +6 of the sort mode's row (table 44) is non-zero.

## Open questions

None recorded.
