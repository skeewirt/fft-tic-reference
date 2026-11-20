# Deployment_SelectTile

- **Address:** `0x1401F474C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool Deployment_SelectTile(DeploymentState *state, bool quiet)`
- **Callers:** sub_1401F22D0
- **Callees:** sub_1401F3060, sub_1402607E4, sub_1401F4F20, Deployment_SelectArea, Deployment_CountUnitsInArea, BattleMsg_SetKind1, sub_140152494, sub_1401F2D80

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs when A is pressed on the deployment tile cursor: selects the placed unit on the tile, or opens the carousel for an empty cell of an area that has room.

## Behavior

- V: sub_1401F3060 sets the current area (+12) from the cursor tile; when it is -1 (not a deployment cell) it shows notice 110 (sub_140152494 on the UI module's +152) unless quiet, and returns 0.
- V: stores the cursor tile (dword_140C6AFB8, dword_140C6ADAC, dword_140C6AFBC) in +1888..+1890 and looks up the unit node standing there (sub_1402607E4).
- V: a unit with a battle record (node +328) stands there: +24 = the node (sub_1401F4F20 when quiet), +101..+103 = the record's tile x, y and layer bit (+0x4F, +0x50, +0x51 >> 7).
- V: an empty cell: +24 = 0 and +101..+103 = -1; when Deployment_CountUnitsInArea(current area) is not below the area's count (Deployment_SelectArea), it sends a kind-1 battle message with the count (BattleMsg_SetKind1) and shows notice 122 unless quiet, and returns 0.
- V: otherwise sets the placement step +1884 to 1, calls sub_1401F2D80(state, empty, 0, 0) and returns 1.
- V (seen live): with the area's count at 5 and five units on its cells, A on a free cell showed the red banner 'this group is full' ('up to 5 units'); with the count raised to 6 in memory the carousel opened and a sixth unit was placed.

## State touched

- Calls: [Deployment_SelectArea](Deployment_SelectArea.md), [Deployment_CountUnitsInArea](Deployment_CountUnitsInArea.md), [BattleMsg_SetKind1](BattleMsg_SetKind1.md)

## Referenced by

- Observed behaviours: [DeploymentAcceptsOneToFivePlacedUnits](../behaviors/DeploymentAcceptsOneToFivePlacedUnits.md), [TwoDeploymentAreasShareOneCapacity](../behaviors/TwoDeploymentAreasShareOneCapacity.md)

## Notes

Behaviors: DeploymentAcceptsOneToFivePlacedUnits, TwoDeploymentAreasShareOneCapacity.

## Open questions

None recorded.
