# ScenarioWeatherLevelAndNightFlag

- **Kind:** observed behaviour
- **Scope:** engine (scene variables 35 and 36)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [ScenarioSetup_ApplyRecord](../functions/ScenarioSetup_ApplyRecord.md), [MapRow_SelectVariation](../functions/MapRow_SelectVariation.md), [sub_140306C90](../functions/sub_140306C90.md), [Battle_MoveRange_WeatherCost](../functions/Battle_MoveRange_WeatherCost.md), [Formula_SceneVarElemMod](../functions/Formula_SceneVarElemMod.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The weather level (0..4) and the night flag (0 / 1) that a scenario setup record gives a scene decide which variation of the battle map is drawn, bow hit chances, the movement cost of terrain, an elemental modifier and the lighting kind of a random battle.

## Behavior

- V: ScenarioSetup_ApplyRecord writes the record's byte +3 low nibble to scene variable 35 (weather, 0..4) and byte +4 to scene variable 36 (night). Stock: weather 0 on 594 rows, 1 on 47, 2 on 33, 3 on 25, 4 on 14; night 0 on 601, 1 on 112 (M, over the rows).
- V: MapRow_SelectVariation matches variable 36 against the variation struct's night selector (2 = any) and variable 35 against its weather selector (5 = any).
- V: sub_140306C90: for an item whose equipment category is 11 or 12, night (variable 36 == 1) multiplies the formula block's high byte by 3 / 4 and weather 3 or 4 does so again (both together: 9 / 16).
- V: Battle_MoveRange_WeatherCost and Formula_SceneVarElemMod read variable 35.
- V: in a random battle the lighting kind is 1 / 2 / 3 for weather 0 / 1..2 / 3..4 by day and 4 / 5 / 6 at night (variable 36 not 0), picked among the variation structs by their lighting kind.

## Open questions

? what Battle_MoveRange_WeatherCost and Formula_SceneVarElemMod do with the level.
