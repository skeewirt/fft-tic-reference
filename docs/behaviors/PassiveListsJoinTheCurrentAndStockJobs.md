# PassiveListsJoinTheCurrentAndStockJobs

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [sub_14028A8B0](../functions/sub_14028A8B0.md), [JobScreen_BuildJobTabRows](../functions/JobScreen_BuildJobTabRows.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The reaction, support and movement lists of the Status screen join the rows of the unit's current job and of the stock jobs 75..92 only.

## Behavior

- V (code): sub_14028A8B0 calls JobScreen_BuildJobTabRows for Party_GetUnitJobId's job and then for job ids 75..92; in modes 2 / 4 / 6 a job JobList_BuildForPartyUnit does not hold is skipped.

## Open questions

? a list longer than the game's 200 rows.
