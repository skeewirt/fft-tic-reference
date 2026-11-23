# Deployment_FindFreeCell

- **Address:** `0x1401F5238`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char Deployment_FindFreeCell(DeploymentState *state, uint8_t *cells, uint8_t *x, uint8_t *y, uint8_t *layer)`
- **Callers:** Deployment_MoveCursorToFreeCell, sub_1401EE9B4, Battle_JoinUnitAndLoad, two calls at 0x1401F344A / 0x1401F34D4
- **Callees:** sub_1402607E4, qsort

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds a free placeable cell in one area's grid (25 cell records of Deployment_LoadAreaPlacement): the cell under (x, y, layer) when free, else the nearest free one; writes it back and returns 1, or returns 0.

## Behavior

- V: when (x, y, layer) is a placeable cell (+0 = 1) of the grid: returns 1 at once when no unit stands there (sub_1402607E4); else searches rings around it, radius 1 up to 4 (the four straight neighbours first, then the ring's other cells), and takes a placeable cell with no unit on it; with any cell's list byte (+5) set, a cell with a higher byte than the start cell's comes first, the lowest byte winning.
- V: when the start tile is no cell of this grid, it lists the placeable cells in grid order, sorts them by the list byte when any is set (qsort, sub_1401F5208), and takes the first with no unit on it.
- V: 'free' is only 'no unit stands on the tile': the cell's own tile is not checked, so a placeable cell on a tile no unit can stand on (a wall, a drop, off the map) is found as free (seen live 2026-11-22 with grids opened on all 25 cells).

## Referenced by

- Called by: [Deployment_MoveCursorToFreeCell](Deployment_MoveCursorToFreeCell.md)
- Observed behaviours: [DeploymentCellsAreNotCheckedAgainstTheMapAndCountByTile](../behaviors/DeploymentCellsAreNotCheckedAgainstTheMapAndCountByTile.md)

## Notes

Name is ours (was sub_1401F5238).

## Open questions

None recorded.
