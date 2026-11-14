# SceneTask_FindTag

- **Address:** `0x140242588`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneTask_FindTag(int tag)`
- **Callers:** 10 routines (19 call sites): EventScript_Run (7), sub_1403015A4 (3), sub_140227558 (2), sub_140228778, sub_14022A19C, sub_140234468, EventScript_LoadCurrent, sub_1402F8684, sub_140338A28 and sub_1403980AC.
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds a running task in the second table by its tag. The event script uses it to wait while a task of a given kind is still running.

## Behavior

- V: checks slots 1 to 16 in order and returns the first slot that matches.
- V: skips slot `dword_140D40948` (the current task), any slot whose runnable qword at block +144 of `off_140783088` is zero, and any slot whose tag differs.
- V: the tag of slot n is the qword at `qword_140D40B38 + 2048 * n` (the same as `qword_140D40B38[256 * n]`). It is compared with the whole argument as a 64-bit value.
- V: returns the slot number 1 to 16, or 0 when no task matches.
- V: EventColor_Task writes tag 6 and EventCamera_MoveTask writes tag 7 into this tag table, which is the table read here.

## Referenced by

- Called by: [sub_1402F8684](sub_1402F8684.md), [sub_1403015A4](sub_1403015A4.md), [sub_140338A28](sub_140338A28.md), [sub_1403980AC](sub_1403980AC.md)
- Called by event opcodes: [0xDB](../opcodes/README.md), [0xE3](../opcodes/README.md)

## Notes

The tag table `qword_140D40B38` is separate from the task table `off_140783088`, but both use 2048-byte blocks indexed by slot. EventScript_Run's calls use tags 8, 13, 14, 55 and 61.

## Open questions

Which task kinds carry tags 8, 13, 14, 55 and 61.
