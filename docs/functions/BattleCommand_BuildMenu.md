# BattleCommand_BuildMenu

- **Address:** `0x1402EAD14`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleCommand_BuildMenu(void)`
- **Callers:** none found
- **Callees:** sub_14030DD1C, EventTask_Start, sub_1402BA718, EventTask_Terminate, sub_1402EB96C, sub_1402E9B64, sub_1402EA58C, sub_1402030E0, BattleCommand_BuildScreen, sub_140101CC8, sub_1402EA4C0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The battle command task: it reads the cell text of the command menu, starts the list and screen tasks, and runs the menu until the unit action is chosen.

## Behavior

- V: the task reads the 2-byte cell word through the menu list and subtracts 0x7000 from it, so the menu entries are text ids in the 0x7000 space.
- V: the word is stored to 0x14377D460 and 0x14377D462, the two cells the command labels use.
- V: sub_1402EA58C builds the item and throw lists for the second menu, and BattleCommand_BuildScreen builds the screen.
- V: it starts the helper tasks with EventTask_Start and waits for them through sub_1402BA718 and sub_1402EB96C.
- V: the task ends with EventTask_Terminate after the action is committed.
- V: it has no direct caller; the battle command dispatcher starts it as a task entry.
- I: this is the outer command menu task, because it owns the label cells and starts the screen rather than drawing rows itself.
- ?: which branch handles the cancel/back button; the task does not name it.

## State touched

- Calls: [EventTask_Start](EventTask_Start.md), [EventTask_Terminate](EventTask_Terminate.md), [sub_1402EA58C](sub_1402EA58C.md), [BattleCommand_BuildScreen](BattleCommand_BuildScreen.md)

## Notes

Whole function read (1117 bytes). The 0x7000 subtraction is a fact about the cell word.

## Open questions

None recorded.
