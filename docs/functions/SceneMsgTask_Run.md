# SceneMsgTask_Run

- **Address:** `0x140231D7C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneMsgTask_Run(void)`
- **Callers:** the scene task scheduler (the entry is reached through the scene task table; there is no direct call site, and the dispatcher was not read)
- **Callees:** sub_1400FC85C, sub_1400EF9EC, sub_1400E5F78, sub_1400EEC18, sub_1401EC01C, sub_140243330, SceneTask_WaitFrame, SceneTask_Terminate and other scene and UI helpers (39 direct calls in all)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task that reads the current scene's message word and dispatches a message descriptor built from it.

## Behavior

- V: reads the current scene task record, selected by dword_140D40948 in the table at off_140783088 (entry index shifted left 8, a 256-byte stride).
- V: takes the 16-bit message word at record +28 (0x1C); group = word >> 11 selects qword_140D40990[group] (32 entries), index = word & 0x7FF.
- V: sub_1400FC85C(group object, &class, &kind) yields the descriptor's class and kind.
- V: passes the descriptor to sub_1400EF9EC and sub_1400E5F78, and posts the word to the text command at sub_140243330.
- V: some scene codes are handled before the message dispatch (codes 0x1F and 0x2B are compared), and one branch resolves index 0x1C5 through the battle message object.
- V: the traced descriptor {0, 2, 10, 0x5062} is group 10, index 98 of an event-script message (0x5062 = 10 << 11 | 98).
- V: whether the banner call traced during an ability cast came from this task is not established.
- V: the function returns no value and runs as a task, not as a callee.
- I: the message word is an event-script message reference, not an ability or item id; the traced descriptor with group 10 and index 98 is consistent with that.
- I: its role in battle is inferred; the scene task table and the message group table are read, but the task's place in the battle banner path was not proven.
- ?: which scene table entry selects this task and what the pre-dispatch scene codes mean.

## State touched

- Calls: [sub_1400FC85C](sub_1400FC85C.md), [sub_1400EEC18](sub_1400EEC18.md), [sub_1401EC01C](sub_1401EC01C.md), [sub_140243330](sub_140243330.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Notes

The name is ours (IDB: sub_140231D7C). It is a void(void) scene task, 0x6B8 bytes (about 1.7 KB). Read for the group and kind decode, as part of the item text research; the task scheduler that reaches it was not read.

## Open questions

Whether it produces any battle banner descriptor (the traced ability-cast banner call is not attributed to it); what sub_1400EF9EC and sub_1400E5F78 do with the descriptor; what the group objects at qword_140D40990 are; the task-table slot that runs it; the meaning of the 0x1C5 special case.
