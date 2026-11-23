# Deployment_CountUnitsInArea

- **Address:** `0x1401EE830`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Deployment_CountUnitsInArea(DeploymentState *state, int area)`
- **Callers:** DeploymentGrid_CommenceCheck, Deployment_SelectTile, sub_1401F49EC, sub_1401F5078, sub_1401F5B64
- **Callees:** Deployment_LoadAreaPlacement, Battle_FindUnitNodeAt

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Counts the units that stand on the deployment cells of area 0 or 1.

## Behavior

- V: walks the 25 cell records that Deployment_LoadAreaPlacement(area) returns (8 bytes each) and counts the cells whose flag byte is 1 and on which Battle_FindUnitNodeAt(x, y, layer bit) finds a unit.

## State touched

- Calls: [Deployment_LoadAreaPlacement](Deployment_LoadAreaPlacement.md), [Battle_FindUnitNodeAt](Battle_FindUnitNodeAt.md)

## Referenced by

- Called by: [DeploymentGrid_CommenceCheck](DeploymentGrid_CommenceCheck.md), [Deployment_MoveCursorToFreeCell](Deployment_MoveCursorToFreeCell.md), [Deployment_SelectTile](Deployment_SelectTile.md)
- Observed behaviours: [DeploymentAcceptsOneToFivePlacedUnits](../behaviors/DeploymentAcceptsOneToFivePlacedUnits.md), [DeploymentCellsAreNotCheckedAgainstTheMapAndCountByTile](../behaviors/DeploymentCellsAreNotCheckedAgainstTheMapAndCountByTile.md)

## Notes

The first argument is not used by the body.

## Open questions

None recorded.
