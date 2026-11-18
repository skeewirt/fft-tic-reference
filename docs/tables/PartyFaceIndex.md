# PartyFaceIndex

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x14067F840`
- **Rows:** 74 rows of 1 byte
- **Keyed by:** unit marker byte below 0x4A
- **Read by:** [PartyUnit_GetFaceRecord](../functions/PartyUnit_GetFaceRecord.md), [Unit_GetFaceIndex](../functions/Unit_GetFaceIndex.md), [PartyUnit_FaceIndexForJob](../functions/PartyUnit_FaceIndexForJob.md)
- **Row layout:** [PartyFaceIndexRow](../structs/PartyFaceIndexRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Maps a unit marker or job to a face record index. Entries 0..52 carry values, 53..73 are zero; the function also hard-codes face records for jobs 72, 144, 145, 150, 151, 153, 154 and markers 0x82, 0xA2, 0xA3.

## Behavior

- V: the reader guard is below 0x4A and the next table starts at +74.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
