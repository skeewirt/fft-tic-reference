# Deployment_MoveCursorToFreeCell

- **Address:** `0x1401F49EC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Deployment_MoveCursorToFreeCell(DeploymentState *state)`
- **Callers:** sub_1401F22D0
- **Callees:** SceneVar_Read, sub_1401F3060, Deployment_SelectArea, Deployment_CountUnitsInArea, Deployment_LoadAreaPlacement, Deployment_FindFreeCell, Deployment_AreaOfPlacedUnit, sub_1403033CC, sub_1401F4E74, sub_1402607E4, sub_140202208

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Moves the deployment tile cursor to a free cell after a placement or a group switch: per area it finds a free cell, then picks one by the area the state names, the areas' room and the distance from the cursor.

## Behavior

- V: takes at most 2 areas (scene variable 52, cut to 2); for each it sets a room flag (Deployment_SelectArea > Deployment_CountUnitsInArea) and asks Deployment_FindFreeCell for a free cell of that area's grid (Deployment_LoadAreaPlacement), starting from no tile (0xFF).
- V: walks the placed list's first 5 entries (state +68 .. +84, from the last) for the tile of a placed unit per area (Deployment_AreaOfPlacedUnit, sub_1403033CC), then sub_1401F4E74.
- V: with two areas it computes the distance from the cursor (dword_140C6AFB8 / dword_140C6ADAC / dword_140C6AFBC) to each area's free cell and, by state +12 and the room flags, writes one area's free cell (or a placed unit's tile) into the cursor; then sets state +0x77F and focuses the unit on the new tile (sub_1402607E4, sub_140202208).
- V (seen live 2026-11-22): an area's room flag is 0 once Deployment_CountUnitsInArea reaches its count, and that function counts the units standing on the area's cells, so with two grids sharing tiles the units of one area on a shared tile filled the other: the cursor stayed on an occupied tile and switching groups (LT) did nothing.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [Deployment_SelectArea](Deployment_SelectArea.md), [Deployment_CountUnitsInArea](Deployment_CountUnitsInArea.md), [Deployment_LoadAreaPlacement](Deployment_LoadAreaPlacement.md), [Deployment_FindFreeCell](Deployment_FindFreeCell.md), [Deployment_AreaOfPlacedUnit](Deployment_AreaOfPlacedUnit.md)

## Referenced by

- Observed behaviours: [DeploymentCellsAreNotCheckedAgainstTheMapAndCountByTile](../behaviors/DeploymentCellsAreNotCheckedAgainstTheMapAndCountByTile.md)

## Notes

Name is ours (was sub_1401F49EC).

## Open questions

None recorded.
