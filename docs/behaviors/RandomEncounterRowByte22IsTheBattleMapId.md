# RandomEncounterRowByte22IsTheBattleMapId

- **Kind:** observed behaviour
- **Scope:** engine (random battle start)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [WorldEncounter_Roll](../functions/WorldEncounter_Roll.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A random battle at a battleground takes its battle map from byte 22 of the encounter row, not from a scenario setup record: the row's byte 22 becomes variable 51 when the world-map screen ends, the chosen formation byte becomes variable 50, 0x200 plus the row's battle number becomes variable 53, variable 52 is 1 and variable 39 is 0.

## Behavior

- V: only locations 24..42 have rows (three per location); the row is the one whose first byte equals the arrival road.
- V (data): byte 22 holds 85 for Mandalia Plain, 74 for the Siedge Weald, 83 for Zeirchele Falls and so on; for all 19 locations the place name of that map equals the location's name.
- V: WorldEncounter_Roll stores the picked formation byte, byte 22 and 0x200 + byte 1 in three globals; sub_140248254 writes the formation to variable 50, 1 to variable 52, the battle number to variable 53 and 0 to variable 39, and keeps byte 22 for the exit of the world-map screen task, which writes it to variable 51.
- V: the same roll serves the walk onto a battleground and the 'Search for Enemies' action (forced roll).
- V: variable 39 is 0, so the scenario setup applier finds no record and leaves variable 51 as the world-map screen wrote it.

## Notes

The field was not decoded before; the byte is an unsigned value 0..255.

## Open questions

? whether anything between the screen's exit and the scene entry rewrites variable 51.
