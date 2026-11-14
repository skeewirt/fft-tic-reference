# BattleActionJpFormulaAndSpillover

- **Kind:** observed behaviour
- **Scope:** engine (battle JP award)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [Battle_AwardUnitJp](../functions/Battle_AwardUnitJp.md), [Unit_AwardJobJp](../functions/Unit_AwardJobJp.md), [Job_IdToIndex](../functions/Job_IdToIndex.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

JP for an action is 8 + 2 x the job level of the acting unit's current job + the unit's level / 4, scaled by an event percentage and by JP Boost; every other unit of the battle gets a quarter of that base amount in the same job slot.

## Behavior

- V (decompile, 2026-11-08): the base amount is zero when the action earned no experience; otherwise (unit level >> 2) + 8 + 2 x the job level nibble of the slot Job_IdToIndex gives for the unit's job byte; units with flag 0x20 in byte +6 get nothing.
- V: each of the 21 battle units except the actor receives base >> 2 through Unit_AwardJobJp in that same job slot (the award itself refuses units of another team).
- V: the actor receives base x percent / 100 (the percent is 100 unless a shop-mode table row sets another), then x 1.5 with integer arithmetic when byte +153 has bit 0x40 (JP Boost), or x 1.5 in floating point when the unit's word at +504 has bit 0x800; Unit_AwardJobJp caps at 9999.

## Open questions

None recorded.
