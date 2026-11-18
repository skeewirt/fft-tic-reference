# PartyFaceRecords

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x14080C660`
- **Rows:** 90 rows of 12 bytes
- **Keyed by:** face record index (maximum code index 89)
- **Read by:** [PartyUnit_FaceIndexForJob](../functions/PartyUnit_FaceIndexForJob.md), [PartyUnit_GetFaceRecord](../functions/PartyUnit_GetFaceRecord.md)
- **Row layout:** [PartyFaceRecordRow](../structs/PartyFaceRecordRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Portrait rectangle and variant of each party face. A pointer follows the last record at +0x438.

## Behavior

- V: the reader copies a qword and a dword of the record.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: meaning of the variant and page words in every row
