# NewUnitsGetStartingJpInEveryJob

- **Kind:** observed behaviour
- **Scope:** engine (starting JP of a new unit)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [Unit_InitJobJp](../functions/Unit_InitJobJp.md), [Unit_InitAbilitiesFromJob](../functions/Unit_InitAbilitiesFromJob.md), [Job_LevelFromTotalJp](../functions/Job_LevelFromTotalJp.md), [UnitWork_InitFromSpawnRecord](../functions/UnitWork_InitFromSpawnRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A new unit (a spawn: battle entries, the New Game party, recruits built by Unit_BuildFromRecord) gets starting JP in every job by the game's own rule for stock jobs (Unit_InitJobJp: the curve's value at the level plus up to 99).

## Behavior

- V (code): Unit_InitAbilitiesFromJob runs Unit_InitJobJp for indices 0..19 only; Job_LevelFromTotalJp gives level 0 below job_level_jp[1] (100 in the stock curve), so a job with no starting JP is at level 0.
- V (live 2026-11-10, Fitting): a job at level 0 shows 'Lv. --' and no JP on the unit panels.
- V (live 2026-11-10, slot 49): every stock job a unit may have held 100 or more total JP (only the gender-locked index 17 / 18 rows were 0).

## Open questions

? a recruit at the Warriors' Guild not checked live.
