# EventMapTitle_SweepTask

- **Address:** `0x14030299C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventMapTitle_SweepTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x91.
- **Callees:** EventMapTitle_DrawSweep, sub_1400FC598, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x91: runs three sweeps of a 0-to-255 value over frames (up, hold at 255, sweep again with the second layout), one draw and one frame per value, using the operand 3 step, and ends early when the input test is true.

## Behavior

- V: sets the low dword of xmmword_142FF9E14 to 0 on entry.
- V: the step is the dword at +16 of the running task block (operand 3 as stored by the 0x91 handler, sign-extended). A step of 0 is replaced by 1. A negative step is not guarded, so the counters never reach their end values and only the input test ends the task.
- V: each draw alternates between two 736-byte buffers at unk_1437A5400: the first draw uses offset 736, the next uses 0, and so on.
- V: each draw is a call to EventMapTitle_DrawSweep with the buffer, the value, 100 and a layout; then one SceneTask_WaitFrame; then the input test. When the input test is non-zero the task calls SceneTask_Terminate at once and the remaining phases do not run.
- V: the input test is a call to sub_1400FC598 with a mask, 2048, 31 and 0. The mask is the bitwise inverse of a 32-bit value whose low byte is byte +3 of qword_142E942E8, next byte is byte +2 of qword_142E942E8, next byte is byte +3 of qword_142E94348 and high byte is byte +2 of qword_142E94348.
- V: phase 1 (sweep up, layout 0): draws the values 0, step, 2 times step and so on, for every value below 255. That is ceil(255 / step) draws.
- V: phase 2 (hold, layout 0): draws the value 255 with a counter that starts at 0 and rises by the step after each draw; it stops once the counter reaches 110. That is ceil(110 / step) draws.
- V: phase 3 (sweep again, layout 1): draws the values 0, step, and so on, for every value below 255, with layout 1. That is ceil(255 / step) draws.
- V: after phase 3 the task calls SceneTask_Terminate. It does not tag its slot in qword_140D40B38. For a step of 1 the full run is 255 + 110 + 255 = 620 draws.
- I: the on-screen effect of each value is not traced beyond the draw routine.

## State touched

- Calls: [EventMapTitle_DrawSweep](EventMapTitle_DrawSweep.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Started by event opcodes: [0x91](../opcodes/README.md)

## Notes

The opcode record for 0x91 (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What the input test in sub_1400FC598 checks for the flags and the mask (its decompile reads a register the decompiler shows as unassigned in the non-zero a2 path, and it returns 0 early when a state byte equals 2); what the sweep value does on screen.
