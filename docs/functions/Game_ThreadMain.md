# Game_ThreadMain

- **Address:** `0x140348658`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void __noreturn Game_ThreadMain(void)`
- **Callers:** installed by sub_140256EF0 (0x140256FFE) as task slot 0; run by the task-thread loop sub_1402F3698
- **Callees:** sub_14039D414, sub_1403485E8, EffectFile_ResetBasePointers, Game_MainLoopReset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The entry installed for the game task thread: on first use it prepares the 4 MB work arena and the 512x272 display state, points every effect base slot at the shared effect buffer, then resets the game state and enters the outer loop.

## Behavior

- V: when `dword_143807798` is zero, calls `sub_14039D414`, which zeroes the 4 MB block at 0x143846740 and links its free list, then stores 0x400000 in `dword_143807798`.
- V: calls `sub_1403485E8`, which calls `sub_140260284`, sets the 512x272 surface fields `dword_1435401B4` and `dword_1435401B8`, calls `sub_140260428` with 1 and 2, and sets `word_1411A3744` to -1.
- V: calls `EffectFile_ResetBasePointers`, which points all 512 entries of the effect base array at the one shared effect buffer.
- V: calls `Game_MainLoopReset` (IDB `sub_1402D4A2C`, the pre-loop wrapper), its only direct call at the end; the wrapper calls `Game_MainLoop` and never returns, so this function never returns either.
- I: the zero test is a first-use guard: a second task thread would skip the 4 MB clear and reuse the arena (rests on the branch around `sub_14039D414`).
- ?: which allocator or subsystem owns the 4 MB arena, and what the 512x272 surface is used for before the first scene.

## State touched

- Calls: [EffectFile_ResetBasePointers](EffectFile_ResetBasePointers.md), [Game_MainLoopReset](Game_MainLoopReset.md)

## Referenced by

- Appears in flows: [ApplicationLifecycle](../flows/ApplicationLifecycle.md), [BootToGameThread](../flows/BootToGameThread.md)

## Notes

Whole function read (44 bytes), plus the two setup helpers it calls. This is a task entry, not a Win32 thread procedure: the thread factory stores it in the first slot of the task table and the slot loop calls it.

## Open questions

Whether anything can restart the game thread after the outer loop is entered (no such path was found).
