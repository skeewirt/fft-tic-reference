# EffectAnchor_GetPoint

- **Address:** `0x140384240`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int EffectAnchor_GetPoint(int withHeight, int index, EffectUnitList *list)`
- **Callers:** EffectEmitter_Spawn
- **Callees:** SceneObject_FindBySlot, BattleMap_GetTileRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives an effect's caster (index -1) or target (index 0..) position: a unit's scene position or a tile's centre.

## Behavior

- V: index -1 reads the caster entry at list +196, index n the target entry at list + 4 + 12 n; an entry with a non-zero first word is a tile: (28 x + 14, -12 height, 28 z + 14) from the map tile (BattleMap_GetTileRecord); otherwise the scene object of its slot (SceneObject_FindBySlot) gives the position.
- V: with withHeight set the tile height adds the half-step bits (byte +3 >> 5), and a unit is not placed below its tile.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [BattleMap_GetTileRecord](BattleMap_GetTileRecord.md)

## Referenced by

- Called by: [EffectEmitter_Spawn](EffectEmitter_Spawn.md), [EffectObject_InitMotion](EffectObject_InitMotion.md), [EffectSequence_SpawnGroup14Ring](EffectSequence_SpawnGroup14Ring.md)

## Notes

Name is ours (was sub_140384240). The list is word_141873080 (the effect unit list).

## Open questions

None recorded.
