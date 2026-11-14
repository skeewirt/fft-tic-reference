# UnitWork_PickStartingItem

- **Address:** `0x140277F10`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `uint8_t UnitWork_PickStartingItem(void *work, uint8_t category, uint8_t slot, uint8_t flags)`
- **Callers:** UnitWork_ApplyStartingEquipment
- **Callees:** Item_GetRecord, Item_GetWeaponRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses one item id for a starting-equipment slot: it scans a category of the item table, keeps the ids the unit may use at its level, and returns one of them at random, or 0xFE when the category offers nothing.

## Behavior

- V: the second argument is a category base id (0xD0, 0xAC, 0x90, 0x80 or 0x100 after the shift) and selects the id range to scan; the range end is derived from the base.
- V: each candidate record is rejected when its slot-flags byte +3 has bit 2 set (the "skip in best-equipment" flag).
- V: when the fourth argument is not 0xFF the record equip-category byte +5 must equal it.
- V: the record level byte +2 must not exceed the unit level at work +0x29.
- V: the unit equipment bits at work +0x52 are tested against the record equip-category byte +5, so an item the job cannot equip is skipped.
- V: when the third argument is non-zero it is a mask tested against the flags of the weapon record byte +1.
- V: accepted ids are collected on the stack and one is chosen with the global random state at 0x1408E5FC8; the function returns 0xFE when the list is empty.
- I: the random pick is unweighted over the collected ids; the level test only filters, it does not bias the choice.
- ?: what the two 16-bit words written to the global random state represent; the same state is advanced on every call.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md)

## Referenced by

- Called by: [UnitWork_ApplyStartingEquipment](UnitWork_ApplyStartingEquipment.md)

## Notes

Whole function read (415 bytes). Only called from the starting-equipment walk.

## Open questions

None recorded.
