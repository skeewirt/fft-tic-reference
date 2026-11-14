# EventPanel_ShowWaitTask

- **Address:** `0x140221564`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventPanel_ShowWaitTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0xAB; EventScript_Run starts it only when `dword_1407D453C` is 1
- **Callees:** `sub_1401402BC`, `sub_14014D4CC`, `sub_140140078`, `sub_140140160`, a virtual call on the sub-object at owner+160+64 (not named), SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0xAB when the enhanced flag is set: shows the UI table row named by its operand on the panel and waits until the panel closes or the skip test passes.

## Behavior

- V: tags its task slot with 73 (0x49) in `qword_140D40B38[256 * index]`.
- V: reads the dword at +0 of its task block into `edi`, the operand value the opcode handler stores there, and uses it as a row id.
- V: the panel owner is `*(qword_143CD9DA8 + 16) + 144`. It calls `sub_1401402BC(owner, 0)`, which plays the GUI state keyed Top on the panel object at owner+160.
- V: when owner+160 is set it calls `sub_14014D4CC(owner+160, id)`, which reads row `id` of UI table 34 and sets the dword at +1904 to the number of non-zero dwords among that row's dwords 2, 3 and 4.
- V: calls `sub_140140078(owner, 0)`, then `sub_140140160(owner)`. If that returns 0 (the panel state's active byte at +416 is clear) the task ends at once.
- V: at the top of each pass, if the dword at +4 of `qword_142FF9E08` is non-zero and the dword at +4 of `qword_142FF9E00` is 3 (the skip test), the task ends at once without the closing call.
- V: otherwise it sets a local dword to -1 and, when owner+160 is set, calls the virtual function at vtable offset 56 of the sub-object at owner+160+64 with a pointer to that local, the dword read through `off_1407DCB48` and the word read through `off_1407DD348`. The output is only compared with -1 and is not kept.
- V: if the local no longer equals -1 the task calls `sub_140140078(owner, -1)` and ends.
- V: otherwise, if the skip test is true it calls `sub_140140078(owner, -1)` and ends; if not, it calls SceneTask_WaitFrame and loops while `sub_140140160(owner)` is non-zero, and ends when it is zero.
- V: ends through SceneTask_Terminate.

## State touched

- Calls: [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Started by event opcodes: [0xAB](../opcodes/README.md)

## Notes

The opcode record for 0xAB (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What the virtual function in vtable slot 56 does with its dword and word arguments, what `sub_140140078` does with 0 and -1 on the panel, and what the rows of UI table 34 contain.
