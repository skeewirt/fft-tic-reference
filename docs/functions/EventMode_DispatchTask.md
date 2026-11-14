# EventMode_DispatchTask

- **Address:** `0x14023354C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventMode_DispatchTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x78.
- **Callees:** `sub_1402CB9E8`, SceneTask_FindFree, `sub_1402CB054`, `sub_1402C5290`, `sub_1402F7F4C`, `sub_1402C7DAC`, `sub_1402C53F0`, `sub_1402C6514`, `sub_1402C72B8`, `sub_1402C8818`, `sub_140326180`, `sub_1402CA3AC`, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x78: clears a global and hands the task's mode and argument to the mode dispatcher, which starts one of several helper tasks.

## Behavior

- V: clears the global dword_140D40844 to 0.
- V: tail-calls sub_1402CB9E8 and returns its result. This body does not read the task block itself.
- V: sub_1402CB9E8 reads the first dword of the task block as the mode and the second dword as the argument.
- V: mode 0: starts sub_1402CB054 in a slot from SceneTask_FindFree(16), clears that slot's first qwords, calls sub_1402C5290 with the argument, sets the slot's third qword to 2, calls sub_1402F7F4C to wait for the slot to finish, sets xmmword_142FF9EC8 to 1, and terminates.
- V: mode 1: starts sub_1402C7DAC in a new slot, clears its first qwords, sets the third qword to 0, waits with sub_1402F7F4C, and terminates.
- V: mode 2: starts sub_1402C53F0 in a new slot, clears its first qwords, waits with sub_1402F7F4C, sets dword_1411A7D08 from 1 to 2 when it is 1, and terminates. With bit 8 of dword_1437ADF48 set, mode 2 first reads SceneVar 508 and checks dword_1437EDF50; for values 570 to 577 and 543 to 547 it calls sub_140326180 (with 30 or 42) before the same start.
- V: mode 3 and mode 4 terminate at once with no other work.
- V: mode 5 starts sub_1402C6514 and mode 6 starts sub_1402C72B8, both in the same way as mode 1.
- V: mode 7 calls sub_1402C8818 when qword_142FF9E4C is not 1, then terminates.
- V: argument values of 8 or more first call sub_1402CA3AC with the argument and the tag array; dispatch then continues as above.
- V: every path ends through SceneTask_Terminate; no mode waits on its own before ending except through sub_1402F7F4C.

## State touched

- Calls: [SceneTask_FindFree](SceneTask_FindFree.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Started by event opcodes: [0x78](../opcodes/README.md)

## Notes

The opcode record for 0x78 (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What the started bodies (sub_1402CB054, sub_1402C7DAC, sub_1402C53F0, sub_1402C6514, sub_1402C72B8) do; what dword_140D40844 is used for; what bit 8 of dword_1437ADF48 and the values in dword_1437EDF50 represent; what sub_1402CA3AC does.
