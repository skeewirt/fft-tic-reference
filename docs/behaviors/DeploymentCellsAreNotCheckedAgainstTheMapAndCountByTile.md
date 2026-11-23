# DeploymentCellsAreNotCheckedAgainstTheMapAndCountByTile

- **Kind:** observed behaviour
- **Scope:** engine (battle deployment)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Deployment_LoadAreaPlacement](../functions/Deployment_LoadAreaPlacement.md), [Deployment_FindFreeCell](../functions/Deployment_FindFreeCell.md), [Deployment_MoveCursorToFreeCell](../functions/Deployment_MoveCursorToFreeCell.md), [Deployment_CountUnitsInArea](../functions/Deployment_CountUnitsInArea.md), [Deployment_PlaceUnitAtCursor](../functions/Deployment_PlaceUnitAtCursor.md), [Unit_CheckSpawnTile](../functions/Unit_CheckSpawnTile.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A deployment area's placeable cells come only from its placement record (the 25-bit cell mask, anchor and orientation); nothing checks that a unit can stand on a cell's tile, and an area counts its units by the units standing on its cells. The stock grids open only usable tiles and never share one, so neither shows in the stock game.

## Behavior

- V: Deployment_LoadAreaPlacement sets a cell placeable from the mask bit alone; the cell's tile is the anchor (+4 / +5) plus the cell's offset of -2..+2 in the orientation's order, so a grid near the map's edge has cells off the map (seen: anchor (0, 5) gives x -2..2, anchor (5, 9) gives y 7..11 on a map 10 tiles deep).
- V: Deployment_FindFreeCell takes a cell as free when no unit stands on its tile, so the cursor can be sent to such a tile; A there joins a unit whose spawn check fails (no shape, no drawn unit) and Deployment_PlaceUnitAtCursor faults (seen live 2026-11-22, cell (4, 5) at Sand Rat's Sietch).
- V (seen live 2026-11-22): with two grids sharing tiles, a unit of one area standing on a shared tile counted for the other too (Deployment_CountUnitsInArea counts by tile), so that area read full while its 'Remaining' showed room, and the cursor did not move to it.
- V (seen live 2026-11-22): a cell on a usable tile that no stock grid opens works as a stock cell (placement, the cursor's moves, the battle, a retry): Sand Rat's Sietch's two grids opened on all their usable tiles took 10 + 10, 19 + 1 (area 260's anchor moved 2 tiles along x) and 1 + 19 (area 261's moved 2 along y).

## Open questions

? the meaning of the list byte (+5, EntryArea byte +4); every stock row read 0 here.
