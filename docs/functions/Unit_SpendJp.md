# Unit_SpendJp

- **Address:** `0x1402B9AD0`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `void Unit_SpendJp(int ability, int jobId)`
- **Callers:** ability learn flow
- **Callees:** Ability_GetJpCost, Job_IdToIndex, sub_1400F4BCC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Subtracts the ability's JP cost from the unit's JP of the given job: *(u16 *)(g_PartyUnits[unit] + 2 * Job_IdToIndex(jobId) + 202) -= cost.

## Behavior

- V: JP per job is a u16 array at unit +202 indexed by the Job_IdToIndex value (0..21).

## State touched

- Calls: [Ability_GetJpCost](Ability_GetJpCost.md), [Job_IdToIndex](Job_IdToIndex.md), [sub_1400F4BCC](sub_1400F4BCC.md)
- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Called by: [JobScreen_BuildLearnList](JobScreen_BuildLearnList.md), [JobScreen_UpdateState](JobScreen_UpdateState.md), [sub_1403358FC](sub_1403358FC.md)

## Open questions

Array length (24 entries up to +250?).
