# Deployment_LoadAreaPlacement

- **Address:** `0x140303408`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void *Deployment_LoadAreaPlacement(int index)`
- **Callers:** Battle_JoinUnitAndLoad, sub_1401EE734, sub_1401EE830, sub_1401EE9B4, sub_1401EF0D8, sub_1401F3060, sub_1401F49EC, sub_1401F5808
- **Callees:** SceneVar_Read, NxdRegistry_Find, NxdTable_GetRowById, NxdTable_GetEntryCount, NxdTable_GetEntryByKeys2, NxdEntry_GetRow, sub_1402FF440

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the deployment area index (scene variable 53 + index): selects its placement record and builds the grid of placeable cells around it.

## Behavior

- V: returns null when the index is not below the number of areas (scene variable 52).
- V: stores the area id in dword_1437A0324 and the placement record (12 bytes at off_1408ECA58 + 12 * area) in off_1408ECA60.
- V: reads the EntryArea table (nxd 244) rows keyed (area, n) for n below 25 and collects byte +4 of each existing row into a 16-byte list in row order.
- V: the placement record's bytes +4 .. +7 pick the orientation and the anchor of a 5 x 5 cell grid (25 eight-byte cell records at 0x1437A01F0): each cell takes its flag byte from the grid at 0x1437A0420, its position offsets from the record +4 / +5 and its facing bits from +6; a cell with a non-zero flag takes the next byte of the collected list.
- I: the list bytes are what each placeable cell shows or assigns; the byte's meaning is not decoded.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdTable_GetEntryCount](NxdTable_GetEntryCount.md), [NxdTable_GetEntryByKeys2](NxdTable_GetEntryByKeys2.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [Deployment_AreaOfPlacedUnit](Deployment_AreaOfPlacedUnit.md)
- Observed behaviours: [DeploymentAcceptsOneToFivePlacedUnits](../behaviors/DeploymentAcceptsOneToFivePlacedUnits.md)

## Open questions

? EntryArea row byte +4 and the placement record bytes +4..+8 are not decoded.
