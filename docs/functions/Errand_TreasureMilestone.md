# Errand_TreasureMilestone

- **Address:** `0x1402D3520`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `int Errand_TreasureMilestone(void)`
- **Callers:** Errand_Finish and several UI functions (`sub_1401A4E00`, `sub_1402D3400`, `sub_1402D34D4`, `sub_1402D35F8`, `sub_14036FED4`)
- **Callees:** EventVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

After a successful errand, reports whether the number of treasures found has reached a milestone.

## Behavior

- V: returns 0 unless the grade is 0 and a treasure was won (loot kind 1 or 2).
- V: counts the owned treasures of the pool (event variables 801..831 for kind 1, 848..863 for kind 2).
- V: compares the count with an 8-entry milestone byte table of that pool and returns index + 1 on a match, else 0.
- I: the non-zero result selects a special notification instead of the normal one.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md)

## Referenced by

- Called by: [Errand_Finish](Errand_Finish.md), [Errand_ProfitEndStep](Errand_ProfitEndStep.md)
- Reads tables: [ErrandTreasureMilestones](../tables/ErrandTreasureMilestones.md), [ErrandTreasureMilestones2](../tables/ErrandTreasureMilestones2.md)

## Notes

None.

## Open questions

What each milestone grants.
