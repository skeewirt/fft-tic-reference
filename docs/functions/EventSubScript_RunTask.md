# EventSubScript_RunTask

- **Address:** `0x1402358C8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventSubScript_RunTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x2A
- **Callees:** SceneVar_Write, SceneTask_WaitFrame, SceneTask_Terminate, SceneTask_Start, EventScript_InstructionLength, EventRef_ResolveSlot, `sub_1402355E0`, `sub_140240B8C`, `sub_140242A08`, `sub_1402356B0`, `sub_14023577C`, `sub_14023565C`, `sub_140241DF8`, `sub_140240F34`, `sub_140240D5C`, `sub_140240144`, `sub_140242140`, `sub_140240C9C`, `sub_1402F7C20`, SceneObject_FindBySlot, `sub_140269074`, `sub_140260AEC`, SceneUnit_SetFlag156, ScenePreview_ClaimForUnit, EventUnitMove_Task, EventObject_MoveTask

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x2A: runs the instructions after 0x2A up to 0x2B as a parallel script, dispatching each opcode to unit, scene-variable and wait helpers, and ends when the block ends or the skip test fires.

## Behavior

- V: tags its task slot with the value 8 in `qword_140D40B38[256 * index]`.
- V: walks the instructions from its operand pointer until opcode 0x2B, or until the skip test (the high dword of `qword_142FF9E08` non-zero and the high dword of `qword_142FF9E00` equal to 3) fires; the next instruction is found with EventScript_InstructionLength.
- V: opcode 0x21 sets `dword_140782CAC` to its operand word when there is no skip and the current value is not 166 or the operand is -1.
- V: opcode 0x43 writes scene variable 83 as 1 when its operand byte is 9, or as 0 when it is 10; other values do nothing.
- V: opcode 0x72 waits one frame, then sets `word_140D408E4` to 1.
- V: opcode 0x28 sets `qword_140D40940` to `sub_1402355E0` and calls it on its operand; in a task slot other than 0 it clears two entries of the task pointer table first.
- V: unit opcodes resolve their unit id through EventRef_ResolveSlot, and do nothing when it returns 2000. Opcode 0x79 stores its operand word at instruction byte 3 into `xmmword_142FEC620` at the unit's index. Opcode 0x29 calls `sub_14023577C`, which waits frames until the unit's byte at record offset 168 is zero. Opcode 0x68 calls `sub_14023565C`, which sets the unit byte at record offset 341 to 2 when the operand byte is 1, otherwise to 0. Opcode 0x97 calls `sub_140269074` on the unit record when it exists. Opcode 0x71 calls `sub_140260AEC`. Opcode 0x46 calls SceneUnit_SetFlag156 and, when `dword_1418112B8` is 2, also appends an entry to the table at `dword_1418112C0`. Opcode 0x44 calls ScenePreview_ClaimForUnit. Opcode 0x12 resolves the id only. Opcode 0x32 calls `sub_1402F7C20` with the unit index and the operand bytes at instruction offsets 3, 7, 4, 5 and 6.
- V: opcode 0xF1 waits the number of frames given by its two operand bytes as a 16-bit value, one SceneTask_WaitFrame per frame.
- V: opcode 0x7E calls `sub_140242A08`, which waits until `SceneVar_Read` of the operand variable is at least the operand value; it ends early when `word_141874530` or `word_142FEC554` is set, or when `dword_142E7FB3C` and the high dword of `qword_142FF9E08` are both set.
- V: opcode 0x5F calls `sub_140240B8C`, 0x2D calls `sub_140240F34`, 0x53 calls `sub_140240D5C` with flag 1, 0x8C calls `sub_140240C9C`, and 0x11 calls `sub_140241DF8`, each with the operand pointer.
- V: opcode 0x6F calls `sub_140240144`, which waits frames while a task with tag 11 for that unit is still running.
- V: opcode 0x64 calls `sub_140242140` with its signed byte operand; opcode 0x65 calls it with -1, which waits frames.
- V: opcode 0x3B (or 0x6E) searches the slots after this one, up to 16, for one whose qword 18 is zero, starts EventUnitMove_Task (for 0x3B) or EventObject_MoveTask (for 0x6E) in it with SceneTask_Start, and stores the operand pointer in `unk_140D40AA0` at that slot, tag 11 in `qword_140D40B38` at that slot, and the resolved unit id in `unk_140D40B40` at that slot. When no slot is free it calls SceneTask_Terminate and uses slot 0 (not traced further).
- V: the task ends through SceneTask_Terminate when the block or the skip test ends its loop.
- I: this is the same kind of interpreter as the main script loop, restricted to the opcodes listed here; the other opcodes in the block are skipped.

## State touched

- Calls: [SceneVar_Write](SceneVar_Write.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md), [SceneTask_Start](SceneTask_Start.md), [EventScript_InstructionLength](EventScript_InstructionLength.md), [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [SceneUnit_SetFlag156](SceneUnit_SetFlag156.md), [ScenePreview_ClaimForUnit](ScenePreview_ClaimForUnit.md), [EventUnitMove_Task](EventUnitMove_Task.md), [EventObject_MoveTask](EventObject_MoveTask.md)

## Referenced by

- Started by event opcodes: [0x2A](../opcodes/README.md)

## Notes

The opcode record for 0x2A (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

Names for EventRef_ResolveSlot (unit id lookup) and SceneObject_FindBySlot (unit record lookup), the meaning of `dword_140782CAC` and of the table at `dword_1418112C0`, what the free-slot fallback to SceneTask_Terminate ends, and the helpers `sub_140240B8C`, `sub_140240F34`, `sub_140240D5C`, `sub_140241DF8` and `sub_1402F7C20`, which were not traced.
