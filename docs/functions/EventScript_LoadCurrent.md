# EventScript_LoadCurrent

- **Address:** `0x14023F37C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventScript_LoadCurrent(void)`
- **Callers:** EventScript_TaskMain, `sub_14023A868`
- **Callees:** SceneTask_WaitFrame, SceneVar_Read, EventScript_LoadIntoBuffer, `sub_140242588`, the NXD helpers

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the event the game is currently on, if it is not already loaded.

## Behavior

- V: waits frames until `sub_140242588` returns 0 for each of the scene task slots 4 to 14, so no earlier task is still using the buffer.
- V: reads event variable 39 with SceneVar_Read; this is the current event number.
- V: if it equals the last loaded event number `dword_140782A94` it returns 0 and does nothing else.
- V: otherwise it consults row 156 of the NXD table list (through the table helpers `sub_1403D325C`, `sub_1403D3AE8` and `sub_1403D2FD8`) and an eight-entry list to set a flag in `qword_142FF9E4C`, sets a byte in the record at `qword_143CD9FD0 + 52`, calls EventScript_LoadIntoBuffer with the event number, stores it in `dword_140782A94` and returns 1.
- I: variable 39 holds the story event number that decides which script plays.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneVar_Read](SceneVar_Read.md), [EventScript_LoadIntoBuffer](EventScript_LoadIntoBuffer.md)

## Referenced by

- Called by: [EventScript_TaskMain](EventScript_TaskMain.md)
- Called by event opcodes: [0xDB](../opcodes/README.md), [0xE3](../opcodes/README.md)

## Notes

Together with EventScript_LoadIntoBuffer and EventScript_LoadFile this is the whole path from the current event number to bytes in memory.

## Open questions

What NXD table row 156 supplies and what the eight-entry list selects.
