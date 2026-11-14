# EventUnitMove_Task

- **Address:** `0x1402400C0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventUnitMove_Task(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x3B; also started by EventSubScript_RunTask (EventSubScript_RunTask) for opcode 0x3B inside its block
- **Callees:** EventObject_MoveWorker (the shared worker), EventRef_ResolveSlot, SceneObject_FindBySlot, `sub_140273908`, `sub_140272F04`, `sub_140273838`, `sub_140380310`, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x3B: moves a unit's three-value vector from its current value to three operand targets over the operand step count, then ends. It shares its worker with the 0x6E variant.

## Behavior

- V: tags its task slot with the value 11 in `qword_140D40B38[256 * index]`, then calls EventObject_MoveWorker with flag 0 on its operand pointer and ends through SceneTask_Terminate.
- V: the 0x6E variant (EventObject_MoveTask, a separate function) calls the same worker with flag 1.
- V: the worker resolves the unit id from operand bytes 0 and 1 with EventRef_ResolveSlot; when it does not resolve it does nothing. Otherwise it stores the unit index in `unk_140D40B40` for this slot.
- V: reads the unit's three-value vector from the unit record at offset 108 (three 16-bit values) as the start values.
- V: reads the three targets from operand bytes 2 to 7, the mode byte from byte 8, the weight byte from byte 9, and the step count as a 16-bit value from bytes 10 and 11.
- V: with flag 1 it replaces the step count: the square root of the summed squared differences (each difference times 16) divided by the operand step count.
- V: scales the start values and targets by 256 (8.8 fixed point).
- V: for each step from 1 to steps minus 1 it waits one frame, calls `sub_140273908` on the unit, and computes each component by the mode byte: mode 0 is linear (start + (target - start) * step / steps); modes 1 to 3 use the weight and other curve formulas; any other mode leaves that component unchanged.
- V: it applies each step's change to the unit with `sub_140272F04`, first the negated previous offset and then the new value, and then calls `sub_140273838`.
- V: it ends early when the unit record is gone (SceneObject_FindBySlot returns 0) during the steps.
- V: at the end it applies the final targets the same way, clears the byte at unit record offset 139, waits one frame if the step count was 1, and ends through SceneTask_Terminate.

## State touched

- Calls: [EventObject_MoveWorker](EventObject_MoveWorker.md), [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Called by: [EventSubScript_RunTask](EventSubScript_RunTask.md)
- Started by event opcodes: [0x3B](../opcodes/README.md)

## Notes

The opcode record for 0x3B (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What the unit vector at record offset 108 is in scene terms (position or rotation), what the weight means in curve modes 1 to 3, and what `sub_140273908` and `sub_140273838` do.
