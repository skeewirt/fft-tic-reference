# EventFlagWait_Task

- **Address:** `0x14023589C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventFlagWait_Task(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x8B.
- **Callees:** `sub_140235804`, `sub_1402737B8`, `sub_1402737D0`, `sub_14031A7E0`, `sub_14031A6AC`, `sub_140381A54`, `sub_14031A740`, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x8B: waits frame by frame until the global dword_140CDB824 becomes zero, then ends.

## Behavior

- V: tags its task slot with the value 65 in qword_140D40B38[256 * dword_140D40948].
- V: calls sub_140235804, which sets the function slot qword_140D40940 to sub_1402737B8 and calls it once; for a task that is not slot 0 it zeroes task block fields 12 and 13 and calls through the slot pointer with 0.
- V: sub_1402737B8 sets dword_1418732C8 to 2 when it is 1, and returns the value.
- V: then it loops: waits one frame, sets qword_140D40940 to sub_1402737D0 and calls it the same way; sub_1402737D0 returns dword_140CDB824.
- V: the loop ends when that value is 0. The task then returns the result, and the body ends through SceneTask_Terminate.
- V: on each pass the skip condition (the high dword of `qword_142FF9E08` nonzero and the high dword of `qword_142FF9E00` equal to 3) is checked; when it holds, the loop calls sub_14031A7E0 and returns its result instead.
- V: sub_14031A7E0 clears dword_143C51C6C, dword_143C51C98, dword_143C51CA4 and qword_143C51D30, calls sub_14031A6AC, sub_140381A54 and sub_14031A740, sets word_141D330BC and dword_142E801F4 to -1, and when dword_140C6B1CC is not 52 writes 1281 to a word at qword_143CDA758 + 288.
- I: the global dword_140CDB824 is the value this task waits on, and the opcode record says EventScript_Run sets a flag to 1 before starting it.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Started by event opcodes: [0x8B](../opcodes/README.md)

## Notes

The opcode record for 0x8B (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What dword_140CDB824 and dword_1418732C8 are and what writes dword_140CDB824; what sub_14031A6AC, sub_140381A54 and sub_14031A740 do (not read here); the caller sub_140241DF8, which also calls sub_140235804.
