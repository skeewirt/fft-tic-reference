# EventScript_TaskMain

- **Address:** `0x14023A830`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventScript_TaskMain(void)`
- **Callers:** Started as a task entry (SceneTask_Start)
- **Callees:** EventScript_LoadCurrent, EventScript_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The entry function of the event interpreter task: loads the current event, adjusts one global flag, and runs the interpreter.

## Behavior

- V: calls EventScript_LoadCurrent first.
- V: when the low dword of `xmmword_1437A62B0` is 0 it keeps the low dword of `qword_142E7FB1C` unless the high dword of `xmmword_142FF9E38` is 1, in which case it sets it to 1.
- V: returns EventScript_Run().
- V: it is started once as a task entry through SceneTask_Start.

## State touched

- Calls: [EventScript_LoadCurrent](EventScript_LoadCurrent.md), [EventScript_Run](EventScript_Run.md)

## Notes

This is where an event begins to run as a task.

## Open questions

What the two global flags select.
