# EventMenu_WaitThenListTask

- **Address:** `0x1402E9A1C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void *EventMenu_WaitThenListTask(void)`
- **Callers:** the task entry of nodes 10 and 56 of the event menu node tables
- **Callees:** sub_1402737D8, EventTask_WaitFrame, EventMenu_NodeListTask

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Task of nodes 10 and 56 of the event menu node tables: waits until the battle is idle, then runs the generic node list task.

## Behavior

- V: sets the slot block's state qword to 66, waits frames while sub_1402737D8() is nonzero or word 0x14184B238 is set, clears dword 0x14184B2D0 and jumps to EventMenu_NodeListTask.
- V (table data, not in the body): node 56's row list is 0x14078DA90 = [29, 12, 11, 57, 44]: rows 0..4 open nodes 29, 12, 11, 57 and 44 (44 = the battle unit editor, BattleUnitEditor_EventTask); node 10's rows are all -1 (close one level).
- V: the scene menu node table has the same rows for node 56 with its own task (sub_1402339D4).
- ?: which code opens node 56.

## State touched

- Calls: [EventTask_WaitFrame](EventTask_WaitFrame.md), [EventMenu_NodeListTask](EventMenu_NodeListTask.md)

## Open questions

None recorded.
