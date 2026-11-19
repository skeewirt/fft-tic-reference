# UnitWork_ApplyStartingEquipment

- **Address:** `0x140277564`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void UnitWork_ApplyStartingEquipment(void *work, const void *setup)`
- **Callers:** sub_140275CA4
- **Callees:** UnitWork_PickStartingItem, Item_GetRecord, Item_GetWeaponRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Seeds a unit work record with its starting equipment while the unit is built from a setup record: the five slot bytes of the setup record are resolved to item ids and the hand slots and the two-handed state are derived from them.

## Behavior

- V: the first argument is the 512-byte unit work record and the second the setup record read by the spawn initialiser; the five bytes at setup +0x12..+0x16 are the starting ids for the five equipment slots.
- V: when work +6 bit 0x20 is set the five bytes are copied straight to the work words at +0x1A, +0x1C, +0x1E, +0x20 and +0x24, with 0xFF written to +0x22 and +0x26.
- V: otherwise each slot is walked in a fixed order; a byte of 0xFE means "pick a default" and is passed to UnitWork_PickStartingItem with the category base 0x80 and the slot index.
- V: the first slot that yields an id other than 0xFE fills the right hand at +0x20; when the slot still returns 0xFE the left-hand path is tried instead.
- V: Item_GetRecord is called on the chosen hand id and its slot-flags byte +3 bit 0x40 clears the left hand at +0x22.
- V: Item_GetWeaponRecord is called on the right-hand id and its flags byte +1 bit 1 also clears the left hand; unit +0x9A bit 1 has the same effect.
- V: the picked head, body and accessory ids land in the work words at +0x1A, +0x1C and +0x1E.
- I: the 0xFE sentinel means "no forced item, use a level-appropriate default", because the picker only accepts records whose level is not above the unit level.
- I: the routine runs during unit construction only; the saved equipment path (Unit_LoadEquipmentAndEvade) later overwrites the hands and evade values.
- ?: whether a setup record with a non-0xFE byte can name an item the unit cannot equip; this body does not test the equip flags for those ids.

## State touched

- Calls: [UnitWork_PickStartingItem](UnitWork_PickStartingItem.md), [Item_GetRecord](Item_GetRecord.md)

## Referenced by

- Called by: [Unit_BuildFromRecord](Unit_BuildFromRecord.md)
- Observed behaviours: [PreplacedUnitsStartWithOneByteItems](../behaviors/PreplacedUnitsStartWithOneByteItems.md)

## Notes

Whole function read (806 bytes, single caller). The five-byte setup field and the 0xFE sentinel are read from this body; the field has not been tied to a named column of the spawn record.

## Open questions

None recorded.
