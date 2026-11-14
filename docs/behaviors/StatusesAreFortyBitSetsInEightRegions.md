# StatusesAreFortyBitSetsInEightRegions

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_StatusResolve](../functions/Battle_StatusResolve.md), [sub_1403052DC](../functions/sub_1403052DC.md), [Battle_StatusApply](../functions/Battle_StatusApply.md), [Battle_StatusRefresh](../functions/Battle_StatusRefresh.md), [sub_140278CF0](../functions/sub_140278CF0.md), [Unit_ReinitStatusCountdowns](../functions/Unit_ReinitStatusCountdowns.md), [StatusList_BuildFromResultBlock](../functions/StatusList_BuildFromResultBlock.md), [StatusList_BuildFromSet](../functions/StatusList_BuildFromSet.md), [Ai_StatusLastsTurns](../functions/Ai_StatusLastsTurns.md), [Battle_ResultResetStatusSets](../functions/Battle_ResultResetStatusSets.md), [UnitWorkRecord.status_effective](../structs/UnitWorkRecord.md#status_effective), [UnitWorkRecord.applied_status](../structs/UnitWorkRecord.md#applied_status), [UnitWorkRecord.pending_status_add](../structs/UnitWorkRecord.md#pending_status_add), [UnitWorkRecord.pending_status_remove](../structs/UnitWorkRecord.md#pending_status_remove)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A unit's statuses are 40-bit sets (status s = bit 0x80 >> (s & 7) of byte s >> 3) kept in eight regions of the battle unit record: innate a, innate b, the effective set, the applied set, the pending add and remove pair, 16 countdown bytes for the statuses 24..39, and the KO counter. Nothing is saved. The code is written to this shape in about 1,000 places: fixed loops of 40, fixed five-byte copies, and fixed bytes and masks that name one status each.

## Behavior

- V: the effective set is always innate a OR applied; the three loops of Resolve (filter, refresh, apply) are the only code that sets or clears applied bits for combat; events and previews copy sets wholesale.
- V (census): 23 compares against 40 or 39 over status ids in 20 functions, 190 literal-mask tests naming 38 statuses in 102 functions, 10 computed-bit sites, about 240 fixed five-byte or 16-byte accesses.
- V: the immunity sets (+58, +63, +68), remove mask (+466) and fourth group (+408) are the same bytes as innate a, innate b, the effective set and the applied set seen through the result block base; they are not separate regions.
- V: the property table is read with a 16-byte row, the group masks with a 5-byte row, the added-effect records with a 6-byte row, all indexed by status id below 40.

## Open questions

? untyped readers of the sets (about 51 candidate masks marked I in the census) need a live write-watch.
