# DeploymentPlacedIndicesReaders

- **Kind:** observed behaviour
- **Scope:** engine (battle deployment)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [g_GenerateAttackTeamManager](../globals/g_GenerateAttackTeamManager.md), [Deployment_CountPlaced](../functions/Deployment_CountPlaced.md), [Deployment_CompactPlaced](../functions/Deployment_CompactPlaced.md), [Deployment_AreaOfPlacedUnit](../functions/Deployment_AreaOfPlacedUnit.md), [DeploymentGrid_CommenceCheck](../functions/DeploymentGrid_CommenceCheck.md), [Battle_RebuildUnitTable](../functions/Battle_RebuildUnitTable.md), [Deployment_FindPlacedUnitArea](../functions/Deployment_FindPlacedUnitArea.md), [Battle_AddJoinedUnit](../functions/Battle_AddJoinedUnit.md), [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Every place the deployment code reads or writes the five placed party indices of the deployment state (g_GenerateAttackTeamManager +0x44), what each loop over them assumes, and the readers that take the placed party as battle records 16..20.

## Behavior

- V: the instructions that name the five indices through the state (a one-byte displacement +0x44, or +0x54 for entry 4): Deployment_CountPlaced 0x1401EE6C0, Deployment_CompactPlaced 0x1401EE6EA (it copies exactly five through a 40-byte stack buffer addressed from the state), Deployment_AreaOfPlacedUnit 0x1401EE750, DeploymentGrid_CommenceCheck 0x1401EE95A (an add of 0x44 to the state pointer), sub_1401F0948 0x1401F098F, Battle_RebuildUnitTable 0x1401F0B20, sub_1401F0FD0 0x1401F1082, sub_1401F22D0 0x1401F260E and its store 0x1401F2626, sub_1401F3128 0x1401F32A9 / 0x1401F332C and its stores 0x1401F32C0 / 0x1401F337B, sub_1401F358C 0x1401F35AB, sub_1401F3858 0x1401F387C / 0x1401F3C3F, Deployment_FindPlacedUnitArea 0x1401F3E5A, sub_1401F3F70 0x1401F4519, sub_1401F4898 0x1401F48D4 / 0x1401F497B, sub_1401F49EC 0x1401F4ACA, sub_1401F5078 0x1401F50C1 / 0x1401F514E; the fills: the constructor sub_1401EE21C zeroes them (0x1401EE271), Deployment_ResetState (0x1401EE568) and sub_1401EE9B4 (0x1401EED61) set them to -1. Found by a scan of every operand +0x44 / +0x54 next to a capacity read (+0x40) in the deployment code and confirmed by a hardware watch of +0x40..+0x5F through a deployment (seen live).
- V: sub_1401F4898 and sub_1401F49EC walk back from entry 4 (a counter loaded with 4) to the last placed entry; sub_1401F358C walks back from entry capacity - 1; Deployment_FindPlacedUnitArea and sub_1401F3858 walk exactly five entries; the others walk up to the capacity.
- V: sub_1401F3858 fills the deployment screen's portrait column and its 'Remaining' text: the text is the area's count byte minus the area-0 units its walk of five entries counted; its widget setters SortieScreen_SetArea0Face and SortieScreen_SetArea1Face return without drawing for a position above 4 / 3.
- V: Deployment_AreaOfPlacedUnit looks for the unit's battle record among records 16..20 only: slot byte +1 not 0xFF and +2 equal to the placed roster index (seen live: enemy records hold 0xFF at +2, empty records 0, party records their roster index).
- V: the capacity (+0x40) is set at 0x1401EFCD4 in sub_1401EF0D8: the sum of the battle's areas' count bytes.
- V: Battle_AddJoinedUnit takes the first record of 16..20 whose slot byte is 0xFF; with none, while g_BattleState is 83, the first such record of 0..15; with none at all it returns -1 and builds nothing.
- V: after a successful commence check sub_1401F16F4 numbers the event unit id (+0x191) of records 16..20 from 120 (0x1401F1E12..0x1401F1E60); a record whose character byte (+0) is 1..3 keeps that byte. Records 0..15 are not numbered there.
- V: readers that take the placed party as records 16..20: sub_1402C53F0 (a result page's top unit), Party_CountUnitsAtLevel (at least 5 of them at a level). SaveHeader_FillBattleFields looks for Ramza in 16..20 and then in 0..15.
- V: Battle_PlaceEntryUnits' entry budget: 9 - scene variable 57 distinct looks (the constant 9 at 0x14027135B, clamped to 0 when the variable is above 9 at 0x140271370) and that + 7 units (0x140271389); a battle without a scenario record sets the variable to its first area's count byte (Deployment_PrepareCandidates).
- V (tested limit, Mandalia random battle): with the five indices widened, the checks of 5 raised and the area's count byte at 8, eight party units were placed, three of them in free records of 0..15; each had player turns, the two of them that hit an enemy gained EXP and JP from those hits, and their roster records held the gains after the victory. With 16 entry units the records 0..15 were all taken: five placed and the battle started.

## Open questions

None recorded.
