# Battle_AwardUnitJp

- **Address:** `0x14028338C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Battle_AwardUnitJp(int unit_slot, uint32_t *out_jp)`
- **Callers:** sub_140206050
- **Callees:** sub_1402175F8, SceneVar_Read, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_140278AD8, Job_IdToIndex, Unit_AwardJobJp

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Awards job JP to a battle unit after an action: it validates the unit, resolves its job index and JP amount, applies the award and reports the amount.

## Behavior

- V: the first argument is the unit slot and the second a pointer that receives the awarded JP; it is zeroed at entry.
- V: a unit marker of 0xFF, unit +0x61 bit 0x60 or unit +0x62 bit 0x81 makes it return 0 without an award.
- V: job ids 0xA1 and 0xA4 are excluded before the award (the second is reached as 0xA1+3); there is no further job-specific special case.
- V: the job index comes from Job_IdToIndex and the award goes through Unit_AwardJobJp.
- V: the JP row is resolved through the NXD registry and table lookups, and SceneVar_Read supplies a multiplier.
- V: sub_1402175F8 is called first as a gate and sub_140278AD8 computes a level-derived value.
- V: it returns 1 when JP was awarded and 0 otherwise.
- I: this is the battle end/action award path, because it runs from the battle result notifier and writes the per-job totals.
- ?: the exact JP formula; the NXD row fields and the multiplier were not decoded here.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [Job_IdToIndex](Job_IdToIndex.md), [Unit_AwardJobJp](Unit_AwardJobJp.md)

## Referenced by

- Observed behaviours: [BattleActionJpFormulaAndSpillover](../behaviors/BattleActionJpFormulaAndSpillover.md)

## Notes

Whole function read (728 bytes). The writers it calls are the job-state writers.

## Open questions

None recorded.
