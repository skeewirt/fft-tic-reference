# EventCamera_MoveTask

- **Address:** `0x1402401A8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventCamera_MoveTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x1B
- **Callees:** SceneTask_WaitFrame, SceneTask_Terminate, `Math_BuildRotationMatrix`, `sub_14027483C`, `sub_140274AAC`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x1B: moves the camera from its current state to six target values over a number of frames.

## Behavior

- V: tags its task slot with the value 7 in `qword_140D40B38[256 * index]`.
- V: reads seven 16-bit values from the instruction's operand bytes (the pointer is in the first field of its task block): six targets and a step count.
- V: the first three targets are compared with the three 16-bit camera angles at `qword_140D408C0`, and the last three with the three-part camera position at `xmmword_140D408C8`; each difference is divided by the step count to give a per-frame increment.
- V: each frame it computes the interpolated angles and position, builds the camera matrices with `Math_BuildRotationMatrix`, `sub_14027483C` and `sub_140274AAC`, writes the results to the camera globals, then waits one frame with SceneTask_WaitFrame.
- V: it stops early when `dword_142E7FB3C` and the high dword of `qword_142FF9E08` are both non-zero, which the interpreter also uses as its skip condition.
- V: on exit it stores the final angles and position back into `qword_140D408C0` and `xmmword_140D408C8`, then ends through SceneTask_Terminate.
- I: the six targets are three rotation angles and a three-part position.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md), [Math_BuildRotationMatrix](Math_BuildRotationMatrix.md)

## Referenced by

- Started by event opcodes: [0x1B](../opcodes/README.md)

## Notes

The opcode record for 0x1B (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

Which camera axes the three angles and three position parts are, and the units of the step count.
