# DeploymentAcceptsOneToFivePlacedUnits

- **Kind:** observed behaviour
- **Scope:** engine (battle deployment)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [DeploymentGrid_CommenceCheck](../functions/DeploymentGrid_CommenceCheck.md), [Deployment_SelectArea](../functions/Deployment_SelectArea.md), [Deployment_LoadAreaPlacement](../functions/Deployment_LoadAreaPlacement.md), [Battle_JoinUnitAndLoad](../functions/Battle_JoinUnitAndLoad.md), [Deployment_CountPlaced](../functions/Deployment_CountPlaced.md), [Deployment_CompactPlaced](../functions/Deployment_CompactPlaced.md), [sub_1401EF0D8](../functions/sub_1401EF0D8.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle's deployment capacity is data (the count bytes of its one or two deployment areas), but the deployment state holds the placed party indices in a five-entry array and three checks refuse more than 5; a placed unit takes a free deployment cell of the area, so the area's cells limit it too.

## Behavior

- V: at the start of deployment sub_1401EF0D8 sets the capacity (deployment state +64) to the count byte (+8) of the placement record of area 0, plus area 1's when scene variable 52 is 2; over the 768 placement records the byte is 0 to 5 (195 zero, 394 five).
- V: the placed party indices are 5 dwords at +68..+87 (set to -1 at the start); +88 is the next field (zeroed at the start). Seen live: with the capacity raised to 6 in memory, the game read +88 (0) as a sixth placed unit with party index 0, so the leader was listed twice.
- V: code limit: DeploymentGrid_CommenceCheck returns 0 unless the capacity is 1 to 5 (capacity - 1 compared unsigned with 4); Deployment_CountPlaced (count of placed entries) returns 0 above 5; Deployment_CompactPlaced (compacts the array through a stack copy) skips above 5 and copies exactly 5 entries.
- V: Deployment_LoadAreaPlacement takes at most 25 rows of the area (the row count is cut to 0x19) and sub_1401EE830 walks 25 placement cells.
- V: placing a unit runs Battle_JoinUnitAndLoad (Deployment_LoadAreaPlacement for the cell, then Battle_AddJoinedUnit), so placed party units take the joiner records 16..20. Seen live in a random battle at Mandalia Plain: the five placed units took records 16, 17, 18, 19 and 20 in placing order.
- V (seen live): the 'Remaining' counter follows the free deployment cells of the area: with the capacity at 6 in memory and an area of 5 cells, it read 0 after five placements and A on another tile placed nothing.
- I: the carousel's 5 visible rows (sub_1401F36A0 compares the candidate count +1828 with 5) are a list window, not a capacity.

## Open questions

? which code reads the sortie screen's max-units text column; ? what +88 holds after deployment starts.
