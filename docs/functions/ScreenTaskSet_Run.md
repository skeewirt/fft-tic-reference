# ScreenTaskSet_Run

- **Address:** `0x1402E9FBC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void ScreenTaskSet_Run(void)`
- **Callers:** not recorded
- **Callees:** EventTask_Start, EventTask_WaitFrame, EventTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Keeps the window tasks of one legacy screen set running; never returns.

## Behavior

- V: reads the set number from the running task record, takes row (number x 64) of the screen task set table (0x140681650) and walks its four slots.
- V: a slot whose task is not running gets its handler started with EventTask_Start (handler all-ones = unused); a running slot whose tag differs from the expected tag is flagged, cleared and, once every flagged slot has ended, started again with the handler.
- V: loops until the task record's first word becomes 255, then ends its own task.
- I: the nine rows are the screens of the command menu family.

## State touched

- Calls: [EventTask_Start](EventTask_Start.md), [EventTask_WaitFrame](EventTask_WaitFrame.md), [EventTask_Terminate](EventTask_Terminate.md)

## Referenced by

- Reads tables: [ScreenTaskSets](../tables/ScreenTaskSets.md)

## Notes

Read in full.

## Open questions

?: which screens the nine sets belong to.
