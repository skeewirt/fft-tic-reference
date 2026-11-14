# EventColor_Task

- **Address:** `0x14023FA14`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventColor_Task(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x1A
- **Callees:** `sub_1402F57D0`, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x1A: applies a screen colour change and waits out its duration.

## Behavior

- V: tags its task slot with the value 6 in `qword_140D40B38[256 * index]`; the interpreter and other tasks use this tag to find tasks by kind.
- V: takes a pointer to the instruction's operand bytes from the first field of its task block.
- V: calls `sub_1402F57D0(mode, durationIndex, c1, c2, c3)` with the operand bytes: the first byte is a mode, the second to fourth are three signed colour adjustments, and the fifth is a duration index.
- V: then waits a number of frames read from the 16-bit table `word_140672108` at the duration index (no wait when that entry is 0), and ends through SceneTask_Terminate.
- V: `sub_1402F57D0` is a colour-grading routine with modes 0 to 11; modes 6 and 7 compute a grey from the current colour and mode 10 clears a flag.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Started by event opcodes: [0x1A](../opcodes/README.md)

## Notes

The opcode record for 0x1A (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What each of the 12 colour modes does to the screen, and the order of the three colour channels.
