# PartyResultsAreFoundBySaveIndexInAllRecords

- **Kind:** observed behaviour
- **Scope:** engine (after a battle)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [SaveHeader_FillBattleFields](../functions/SaveHeader_FillBattleFields.md), [sub_1402C60E4](../functions/sub_1402C60E4.md), [sub_1402C53F0](../functions/sub_1402C53F0.md), [Party_CountUnitsAtLevel](../functions/Party_CountUnitsAtLevel.md), [Deployment_AreaOfPlacedUnit](../functions/Deployment_AreaOfPlacedUnit.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

After a battle the game finds each roster unit's battle record by its save index (+2) among all 21 records, not only in the placed range 16..20.

## Behavior

- V: sub_1402C60E4 (called by Battle_InitScene) walks the 54 roster records and, for each, searches records 0..20 for one whose +2 is the roster index, whose +0x1B5 is not 0xFF and whose +401 is not 0.
- V: SaveHeader_FillBattleFields walks records 16..20 first, then 0..15.
- V: Party_CountUnitsAtLevel (true when at least 5 units reach a level) counts records 16..20 and then the roster units not among them.
- V: readers that take the placed party from records 16..20 only: sub_1401F16F4 (numbering after the commence check), Deployment_AreaOfPlacedUnit (the record of placed entry n, searched by party index in 16..20), sub_1402C53F0 (the victory screen's top unit, picked from a per-record score of the battle controller for 16..20) and Party_CountUnitsAtLevel.
- V: the other functions that load 16 near the unit table use it for something else (16-byte status copies, range marks, a 16-entry tile loop).

## Open questions

? readers that take the party by index without the immediate 16 (not searched).
