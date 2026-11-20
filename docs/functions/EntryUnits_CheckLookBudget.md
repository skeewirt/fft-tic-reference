# EntryUnits_CheckLookBudget

- **Address:** `0x140271844`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool EntryUnits_CheckLookBudget(int slot, int16_t sprite, int budget)`
- **Callers:** Battle_PlaceEntryUnits
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Keeps the list of distinct sprite numbers met while the entry units of a battle are placed and answers whether a unit's sprite is past the budget.

## Behavior

- V: slot 255 clears the count (dword_143D1A16C); slot 0 starts the list (word_143D1A170) with the sprite and returns false.
- V: any other slot: finds the sprite in the list, appends it when absent, and returns true when its position is not below the budget.
- V: its only caller, Battle_PlaceEntryUnits, passes the entry index and 9 - scene variable 57 (0 when the variable is above 9), and drops the unit on true.

## Referenced by

- Observed behaviours: [EntryUnitsShareADistinctLookBudget](../behaviors/EntryUnitsShareADistinctLookBudget.md), [OnlyTenDistinctLooksDrawCorrectly](../behaviors/OnlyTenDistinctLooksDrawCorrectly.md)

## Notes

Behavior: EntryUnitsShareADistinctLookBudget.

## Open questions

None recorded.
