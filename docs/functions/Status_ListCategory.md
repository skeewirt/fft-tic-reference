# Status_ListCategory

- **Address:** `0x1400FAAB4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Status_ListCategory(unsigned int status)`
- **Callers:** sub_14010A42C, sub_14010C1FC, sub_140112A04, sub_1402C25E0
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the list category of a status from its UIStatusEffect text row: 1 a gain, 2 an ailment, anything else not listed.

## Behavior

- V: returns -1 at once for a status above 39 (an unsigned compare of the id with 39 and a jump when above).
- V: finds nxd table 57 (UIStatusEffect) through NxdRegistry_Find once and keeps it in qword_143CDA3D0, looks up the row whose key is the status + 1 with NxdTable_GetRowById, and returns -1 when the table or the row is missing.
- V: returns the dword at row +0x14 (the Unknown14 column: 1 for Float, Reraise, Regen, Protect, Shell, Haste, Faith, Atheist, Reflect; 2 for KO, Stone, Poison, Slow, Stop, Doom and the other ailments; 0 for Readying, Jumping, Evading, Performing).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Observed behaviours: [StatusScreenReadersAndIconPath](../behaviors/StatusScreenReadersAndIconPath.md)

## Notes

Name is ours.

## Open questions

None recorded.
