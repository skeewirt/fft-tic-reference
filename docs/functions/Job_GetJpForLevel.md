# Job_GetJpForLevel

- **Address:** `0x1402CC008`
- **Area:** [Job data](../areas/job-data.md)
- **Prototype:** `unsigned __int16 Job_GetJpForLevel(unsigned int jobIndex, int level)`
- **Callers:** sub_1400FBB7C (job record JP-to-next-level field)
- **Callees:** sub_1403D325C, sub_1403D3AE8, sub_1403D2FD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns RequiredJobExp[level] of the GeneralJob row (table 189, cache qword_143CD9F00): u16 at row-data + 4 * level where the list offset is the dword at row +8.

## Behavior

- V: decompiled; the 9-element lists are [0,100,200,400,700,1100,1600,2200,3000].

## Referenced by

- Called by: [Job_LevelFromTotalJp](Job_LevelFromTotalJp.md), [UnitWork_StoreToSaveSlot](UnitWork_StoreToSaveSlot.md), [Unit_InitJobJp](Unit_InitJobJp.md), [sub_1403928D4](sub_1403928D4.md)
- Reads tables: [NxdDataGeneralJob](../tables/NxdDataGeneralJob.md)

## Notes

Also known as GeneralJobTable_GetExpForLevel (earlier sheet name).

## Open questions

None recorded.
