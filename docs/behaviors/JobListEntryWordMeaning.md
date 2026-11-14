# JobListEntryWordMeaning

- **Kind:** observed behaviour
- **Scope:** engine (runtime job list)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [JobListWord](../structs/JobListWord.md), [JobList_Build](../functions/JobList_Build.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [JobScreen_UpdateState](../functions/JobScreen_UpdateState.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How JobList_Build fills an entry and what the readers do with its three parts: the id is the low 13 bits the mask keeps, bit 13 means locked for the whole party, and bit 14 means the unit's own job in mode 2 and 'unlocked by another party member' in mode 3.

## Behavior

- V: entry 0 is always the unit's current job (the marker 128 or 129 becomes job 74, marker 130 takes the job word); in mode 2 it carries 0x4000.
- V: positions 1.. come from a loop over i = 1..21 reading mask bit i: id = i + 74 for i < 20, i + 140 for 20 and 21 (jobs 75..93, 160, 161); job 91 is left out when unit flag 0x40 is set and job 92 when 0x80 is set.
- V: mode 3 (the Jobs screen and the tree): bit set = plain id; bit clear = id | 0x2000 when Job_IsLockedForParty says no party member holds it, else id | 0x4000. So in mode 3 bit 14 means unlocked by another party member, which is the tree state 1 (LockReleased); state 2 (LockUnreleased) is bit 13; state 0 is a plain id.
- V: JobTree_FillJobRecords turns the word into the record state: bit 13 gives state 2, else bit 14 gives state 1, else state 0; a unit whose job is hidden from the tree gets a list of length 1.
- V: JobScreen_UpdateState passes the whole 16-bit word (flags included) to Unit_SpendJp, JobScreen_OpenJobPage, JobChange_RunPreviewAnim and sub_1402888E8 and only the low byte to Unit_ResolvePreviewShape; the callees take it as a 16-bit job id.
- I: the callers rely on the word being flag-free for the entries that reach the job change (an unlocked entry); this was not traced for every entry.

## Open questions

? whether JobListWord's bit 14 text ('current job') should say mode 2 only: the sheet for the struct was not edited here.
