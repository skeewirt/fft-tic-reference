# PartyUnit_BuildJobRecord

- **Address:** `0x1402B5644`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `int PartyUnit_BuildJobRecord(unsigned saveIndex)`
- **Callers:** PartyUnit_GetFaceRecord
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the classic-graphics face value of a save unit record: it finds the record's portrait code the way sub_14032AB3C does (marker, job byte, job row), from its own copy of the code words, and turns the code into the value PartyUnit_GetFaceRecord builds the classic face record from.

## Behavior

- V: saveIndex below 0x36 selects g_UnitSaveData + 600 * index; a larger index leaves the record pointer null and the marker read goes through it (a fault; the one caller passes a record index).
- V: the look index: a marker below 0x80 is the index itself; 0x80 gives 2 * job - 52 and 0x81 (tested by subtracting 0x80, then 1) 2 * job - 51 (Mime, job 93, two less); 0xA2 and 0xA3 give index 0; every other marker of 0x80 and up takes byte +46 of the job row of the job byte.
- V: on every path of a marker 0x80 and up (except Mime with 0x80) job 91 gives index 130 and job 92 index 131.
- V: an index below 0xD3 reads the code word of g_PortraitCodeA; otherwise, and for marker 0, the code is 0.
- V: markers 0x80 and 0x81 with job 160 give code 104 (105 for 0x81), with job 161 or 164 code 106 + (marker & 1); these tests read the job byte from the record again.
- V: the value: code 24 returns 122; a code below 63 is the value (one less for a marker of 0x80 and up); codes 63 to 82 read a signed byte table at 0x14067FAC9 (its entries 63 to 82 hold 62 to 81 in another order), codes of 83 and up and markers 0xA2 / 0xA3 its entry 63 (marker 0x82 skips the job and 0xA2 / 0xA3 tests).
- V: a value of 62 or more returns 3 * value - 124 + job row byte +47 (0 when no job row was read: markers below 0x80, 0x80, 0x81, 0xA2, 0xA3).
- V: writes nothing; the result is in eax.

## State touched

- Reads: [g_PortraitCodeA](../globals/g_PortraitCodeA.md), [g_UnitSaveData](../globals/g_UnitSaveData.md), [g_JobTable](../globals/g_JobTable.md)

## Referenced by

- Observed behaviours: [GenericUnitSpriteNumberFromJob](../behaviors/GenericUnitSpriteNumberFromJob.md), [LookSitesUseTheSaveRecordNotTheSlot](../behaviors/LookSitesUseTheSaveRecordNotTheSlot.md), [LookSumSeesTheBaseJob](../behaviors/LookSumSeesTheBaseJob.md), [SpriteTablesCanLiveInBlocksOf1300Rows](../behaviors/SpriteTablesCanLiveInBlocksOf1300Rows.md), [UnitFaceFromSpriteNumber](../behaviors/UnitFaceFromSpriteNumber.md)
- Reads tables: [JobTable](../tables/JobTable.md), [PortraitCodes](../tables/PortraitCodes.md)

## Notes

Whole function read (2026-11-08). Rewritten from the 2026-10-27 reference sheet, which read the 0xA0..0xA4 tests as markers (they test the job byte) and the job 91 test as a table choice (it sets the index). The look index part is the same code as sub_14032AB3C, EventMessage_Scripted, sub_140300768 and sub_140300D74, each against its own copy of the code words (behaviour LookSumSeesTheBaseJob). The name is historical: the function returns a face value, not a record.

## Open questions

? what the value 3 * v - 124 + job row byte +47 selects in the classic face record (atlas cell ((code >> 2) + 224) << 6).
