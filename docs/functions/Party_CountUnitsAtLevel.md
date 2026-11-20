# Party_CountUnitsAtLevel

- **Address:** `0x1400DC698`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool Party_CountUnitsAtLevel(int level, void *unused, char skip_battle)`
- **Callers:** sub_1400DCADC, sub_1400DCB0C
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when at least 5 party units have reached a level.

## Behavior

- V: unless the third argument is set, counts the units of records 16..20 (slot byte not 0xFF) whose level (+0x29) is at least the given level and marks their roster indices; then counts the roster units (54 records) not marked whose level byte (+29) is at least the level; returns count >= 5.

## Referenced by

- Observed behaviours: [PartyResultsAreFoundBySaveIndexInAllRecords](../behaviors/PartyResultsAreFoundBySaveIndexInAllRecords.md)

## Open questions

None recorded.
