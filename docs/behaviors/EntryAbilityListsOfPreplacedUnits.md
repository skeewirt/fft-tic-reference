# EntryAbilityListsOfPreplacedUnits

- **Kind:** observed behaviour
- **Scope:** engine (battle unit build)
- **Area:** [Unit data](../areas/unit-data.md)
- **Affects:** [Unit_InitAbilitiesFromJob](../functions/Unit_InitAbilitiesFromJob.md), [Unit_QueueJobAbilitiesToLearn](../functions/Unit_QueueJobAbilitiesToLearn.md), [UnitWork_InitFromSpawnRecord](../functions/UnitWork_InitFromSpawnRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A pre-placed unit's OverrideEntryData row can name abilities its skillsets start with learned and abilities that the learning pass leaves out, and can turn off the JP cost of the learning.

## Behavior

- V: Unit_InitAbilitiesFromJob reads the row's array at +0x4C (granted_abilities: offset +0x4C, count +0x50, i32 elements, low 16 bits used), its array at +0x54 (withheld_abilities: offset +0x54, count +0x58) and byte +0x9A (free_abilities).
- V: list 1 is the entry's reaction / support / movement words (when below 0x1FE) plus the granted array; list 2 is the withheld array; both are passed with the byte +0x9A to Unit_QueueJobAbilitiesToLearn for every pair of generic jobs.
- V: pass 1 learns, as guaranteed, every ability of the job's 24-slot skillset that is in list 1; it charges JP only when byte +0x9A is 0 and the job is not the unit's own job with the default skillset.
- V: pass 2 goes over every ability of the skillset that is not in list 2.
- I: the words 'granted' and 'withheld' follow from the two passes; the pass-2 JP rule is not read beyond the arguments it passes.

## Open questions

? what the effect of the withheld list is on the final learned set in play.
