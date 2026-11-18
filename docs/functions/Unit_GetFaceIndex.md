# Unit_GetFaceIndex

- **Address:** `0x1402896B8`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int Unit_GetFaceIndex(const void *unit)`
- **Callers:** sub_1402BF730
- **Callees:** PartyUnit_FaceIndexForJob (tail jump)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps a unit job and its variant byte to the face index the portrait and unit panel draw.

## Behavior

- V: the job word is unit +0x24; jobs 0x5E through 0x8D (the bound is job-0x5E at most 0x2F) are looked up as a dword at 0x140715378 + job*4 and the table value is returned.
- V: job 0x48 returns 0x4C; 0x90 returns 0x4E; 0x91 returns 0x51; 0x96 returns 0x4E; 0x97 returns 0x4F; 0x99 and 0x9A return 0x51 (the later ids are reached by chained subs from 0x48 and 0x90).
- V: the remaining jobs read the variant byte at unit +0x72.
- V: a variant of 0x82 returns unit +0x166 plus 0x3D; variant 0xA2 (0x82+0x20) returns 0x58 and 0xA3 (+1) returns 0x59.
- V: a variant below 0x4A is looked up in the byte table at 0x14067F840; a variant of 0x4A or above tail-jumps to PartyUnit_FaceIndexForJob with the job and unit +0x70 bit 0x40 as arguments.
- V: the return value is a small face index; the function writes nothing.
- I: the table and the fixed values cover the generic jobs, while the special jobs (Mime, monsters, story characters) get hand-written indices.
- ?: the meaning of the 0x4A threshold and of the 0x14067F840 table; the table contents were not decoded.

## State touched

- Calls: [PartyUnit_FaceIndexForJob](PartyUnit_FaceIndexForJob.md)
- Reads: [UnitWorkRecord.job](../structs/UnitWorkRecord.md#job)

## Referenced by

- Observed behaviours: [UnitFaceIndexReadsTheTableAfterTheHdTable](../behaviors/UnitFaceIndexReadsTheTableAfterTheHdTable.md)
- Reads tables: [PartyFaceIndex](../tables/PartyFaceIndex.md), [SpriteHdEntryByShape](../tables/SpriteHdEntryByShape.md)

## Notes

Whole function read (204 bytes, no unwind entry). The T2 live census lists it as a face-index reader that its scenarios did not reach.

V (2026-11-08): the read at 0x1402896D3 is `dword_140715378[word +0x24]` behind the guard word - 0x5E <= 0x2F, so it reads the 48 dwords at 0x1407154F0 (one per monster job 94..141), the table right after the HD sheet entry table. 0x140715378 is a virtual base 392 bytes inside the HD table.

## Open questions

None recorded.
