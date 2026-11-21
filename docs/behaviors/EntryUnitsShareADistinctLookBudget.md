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
- V: scene variable 57 has three writers (no event script writes it; all 560 scripts scanned): ScenarioSetup_ApplyRecord writes 0 whenever the scene has a scenario setup record (it also sets word_140D407CC); BattleLoad_ClearPartyReserve writes 0 in battle load state 1, before the units are built in state 5; Deployment_PrepareCandidates writes the count byte (+8) of the first deployment area's placement record (scene variable 53) when word_140D407CC is 0, that is when no scenario record was applied.
- V: so a story battle (one with a scenario setup record) always places its units with variable 57 = 0: at most 9 distinct sprites and 16 kept units; a random battle (no record: variable 39 is 0) uses its area's count: the 57 random-battle areas (rows 513..569) all hold 5, so at most 4 distinct sprites and 11 kept units.
- V (seen live, random battle at Mandalia Plain, twice): variable 57 was written 5 -> 0 -> 5 by the event thread, both writes before Battle_PlaceEntryUnits ran (breakpoint at its entry: 5); at Orbonne Monastery (the first story battle) it read 0, with 11 units on the field using 9 distinct sprites.
- V: the budgets are checked only by Battle_PlaceEntryUnits at load: the deployed party (Battle_AddJoinedUnit) and units revealed later (BattleUnit_RevealOnField) never pass through them.
- V: the two numbers are one constant in Battle_PlaceEntryUnits: 9 loaded at 0x14027135B (minus variable 57, 0 when the variable is above 9) is the look budget, and the unit budget is that value + 7 (0x140271389); the sprite list word_143D1A170 has room for 24 sprites before the next global (dword_143D1A1A0), more than the 16 entries can add.
- V (tested limit 2026-11-20, random battle at Mandalia Plain, var57 = 5, the entries replaced at Battle_PlaceEntryUnits by 8 placed units with 6 distinct sprites): with the stock constant, 4 sprites loaded and the two entries of the 5th and 6th sprites (records 4 and 5) were built but left off the field (6 on the field); with the immediate at 0x14027135B and the clamp at 0x140271370 both raised from 9 to 14 in memory, the same setup put all 8 on the field with 6 sprites (8 drawing slots, 6 look pool records).
- V: in Deployment_PrepareCandidates' second branch (scene variable 510 set) the area row is picked by the map id (row byte +9), variables 52..54 are written (two areas) and the row's count byte is rewritten to 4 after variable 57 takes the old count.

## Open questions

? what scene variable 510 marks (the branch that rewrites an area count to 4).
