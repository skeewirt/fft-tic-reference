# EventChannel_StepTask

- **Address:** `0x14024223C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventChannel_StepTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x6A; also tail-called by EventChannel_BindStepTask (opcode 0x6B).
- **Callees:** SceneTask_WaitFrame, SceneTask_Terminate, `sub_1402BA9C8`, `sub_1401D7808`, `sub_1401D6F2C`, `sub_1402B20E4`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x6A: runs a per-frame refresh of a keyed object's channel for a set number of frames, then releases or keeps the key.

## Behavior

- V: tags its task slot with the value 53 in qword_140D40B38[256 * dword_140D40948].
- V: reads its operand bytes through the task block pointer at off_140783088 + (slot << 11): byte 0 is the key, byte 2 is the end flag, and byte 4 is the frame count.
- V: byte 1 feeds a local accumulator (byte 2 minus byte 1) that the decompiled code never reads, and byte 3 is not read.
- V: the key handle is the key plus 0x10000; the lookup value is the handle minus 1, passed through sub_1402BA9C8, which remaps values above 0xA7 through the 7-pair table at dword_140718C50 and returns the value unchanged when there is no match.
- V: for the frame count it loops: SceneTask_WaitFrame, then if dword_141856AA8 (the current key) equals the handle and channel 12 is live (sub_1401D7808), it calls sub_1401D6F2C on channel 12 with 0.0.
- V: in the same pass it searches the 7 bound keys in dword_14375F8C4 (channels 13 to 19, stopping at dword_14375F8E0) for the lookup value; when found and that channel is live, it calls sub_1401D6F2C on that channel with 0.0.
- V: the loop breaks early when the high dword of `qword_142FF9E08` is nonzero and the high dword of `qword_142FF9E00` equals 3, the skip condition the other event tasks test.
- V: after the loop, when byte 2 is nonzero it repeats the channel 12 and bound-channel refresh once and keeps the key bound.
- V: when byte 2 is zero it calls sub_1402B20E4(handle), which releases the key from its channel.
- V: ends through SceneTask_Terminate. It does not call SceneTask_Start and does not wait after the loop.
- V: sub_1401D6F2C (called for each refresh) stores 0.0 in a field of each live object on the channel, stores a register value in another field, sets a flag byte when the object's type word equals 656, and then calls sub_1401D6080.
- V: sub_1401D7808 walks up to five objects of a channel and returns 1 at the first one that is non-null, has a nonzero word at +16, and passes the test in sub_1400991DC or the byte at +36 checks; it returns 0 when none pass.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Called by: [EventChannel_BindStepTask](EventChannel_BindStepTask.md)
- Started by event opcodes: [0x6A](../opcodes/README.md)

## Notes

The opcode record for 0x6A (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What sub_1401D6080 changes on the object; what sub_1400991DC tests; what the field stored from an unnamed register in sub_1401D6F2C holds (the decompiler shows it uninitialised); what the remap table dword_140718C50 represents.
