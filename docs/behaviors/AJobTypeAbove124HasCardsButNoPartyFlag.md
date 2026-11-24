# AJobTypeAbove124HasCardsButNoPartyFlag

- **Kind:** observed behaviour
- **Scope:** engine (job types, job cards)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [JobList_RecomputeAvailability](../functions/JobList_RecomputeAvailability.md), [JobRecord_FillIconAndGenericFlag](../functions/JobRecord_FillIconAndGenericFlag.md), [GameState_ResetJobFlags](../functions/GameState_ResetJobFlags.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A Job row's job type is a 32-bit key of the JobType table, whose row names the Icon rows of the male and female job card. The party-wide flag the game keeps per job type exists only for types 1..124, and every reader tests that bound itself; a type above 124 is drawn like any other and simply has no flag.

## Behavior

- V: JobList_RecomputeAvailability reads the job type (Job row +24) as an int and touches g_UnitJobFlags[type + 21] only when the type is above 0 and below 125; in its second loop a type of 125 or more counts as 'flag set' and is never written.
- V: Job_SameJobType (0x1400F72F0) compares the two rows' job type dwords; JobRecord_FillIconAndGenericFlag looks the JobType row up by that key (table 200) and takes the card's Icon key by the unit's sex.
- V (seen live 2026-11-24): a job whose Job row names job type 1500, with a JobType row of that key naming Icon rows 21000 and 21001 (their paths the part files of two 400 x 652 pictures), drew its own card behind a generic unit's Status panel; a second job with type 1510 drew its own in the job popup. No fault; the job grid, the popup and the Status screen behaved as with a type below 125.

## Notes

The stock JobType table has keys 1..124; 115..124 are rows with no cards.

## Open questions

? what the per-type flag changes in play besides the Guide's lessons (GuideLessons_UpdateUnlocked reads it).
