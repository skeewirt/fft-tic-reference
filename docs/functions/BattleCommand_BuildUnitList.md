# BattleCommand_BuildUnitList

- **Address:** `0x1402EB174`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleCommand_BuildUnitList(void)`
- **Callers:** sub_1402EB408
- **Callees:** sub_14030E010, EventText_FindMessage, Unit_GetActionGateState, sub_1400E4BDC, EventVar_Read, sub_1404200F8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the command list for the active unit: it asks the list builder for the commands, resolves their text and writes the cell words the menu reads.

## Behavior

- V: it calls sub_14030E010 to build the unit command list and stores the count at 0x14184B2C0.
- V: the list cells are written into 0x14377D454, the same cell block the menu task reads.
- V: EventText_FindMessage resolves the command names, and EventVar_Read supplies the story-dependent flags.
- V: the routine clears the selected flag byte and refreshes the list through sub_1400E4BDC.
- V: the single caller is the battle command task starter.
- V: sub_1404200F8 is the stack probe, not a game helper.
- I: the list is the command (not item) list, because it goes through sub_14030E010 and not through the item or throw list builders.
- ?: what the count at 0x14184B2C0 bounds; the list builder owns that value.

## State touched

- Calls: [sub_14030E010](sub_14030E010.md), [EventText_FindMessage](EventText_FindMessage.md), [Unit_GetActionGateState](Unit_GetActionGateState.md), [EventVar_Read](EventVar_Read.md)

## Notes

Whole function read (659 bytes). The cell block is the one the menu task reads.

## Open questions

None recorded.
