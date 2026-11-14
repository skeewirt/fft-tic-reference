# Unit_LoadEquipmentAndEvade

- **Address:** `0x1402778D4`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void Unit_LoadEquipmentAndEvade(uint8_t *work, void *unused)`
- **Callers:** not enumerated
- **Callees:** Item_GetRecord, sub_1402B8C74, sub_1402B8CD4, sub_1402B8DA0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the unit work record's weapon and evade bytes (+68..+78) from the job row and the equipped items.

## Behavior

- V: clears +68..+78; +75 = JobTable byte 26 (class evade) of the unit's job (job 0xA1 uses row 164 when the job level nibble at +238 is 8 or more).
- V: skipped when bit 0x20 of work+6 is set.
- V: item at +30: when record +3 has bit 0x08, accessory sub-record bytes 0 / 1 go to +72 / +76.
- V: items at +34 and +38: when record +3 has bit 0x40, shield sub-record bytes 0 / 1 go to +73 / +77 and +74 / +78.
- V: items at +32 and +36: when record +3 has bit 0x80, weapon sub-record bytes 4 / 5 go to +68 / +70 and +69 / +71.
- V: keeps the work pointer in r11 across every item call.
- I: +30 accessory, +32 / +36 right / left hand, +34 / +38 shields; +68.. weapon power, +70.. weapon evade, +72..+74 physical and +76..+78 magic evade.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md), [sub_1402B8C74](sub_1402B8C74.md), [sub_1402B8CD4](sub_1402B8CD4.md), [sub_1402B8DA0](sub_1402B8DA0.md)

## Referenced by

- Called by: [Unit_BuildInnateStatuses](Unit_BuildInnateStatuses.md)

## Notes

- Only the item reads were studied.

## Open questions

None recorded.
