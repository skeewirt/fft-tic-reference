# JobCommand_SameGroup

- **Address:** `0x1400F7334`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `bool JobCommand_SameGroup(unsigned int idA, unsigned int idB)`
- **Callers:** Inventory_RebuildOrders, JobChange_FillUnitEntry, sub_1401161E4, sub_1403333F0
- **Callees:** JobCommandTable_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when two job command ids are the same command: equal ids, or rows with the same group key.

## Behavior

- V: equal ids are the same; otherwise both JobCommand rows (table 41) are fetched and the dword at +0x14 (column group) is compared; a missing row gives false.

## State touched

- Calls: [JobCommandTable_GetRow](JobCommandTable_GetRow.md)

## Referenced by

- Observed behaviours: [JobAndAbilityDisplayFlagColumns](../behaviors/JobAndAbilityDisplayFlagColumns.md)

## Notes

Variants of one command (different rows) share one group key.

## Open questions

None recorded.
