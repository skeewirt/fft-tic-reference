# EventSequence_RecordTask

- **Address:** `0x140233558`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventSequence_RecordTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x76.
- **Callees:** `sub_1402334FC`, `sub_1402CB7D4`, SceneTask_WaitFrame, SceneTask_Terminate, SceneVar_Read, `sub_1402600BC`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x76: takes a turn in the shared sequencer, then records two values per frame into a history until the task is stopped.

## Behavior

- V: tags its task slot with the value 54 in qword_140D40B38[256 * dword_140D40948].
- V: calls sub_1402334FC(6, ...): it waits while dword_140D408B8 or dword_140D408BC is nonzero, sets dword_140D408B8 to 6, and waits until that value is cleared. It ends the task when word_140D408F8 equals 1.
- V: the body does not read the operand bytes.
- V: then tail-calls sub_1402CB7D4, which stores the current slot in dword_140809284, copies qword_140D409A0 into qword_140D40A38, calls SceneVar_Read(39), and calls sub_1402600BC twice to build two command records (the first with flag argument 6).
- V: sub_1402CB7D4 writes constant values into a block of globals at 0x1437707AA to 0x143770808 and copies element 5 of each row into element 0 for a 12 by 32 table at unk_143770880.
- V: it sets the slot's tag to 55 in qword_140D40B38 (the tag changes from 54 to 55 inside this task).
- V: each frame it waits (SceneTask_WaitFrame), copies word_140809164 and byte_140809166 into the current half of the history buffers dword_1437707AA and dword_1437707AE (the half is chosen by the frame counter's parity), and breaks out when the qword at task block field 19 of the current slot equals 54 or the skip condition holds (the high dword of `qword_142FF9E08` nonzero and the high dword of `qword_142FF9E00` equal to 3).
- V: the outer loop body runs once; after the inner loop it waits one more frame and ends through SceneTask_Terminate.
- I: the history looks like a per-frame log of two values, but its reader is not in this entry.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md), [SceneVar_Read](SceneVar_Read.md)

## Referenced by

- Started by event opcodes: [0x76](../opcodes/README.md)

## Notes

The opcode record for 0x76 (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

Who reads the history buffers and what word_140809164 and byte_140809166 hold; what field 19 of the task block is and who writes the value 54 there (the body writes 54 to the tag array, a different array); what sub_1402600BC's command records are used for.
