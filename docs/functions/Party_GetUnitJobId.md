# Party_GetUnitJobId

- **Address:** `0x1402863E4`
- **Area:** [Job list and unlock](../areas/job-list.md)
- **Prototype:** `int Party_GetUnitJobId(int partyIndex)`
- **Callers:** JobList_Build, JobTree_FillJobRecords, sub_140286A78, sub_14028A8B0
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the job id of a party member, normalising the generic-unit marker values.

## Behavior

- V: unit = g_PartyUnits[partyIndex] (int16 index); marker = unit+114.
- V: marker 128 or 129 -> 74 (generic male/female base job).
- V: marker 130 -> the int16 at unit+36 (the unit's actual job id).
- V: any other marker -> returned unchanged.

## State touched

- Reads: [g_PartyUnits](../globals/g_PartyUnits.md)

## Referenced by

- Called by: [sub_140286A78](sub_140286A78.md), [sub_14028A8B0](sub_14028A8B0.md)

## Notes

The same normalisation is inlined in JobChange_FillUnitEntry. Markers 128/129/130 are the generic-unit variants.

## Open questions

What marker 130 means exactly (a generic unit whose job id is stored at +36).
