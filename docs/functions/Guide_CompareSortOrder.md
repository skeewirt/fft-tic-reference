# Guide_CompareSortOrder

- **Address:** `0x1400DB2B4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool Guide_CompareSortOrder(int idA, int idB)`
- **Callers:** not recorded
- **Callees:** Guide_GetEntry

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Comparator for guide id lists.

## Behavior

- V: true when row A's sort_order (+0x28, u16) is less than row B's; a missing A is never less, a missing B always greater.
- V: used by the sort routines sub_1400DBB5C (introsort), sub_1400DBD2C (median / partition) and sub_1400DC094 (heap adjust).

## State touched

- Calls: [Guide_GetEntry](Guide_GetEntry.md)

## Open questions

None recorded.
