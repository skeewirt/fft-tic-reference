# MapVariationStruct

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 72 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One 72-byte variation struct of a Map row (nxd 60): which scene conditions it applies under. MapRow_SelectVariation tries them from the last to the first; index 0 is the fallback. Row +24 of the Map row is the variation count and row +20 the offset of the array.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="night"></a>`0x0` | night | `int32` | V | Night selector: matches scene variable 36 (ScenarioSetupRow night); 2 = any. |
| <a id="weather"></a>`0x4` | weather | `int32` | V | Weather selector: matches scene variable 35 (ScenarioSetupRow weather); 5 = any. |
| <a id="map_state"></a>`0x8` | map_state | `int32` | V | Map state selector: matches scene variable 48 (ScenarioSetupRow map_state); -1 = any. |
| <a id="variation_event"></a>`0xC` | variation_event | `int32` | V | Key of a MapVariationEvent row (nxd 207); 0 = none. That row's +8 is an event number and +12 / +16 an array and count of more event numbers; the scene's event must be one of them. |
| <a id="lighting_kind"></a>`0x10` | lighting_kind | `int32` | V | Random-battle lighting kind: must be 0 for a story variation (a non-zero value matches only in random-battle mode, where the kind 1..6 is picked from weather and night). |
| <a id="user_situation"></a>`0x24` | user_situation | `int32` | V | UserSituation condition that must hold; 0 = none. |

## Behavior

- V: MapRow_SelectVariation compares the four selectors with the scene variables passed in (night, weather, map state, event) and accepts the first struct from the end whose fixed field +16 is 0 and whose event and situation tests pass.

## Notes

Detail and evidence: the function sheet MapRow_SelectVariation. The bytes between the listed members are not read by that function.

## Open questions

? the members at +0x14 .. +0x23 and +0x28 .. +0x47 (read by the renderer, not decoded here).
