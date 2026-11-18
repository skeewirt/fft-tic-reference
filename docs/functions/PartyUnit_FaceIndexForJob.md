# PartyUnit_FaceIndexForJob

- **Address:** `0x1402897B4`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int PartyUnit_FaceIndexForJob(short job, ...)`
- **Callers:** PartyUnit_GetFaceRecord
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps a job id to the face (portrait) record index of a generic unit.

## Behavior

- V: Mime (0x5D) gets a fixed index; ids below 0xA0 give 2*job - 124; 0xA2 / 0xA3 give 88 / 89; other ids 2*job - 236.

## Referenced by

- Called by: [Unit_GetFaceIndex](Unit_GetFaceIndex.md)
- Reads tables: [PartyFaceIndex](../tables/PartyFaceIndex.md), [PartyFaceRecords](../tables/PartyFaceRecords.md)

## Open questions

None recorded.
