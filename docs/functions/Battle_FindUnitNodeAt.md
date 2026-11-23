# Battle_FindUnitNodeAt

- **Address:** `0x140260824`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 __fastcall Battle_FindUnitNodeAt(int a1, int a2, int a3)`
- **Callers:** many battle and deployment paths, including BattleAction_ConfirmCommand, Battle_TimelineFocusCamera, sub_140210AF0, Deployment_AreaOfPlacedUnit, Deployment_CountUnitsInArea and TileCursor_Draw
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the scene object for a unit standing at a tile coordinate, preferring the current actor when several objects match.

## Behavior

- V: walks `g_SceneObjectList` through the next pointer at +0 and returns 0 when the list is empty.
- V: a scene object is a candidate when its three stored tile-coordinate bytes (+136/+137/+138) equal the three arguments, its unit record pointer at +328 is non-null, the unit record's byte +1 is not 0xFF, and the scene object's flag byte at +352 has none of 0x49 set.
- V: it buffers the candidates; with one it returns that object.
- V: with several it returns the candidate whose byte +8 equals the current actor id `dword_140CF873C`; if none matches, the first candidate whose byte +300 low two bits equal 1; otherwise the first candidate.
- ?: the meaning of the 0x49 flag mask and of the +300 low bits.

## State touched

- Reads: [g_SceneObjectList](../globals/g_SceneObjectList.md)

## Referenced by

- Appears in flows: [BattleTimelineCameraFlow](../flows/BattleTimelineCameraFlow.md)
- Called by: [BattleAction_ConfirmCommand](BattleAction_ConfirmCommand.md), [Battle_TimelineFocusCamera](Battle_TimelineFocusCamera.md), [CursorUnit_TopPoint](CursorUnit_TopPoint.md), [Deployment_AreaOfPlacedUnit](Deployment_AreaOfPlacedUnit.md), [Deployment_CountUnitsInArea](Deployment_CountUnitsInArea.md), [TileCursor_Draw](TileCursor_Draw.md), [sub_140203450](sub_140203450.md), [sub_140206F90](sub_140206F90.md)

## Notes

Whole body read (211 bytes). Leaf function; the candidate buffer is a 17-slot local array and the loop has no bound check.

## Open questions

What do the 0x49 flag mask and the +300 low bits select?
