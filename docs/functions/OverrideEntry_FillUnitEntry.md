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
- V: the dword +0x10 (column job), when not 0, is stored as one byte into unit +10 (load 0x1401EA6D0, store 0x1401EA6D4): a job id above 255 keeps only its low byte (300 becomes job 44).
- V: the 40-byte unit entry is a spawn record: OverrideEntry_LoadBattleEntries fills the battle's entry block in place, and Battle_PlaceEntryUnits builds battle unit i from entry i through Unit_BuildFromRecord, whose UnitWork_InitFromSpawnRecord copies +10 into C +3 (2026-11-09).
- V: a dword +0x44 that is not 0 is a key of nxd table 218 whose row byte +8 goes to unit +32.
- V: bytes +0x8E..+0x97 and +0x99 set bits 0..10 of *flags; Battle_PlaceEntryUnits stores that flag set at battle unit +504, and bit 2 (the byte at +0x90, column flag_2) is the one BattleObjective_ShowsTarget tests.
- V: the row fields land in the spawn entry as follows: level (+0x7C) -> entry +3, brave (+0x82) -> +6, faith (+0x84) -> +7, from_guest_record (+0x98) -> bit 3 of entry +1 (build the unit from the guest save record 50..53 with the same marker), head / body / accessory / right_hand / left_hand (+0x2C, +0x30, +0x34, +0x38, +0x3C) -> entry +18..+22 as one byte each, presence (+0x48) -> bits 0xC0 of entry +24.
- V: each item dword is stored as one byte, so a pre-placed unit cannot start with an item id above 255 (the same one-byte limit as the job); 0xFF in the entry means an empty slot and 0xFE a default pick (markers compared by the consumer UnitWork_ApplyStartingEquipment, not by this function).
- V: the name key (+0x0C, column chara_name) is not copied here; Unit_ApplySpawnRecord and UnitWork_SetNameKey read it from the row directly.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [OverrideEntry_LoadBattleEntries](OverrideEntry_LoadBattleEntries.md)
- Observed behaviours: [PreplacedUnitsStartWithOneByteItems](../behaviors/PreplacedUnitsStartWithOneByteItems.md), [SpawnedUnitsCarryAOneByteJob](../behaviors/SpawnedUnitsCarryAOneByteJob.md), [StockBattleEntryListsHoldAtMostSixteenUnits](../behaviors/StockBattleEntryListsHoldAtMostSixteenUnits.md), [UnitEventFlagWord](../behaviors/UnitEventFlagWord.md)
- Reads tables: [NxdDataCharaControlId](../tables/NxdDataCharaControlId.md)

## Notes

The OverrideEntryData rows are 156 bytes apart in the retail file; the last column, Unknown9C (+0x9C), is therefore the next row's first byte, which this reader never reads. X6 locks that column on stock rows.

## Open questions

? the meaning of the copied fields not listed above.
