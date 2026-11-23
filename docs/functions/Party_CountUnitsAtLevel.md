# Party_CountUnitsAtLevel

- **Address:** `0x1400DC698`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool Party_CountUnitsAtLevel(int level, void *unused, char skip_battle)`
- **Callers:** sub_1400DCADC, sub_1400DCB0C (achievement conditions)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when at least 5 party units have reached a level.

## Behavior

- V: unless the third argument is set, counts the units of records 16..20 (slot byte not 0xFF) whose level (+0x29) is at least the given level and marks their roster indices; then counts the roster units (54 records) not marked whose level byte (+29) is at least the level; returns count >= 5.
- V: its two callers are achievement conditions: sub_1400DCADC asks for level 30 and sub_1400DCB0C for level 40, each passing as the third argument whether a virtual call on its argument returned 28; they sit in the vtables of the achievement classes next to the AchievementDevelopment entries (0x140703BD8, 0x140703B18).
- I: the records 16..20 walk takes the party's battle records to be those five; a party unit in records 0..15 is counted through its roster record instead.

## Referenced by

- Observed behaviours: [PartyResultsAreFoundBySaveIndexInAllRecords](../behaviors/PartyResultsAreFoundBySaveIndexInAllRecords.md)

## Open questions

None recorded.
