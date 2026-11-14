# EventChannel_BindStepTask

- **Address:** `0x1402421AC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventChannel_BindStepTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x6B.
- **Callees:** `sub_1402B20E4`, `SoundCue_Play`, `sub_1402B2098`, `sub_140346648`, EventChannel_StepTask

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x6B: releases a keyed object, binds or selects its channel, then runs the same frame loop as opcode 0x6A.

## Behavior

- V: tags its task slot with the value 53 in qword_140D40B38[256 * dword_140D40948].
- V: reads the operand bytes through the task block pointer: byte 0 is the key, byte 1 is a count (0 is replaced by 1), byte 3 selects the mode, and bytes 2 and 4 are left for the step task.
- V: calls sub_1402B20E4(handle), where the handle is the key plus 0x10000, to release the key's current binding first.
- V: when byte 3 is nonzero it calls SoundCue_Play(handle - 1), which binds the mapped key to a free channel from 13 to 19 and returns that channel, or -1 when no channel is free or the mapped value is above 0x2B1.
- V: when byte 3 is zero it calls sub_1402B2098(handle), which sets dword_141856AA8 to the handle and sets channel 12 to the value from sub_1402BA8E8.
- V: then it calls sub_140346648(handle, count), which refreshes the channel for the key; that routine uses only its first argument.
- V: the else branch (sub_1402B20E4 for a zero count) cannot run, because the count is set to 1 when byte 1 is zero.
- V: it then tail-calls EventChannel_StepTask (EventChannel_StepTask) with the same task block, so the same operand bytes drive the frame loop. This body does not wait itself.

## State touched

- Calls: [SoundCue_Play](SoundCue_Play.md), [EventChannel_StepTask](EventChannel_StepTask.md)

## Referenced by

- Started by event opcodes: [0x6B](../opcodes/README.md)

## Notes

The opcode record for 0x6B (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

How the channel bound by SoundCue_Play is used by the drawing code (not read here); whether the unreachable zero-count branch was meant to run.
