# Job_LearnAbilityByMenu

- **Address:** `0x14028936C`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `void Job_LearnAbilityByMenu(int unusedArg, int16_t jobId, int16_t abilityId)`
- **Callers:** Unit_SpendJp
- **Callees:** Job_IdToIndex, Skillset_BuildAbilityList, GeneralJob exp getter (sub_1402CC008), sub_1402867BC, sub_140285744, sub_1402BD05C, sub_1400DF354

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Marks an ability as learned in the current party member's record when the player buys it in the job menu, then refreshes the hidden Onion Knight level and posts the learning notification.

## Behavior

- V: the first argument is not used; Unit_SpendJp passes the ability id there and then deducts the JP cost itself.
- V: the skillset id comes from byte 0 of the JobTable row of `jobId` (0 for ids of 174 or more); the ability list is Skillset_BuildAbilityList(set, 47) when bit 0x40 of party byte +112 is set, else 31.
- V: the ability's position in that list picks the learned bit: party record B byte +123 + 3 * Job_IdToIndex(jobId) + position / 8, bit 7 - (position mod 8). The position search has no bound, so the ability must be in the list.
- V: afterwards it counts jobs 76..92 (74, 75 and 93 are skipped) for which sub_1402867BC with mode 3 reports no unlearned ability left; the count is halved and capped at 8.
- V: that value becomes the level of job id 161 (index 21): the nibble in the level array at B+189 and the JP at B+248+2*index, taken from Job_GetJpForLevel(index, level) (I: the stock rule that the hidden class levels with mastered jobs).
- V: then it writes the party record back to the save (sub_140285744), runs sub_1402BD05C, and sends an AbilityLearningByMenu notification (party index and job id).

## State touched

- Calls: [Job_IdToIndex](Job_IdToIndex.md), [Skillset_BuildAbilityList](Skillset_BuildAbilityList.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Observed behaviours: [JobArrayAccessesPutTheRecordPointerInTheIndexRegister](../behaviors/JobArrayAccessesPutTheRecordPointerInTheIndexRegister.md)
- Reads tables: [JobTable](../tables/JobTable.md)

## Notes

The current party member is the index in word_141811428. Learning from a menu always succeeds; the learn-chance roll is only in Unit_TryLearnAbility. Its JobTable row guard is the bound 0xAE loaded into a register, then compared.

## Open questions

What sub_1402BD05C refreshes.
