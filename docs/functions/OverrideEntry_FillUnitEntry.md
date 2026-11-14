# OverrideEntry_FillUnitEntry

- **Address:** `0x1401EA638`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void OverrideEntry_FillUnitEntry(uint8 *unit, int *flags, const uint8 *row)`
- **Callers:** OverrideEntry_LoadBattleEntries
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies one OverrideEntryData row into a 40-byte unit entry of a scripted battle: the fields whose row value is not the 'keep' marker overwrite the entry, and the flag bytes build a bit set.

## Behavior

- V: does nothing unless the unit, flags and row pointers are set; when row byte +0x8D (141) is non-zero it only clears unit byte 0 (no field is copied, *flags is left as it was).
- V: reads the row at +0x08, +0x10..+0x48 (dwords), +0x7C..+0x8A (words), +0x8C..+0x99 (bytes); the largest offset read is +0x99.
- V: the dword +0x10 (column MainJob), when not 0, is stored as one byte into unit +10 (load 0x1401EA6D0, store 0x1401EA6D4): a job id above 255 keeps only its low byte (300 becomes job 44).
- V: the 40-byte unit entry is a spawn record: OverrideEntry_LoadBattleEntries fills the battle's entry block in place, and Battle_PlaceEntryUnits builds battle unit i from entry i through Unit_BuildFromRecord, whose UnitWork_InitFromSpawnRecord copies +10 into C +3 (2026-11-09).
- V: a dword +0x44 that is not 0 is a key of nxd table 218 whose row byte +8 goes to unit +32.
- V: bytes +0x8E..+0x97 and +0x99 set bits 0..10 of *flags.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [OverrideEntry_LoadBattleEntries](OverrideEntry_LoadBattleEntries.md)
- Observed behaviours: [SpawnedUnitsCarryAOneByteJob](../behaviors/SpawnedUnitsCarryAOneByteJob.md)

## Notes

The OverrideEntryData rows are 156 bytes apart in the retail file; the layout's last column Unknown9C (+0x9C) is therefore the next row's first byte, which this reader never reads.

## Open questions

? the meaning of most copied fields (the layout comments name a few).
