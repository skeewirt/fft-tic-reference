# EventObject_MoveTask

- **Address:** `0x140240100`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventObject_MoveTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x6E; also called directly from EventSubScript_RunTask (a call site at 0x140235CB7).
- **Callees:** EventObject_MoveWorker, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x6E: tags itself as a move task and runs the movement worker for the object named in its operands.

## Behavior

- V: tags its task slot with the value 11 in qword_140D40B38[256 * dword_140D40948], which opcode 0x6F tests to wait for moves.
- V: calls EventObject_MoveWorker (EventObject_MoveWorker) with the operand pointer from its task block and the argument 1.
- V: then ends through SceneTask_Terminate. This body reads no operand bytes itself; the worker reads 12 bytes (see EventObject_MoveWorker).
- V: the worker does the frame loop, so the tag stays set for the whole move; this body does not wait by itself.

## State touched

- Calls: [EventObject_MoveWorker](EventObject_MoveWorker.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Called by: [EventSubScript_RunTask](EventSubScript_RunTask.md)
- Started by event opcodes: [0x6E](../opcodes/README.md)

## Notes

The opcode record for 0x6E (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What EventSubScript_RunTask does and whether it passes operands in the same 12-byte layout.
