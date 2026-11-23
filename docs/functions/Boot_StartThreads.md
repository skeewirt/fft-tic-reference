# Boot_StartThreads

- **Address:** `0x140256EF0`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void *__fastcall Boot_StartThreads(void)`
- **Callers:** Boot_UpdateVideo (0x140256229)
- **Callees:** memset, sub_14001B798, sub_14006A67C, sub_1402B1CD0; sub_140037BD8 and sub_1402F3698 are stored as task callbacks, not called

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Creates the game's 17 task threads and installs the game-thread entry in the task scheduler. It is the thread factory called from boot state 2.

## Behavior

- V: sets the scheduler dwords at 0x143791D44 and 0x143791D68 to 0, sets `dword_1408115C4` and `dword_1408115F4` to -1, and zeroes the 0x1320-byte block at 0x143791D70.
- V: loops 17 times; each iteration uses the 96-byte TaskThread at `qword_143CD9E98+8+96*i`, sets its id at +88, its scheduler block pointer at +80 (8-byte stride through `unk_143793090`), puts `sub_140037BD8` at +48 and `sub_1402F3698` at +56, and zeroes the 16 bytes at +64.
- V: for each index it formats `task%02d` into a 256-byte local buffer; the buffer is not passed to the thread helper.
- V: calls `sub_14006A67C` with the task record, a 0 argument and a 0x60000-byte stack.
- I: that helper creates the thread, stores the handle at +8 and the thread id at +16, disables priority boost and resumes it (its body is not read here; the call and the 0x60000 stack are the visible part).
- V: after the loop, calls `sub_1402B1CD0`.
- I: `sub_1402B1CD0` sets up the two scheduler slots at 0x143846730 and 0x143846738 (its body is not read here).
- V: installs `sub_140348658` in the task-0 command slot at 0x143791D78, sets `dword_143791E88 = 1`, `dword_143791E80 = 1`, `dword_143791E8C = 0`, `dword_140811624 = 0` and the qword at `off_140783088+144` to 1.
- V: sets `dword_140D3A8D4 = 2` and returns `off_140783088`.
- V: the only caller is `Boot_UpdateVideo` (0x140256229).
- I: the command slot is polled by `sub_1402F3698`: it copies the slot at +8 into +0 and calls the copy, so the installed entry runs on task 0 at its next turn (rests on the copy-and-call loop).
- I: the 17 threads correspond to the 17 scheduler blocks of 0x120 bytes that `GameTasks_RunFrameSteps` walks (same count and loader).

## Referenced by

- Appears in flows: [BootToGameThread](../flows/BootToGameThread.md), [BootToGameThread](../flows/BootToGameThread.md)
- Called by: [Boot_UpdateVideo](Boot_UpdateVideo.md)

## Notes

Whole body read. The thread objects are created earlier by the boot init `sub_1400B532C`; this function creates the threads and fills their run fields. The installed entry `Game_ThreadMain` is 44 bytes and never returns.

## Open questions

Why the `task%02d` name is formatted but not passed to the thread helper, and what the two function pointers at +48/+56 are called in the engine's own code.
