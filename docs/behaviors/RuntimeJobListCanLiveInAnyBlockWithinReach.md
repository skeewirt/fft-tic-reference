# RuntimeJobListCanLiveInAnyBlockWithinReach

- **Kind:** observed behaviour
- **Scope:** engine (runtime job list)
- **Area:** [Job data](../areas/job-data.md)
- **Affects:** [JobList_IsSelectedEntryUnflagged](../functions/JobList_IsSelectedEntryUnflagged.md), [JobTree_FillJobRecords](../functions/JobTree_FillJobRecords.md), [JobScreen_UpdateState](../functions/JobScreen_UpdateState.md), [JobList_BuildForPartyUnit](../functions/JobList_BuildForPartyUnit.md), [g_RuntimeJobList](../globals/g_RuntimeJobList.md), [g_RuntimeJobListLen](../globals/g_RuntimeJobListLen.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Every reference to g_RuntimeJobList is a 32-bit displacement (four rip-relative `lea`, six reads through the image base plus a sign-extended index), the list is in the zero-filled tail of the data section and no data pointer names it, so it can be moved to a larger block by rewriting ten displacements.

## Behavior

- V (census of every instruction of the code section, base relocation directory): the ten code references are the only references to the 96 bytes of the list; none is a data pointer, so the base relocation directory needs no change.
- V: the list lies past the raw data of the section that holds it (the bss tail): it is zero when the game starts and the game itself fills it each time JobTree_FillJobRecords runs.
- V: the four rip-relative `lea` (0x140367F15 in JobList_IsSelectedEntryUnflagged; 0x1403684B8, 0x1403687A5, 0x14036885A in JobTree_FillJobRecords) reach any block within 2 GB of the instruction; the six reads in JobScreen_UpdateState add a 32-bit displacement to the image base held in rsi, so the block must also lie within 2 GB above or below the image base.
- V: in JobScreen_UpdateState the reads at 0x140368D06 and 0x140368D42 index the list with g_JobListSelectedEntry (sign-extended from 16 bits); the reads at 0x140368DB9, 0x140368E7D, 0x140368EC5 and 0x140368F9A index it with the result of the cursor call just before (sign-extended from 16 or 32 bits); so the reads accept an index up to 32767, the range of the int16 length.
- V: the reads at 0x140368D06, 0x140368D42, 0x140368DB9, 0x140368E7D and 0x140368EC5 load a 16-bit entry; 0x140368F9A loads only its low byte; JobTree_FillJobRecords tests the 0x2000 and 0x4000 flags with word tests through the register of its `lea` at 0x14036885A (second test at 0x140368884).
- V (offline test on a copy of the exe mapped into a test process, with the ten displacements rewritten): JobList_IsSelectedEntryUnflagged, called natively, reads entry 1000 and entry 1279 of the 1280-word block and its 0x4000 flag; the 48 stock words stay zero (never read or written).
- I: the game writes at most 23 words into the list and reads only those.

## Open questions

? not run in the game yet: a Change Job list of more than 48 entries (scrolling to the end, selecting and changing to a late entry, the preview of a late entry); ? the time the fill loop takes over about 1000 positions when the window scrolls.
