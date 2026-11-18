# JobRecord_FromJobId

- **Address:** `0x1400FBB7C`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `int64_t JobRecord_FromJobId(JobRecord *rec, JobKey *key)`
- **Callers:** JobTree_FillJobRecords, JobChange_FillUnitEntry and about a dozen other screens (`BattleUnit_BuildJobRecord`, `sub_14013297C`, `sub_14022F868`, `sub_1402B5AE8`, `sub_1402BA1FC`, `sub_1402C1310`, `sub_1402C185C`)
- **Callees:** JobTable_GetRow, Job_IdToIndex, UIText_Get, Str_Format, `sub_1402CC008` (level threshold), `sub_1400FE9D0`, `sub_1403F0B10`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the 148-byte job record used by the job tree and job-change screens from a job key and the unit's job arrays.

## Behavior

- V: stores the key's job id at rec+72.
- V: the Job row is taken from the key id (or the key's +36 field when the id is not positive) via JobTable_GetRow; rec+64 receives the row's dword at +44 (TexturePartsIndex, the job icon number), 0 if no row.
- V: rec+0..63 receives the display text: a formatted UI text 0x3FA with the job id and a flag (key +32 bit 0x40) for positive ids, or text 0x50 otherwise.
- V: if the key carries a level array (+8) rec+68 gets the job's 4-bit level (high nibble for even job index, low nibble for odd).
- V: if the key also carries a total-points array (+24), rec+84 is the points still needed for the next level (a threshold lookup for level+1 minus the stored total); level 8 or above, and job 161, give 0x20000000.
- V: rec+76 and rec+80 are 16-bit values read from the key's arrays at +16 and +24 indexed by the job index.
- I: the two arrays are most likely the unit's current and total job points.
- V: the level is read through [array pointer + index / 2] with the pointer in the second address register (0x1400FBE09) and no bound check on the index (behavior JobArrayAccessesPutTheRecordPointerInTheIndexRegister).

## State touched

- Calls: [JobTable_GetRow](JobTable_GetRow.md), [Job_IdToIndex](Job_IdToIndex.md), [UIText_Get](UIText_Get.md), [Str_Format](Str_Format.md)
- Writes: [JobRecord.jobId](../structs/JobRecord.md#jobid)

## Referenced by

- Called by: [BattleCommand_BuildScreen](BattleCommand_BuildScreen.md), [BattleUnit_BuildJobRecord](BattleUnit_BuildJobRecord.md), [JobScreen_ShowJobAbilities](JobScreen_ShowJobAbilities.md), [UnitInfo_FillFromBattleUnit](UnitInfo_FillFromBattleUnit.md), [sub_14022F868](sub_14022F868.md), [sub_1402C185C](sub_1402C185C.md), [sub_140367AA0](sub_140367AA0.md)
- Observed behaviours: [BattleCommandHeaderTakesTheUnitsJobByte](../behaviors/BattleCommandHeaderTakesTheUnitsJobByte.md), [BattlePanelJobLineShowsDashesAtLevelZero](../behaviors/BattlePanelJobLineShowsDashesAtLevelZero.md), [BattlePanelsNameTheJobByte](../behaviors/BattlePanelsNameTheJobByte.md), [JobArrayAccessesPutTheRecordPointerInTheIndexRegister](../behaviors/JobArrayAccessesPutTheRecordPointerInTheIndexRegister.md), [JobArraysInThePartyRecordHoldStockIndicesOnly](../behaviors/JobArraysInThePartyRecordHoldStockIndicesOnly.md), [JobLevelZeroDrawsDashesAndGreysChangeJob](../behaviors/JobLevelZeroDrawsDashesAndGreysChangeJob.md)

## Notes

rec+64 is the value JobTreePanel_SetJobIcon later turns into the j_NNN icon path.

## Open questions

Meaning of text ids 0x3FA and 0x50.
