# Battle_JoinUnitAndLoad

- **Address:** `0x1401F2E4C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void Battle_JoinUnitAndLoad(void *a1)`
- **Callers:** not recorded
- **Callees:** Battle_AddJoinedUnit, CharaPalette_ReloadForShape

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The mid-battle join: runs Battle_AddJoinedUnit, then the look loader once per frame until it returns 0.

## Behavior

- V: the loader is CharaPalette_ReloadForShape.
- V: after the look loader it sets state +0x18 to the drawn unit (SceneObject_FindByUnitIndex) of the record whose slot byte is its own index and whose +2 is the joined roster index, and copies that record's tile and layer into +0x77C..+0x77E; when no record matches, or the record has no drawn unit, +0x18 keeps its old value (record BattleRetriesRestoreTheirOwnCapture).

## State touched

- Calls: [Battle_AddJoinedUnit](Battle_AddJoinedUnit.md), [CharaPalette_ReloadForShape](CharaPalette_ReloadForShape.md)

## Referenced by

- Called by: [Deployment_PlaceUnitAtCursor](Deployment_PlaceUnitAtCursor.md)
- Observed behaviours: [BattleRetriesRestoreTheirOwnCapture](../behaviors/BattleRetriesRestoreTheirOwnCapture.md), [BattleUnitTableIsSixteenEntriesPlusFiveJoiners](../behaviors/BattleUnitTableIsSixteenEntriesPlusFiveJoiners.md), [DeploymentAcceptsOneToFivePlacedUnits](../behaviors/DeploymentAcceptsOneToFivePlacedUnits.md), [DeploymentStateLayout](../behaviors/DeploymentStateLayout.md), [MidBattleJoinLoadsLooks](../behaviors/MidBattleJoinLoadsLooks.md)

## Open questions

None recorded.
