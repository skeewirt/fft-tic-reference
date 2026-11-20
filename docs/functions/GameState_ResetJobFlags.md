# GameState_ResetJobFlags

- **Address:** `0x14028433C`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `void GameState_ResetJobFlags(void)`
- **Callers:** new-game path (not traced)
- **Callees:** sub_1400DF7D8, sub_1400B6390, sub_1400C61BC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

New-game reset that initialises byte_1411A7490: 125 per-jobtype flags (at +21) to 1 and 21 per-generic-job flags (at +0) to (GeneralJob byte +0x78 == 0), then clears a block of party/story state.

## Behavior

- V: loop `for (j = 0; j < 21; ++j) flag[j] = (GeneralJob[j] byte +120 == 0)`; the byte is 0 only in rows 0 and 1.
- V: no reader of bytes 0..20 of the block was found in the executable (only this reset, the save pack and unpack routines and the block copy touch them), so the GeneralJob +0x78 value has no visible effect; bytes 21..145 (the 125 job type flags) are read by JobList_RecomputeAvailability and GuideLessons_UpdateUnlocked.

## Referenced by

- Called by: [GameState_ResetParty](GameState_ResetParty.md)
- Observed behaviours: [UnreadColumnsOfJobAbilityStatusTables](../behaviors/UnreadColumnsOfJobAbilityStatusTables.md)
- Reads tables: [NxdDataGeneralJob](../tables/NxdDataGeneralJob.md), [UnitJobFlags](../tables/UnitJobFlags.md)

## Notes

M: row 20 gets flag 0: its byte +0x78 is 1 in stock (data).

## Open questions

Meaning of the flag array (I: 'job / type not yet owned').
