# EventTask_Terminate

- **Address:** `0x1402BA698`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventTask_Terminate(void)`
- **Callers:** About 80 callers, mostly event and script-VM handlers.
- **Callees:** EventPad_UpdateRepeat, EventThread_ReturnToEntry

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ends the current event task. It is also the VM's error trap: a divide by zero or an out-of-range variable id calls it.

## Behavior

- V: clears the qwords at +144 and +152 of the current task's block, marking it no longer runnable.
- V: advances the current-task index to the next block whose +144 qword is non-zero, up to 16, wrapping to 0.
- V: calls EventPad_UpdateRepeat, restores the original index, then calls EventThread_ReturnToEntry, which does not return to the caller's code path.
- V: called from about 80 places, including EventVar_Alu (divide by zero) and EventVar_ResolveSlot (id 1024 or more).
- I: the effect is that the task that hit the error stops and its thread restarts from its saved entry point.

## State touched

- Calls: [EventPad_UpdateRepeat](EventPad_UpdateRepeat.md), [EventThread_ReturnToEntry](EventThread_ReturnToEntry.md)

## Referenced by

- Called by: [BattleCommand_BuildMenu](BattleCommand_BuildMenu.md), [BattleCommand_CommitCursor](BattleCommand_CommitCursor.md), [BattleMsg_SetCellText](BattleMsg_SetCellText.md), [EventMessage_Scripted](EventMessage_Scripted.md), [EventScene_QueueHelpText](EventScene_QueueHelpText.md), [EventVar_Alu](EventVar_Alu.md), [EventVar_ResolveSlot](EventVar_ResolveSlot.md), [LegacyMenu_PickLocation](LegacyMenu_PickLocation.md), [LegacyOptions_Open](LegacyOptions_Open.md), [ScreenTaskSet_Run](ScreenTaskSet_Run.md), [sub_1402DF374](sub_1402DF374.md), [sub_14032B1A4](sub_14032B1A4.md), [sub_14032EDB8](sub_14032EDB8.md), [sub_14032F410](sub_14032F410.md), [sub_14032F9F8](sub_14032F9F8.md), [sub_140364408](sub_140364408.md)

## Notes

Named for its observable effect; the task block fields are only partly decoded.

## Open questions

Whether a task can be restarted later, and what clears the task table entry for a new task.
