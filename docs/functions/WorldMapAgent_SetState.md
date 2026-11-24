# WorldMapAgent_SetState

- **Address:** `0x140157864`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapAgent_SetState(int64_t agent, int state, char instant)`
- **Callers:** sub_1400EDCB4, sub_14014DC80, sub_140157580, WorldMapRoute_StartGrow, WorldMapBaseScreen_Open, sub_1402473EC, sub_1402D05A0, sub_1402D1F24
- **Callees:** sub_1401D1E30, sub_1401D1EAC, sub_140158BEC, sub_140158B70, UIGuide_Show, GUINode_PlayShowHide, sub_14015C020, sub_14015C04C, GlobalWork_GetFastForwardMode, sub_14015B970, UIGuide_Set

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the world map agent's state (+228): shows and hides its addons, notifies every addon of the change and sets the footer guide.

## Behavior

- V: nothing happens when the state is unchanged.
- V: state 1: shows the main map (+64) and frame menu (+72), hides the Locations list (+80) and the deep dungeon menu (+96); guide from the main map (sub_14015B970, none when -1).
- V: state 2: shows +64 and +72, hides +80; guide 3006. State 3: shows +64, +72 and +80 (the Locations list); guide 3002. State 4: shows +64, +72 and +96; guide 3005.
- V: states 0 and 9 hide all four; 5, 6 and 8 only change the frame menu (sub_140158BEC / sub_140158B70).
- V: each addon in the agent's vector gets vtable slot 25 called with (new state, old state); for the Locations list that is WorldMapBaseList_ClearRecords, which empties the records unless the new state is 3.
- I: with fast-forward mode 3 a dword is cleared; the decompiled target is not shown clearly (main map assumed).

## State touched

- Calls: [sub_1401D1E30](sub_1401D1E30.md), [sub_1401D1EAC](sub_1401D1EAC.md), [UIGuide_Show](UIGuide_Show.md), [GUINode_PlayShowHide](GUINode_PlayShowHide.md), [GlobalWork_GetFastForwardMode](GlobalWork_GetFastForwardMode.md), [UIGuide_Set](UIGuide_Set.md)

## Referenced by

- Resolves registries: [WorldMapAgentStates](../registries/WorldMapAgentStates.md)

## Notes

sub_1401D1E30 shows an addon and sub_1401D1EAC hides it (I: from their use in pairs here).

## Open questions

? what states 5, 6 and 8 are.
