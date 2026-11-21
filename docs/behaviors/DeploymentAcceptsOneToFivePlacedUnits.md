# DeploymentAcceptsOneToFivePlacedUnits

- **Kind:** observed behaviour
- **Scope:** engine (battle deployment)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [DeploymentGrid_CommenceCheck](../functions/DeploymentGrid_CommenceCheck.md), [Deployment_SelectArea](../functions/Deployment_SelectArea.md), [Deployment_LoadAreaPlacement](../functions/Deployment_LoadAreaPlacement.md), [Battle_JoinUnitAndLoad](../functions/Battle_JoinUnitAndLoad.md), [Deployment_CountPlaced](../functions/Deployment_CountPlaced.md), [Deployment_CompactPlaced](../functions/Deployment_CompactPlaced.md), [sub_1401EF0D8](../functions/sub_1401EF0D8.md), [Deployment_SelectTile](../functions/Deployment_SelectTile.md), [Deployment_CountUnitsInArea](../functions/Deployment_CountUnitsInArea.md), [Deployment_FindPlacedUnitArea](../functions/Deployment_FindPlacedUnitArea.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A battle's deployment capacity is data (the count bytes of its one or two deployment areas), but the deployment state holds the placed party indices in a five-entry array and three checks refuse more than 5; each area also refuses a placement once its own count of units stands on its cells. Tested limit: with the checks, the array and the count raised in memory, a sixth placed unit went into a free entry record and played as a normal party unit.

## Behavior

- V: at the start of deployment sub_1401EF0D8 sets the capacity (deployment state +64) to the count byte (+8) of the placement record of area 0, plus area 1's when scene variable 52 is 2; over the 768 placement records the byte is 0 to 5 (195 zero, 394 five).
- V: the placed party indices are 5 dwords at +68..+87 (set to -1 at the start); +88 is the next field (zeroed at the start). Seen live: with the capacity raised to 6 in memory, the game read +88 (0) as a sixth placed unit with party index 0, so the leader was listed twice.
- V: code limit: DeploymentGrid_CommenceCheck returns 0 unless the capacity is 1 to 5 (capacity - 1 compared unsigned with 4); Deployment_CountPlaced (count of placed entries) returns 0 above 5; Deployment_CompactPlaced (compacts the array through a stack copy) skips above 5 and copies exactly 5 entries.
- V: Deployment_LoadAreaPlacement takes at most 25 rows of the area (the row count is cut to 0x19) and Deployment_CountUnitsInArea walks 25 placement cells.
- V: per-area limit: Deployment_SelectTile (A on the tile cursor) refuses an empty tile when Deployment_CountUnitsInArea (units standing on the current area's cells) is not below the area's count byte (Deployment_SelectArea), and shows the banner with that count. Seen live: the red banner 'this group is full' ('up to 5 units') with the capacity at 6 and only the count byte at 5.
- V: the carousel steps (sub_1401F22D0, sub_1401F3128, sub_1401F5CEC) take the smaller of the capacity (+64) and the candidate count (+1828) and stop when Deployment_CountPlaced reaches it.
- V: Deployment_FindPlacedUnitArea (the area and order of a hovered placed unit) walks only the first 5 placed entries.
- V: placing a unit runs Battle_JoinUnitAndLoad (Deployment_LoadAreaPlacement for the cell, then Battle_AddJoinedUnit), so placed party units take the joiner records 16..20. Seen live in a random battle at Mandalia Plain: the five placed units took records 16, 17, 18, 19 and 20 in placing order.
- V (seen live): the 'Remaining' counter follows the area's count byte, not the free cells: area row 554 has 9 cells and count 5, and the counter started at 5 when only the capacity was raised and at 6 when the count byte was raised before the first placement. This corrects an earlier reading that it counted free cells.
- I: 'Remaining' = the area's count byte minus the units placed (seen in one-area battles only; the code that writes the text was not found).
- V (tested limit, random battle at Mandalia Plain, twice): with the three checks raised to 6, the area count byte and the capacity at 6, the sixth placed-index dword (+88) set to -1, and, after commence, the sixth unit's +401 set by hand to a unique value (124), a sixth unit was placed. Battle_AddJoinedUnit put it in the first free record of 0..15 (record 4 in one battle, 1 in the other), on the player team, and the commence check passed.
- V (tested limit): that unit had the player command menu on its turns, acted (an ability and an attack that KO'd an enemy), and after the victory its roster record got EXP and JP like the units in 16..20; a saved and reloaded roster was byte-identical; a mid-battle autosave resumed with all six party records byte-identical and the unit's turns continuing.
- V (tested limit): the numbering after commence (sub_1401F16F4) left that unit's +401 at 120, the same as record 17's (the test then set it to 124 by hand); the portrait column beside the 'Remaining' counter lists 5 units only.
- I: the carousel's 5 visible rows (sub_1401F36A0 compares the candidate count +1828 with 5) are a list window, not a capacity.
- V: Battle_BuildRosterTeam (the battle load's roster team, BattleLoad_StepFresh state 8) builds exactly 5 units from a list of 8-byte entries, into records 16..20 (or 0..4 in its second mode, which also clears 5..15), queues each one's look and returns a bit mask of the entries it could not place (1 << n); its count 5 is a fixed loop count.

## Open questions

? which code reads the sortie screen's max-units text column; ? what +88 holds after deployment starts; ? whether a duplicate +401 matters at all (the tested battles ran with a unique value set by hand), most likely in a battle whose script addresses party units.
