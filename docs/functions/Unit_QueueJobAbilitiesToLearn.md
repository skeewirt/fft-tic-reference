# Unit_QueueJobAbilitiesToLearn

- **Address:** `0x1402781A8`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Unit_QueueJobAbilitiesToLearn(UnitWork *c, uint16 job, ..., uint16 *list, long count, uint16 *list2, long count2, char flag)`
- **Callers:** Unit_InitAbilitiesFromJob (2)
- **Callees:** Job_IdToIndex, Skillset_GetAbility, Unit_TryLearnAbility

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks the abilities of one job as learned in a work record when they appear in a given list (unit setup).

## Behavior

- V: index = Job_IdToIndex(job). Job 74 (Squire) is always taken (a story unit's marker job replaces it); any other job must have its unlock bit set (C +159..161 as a 24-bit value tested against 0x800000 >> index).
- V: jobs 91 / 92 are skipped when C +6 bit 6 / bit 7 are set.
- V: the skillset is C +18 for the unit's own job, else the job's JobTable row byte 0; for each of the 24 slots whose ability is in the first list, Unit_TryLearnAbility(c, index, slot, ability, guaranteed, charge) runs; then every slot not in the second list.
- V: 'the unit's own job' is the compare of the queued job with the job byte C +3 (0x140278248..0x14027824F); the own-job pass also sets the guaranteed flag when the spawn record's skillset byte (+29) is 0.
- V: its only caller, Unit_InitAbilitiesFromJob, queues the jobs 74..93 in pairs (i + 73, i + 74 for i = 1, 3, .. 19), between level fixes of the two jobs (sub_1402770BC).
- V: the last argument (the row's free_abilities byte): pass 1 calls Unit_TryLearnAbility(c, index, slot, ability, 1, charge) with charge = 1 only when that byte is 0 and the job is not the unit's own job with the default skillset (spawn +29 = 0); with the byte set the abilities of list 1 are learned for no JP.
- V: pass 2 goes over every slot whose ability is not in the second list and calls Unit_TryLearnAbility(c, index, slot, ability, own_default, !own_default).

## State touched

- Calls: [Job_IdToIndex](Job_IdToIndex.md), [Skillset_GetAbility](Skillset_GetAbility.md), [Unit_TryLearnAbility](Unit_TryLearnAbility.md)

## Referenced by

- Observed behaviours: [EntryAbilityListsOfPreplacedUnits](../behaviors/EntryAbilityListsOfPreplacedUnits.md)

## Open questions

I: the meaning of the two lists (abilities to learn and abilities to keep) from the callers.
