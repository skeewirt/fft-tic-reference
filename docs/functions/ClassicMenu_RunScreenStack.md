# ClassicMenu_RunScreenStack

- **Address:** `0x140246078`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int ClassicMenu_RunScreenStack(void)`
- **Callers:** the in-engine task runner (I)
- **Callees:** SceneVar_Read, EventVar_Read, EventVar_Write, EventThread_Yield, WorldMap_InitLocations, the table entries

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task that runs the classic menus, world map and towns: each frame it calls the input step of the screen on top of a stack of controllers.

## Behavior

- V: the stack is the dword at 0x140D8DBA0 (its depth), a kind per level in the array at 0x140D4C948 and one 23-dword (92-byte) controller record per level starting at 0x140D8D8C0.
- V: when the pause row, the dword at 0x140D8DC78 and the busy byte at 0x140D3002B allow it, each pass of the inner loop calls the entry of tbl_UiScreenInputSteps (0x140681400) indexed by the kind of level depth-1, with that level's record and the base of the record array. The array has no bound check on the kind.
- V: the inner loop runs while mask 0x1 of the state dword 0x141D32E14 is set; the outer loop around it runs while mask 0x10000 is set. The inner loop also runs the fade and the cursor windows; mask 0x2 of the state dword asks for a redraw.
- V: when the loops end it writes event variable 51 and returns a code from the exit masks of the state dword: 5 for 0x40000000 or 0x10000000, 4 for 0x2000000, 2 for 0x200000 or 0x40000, otherwise mask 0x8000 as 0 or 1.
- V: at the start it reads scene variable 39 and, when the scene check function accepts it, runs a scene change; otherwise a nonzero event variable 85 makes it load that scene and write it to event variable 39.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [EventVar_Read](EventVar_Read.md), [EventVar_Write](EventVar_Write.md), [EventThread_Yield](EventThread_Yield.md), [WorldMap_InitLocations](WorldMap_InitLocations.md)

## Referenced by

- Resolves registries: [ClassicMenuControllers](../registries/ClassicMenuControllers.md)

## Notes

Two more per-kind tables are called by the helpers that pop a screen: WorldMenu_RunTopOpenHook (table at 0x140681220) and WorldMenu_RunTopCloseHook (a second table); they re-open the screen that becomes the top.

## Open questions

? the meaning of most masks of the state dword 0x141D32E14 (0x4 = a close animation runs, 0x8 = a fade runs, I).
