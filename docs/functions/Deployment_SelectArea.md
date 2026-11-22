# Deployment_SelectArea

- **Address:** `0x140303380`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Deployment_SelectArea(int index)`
- **Callers:** DeploymentGrid_CommenceCheck, sub_1401EF0D8, sub_1401F3858, Deployment_SelectTile, sub_1401F49EC, sub_1401F5078
- **Callees:** SceneVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Makes the deployment area of the scene (index 0 or 1) the current one and returns a count byte of its placement record.

## Behavior

- V: returns 0 when the number of areas (scene variable 52) is not above the index.
- V: otherwise stores the area id (scene variable 53 + index) in dword_1437A0324, points off_1408ECA60 at the 12-byte placement record at off_1408ECA58 + 12 * area, and returns the signed byte at record +8.
- V: the byte is the number of party units the area takes: Deployment_SelectTile refuses a placement once that many units stand on the area's cells, and the capacity is the sum over the areas (seen live: raised from 5 to 6 in memory, the area took six).

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md)

## Referenced by

- Called by: [DeploymentGrid_CommenceCheck](DeploymentGrid_CommenceCheck.md), [Deployment_SelectTile](Deployment_SelectTile.md), [sub_1401EF0D8](sub_1401EF0D8.md)
- Observed behaviours: [DeploymentAcceptsOneToFivePlacedUnits](../behaviors/DeploymentAcceptsOneToFivePlacedUnits.md), [DeploymentRowsOfEachBattle](../behaviors/DeploymentRowsOfEachBattle.md), [StockBattleEntryListsHoldAtMostSixteenUnits](../behaviors/StockBattleEntryListsHoldAtMostSixteenUnits.md), [TwoDeploymentAreasShareOneCapacity](../behaviors/TwoDeploymentAreasShareOneCapacity.md)

## Open questions

None recorded.
