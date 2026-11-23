# BattleMap_GetTileRecord

- **Address:** `0x140249000`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char *__fastcall BattleMap_GetTileRecord(int x, int y, int layer)`
- **Callers:** More than 100 call sites, among them EffectAnchor_GetPoint, EffectEmitter_Spawn, EventScript_Run, SceneUnit_MeasureRange and UnitSprite_DepthSort
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the address of the 8-byte tile record for a map position, clamping every coordinate into the map. It never returns null.

## Behavior

- V: x is clamped to 0..width-1 using the width byte of `g_BattleMapSize`, y to 0..H-1 using the byte at 0x140C6AD6B (the height byte of the same pair), and the layer to 0..1.
- V: the record address is `g_BattleTileTable` + 8*x + 8*width*y + 2048*layer.
- V: a special first step lowers y to H-1 when the battle state is 52, `dword_140782A94` is 275 and the loaded map id is 8; the clamp that follows already gives the same result, so the step changes nothing.
- V: callers that compare the result with null (for example `ClutFade_UnitSlotByTerrain`) test for a case this function cannot produce.

## Referenced by

- Called by: [ClutFade_UnitSlotByTerrain](ClutFade_UnitSlotByTerrain.md), [EffectAnchor_GetPoint](EffectAnchor_GetPoint.md), [EffectEmitter_Spawn](EffectEmitter_Spawn.md), [EffectSequence_SpawnGroup7AtTile](EffectSequence_SpawnGroup7AtTile.md), [SceneUnit_MeasureRange](SceneUnit_MeasureRange.md), [UnitSprite_DepthSort](UnitSprite_DepthSort.md), [sub_14027032C](sub_14027032C.md), [sub_14034DE90](sub_14034DE90.md)

## Notes

Whole body read (133 bytes).

## Open questions

None.
