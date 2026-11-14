# EventPanel_QueueAndWait

- **Address:** `0x14033D4C0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventPanel_QueueAndWait(void)`
- **Callers:** EventPanel_PickRow (call at 0x14033D691). Data references at 0x143D3E47C and 0x143D3E488 were not traced.
- **Callees:** sub_1400ED6EC, `sub_1402B2004`, `sub_1402B1DF0`, `sub_1402B1E40`, `sub_1402B1F08`, SceneCallback_Dispatch, SceneTask_WaitFrame

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The kind-1 branch of EventPanel_PickRow: queues the value 50 in a two-entry queue, waits until the queue is released, then calls the callback sub_1402B1F08 with 1 and changes the global dword_1411A7D08 from 1 to 2.

## Behavior

- V: calls sub_1400ED6EC with an argument the caller never sets (the callee does not read it) and 0, 0. That routine tests a virtual method of the object at +144 of the object whose pointer is at +16 of qword_143CD9DA8; when the test is non-zero and the pointer at +72 of that object is not null, it clears the byte at +168 and calls sub_1400FB3B0 and sub_14014129C (not traced).
- V: sets the callback qword_140D40940 to sub_1402B2004 and calls it with 0. When the running task slot is not 0, the call first clears the qwords at +96 and +104 of block 0 of the task table and then calls through the callback pointer; otherwise it calls sub_1402B2004 directly.
- V: sub_1402B2004 calls sub_1402B1ED0, then sub_1402B1E74 with 1 and with 2, then sub_1401D9784 on qword_143CD9DD8 plus 1384, and returns 0. Only the first call's effect was read.
- V: sets the callback to sub_1402B1DF0 and calls it with 50, using the same slot rule.
- V: sub_1402B1DF0 looks for a free entry among the two qwords at qword_141862400 (free means zero). It stores 50 in the dword at qword_142E7FB0C plus 4 times the entry index, stores a pointer to unk_14185A2E0 in the entry, sets the low dword of qword_1418623C0 to the index plus 1 (the count) and returns that count. When both entries are used it returns 0 and changes nothing.
- V: loop: waits one frame with SceneTask_WaitFrame, sets the callback to sub_1402B1E40 and calls it with the same slot rule; repeats while it returns non-zero.
- V: sub_1402B1E40 returns 0 when the count (low dword of qword_1418623C0) is zero. Otherwise, when the high dword of qword_141856AB0 is zero, it sets the queue entry at count minus 1 to 0, sets the count to 0 and returns 0; otherwise it returns 1.
- V: sets the callback to sub_1402B1F08 and calls SceneCallback_Dispatch with mode 3 and argument 1.
- V: then, if dword_1411A7D08 is 1 it becomes 2; any other value is kept. The routine returns that value.
- I: the queue entries are consumed by sub_1402B1F08, which was only partly read (its first step is sub_1402B1ED0, which resets the step state from a fixed table at xmmword_140723AE0).

## State touched

- Calls: [SceneCallback_Dispatch](SceneCallback_Dispatch.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md)

## Referenced by

- Called by: [EventPanel_PickRow](EventPanel_PickRow.md)

## Notes

The queue globals are qword_141862400 (two entries), qword_1418623C0 (count) and qword_142E7FB0C (values).

## Open questions

What the value 50 means to the consumer sub_1402B1F08; what the high dword of qword_141856AB0 is; what sub_1402B1E74, sub_1401D9784 and sub_1400FB3B0 do; what the values 0, 1 and 2 of dword_1411A7D08 mean.
