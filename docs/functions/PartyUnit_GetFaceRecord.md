# PartyUnit_GetFaceRecord

- **Address:** `0x140289548`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int16_t PartyUnit_GetFaceRecord(int16_t partySlot, uint8_t *outRecord)`
- **Callers:** JobChange_RunPreviewAnim, sub_1402BF730
- **Callees:** sub_1402B5644 (a JobTable byte 46/47 reader, see the W0 correction), sub_1402897B4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Selects the face / portrait record of a party unit and writes it to the output: 12 bytes copied from `g_PartyFaceRecords` plus a rebuilt face-variant word.

## Behavior

- V (decompile): job word (+36) 72, 144, 145, 150, 151, 153..154 select fixed record indexes (76, 82, 79, 81); marker byte (+114) 0x82, 0xA2, 0xA3 select others (61 + the byte at +358, 88, 89); markers below 0x4A index `g_PartyFaceIndex[marker]`; markers 0x4A and above call sub_1402897B4(job, flag, out).
- V: the record is `g_PartyFaceRecords + 12 * index`: a qword and a dword are copied to the output; for indexes other than 88/89 the word at out+8 is rebuilt from the result of sub_1402B5644.
- V: the job ids it handles are written in the code (hard-coded).

## State touched

- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Reads tables: [PartyFaceIndex](../tables/PartyFaceIndex.md), [PartyFaceRecords](../tables/PartyFaceRecords.md)

## Notes

Data names applied: g_PartyFaceRecords (0x14080C660, 12-byte records), g_PartyFaceIndex (0x14067F840, 80 bytes, marker -> record).

## Open questions

What exactly the face-variant word at out+8 encodes (I: portrait page and cell).
