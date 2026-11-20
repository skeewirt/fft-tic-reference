# Deployment_PrepareCandidates

- **Address:** `0x1402FB4F8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char Deployment_PrepareCandidates(void)`
- **Callers:** sub_14020E578 (battle scene setup, from sub_140210AF0)
- **Callees:** Resource_GetSlotObject, UnitWork_BuildForSlot, sub_140285C30, SceneVar_Read, SceneVar_Write

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Battle setup step that builds the deployment candidate list from the roster and, for a battle without a scenario record, sets scene variable 57 to the first deployment area's party count.

## Behavior

- V: Resource_GetSlotObject(11), sets three script data pointers, UnitWork_BuildForSlot(0, ..., 100), then walks the 54 roster entries of the party order list: an entry that exists, whose save record byte +1 is at most 0x31, byte +286 is 0 and bit 2 of +4 is clear becomes a candidate (dword_1437A0510[n] = its save index, the count in dword_1437A0180, tbl_GridAvailableTemplate[n] = 1); its 16 bytes from save record +220 are copied to a list (0xFE ends it).
- V: when word_140D407CC is 0 (no scenario setup record was applied for this scene): with scene variable 510 = 0 it writes scene variable 57 = the signed count byte (+8) of the placement record of area scene variable 53; with variable 510 set it finds the placement row whose byte +9 equals the map id (variable 51), writes variables 52 = 2, 53 = that row, 54 = row + 1, 57 = that row's count, and rewrites the row's count byte to 4.
- V (seen live, random battle at Mandalia Plain): it wrote variable 57 = 5 before Battle_PlaceEntryUnits ran.

## State touched

- Calls: [Resource_GetSlotObject](Resource_GetSlotObject.md), [UnitWork_BuildForSlot](UnitWork_BuildForSlot.md), [SceneVar_Read](SceneVar_Read.md), [SceneVar_Write](SceneVar_Write.md)

## Notes

Behavior: EntryUnitsShareADistinctLookBudget.

## Open questions

None recorded.
