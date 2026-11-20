# ScenarioMapStateIsOnlyAMapVariationSelector

- **Kind:** observed behaviour
- **Scope:** engine (scene variable 48)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [ScenarioSetup_ApplyRecord](../functions/ScenarioSetup_ApplyRecord.md), [MapRow_SelectVariation](../functions/MapRow_SelectVariation.md), [MapMesh_Load](../functions/MapMesh_Load.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The map state (0..15) of a scenario setup record, scene variable 48, has two readers only: the Map row variation selector and the mesh set that remembers it.

## Behavior

- V: ScenarioSetup_ApplyRecord writes byte +3 high nibble to variable 48. Stock: 0 on 691 rows, 1 on 20, 2 on 2 (M).
- V: MapRow_SelectVariation compares it with the variation struct's map state selector (-1 = any).
- V: MapMesh_Load stores it in the mesh set (+294928); nothing else reads it.

## Open questions

None recorded.
