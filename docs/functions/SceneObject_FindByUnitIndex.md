# SceneObject_FindByUnitIndex

- **Address:** `0x140260ABC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `SceneObject *SceneObject_FindByUnitIndex(int unit_index)`
- **Callers:** BattleFormation_DrawUnits
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Walks the scene object list and returns the object whose battle unit record has the given unit index, or null.

## Behavior

- V: the list head is `qword_140D3A410` (next pointer at +0); the object's battle unit record pointer is at +0x148 and its unit index at record +444.

## Referenced by

- Called by: [BattleFormation_DrawUnits](BattleFormation_DrawUnits.md), [BattleTask_ActorForecastPanel](BattleTask_ActorForecastPanel.md), [BattleUnit_SetStatusVisual](BattleUnit_SetStatusVisual.md), [Battle_TimelineFocusCamera](Battle_TimelineFocusCamera.md), [Deployment_AreaOfPlacedUnit](Deployment_AreaOfPlacedUnit.md), [UnitPanel_FillEffectLine](UnitPanel_FillEffectLine.md), [sub_1401EA2F0](sub_1401EA2F0.md)
- Observed behaviours: [SceneUnitShapeIsTheQueueWord](../behaviors/SceneUnitShapeIsTheQueueWord.md)

## Open questions

None recorded.
