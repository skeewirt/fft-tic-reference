# BattleUnitTableIsSixteenEntriesPlusFiveJoiners

- **Kind:** observed behaviour
- **Scope:** engine (battle unit table)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md), [Battle_BuildRosterTeam](../functions/Battle_BuildRosterTeam.md), [Battle_JoinUnitAndLoad](../functions/Battle_JoinUnitAndLoad.md), [Battle_AddJoinedUnit](../functions/Battle_AddJoinedUnit.md), [Battle_RebuildUnitTable](../functions/Battle_RebuildUnitTable.md), [Unit_CheckSpawnTile](../functions/Unit_CheckSpawnTile.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 21 records of the live battle unit table are two groups: records 0..15 are the 16 entries of a battle (enemies, guests and other scripted units), records 16..20 take the party units placed at deployment, units that join later and, in one mode, the five-unit roster team.

## Behavior

- V: Battle_PlaceEntryUnits builds record i from entry i for i = 0..15 (record +0x1BC = i; +1 = i for a kept unit, 0xFF for an empty or dropped one).
- V: Battle_BuildRosterTeam fills 5 records, from 0x10 when its argument is 0 and from 0 otherwise, from a 5-entry spawn list of 8-byte entries; with a non-zero argument it also marks records 5..15 empty.
- V: Battle_AddJoinedUnit looks for the first record from 16 to 20 whose slot byte (+1) is 0xFF; when none is free and the battle state is 83 it looks in 0..15; otherwise it returns -1 and adds nothing (code limit: 5 joiners outside state 83; not tried in play). sub_1401EE9B4, which starts the deployment screen, sets the state to 83.
- V: Battle_RebuildUnitTable (after a party change) walks every record 0..20 and rebuilds the ones whose slot byte equals their index and whose +2 equals a placed party index.
- V: Unit_CheckSpawnTile rejects a unit whose tile is outside the map, fails the tile and height tests, or is already taken by a unit of a lower record index (tile fields +0x4F, +0x50 and the layer bit of +0x51).

## Open questions

? whether a placement past record 20 falls into a free entry record in play (the fallback in state 83 was not reached in the live test).
