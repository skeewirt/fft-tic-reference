# UnlockMaskStreamRunsIntoLearnedBitsPastIndex23

- **Kind:** observed behaviour
- **Scope:** engine (per-unit job state)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [JobList_Build](../functions/JobList_Build.md), [Job_IsLockedForParty](../functions/Job_IsLockedForParty.md), [Unit_BuildJobUnlockMask](../functions/Unit_BuildJobUnlockMask.md), [JobList_RecomputeAvailability](../functions/JobList_RecomputeAvailability.md), [Party_CountMasteredJobs](../functions/Party_CountMasteredJobs.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The unit's unlock mask is 3 bytes (24 bits) read through a bit stream, and the learned-ability bits follow it directly in the same record, so a bit read at a job index of 24 or more lands in the learned bits of the first jobs.

## Behavior

- V: record layout: unlock mask at A+47, B+120, C+159 (3 bytes) followed by the learned bits at A+50, B+123, C+162 (3 bytes per job index); the bit reader pointer is set from these (qword_143C49BF0 stores in JobList_BuildForPartyUnit, sub_14028668C, JobAbilityList_Build, sub_14028A474, JobScreen_BuildLearnableList, sub_14031E50C, Unit_BuildJobUnlockMask, Party_CountMasteredJobs).
- V: JobList_Build reads mask bits 0..21 only; Job_IsLockedForParty skips Job_IdToIndex(job) bits and reads one bit of each party member's mask, and Job_IdToIndex answers 0 for every job outside 74..93 and 160..161, so any other job id reads bit 0 there.
- V: Unit_BuildJobUnlockMask builds only bits for job index 1..19 from the 12-byte rows of g_JobNeedLevelRows (nibble per job index, 24 indices) and clears bit 0x8 by the mastery check of two jobs; it has no row for a job index above 23.
- V: JobList_RecomputeAvailability and GameState_ResetJobFlags work on g_UnitJobFlags: 21 new-job flags at offset 0 (jobs 74..93, 160, 161 by index) and 125 job-type disable flags at offset 21 (key = the job row's type word, below 125); a job index above 20 used as an index into the first part would address the disable flags.

## Open questions

None recorded.
