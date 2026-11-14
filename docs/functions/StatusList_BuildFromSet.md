# StatusList_BuildFromSet

- **Address:** `0x1402792B0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char StatusList_BuildFromSet(_BYTE *set, _BYTE *list, int *count)`
- **Callers:** sub_14010A42C, sub_14010C1FC, sub_1402C25E0
- **Callees:** qsort

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Lists the statuses set in a five-byte status set, one byte per status, sorted by display priority.

## Behavior

- V: returns 0 when the set or the list pointer is null, otherwise 1.
- V: loops over the ids 0..39 (a fixed bound of 40): each id whose bit (0x80 shifted right by id & 7, byte id >> 3) is set in the set is appended to the list at *count, and *count is advanced.
- V: sorts the appended range with qsort and Status_ComparePriority.

## Referenced by

- Called by: [TurnPanel_FillUnitEntry](TurnPanel_FillUnitEntry.md), [UnitPanel_SetStatusBytes](UnitPanel_SetStatusBytes.md)
- Observed behaviours: [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md)

## Notes

Name is ours. Takes any five-byte set; I: the callers pass the effective set of a unit or party record.

## Open questions

? which screens use the three callers.
