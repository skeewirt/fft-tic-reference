# PreplacedUnitsStartWithOneByteItems

- **Kind:** observed behaviour
- **Scope:** engine (scripted battle entries)
- **Area:** [Unit data](../areas/unit-data.md)
- **Affects:** [OverrideEntry_FillUnitEntry](../functions/OverrideEntry_FillUnitEntry.md), [UnitWork_ApplyStartingEquipment](../functions/UnitWork_ApplyStartingEquipment.md), [Unit_BuildFromRecord](../functions/Unit_BuildFromRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A pre-placed unit of a scripted battle takes its starting equipment from one-byte item ids, so no item above id 255 can be a starting item.

## Behavior

- V: OverrideEntry_FillUnitEntry stores each of the row's item dwords (head, body, accessory, right_hand, left_hand) as one byte into spawn entry +18..+22.
- V: UnitWork_ApplyStartingEquipment widens that byte; 0xFF means an empty slot and 0xFE a default pick.
- V: Unit_BuildFromRecord calls it when the mode is not 130 and work +2 is above 0x13.

## Open questions

None recorded.
