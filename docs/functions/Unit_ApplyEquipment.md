# Unit_ApplyEquipment

- **Address:** `0x1402779EC`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `? (unit record, slot index, output)`
- **Callers:** `Unit_ReloadFromJobRow`, `Unit_ReloadFromJobRowEx`, `sub_1402760E8`
- **Callees:** `Item_GetArmorRecord`, `Item_GetRecord`, `Unit_ComputeStats`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Adds the armor and attribute contributions of a unit's equipped items to the unit's stats.

## Behavior

- V: It clears the output field at +0x3C and walks the unit's equipment words from the slot index passed in the second argument.
- V: Each word is tested against 255 and against the 261 bound before it is used.
- V: For a valid word the item record and then the armor sub-record are read, and the armor's attribute byte is applied to the stat block.
- V: It calls three helpers and has three direct callers.
- I: The 255 test and the 261 bound are both present because the word can hold either an empty marker or a stock id.
- V: it first zeroes +0x3B..+0x3D (a word at +0x3C and a byte at +0x3B) and calls Unit_ComputeStats(unit, mode + 1); for each equipped item it adds the attribute record's three stat bytes (bonus PA, MA, Speed) into +0x3B..+0x3D (capped at 255), Move +3 / Jump +4 into +0x42 (cap 253) / +0x43 (cap 7), ORs its 15 status bytes into +0x57.. (innate a, innate b, effective) and its 5 bytes into +0x76.
- V: the seven equipment words are the 7 u16s from +0x1A (0xFF = empty); an item's attribute record is the 26-byte row g_ItemAttributeRecords + 26 x (item record +7) when that byte is below 0x55, and its 15 status bytes go +5..+9 -> +0x57 (always), +10..+14 -> +0x5C (immune), +15..+19 -> +0x61 (current).
- V: its last loop (a pointer from +0x3E, with -3 and -6 from it) makes the totals: +0x3E = min(+0x38 + +0x3B, 99) (PA), +0x3F = min(+0x39 + +0x3C, 99) (MA), +0x40 = min(+0x3A + +0x3D, 50) (Speed, the CT gain Battle_TurnEngine adds); HP / MP are clamped to their maxima.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md), [Unit_ComputeStats](Unit_ComputeStats.md)

## Referenced by

- Called by: [Unit_BuildInnateStatuses](Unit_BuildInnateStatuses.md)
- Observed behaviours: [AnUnservedIdFromASaveFreezesTheGame](../behaviors/AnUnservedIdFromASaveFreezesTheGame.md), [BattleStatChangeAndCtGainSteps](../behaviors/BattleStatChangeAndCtGainSteps.md)
- Reads tables: [ItemAttributes](../tables/ItemAttributes.md)

## Notes

Name is ours. The offsets +0x38..+0x3F, +0x5C and +0x61 are reached through loops (a pointer walked with a count, and the pointer -3 / -6 of the totals loop), not as constants in the code.

## Open questions

None recorded.
