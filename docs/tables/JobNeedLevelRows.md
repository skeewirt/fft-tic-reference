# JobNeedLevelRows

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** Executable
- **Address:** `0x14067F390`
- **Rows:** 22 rows of 12 bytes
- **Keyed by:** job index 1..22 (row r gates job index r + 1)
- **Read by:** [Unit_BuildJobUnlockMask](../functions/Unit_BuildJobUnlockMask.md)
- **Held in:** [g_JobNeedLevelRows](../globals/g_JobNeedLevelRows.md)
- **Row layout:** [JobNeedLevelRow](../structs/JobNeedLevelRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Prerequisite job levels of each unlockable job. The unlock mask builder compares a unit job levels with the nibbles of the row.

## Behavior

- V: the per-unit unlock mask has 24 bits and is rebuilt every time the job screens open.
- V: a prerequisite on a job index of 20 or more cannot be expressed (only 20 nibbles are compared).

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: use of nibbles 20..23
