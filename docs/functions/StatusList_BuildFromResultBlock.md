# StatusList_BuildFromResultBlock

- **Address:** `0x1402791FC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char StatusList_BuildFromResultBlock(__int64 resultBlock, _BYTE *list, int *count)`
- **Callers:** sub_140217A7C, UnitPanel_FillEffectLine
- **Callees:** qsort

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Lists the statuses a result block adds and removes, as one byte per status, sorted by display priority.

## Behavior

- V: returns 0 when the block or the list pointer is null, otherwise 1.
- V: scans the status ids 0..39 in order (a fixed loop of 40); for each id whose bit is set in the pending-remove set (block +34) it appends the id with bit 0x80 set, and for each id whose bit is set in the pending-add set (block +29) it appends the plain id; the removal of an id is therefore listed before its addition.
- V: the entries are appended at the position *count, which it advances; the bit of id s is 0x80 shifted right by (s & 7) in byte s >> 3 of the set.
- V: finally it sorts the appended range with qsort and Status_ComparePriority (which masks off bit 0x80, gives 0 for an id of 40 or more, and orders by the property table priority, largest first).

## State touched

- Reads: [UnitWorkRecord.pending_status_add](../structs/UnitWorkRecord.md#pending_status_add), [UnitWorkRecord.pending_status_remove](../structs/UnitWorkRecord.md#pending_status_remove)

## Referenced by

- Called by: [UnitPanel_FillEffectLine](UnitPanel_FillEffectLine.md), [sub_140217A7C](sub_140217A7C.md)
- Observed behaviours: [HitLabelsAndThePanelEffectLineAreSeparateLists](../behaviors/HitLabelsAndThePanelEffectLineAreSeparateLists.md), [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md)

## Notes

Name is ours. The list is one byte per entry, so the 0x80 flag leaves seven bits for an id. V (traced live 2026-11-17): UnitPanel_FillEffectLine builds it for the unit status panel (action preview, enemy target panel); the labels over a hit unit do not use it (ResultLabel_QueueFromUnit walks the sets itself).

## Open questions

? what sub_140217A7C shows (it builds the list from a copy of two five-byte sets in the battle control block).
