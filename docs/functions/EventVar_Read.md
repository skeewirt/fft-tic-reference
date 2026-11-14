# EventVar_Read

- **Address:** `0x1402E9898`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint32_t EventVar_Read(uint32_t index)`
- **Callers:** About 86 callers, e.g. the world-map event chooser `sub_1402D3120`, `sub_14033EC0C` and many battle and event routines.
- **Callees:** EventVar_Alu (twice), EventVar_Write (index 34 only)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads one event variable by index. The event system keeps story flags and counters in one packed variable space; this is the shared read accessor, called from about 86 places across the battle, world-map and event code.

## Behavior

- V: saves variable 0 (the first dword of the variable store `off_14078DCE8`), because variable 0 is used as the scratch cell for the read.
- V: for index 34 it first recomputes that variable from variables 35 and 36: `(var35 & 7) << 12` plus bit 0 of var36 shifted to bit 15, stored back with EventVar_Write.
- V: runs two ALU steps through EventVar_Alu: op 190 clears variable 0, then op 177 adds the variable `index` into variable 0, so variable 0 now holds the value.
- V: returns the value of variable 0, then restores variable 0 to its saved value, so the read leaves no trace.
- I: index 34 behaves as a derived status word (an unnamed packed field built from variables 35 and 36).

## State touched

- Calls: [EventVar_Alu](EventVar_Alu.md), [EventVar_Write](EventVar_Write.md)

## Referenced by

- Called by: [BattleCommand_BuildUnitList](BattleCommand_BuildUnitList.md), [Errand_ApplyResult](Errand_ApplyResult.md), [Errand_BuildBoardEntry](Errand_BuildBoardEntry.md), [Errand_IsAvailable](Errand_IsAvailable.md), [Errand_IsOffered](Errand_IsOffered.md), [Errand_Recall](Errand_Recall.md), [Errand_RollBonusLoot](Errand_RollBonusLoot.md), [Errand_Start](Errand_Start.md), [Errand_TreasureMilestone](Errand_TreasureMilestone.md), [EventCmd_AddOffsetIfVarMatches](EventCmd_AddOffsetIfVarMatches.md), [EventCmd_JumpIfVarEqual](EventCmd_JumpIfVarEqual.md), [EventCmd_JumpIfVarNotEqual](EventCmd_JumpIfVarNotEqual.md), [EventCmd_Run](EventCmd_Run.md), [EventMessage_Scripted](EventMessage_Scripted.md), [EventVar_Alu](EventVar_Alu.md), [Party_EggUpkeep](Party_EggUpkeep.md), [Shop_BuildItemList](Shop_BuildItemList.md), [Shop_Open](Shop_Open.md), [TownMenu_BuildItems](TownMenu_BuildItems.md), [UnitWork_BuildForSlot](UnitWork_BuildForSlot.md), [sub_14016E60C](sub_14016E60C.md), [sub_14028B510](sub_14028B510.md), [sub_1402CCEE0](sub_1402CCEE0.md), [sub_1402D2578](sub_1402D2578.md), [sub_140344B68](sub_140344B68.md), [sub_140345FE4](sub_140345FE4.md), [sub_14036E5DC](sub_14036E5DC.md), [sub_14039DA58](sub_14039DA58.md)

## Notes

Variable ids are 0-1023 and map to three storage classes, documented on EventVar_ResolveSlot: full dwords (0-127), single bits (128-863) and 4-bit nibbles (864-1023). The old research called the read accessor `read_eventflag`; this function matches that role, but not the old address.

## Open questions

What variable 34 and the 0x1FC lock variable mean to the game.
