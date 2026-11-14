# Job_LevelFromTotalJp

- **Address:** `0x140278D5C`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int Job_LevelFromTotalJp(unsigned int jobIndex, unsigned short totalJp)`
- **Callers:** Unit_AwardJobJp
- **Callees:** Job_GetJpForLevel

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the job level (0..8) a total JP gives: how many of the 8 GeneralJob thresholds it reaches.

## Behavior

- V: for level 1..8 counts the levels with totalJp >= Job_GetJpForLevel(jobIndex, level).
- V: with no GeneralJob row (or no nxd registry) every threshold is 0 and the answer is 8.
- V (2026-11-10): level 1 needs RequiredJobExp[1], 100 JP in the stock curve [0,100,200,400,700,1100,1600,2200,3000] (rows 0..19): a total below 100 gives level 0. Stock never gets there: Unit_InitJobJp gives a new unit 100 + 0..99 JP in every job (slot 49: every stock job a unit may have held 100 or more).

## State touched

- Calls: [Job_GetJpForLevel](Job_GetJpForLevel.md)

## Referenced by

- Called by: [UnitWork_PackJobLevels](UnitWork_PackJobLevels.md)
- Observed behaviours: [NewUnitsGetStartingJpInEveryJob](../behaviors/NewUnitsGetStartingJpInEveryJob.md)

## Open questions

None recorded.
