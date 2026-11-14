# EventColorPath_Task

- **Address:** `0x14023FB30`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventColorPath_Task(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x3E
- **Callees:** `sub_1402F4618`, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x3E: moves three values in a straight line from a start triple to an end triple, two frames per step, passing each step to `sub_1402F4618` with the operand's value byte, then ends.

## Behavior

- V: tags its task slot with the value 12 in `qword_140D40B38[256 * index]`.
- V: reads the value byte at instruction byte 1 (passed to the helper at every step), the start triple from bytes 2 to 4 (unsigned bytes), the end triple from bytes 5 to 7 (unsigned bytes), and the step bound as a 16-bit value from bytes 8 and 9.
- V: for j = 0, 2, 4, ... below the bound it waits two frames, then computes each component as start + j * (end - start) / bound (integer division) and calls `sub_1402F4618` with the value byte and the three components (low 16 bits of each).
- V: when the bound is zero or negative the loop does not run.
- V: after the loop it calls `sub_1402F4618` with the end triple, waits two frames, and ends through SceneTask_Terminate.
- V: `sub_1402F4618` stores the three bytes as a new target triple in `dword_140782984`, computes the change from the previous triple in `dword_140782980` (scaled by 128 or 256), and calls `sub_1402600BC` with a time of 32 times its first argument (the value byte).
- I: the three bytes are probably colour components and the value byte a duration, because the helper writes a three-byte triple and times the change; this is not confirmed by the code read here.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Started by event opcodes: [0x3E](../opcodes/README.md)

## Notes

The opcode record for 0x3E (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What `sub_1402600BC` does with its time argument, what the triples in `dword_140782980` and `dword_140782984` represent, and whether the value byte is always a duration.
