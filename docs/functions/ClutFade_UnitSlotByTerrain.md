# ClutFade_UnitSlotByTerrain

- **Address:** `0x1402F7ACC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `struct _exception *__fastcall ClutFade_UnitSlotByTerrain(int a1, int a2, unsigned int slot, int16_t r, int16_t g, int16_t b)`
- **Callers:** ClutFade_UnitSlot (two call sites); a data reference
- **Callees:** SceneObject_FindBySlot, sub_140261F60, BattleMap_GetTileRecord, ClutFade_SetTarget

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts two palette fades for a scene object, the second one with its colour change negated under the terrain conditions below.

## Behavior

- V: finds the scene object by slot with `SceneObject_FindBySlot`; does nothing when absent.
- V: reads its position with `sub_140261F60`, divides x and y by 28 to get the tile and takes a layer byte from the object, then gets the tile record with `BattleMap_GetTileRecord`.
- V: calls `ClutFade_SetTarget` with kind 3 and the given colour change, then kind 4; the kind-4 change is negated when the record is null, when the record's byte 3 is below 0x20, or when the object's height word is below -12 times (record height + the top three bits of byte 3).
- I: the negated second change presumably reverses the first on terrain with no water depth (rests on the tile record fields in BattleTileRecord).

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [BattleMap_GetTileRecord](BattleMap_GetTileRecord.md), [ClutFade_SetTarget](ClutFade_SetTarget.md)

## Referenced by

- Called by: [ClutFade_UnitSlot](ClutFade_UnitSlot.md)

## Notes

Whole body read.

## Open questions

The meaning of kinds 3 and 4.
