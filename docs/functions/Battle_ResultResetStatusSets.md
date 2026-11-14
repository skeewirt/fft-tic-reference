# Battle_ResultResetStatusSets

- **Address:** `0x14030A43C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `_BYTE *Battle_ResultResetStatusSets(__int64 resultBlock)`
- **Callers:** Battle_ResultReset, Battle_ApplyActionResult, sub_14030A11C
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Clears the two pending status sets of an action-result block (and a five-byte scratch copy in the battle formula state).

## Behavior

- V: for five bytes it zeroes the pending-add set (result block +29..+33), the pending-remove set (+34..+38) and five bytes at dword_14186B028.
- V: the loop counter is checked against 5 on every pass and ends in the runtime range-check failure handler when it is out of range.
- V: Battle_ResultReset calls it as its last step, after it has reset the other result fields (hit flag, damage words, the +39 flag and the +42 word); the result block is the unit record at +446, so the sets are unit +475 and +480.
- I: dword_14186B028 is a working copy that the formula code (Formula_HealSwap, sub_14030A11C, sub_14030D740, Battle_ResolveAction) reads and writes; its meaning is not decoded.

## State touched

- Writes: [UnitWorkRecord.pending_status_add](../structs/UnitWorkRecord.md#pending_status_add), [UnitWorkRecord.pending_status_remove](../structs/UnitWorkRecord.md#pending_status_remove)

## Referenced by

- Observed behaviours: [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md)

## Notes

Name is ours.

## Open questions

? what dword_14186B028 holds (read by the formula handlers named above).
