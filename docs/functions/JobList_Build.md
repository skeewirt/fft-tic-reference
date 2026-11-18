# JobList_Build

- **Address:** `0x1402864AC`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `void JobList_Build(uint16_t *dst, int mode, void *info)`
- **Callers:** sub_14028662C
- **Callees:** sub_1403609F0, Job_IsLockedForParty, sub_1402863E4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the runtime job list `g_RuntimeJobList` (uint16[], length `g_RuntimeJobListLen`). Entry = job id | 0x2000 (locked/unreleased) | 0x4000 (current job). The job tree and the job-change list both consume this list by position.

## Behavior

- V: dst[0] = the viewed unit's own job (flagged 0x4000 if current).
- V: loop i = 1..21 (stock loop bound: the counter is compared against 0x16 at 0x1402865F1, looping while below): id = i + (i < 20 ? 74 : 140), i.e. 75..93 then 160, 161.
- V: ids 91/92 (Dancer/Bard pair) are filtered by the unit's gender bit, so only one of the pair is listed.
- V: availability uses Job_IsLockedForParty(id): result > 0 -> 0x2000, else unflagged. Hidden extras 160/161 pass in this build, so the stock builder emits both (observed live: [..., 93, 160, 161]).
- V: `info` is not the party record: it carries the job marker (+2), a flags byte (+3: bit 0x20 combined with the hide-from-tree test, bits 0x40 and 0x80 filter jobs 91 and 92) and a byte (+4) that, when non-zero, reduces the list to the unit's own job. The hide-from-tree test is sub_1402CBED4: byte +60 of the Job text-table row is non-zero.
- V: the bits come from a bit reader over the unit's 3-byte unlock mask (party record +120), most significant bit first, one bit per job index; the first bit (index 0) is read and discarded.
- V: mode 2 marks the entry equal to the unit's own job 0x4000; a clear bit is skipped when no party unit has the job (Job_IsLockedForParty) and otherwise listed with 0x4000. Mode 3 lists every job and flags a clear bit 0x2000 when no party unit has it, else 0x4000. Other modes skip clear bits.
- V: the list's first entry, the unit's own job, comes from the marker byte `info` +2 (JobList_BuildForPartyUnit passes party record +114, which PartyUnit_FillFromWork copies from save record +0): 128 or 129 (a generic man or woman) -> Squire 74; 130 (a monster) -> the current job (`info` +0); any other marker (Ramza, a story unit) is itself the job id.
- V: the bit reader is fed the 3-byte mask at B+120 of the viewed unit (set by the caller sub_14028662C); one bit is discarded, then one bit is read per job index 1..21, most significant bit first.
- V: mode 3 (jobs screen): bit set gives the plain job id; bit clear gives id | 0x2000 when Job_IsLockedForParty says no party member has it, otherwise id | 0x4000.
- V: mode 2: bit clear skips the job when no party member has it, else adds 0x4000; the unit's own job is marked 0x4000 in this mode.
- V: when Job_IsHiddenFromTree(unit job) is true and the unit flag 0x20 is set (or the caller's fourth info byte is nonzero), the list is only the unit's own job.

## State touched

- Calls: [Job_IsLockedForParty](Job_IsLockedForParty.md)
- Writes: [JobListWord.job_id](../structs/JobListWord.md#job_id), [JobListWord.locked](../structs/JobListWord.md#locked), [JobListWord.current_job](../structs/JobListWord.md#current_job)

## Referenced by

- Called by: [JobList_BuildForPartyUnit](JobList_BuildForPartyUnit.md), [sub_14028668C](sub_14028668C.md)
- Observed behaviours: [JobListEntryWordMeaning](../behaviors/JobListEntryWordMeaning.md), [JobTreeLockState](../behaviors/JobTreeLockState.md), [JobTreePanelSprite](../behaviors/JobTreePanelSprite.md), [RuntimeJobListIs48WordsFollowedByAnotherGlobal](../behaviors/RuntimeJobListIs48WordsFollowedByAnotherGlobal.md), [UnlockMaskStreamRunsIntoLearnedBitsPastIndex23](../behaviors/UnlockMaskStreamRunsIntoLearnedBitsPastIndex23.md)

## Notes

Stock hidden jobs 160 (Dark Knight gate) and 161 (Onion Knight) are normally kept out by story gating in Unit_BuildJobUnlockMask, not here.

So 0x4000 means different things by mode: the current job in mode 2, and 'known to the party but not unlocked for this unit' in mode 3.

Runtime check on a fresh unit with only the starting levels: the mask allowed the first four jobs and every other job carried the 0x2000 flag.

## Open questions

Who normally keeps 160/161 out of the list in the stock game (story gate on a4 >= 20 path)?
