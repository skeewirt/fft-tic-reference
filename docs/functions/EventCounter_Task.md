# EventCounter_Task

- **Address:** `0x14023FA9C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventCounter_Task(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x41
- **Callees:** SceneTask_Terminate, SceneTask_WaitFrame

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x41: runs without returning on its own, adding to the shared 16-bit counter on a repeating frame cycle until the skip test ends it.

## Behavior

- V: tags its task slot with the value 13 in `qword_140D40B38[256 * index]`.
- V: reads four signed bytes from its operand pointer: byte 0 is the amount added to `word_140D408EC` at each addition, byte 1 is the number of frames between those additions, byte 2 is the amount added once per cycle, and byte 3 is the cycle length in frames.
- V: each frame it first checks the skip test (the high dword of `qword_142FF9E08` non-zero and the high dword of `qword_142FF9E00` equal to 3) and ends through SceneTask_Terminate when it fires, before that frame's update.
- V: then it waits one frame with SceneTask_WaitFrame, increments the frames since the last addition and the frames in this cycle.
- V: when the frames since the last addition equal byte 1, it adds byte 0 to `word_140D408EC` and resets the count; this count carries across cycles.
- V: when the frames in the cycle equal byte 3, it adds byte 2 to `word_140D408EC`, and a new cycle starts.
- V: the comparisons use the signed byte values, so a negative byte 1 never matches.

## State touched

- Calls: [SceneTask_Terminate](SceneTask_Terminate.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md)

## Referenced by

- Started by event opcodes: [0x41](../opcodes/README.md)

## Notes

The opcode record for 0x41 (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

Which tasks or the interpreter read `word_140D408EC`, and what a cycle length of 0 does (the cycle loop only ends when its count equals the length, so a zero length is not guarded).
