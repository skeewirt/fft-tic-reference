# Unit_BuildJobUnlockMask

- **Address:** `0x140348684`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `uint32_t Unit_BuildJobUnlockMask(int64_t *levels, char flags, int64_t statePtr, int storyStage)`
- **Callers:** unlock-evaluation path (not traced)
- **Callees:** sub_140275980, sub_1403609F0, Job_IdToIndex

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the 24-bit job-unlock mask for a unit. Bit (0x400000 >> r) is job index r+1: index 20 (our job) = bit 0x8, index 21 = bit 0x4.

## Behavior

- V: `levels` is the unit's nibble-packed job levels (two jobs per byte).
- V: loops over rows of g_JobNeedLevelRows (12 bytes/row, nibble-packed required levels). A row is satisfied when each required nibble <= the unit's level; satisfied -> the row's mask bit is set.
- V: stock loop count is 19 (rows 0..18 = Chemist..Mime). The plan raises it to 21 so rows 19 and 20 (indices 20 and 21) are evaluated.
- V (disassembly): tail - if storyStage >= 20, a second check for the two hidden jobs (ids at unk_14071EA38) walks 24 entries from sub_140275980; if an entry is unmet, or storyStage < 20, execution reaches the instruction at 0x140348806 that ANDs the mask register with 0xFFFFFFF7, which CLEARS mask bit 0x8.
- I: the story table's exact meaning (what the 24 entries are).
- V: rows of g_JobNeedLevelRows (0x14067F390) hold 24 nibbles, high nibble first; nibble n is the level required in job index n. A row's bit is set only when ALL ten compared bytes (20 nibbles) are at or below the unit's levels, so a bit set means every prerequisite is met.
- V: `flags` 0x20 skips the row loop (mask 0); flag 0x40 pads the local level copy and clears mask bit 0x40; flag 0x80 pads it and clears mask bit 0x20.
- V: for story stage 20 and above, bit 0x8 also needs every listed ability to be learned in both jobs whose ids are stored at 0x14071EA38 (76 and 80 in stock, two u32 values): the learned bits of each job (3 bytes per job index, read with the bit reader) are checked against Skillset_BuildAbilityList(set, 15).
- V: PartyUnit_FillFromWork stores the result at party-record +120..+122 (high byte first), which is where JobList_Build reads it.
- I: the work-record builder also keeps the mask in the save record at +47..+49, so it is recomputed on every entry to the jobs screen and needs no saved unlock bit.
- V: a set bit means all prerequisites of that job's row are met (every required level nibble is satisfied); a clear bit means at least one is not.
- V: callers store the three mask bytes (high byte first) at A+47..49 in the save record (UnitWork_BuildFromSave) and at B+120..122 in the party record (PartyUnit_FillFromWork); the job list and Job_IsLockedForParty read the B+120 copy.

## State touched

- Calls: [Job_IdToIndex](Job_IdToIndex.md)
- Reads: [g_JobNeedLevelRows](../globals/g_JobNeedLevelRows.md)

## Referenced by

- Called by: [Errand_ApplyResult](Errand_ApplyResult.md), [UnitWork_BuildFromSave](UnitWork_BuildFromSave.md), [UnitWork_InitFromSpawnRecord](UnitWork_InitFromSpawnRecord.md), [Unit_AwardJobJp](Unit_AwardJobJp.md), [sub_140275EF4](sub_140275EF4.md)
- Observed behaviours: [UnlockMaskStreamRunsIntoLearnedBitsPastIndex23](../behaviors/UnlockMaskStreamRunsIntoLearnedBitsPastIndex23.md)

## Notes

Row r <-> job index r+1. The earlier session zeroed row 20 (index 21: Onion Knight, Squire 6 + Chemist 6) by mistake; the correct row for index 20 is row 19.

Stock rows verified against the classic requirements: Mime needs Squire 8, Chemist 8, Knight 3, Archer 3, Monk 4 and so on. Rows 19 and 20 exist in the stock data (index 20: Geomancer, Dragoon, Samurai and Ninja at 8; index 21: Squire 6 and Chemist 6) but are only read after the 19 -> 21 row-count change. The executable rows, not the GeneralJob table, decide what the jobs list offers; GeneralJob is read only by the tree panel and the exp getter.

The mask is recomputed on every work/party record build, so the save needs no manual unlock bits. The job list is decided by these executable rows, not by the GeneralJob nxd table.

## Open questions

Who stores the returned mask into the unit (unit+120), and which events re-run this?
