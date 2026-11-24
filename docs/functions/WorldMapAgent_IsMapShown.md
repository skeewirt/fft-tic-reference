# WorldMapAgent_IsMapShown

- **Address:** `0x140157BBC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char WorldMapAgent_IsMapShown(int64_t agent)`
- **Callers:** many world map and classic menu steps (WorldMap_ScreenInput, ClassicMenu_HubStep, WorldMap_OpenLocationsList, LegacyWorldMenu_MainMenuTask, LegacyMenu_PickLocation, ...)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when the world map agent's main map addon exists and is shown (or the agent is in state 9).

## Behavior

- V: returns 0 without a main map addon (+64); 1 when that addon's widget (+24) has byte +74 set, or when the agent state +228 is 9; else 0.

## Referenced by

- Called by: [LegacyWorldMenu_MainMenuTask](LegacyWorldMenu_MainMenuTask.md), [LegacyWorldMenu_StepRosterRequest](LegacyWorldMenu_StepRosterRequest.md), [WorldMap_OpenLocationsList](WorldMap_OpenLocationsList.md)

## Open questions

None recorded.
