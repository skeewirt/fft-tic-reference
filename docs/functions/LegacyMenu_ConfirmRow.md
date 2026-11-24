# LegacyMenu_ConfirmRow

- **Address:** `0x1402E2704`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char LegacyMenu_ConfirmRow(int64_t record, int row)`
- **Callers:** LegacyWorldMenu_MainMenuTask, LegacyMenu_NumberEntryTask, EventMenu_NodeListTask, BattleCommand_BuildScreen, and other node tasks and windows (sub_1402B5AE8, sub_1402B7AE8, sub_1402E32E8, sub_1402E8384, sub_1402E8A38, sub_1402E8E54, sub_1402E981C, sub_1402EB96C, sub_140330ADC, sub_140361410, sub_140362468)
- **Callees:** Input_TestAction, sub_1402E2650, EventTask_Start

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Confirm step of an old menu node: on the confirm action it follows the node's row list and starts the next node's task, or closes levels.

## Behavior

- V: acts only when Input_TestAction(buttons, 32, 26) reports the confirm action and sub_1402E2650 allows it; it clears dword 0x142FF9F28 first.
- V: the next-node word: when the dword at record +40 is a small negative number (-15..-1) it is used for every row; otherwise +40 is a pointer to a list of 16-bit words and the word of `row` is used.
- V: bit 0x1000 is removed first when set (the subtraction of 4096 sticks); in the node table data, the row lists of nodes 3 and 6 at 0x140789378 hold eight words 0x100D, each of which starts node 13.
- V: a word that is negative (before or after that removal) closes -word levels: every task state 1 among the 17 slot blocks becomes 3, the slot blocks from the current one upward get their close qword set, and when the current slot is 8 the saved row words (record +80) of the open levels are copied to the word array 0x14078DA40; it sets dword 0x142FF9F28 = 1.
- V: otherwise a word of 256 or more starts nothing; 1234 makes the stored row -1.
- V: a remaining word below 256 is a node number: EventTask_Start(current slot - 1, active node table + 88 * word + 48) starts that node's task one slot below the current one, and the new slot block's first qword gets a register value (I: the node record).
- V: in every confirmed case it clears the input word at off_1408B9A48 and writes the row through the word pointer at record +72.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [EventTask_Start](EventTask_Start.md)

## Referenced by

- Called by: [EventMenu_NodeListTask](EventMenu_NodeListTask.md), [LegacyMenu_NumberEntryTask](LegacyMenu_NumberEntryTask.md), [LegacyWorldMenu_MainMenuTask](LegacyWorldMenu_MainMenuTask.md)
- Resolves registries: [LegacyWorldMainMenuRows](../registries/LegacyWorldMainMenuRows.md), [LegacyWorldMenuNodes](../registries/LegacyWorldMenuNodes.md)

## Notes

Event task slots count down: the root node runs in slot 8 (LegacyWorldMenu_OpenNode) and each confirm opens the child in the slot below. The scene-task menus use the same record layout.

## Open questions

None recorded.
