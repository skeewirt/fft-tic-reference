# EventObject_MoveWorker

- **Address:** `0x14023FC54`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventObject_MoveWorker(unsigned char *operands, int mode)`
- **Callers:** Called by EventObject_MoveTask (0x140240100) with mode 1; also called from EventUnitMove_Task, whose mode argument is not read in this entry.
- **Callees:** EventRef_ResolveSlot, SceneObject_FindBySlot, `sub_140273908`, `sub_140272F04`, `sub_140273838`, `sub_140380310`, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Movement worker for opcode 0x6E: moves a unit record from its current position to three 16-bit targets over a number of frame steps, shaped by a curve mode.

## Behavior

- V: reads 12 operand bytes: bytes 0 and 1 form a 16-bit object id; bytes 2 to 7 are three 16-bit targets (first, second and third axis, little-endian); byte 8 is the curve mode; byte 9 is a curve weight; bytes 10 and 11 form a signed 16-bit divisor.
- V: resolves the id with EventRef_ResolveSlot(id, mode). When that returns 2000 the worker does nothing and returns 2000.
- V: otherwise it stores the resolved slot in the qword at 0x140D40B40 + 2048 * slot (the qword next to the tag) and finds the unit record with SceneObject_FindBySlot.
- V: reads the unit's three 16-bit position words at record offsets 108, 110 and 112 as the start point.
- V: when mode is 1 the step count is replaced: the squared axis differences, each multiplied by 16, are summed, the square root is taken, and the step count becomes that root divided by the divisor (signed integer division; the remainder is unused).
- I: the square root of 16 times the summed squared differences equals 4 times the straight-line distance in raw units, which matches the opcode record.
- V: start and target values are then shifted left by 8 bits (8.8 fixed point), and the step loop runs for step indices 1 to steps minus 1; when the step count is 1 or less the loop does not run.
- V: mode 0: each axis becomes start + (target - start) * t / steps, where t is the step index.
- V: mode 1: the mode 0 term plus (weight / 16) * (target - start) * t * (steps - t) / steps^2.
- V: mode 2: the steps are split at the midpoint (the second part is selected when 2 * t is at least the steps); the code is a two-part curve that uses the weight and a half-count divisor.
- V: mode 3: each axis becomes start + ((2 * weight * d * t / steps) + 2 * d * (16 - weight)) * t / (32 * steps), where d is target minus start.
- V: any other mode leaves the stored step value unchanged.
- V: each step waits one frame (SceneTask_WaitFrame), calls sub_140273908 on the unit, adds the negated previous offset to the unit's position words with sub_140272F04, adds the new offset (value shifted right by 8), keeps the negated new offset for the next step, and calls sub_140273838.
- V: sub_140273838 sets one flag byte in the unit record only when the global dword_140782A94 equals 386.
- V: after the loop it removes the previous offset, adds the target values (shifted right by 8), waits one frame when the step count was 1, and clears the byte at record offset 139.
- V: when the unit record is missing during the steps or at the end, it calls SceneTask_Terminate instead of finishing.
- V: this worker has no skip-condition check of its own.
- I: the three targets are the unit's position words, and the mode and weight shape the path between the start and the targets.

## State touched

- Calls: [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Called by: [EventObject_MoveTask](EventObject_MoveTask.md), [EventUnitMove_Task](EventUnitMove_Task.md)

## Notes

The opcode record for 0x6E (data/opcodes.jsonl) does not set starts_task; its operand list matches the 12 bytes read here.

## Open questions

The exact fixed-point form of mode 2; what EventRef_ResolveSlot does for its later branches (ids 100 to 105 and the special id ranges); what sub_140273908 writes; what sub_140262808 returns; the caller at EventUnitMove_Task and its mode value.
