# Tavern_RumorsListInput

- **Address:** `0x14036F07C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void Tavern_RumorsListInput(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 6)
- **Callees:** sub_14019DF88, sub_14019DCD4, EventTask_Start, sub_14036F25C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of the tavern rumor list (table index 6): reads the list widget's result and opens the chosen rumor.

## Behavior

- V: while no close animation runs it reads the widget result (sub_14019DF88): 1 starts the close with record dword 0 = 0 (cancel), 2 starts a transition and sets a flag byte, 3 starts event task 12.
- V: when the close animation has finished it pops; a cancel re-opens the screen below, a choice stores the cursor in 0x140D49610 and 0x140D49614 and calls sub_14036F25C with the entry id from the shared list buffer g_ErrandBoardList (masked with 0x7FF; several list builders fill that buffer, it is not errand data), which pushes kind 8.
- I: it is the rumor list because kind 8 rebuilds the list through TavernRumours_BuildList.

## State touched

- Calls: [EventTask_Start](EventTask_Start.md)

## Open questions

None recorded.
