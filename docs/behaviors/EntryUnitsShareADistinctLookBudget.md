# EntryUnitsShareADistinctLookBudget

- **Kind:** observed behaviour
- **Scope:** engine (scripted battle spawn)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md), [EntryUnits_CheckLookBudget](../functions/EntryUnits_CheckLookBudget.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

While the 16 entry units of a battle are placed, two budgets drop units: at most 9 minus scene variable 57 distinct sprite numbers (the battle's unique-sprite limit of 9 when the variable is 0) and at most 16 minus scene variable 57 kept units; both apply before the look pool's 15 records.

## Behavior

- V: EntryUnits_CheckLookBudget(slot, sprite, budget) keeps a list of the sprite numbers met so far (dword_143D1A16C is the count, word_143D1A170 the list); it answers 'over budget' when the sprite's position in that list is not below the budget.
- V: Battle_PlaceEntryUnits passes budget = 9 - scene variable 57 (0 when variable 57 is above 9) and, on 'over budget', sets the unit's slot byte (+1) to 0xFF and its on-field byte (+0x1B5) to 0: the unit is not placed.
- V: the same loop counts the kept units and keeps one only while the count is below the budget + 7 (16 - scene variable 57); a unit past it gets +1 = 0xFF and +0x1B5 = 0xFF.
- V: slot argument 255 clears the sprite list and slot 0 starts it with the sprite as its only member; its only caller, Battle_PlaceEntryUnits, passes the entry index 0..15, so entry 0 always restarts the list and is never dropped by it.
- V: the party units placed at deployment do not pass through this check (they enter through Battle_AddJoinedUnit).
- ?: scene variable 57 is read only here; no code write was found by operand, so it is set by event scripts or scenario data (not traced).
- V (seen live): in a random battle at Mandalia Plain (event 401, one deployment area of 5) scene variable 57 read 5 with one party unit placed, so that battle kept at most 4 distinct entry sprites and 11 entry units; 4 entry units stood on the field.
- I: variable 57 holds the room kept for the party (its capacity), so entry units plus party stay within 9 distinct sprites and 16 units.

## Open questions

? what sets scene variable 57 and its value in story battles and in two-area battles.
