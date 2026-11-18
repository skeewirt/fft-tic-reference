# JobLevelZeroDrawsDashesAndGreysChangeJob

- **Kind:** observed behaviour
- **Scope:** engine (Change Job grid and job popup)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [JobRecord_FromJobId](../functions/JobRecord_FromJobId.md), [JobRecord](../structs/JobRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A job whose level reads as 0 draws 'Lv. --' on the Change Job grid cell, shows level, EXP and JP as '--' in the job popup, and cannot be chosen: its Change Job entry is greyed.

## Behavior

- V (seen live): a job whose level read as 0 showed 'Lv. --' in its cell, '--' for Job Level, Job EXP and JP in the popup, and a greyed Change Job button; the same job with a level of 1 showed 'Lv. 1', its JP, 'To Next Level' and an enabled Change Job.
- I: JobRecord_FromJobId stores the level into the cell record at +68 (the high nibble for an even index, the low nibble for an odd one), and the screens print dashes for a level at or below zero; the drawing code was not read.
- I: the points still needed for the next level (record +84, the threshold of level + 1 minus the stored total) can be negative when the stored total is already above the threshold, and the popup and the Status header then print '--' for Next and To Next Level (seen live with a level of 1 and 500 total points).

## Notes

Cause of a zero level for a large job index: JobArrayAccessesPutTheRecordPointerInTheIndexRegister.

## Open questions

? which function draws the dashes and which one greys the Change Job button.
