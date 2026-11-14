# Job_IsLockedForParty

- **Address:** `0x14028641C`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `int Job_IsLockedForParty(uint16_t jobId)`
- **Callers:** JobList_Build, sub_1402867BC
- **Callees:** Job_IdToIndex, BitStream_ReadBits, sub_1402CBED4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns 1 if NO party member has the job unlocked, else 0.

## Behavior

- V: if `byte_140D407BB` (party count) is 0, returns 1.
- V: per party unit (skipping units where sub_1402CBED4(unit+36) is true): sets `qword_143C49BF8 = unit+120` (unlock bitfield) and `byte_142FF3CA7 = 1`, reads Job_IdToIndex(id) bits, then 1 bit via BitStream_ReadBits. Bit set -> returns 0.
- V: falls through all units -> returns 1.
- V: the bit field it tests is the mask at B+120 of each party record (PartyUnit_FillFromWork stores it there).

## State touched

- Calls: [Job_IdToIndex](Job_IdToIndex.md), [BitStream_ReadBits](BitStream_ReadBits.md)
- Reads: [g_PartyCount](../globals/g_PartyCount.md), [g_PartyUnits](../globals/g_PartyUnits.md)
- Writes: [g_BitReaderPtr](../globals/g_BitReaderPtr.md), [g_BitReaderReset](../globals/g_BitReaderReset.md)

## Referenced by

- Called by: [JobList_Build](JobList_Build.md)
- Observed behaviours: [UnlockMaskStreamRunsIntoLearnedBitsPastIndex23](../behaviors/UnlockMaskStreamRunsIntoLearnedBitsPastIndex23.md)

## Notes

The bitfield is the 24-bit mask Unit_BuildJobUnlockMask produces; index 20 -> mask bit 0x8.

## Open questions

None recorded.
