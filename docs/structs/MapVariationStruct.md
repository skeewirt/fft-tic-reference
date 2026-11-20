# MapVariationStruct

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 72 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One 72-byte variation element of a Map row (nxd 60, the array named by the row's variations offset at +0x14 with the count in the dword at +0x18; both are counted from the start of the row): the scene conditions it applies under and what it sets (post-effect rows, colour pair override, lookup row offset). MapRow_SelectVariation tries the elements from the last to element 1; element 0 is the fallback and is never tested. In a random battle the element is picked by its lighting_kind instead.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="night"></a>`0x0` | night | `int32` | V | Night selector: matches scene variable 36 (ScenarioSetupRow night); 2 = either. |
| <a id="weather"></a>`0x4` | weather | `int32` | V | Weather selector: matches scene variable 35 (ScenarioSetupRow weather level 0..4); 5 = any. |
| <a id="map_state"></a>`0x8` | map_state | `int32` | V | Map state selector: matches scene variable 48 (ScenarioSetupRow map_state); -1 = any. |
| <a id="map_variation_event"></a>`0xC` | map_variation_event | `int32` | V | Key of a MapVariationEvent row (nxd 207); 0 = none. That row's event (+8) or one of its more_events (array at +0xC, count at +0x10) must equal the scene's event number (scene variable 39); a key with no row rejects the element. |
| <a id="lighting_kind"></a>`0x10` | lighting_kind | `int32` | V | Random-battle lighting kind: must be 0 for the story branch to take the element; in a random battle the kind 1..6 is chosen from weather and night (1 / 2 / 3 by day, 4 / 5 / 6 at night for weather 0 or 5+, 1..2, 3..4) and the last element holding it is used. |
| <a id="post_effect_glare"></a>`0x14` | post_effect_glare | `int32` | V | Key of a PostEffectGlare row (nxd 256) loaded as the map's glare setting (MapRenderer_ApplyVariationEffects through EventCharaSprite_SetTable256Entry). |
| <a id="post_effect_lut"></a>`0x18` | post_effect_lut | `int32` | V | Key of a PostEffectLUT row (nxd 285) loaded as the map's colour lookup. |
| <a id="post_effect_depth_lut"></a>`0x1C` | post_effect_depth_lut | `int32` | V | Key of a PostEffectDepthLUT row (nxd 284) loaded as the map's depth lookup. |
| <a id="effect_scale"></a>`0x20` | effect_scale | `float32` | V | Enters the maximum (with 1.0 and two globals) that sets the effect scale limits, stored x4096 and x2048 (MapRenderer_ApplyMapRow); -1.0 and anything below 1.0 change nothing. |
| <a id="user_situation"></a>`0x24` | user_situation | `int32` | V | UserSituation condition that must hold (story branch); 0 = none. |
| <a id="post_effect_dof"></a>`0x28` | post_effect_dof | `int32` | V | Key of a PostEffectDOF row (nxd 227) loaded as the map's depth of field. |
| <a id="depth_bias"></a>`0x2C` | depth_bias | `int32` | V | Key of a DepthBias row (nxd 315); when non-zero its float replaces the renderer's default depth bias. |
| <a id="unknown30"></a>`0x30` | unknown30 | `float32` | V | Stored as a float into the battle control block at +689068 and as (value * 12 - 36) * 4096 at +689084 by MapBlock_ApplyLayerCommand; no reader of those fields was found (? meaning). |
| <a id="unknown34"></a>`0x34` | unknown34 | `float32` | V | Stored the same way at +689072 and +689088; no reader found (? meaning). |
| <a id="background_color_1_red"></a>`0x38` | background_color_1_red | `int16` | V | Byte 0 of the scene colour pair (colour 1); a value above 255 (stock -1) keeps the byte of the map block's light command (MapBlock_RunCommand command 50). |
| <a id="background_color_1_green"></a>`0x3A` | background_color_1_green | `int16` | V | Byte 1 of colour 1; same rule. |
| <a id="background_color_1_blue"></a>`0x3C` | background_color_1_blue | `int16` | V | Byte 2 of colour 1; same rule. |
| <a id="background_color_2_red"></a>`0x3E` | background_color_2_red | `int16` | V | Byte 4 of the pair (colour 2); same rule. |
| <a id="background_color_2_green"></a>`0x40` | background_color_2_green | `int16` | V | Byte 5 of colour 2; same rule. |
| <a id="background_color_2_blue"></a>`0x42` | background_color_2_blue | `int16` | V | Byte 6 of colour 2; same rule. |
| <a id="unknown44"></a>`0x44` | unknown44 | `uint8` | V | Not read by any code (0 on every stock element). |
| <a id="unknown45"></a>`0x45` | unknown45 | `uint8` | V | Stored as a dword into the mesh set at +6070656 by MapRenderer_ApplyMapRow; its one reader, the large draw function sub_1403CDA40, tests it to decide whether to set a float triple from three globals (? what the triple does). |
| <a id="lut_row_offset"></a>`0x46` | lut_row_offset | `uint8` | V | Stored at renderer sub-object +1097; for quads of kind 15 sub_14041AE44 passes it to CharaRender_LutUvForQuad, which adds it to the two vertical LUT coordinates (I: which scene objects are kind 15 quads was not followed). |
| <a id="unknown47"></a>`0x47` | unknown47 | `uint8` | V | Stored inverted (value == 0) into renderer byte +147905 by MapRenderer_ApplyMapRow; no reader of that byte was found (? meaning). |

## Behavior

- V: MapRow_SelectVariation compares the selectors with the scene variables passed in (night, weather, map state, event) and accepts the first element from the end whose fixed field +16 is 0 and whose event and situation tests pass.
- V: the readers of the other members are MapRenderer_ApplyMapRow and MapRenderer_ApplyVariationEffects (+0x14 .. +0x2C, +0x45 .. +0x47), MapBlock_ApplyLayerCommand (+0x30, +0x34) and MapBlock_RunCommand (+0x38 .. +0x42); nothing reads +0x44.

## Referenced by

- Observed behaviours: [MapBackgroundColourPairOverride](../behaviors/MapBackgroundColourPairOverride.md), [MapTablesBytesAndTablesNothingReads](../behaviors/MapTablesBytesAndTablesNothingReads.md), [MapVariationChosenBySceneVariables](../behaviors/MapVariationChosenBySceneVariables.md)

## Notes

Detail and evidence: the function sheets MapRow_SelectVariation, MapRenderer_ApplyMapRow, MapRenderer_ApplyVariationEffects and MapBlock_RunCommand; the behaviours MapVariationChosenBySceneVariables and MapBackgroundColourPairOverride.

## Open questions

? the meaning of +0x30, +0x34, +0x45 and +0x47, and the drawn effect of effect_scale; what the loaders do with the random-battle lighting kind.
