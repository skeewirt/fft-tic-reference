# WorldMap_ScreenInput

- **Address:** `0x1402D0EE0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMap_ScreenInput(int *record, int64_t base)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 0)
- **Callees:** TownMenu_BuildItems, Tavern_HasNewEntries, SettlementEvent_EvaluateConditions, WorldEncounter_Roll, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of the world map screen (table index 0): moves between locations, opens a town menu or starts an encounter.

## Behavior

- V: a confirm is handled differently by the result of sub_140157BBC() (a window-present test). With it nonzero the step first calls SettlementEvent_EvaluateConditions(current location, 8): a nonzero result moves the cursor to the location (sub_140247E8C); a zero result, or location 580, calls TownMenu_BuildItems.
- V: when TownMenu_BuildItems returns items the step opens the town menu window and calls Tavern_HasNewEntries; only when it returns none does it roll WorldEncounter_Roll for the party and start the encounter scene (sub_1402477C8 with 3).
- V: with the window test zero, a confirm builds the town menu directly (TownMenu_BuildItems) and the encounter roll is not reached.
- V: a button toggles mask 0x2 of the dword 0x140D49AA0, which slides the map camera between two framings over dword_140D49AA8 steps (cues 15 and 16).
- V: other interface cues are 1, 2, 0x65 and 0x66.

## State touched

- Calls: [TownMenu_BuildItems](TownMenu_BuildItems.md), [Tavern_HasNewEntries](Tavern_HasNewEntries.md), [SettlementEvent_EvaluateConditions](SettlementEvent_EvaluateConditions.md), [WorldEncounter_Roll](WorldEncounter_Roll.md), [Input_TestAction](Input_TestAction.md)

## Notes

Large function: states are the cursor path, the camera slide path and the open-menu path; the camera tween arithmetic was not decoded.

## Open questions

? the meaning of the other masks of dword 0x140D49AA0.
