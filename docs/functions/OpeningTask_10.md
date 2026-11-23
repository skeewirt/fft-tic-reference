# OpeningTask_10

- **Address:** `0x14037F1F0`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void __fastcall sub_14037F1F0(void)`
- **Callers:** SceneLoop_Run (0x140331D2D), SceneLoop_RunAlt (0x14039DE79), both indirect through SceneTaskTable; pushed by sub_14037F188 (0x14037F1DC)
- **Callees:** sub_1401BC2A8, UIState_BeginTransition, UIState_EndTransition, UIAgent_DetachAddon, sub_14033E898

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task 10: the closing task of the alternate scene loop (`SceneLoop_RunAlt`); nothing ties it to the opening scene beyond sharing the opening's task table. It waits for the movie requested by task 9 to end, fades the +400 UI screen to UI state 15, waits for that screen's state 4/1, closes it and toggles bit 0 of the scene flag word (normally set, so this ends the loop).

## Behavior

- V: the first test is `g_MovieRequestId`; while a movie is requested (0 or greater) it returns and changes nothing. The instruction at 0x14037F1FF compares `g_MovieRequestId` (0x142E7FB04) with 0.
- V: it takes the UI agent at `*(qword_143CD9DA8 + 16) + 400`. When the agent's vtable slot +16 (the same busy test `Boot_Update` uses) returns 0, it calls `sub_1401BC2A8(agent, 0)`, zeroes the 16 bytes at +40 and the qword at +56, sets byte +94 to 1, and starts a fade to UI state 15: when `g_UIStateFade+24` is not 15 it clears the fade timer at +16 if the state is non-zero, writes 15 to +24 and calls `UIState_BeginTransition(g_UIStateFade+16, 15)`.
- V: `sub_1401BC2A8` allocates a 664-byte add-on, attaches it to the agent, loads UI row 30 and writes the selector in its second argument to the add-on's +628 and the agent's +92. The boot load route calls the same helper with selector 1 on the same +400 agent.
- V: once per frame it reads the fade timer at `g_UIStateFade+16`; when byte +94 is set and the timer has reached zero it calls `UIState_EndTransition(g_UIStateFade, 15)` and clears +94.
- V: when the agent reports +40 == 4 and +44 == 1 and either byte +95 is 0 or the fade timer was above zero, it ensures a fade to 15 and sets +95 to 1.
- V: on a later frame with +95 set and the timer at zero, it ends the fade, detaches the add-on at agent+64, passes `qword_14187A5D8`, `qword_1418825E0` and (when non-null) `qword_1418825F0` to `sub_14033E898`, clears `dword_141877484`, pops itself and toggles bit 0 of `dword_141876EE8`, which ends the alternate loop.
- V: the +40/+44 == 4/1 pair is exactly the pair `Boot_Update` stage 7 waits for on the same +400 agent before it detaches the add-on and opens the launcher in mode 2.
- V: the three release pointers are read only in this function; no write to any of them exists in the image, and their initial value is -1 (all bits set). `sub_14033E898` treats its argument as a block pointer and would read the header before the address, so passing -1 is not a null no-op.
- I: the +400 agent is the screen created through `sub_1401BC2A8` on this path, and its +40/+44 == 4/1 is its finished state (rests on the same wait in `Boot_Update` and here).
- I: the exit branch is either not reached in this build or the three pointers are filled by a path that does not reference them by address; the code shown here does not set them.
- ?: what the +400 screen is, whether the exit branch runs, and what the three pointers were meant to hold.

## State touched

- Calls: [UIState_EndTransition](UIState_EndTransition.md), [UIAgent_DetachAddon](UIAgent_DetachAddon.md)
- Reads: [g_MovieRequestId](../globals/g_MovieRequestId.md), [g_UIStateFade](../globals/g_UIStateFade.md)
- Writes: [g_UIStateFade](../globals/g_UIStateFade.md)

## Referenced by

- Appears in flows: [OpeningTransitionTasks](../flows/OpeningTransitionTasks.md)

## Notes

Whole body read (355 bytes). The +400 agent, its add-on and bytes +94/+95 are the fields the boot load route also uses. The three release pointers start at -1 and have no writer, so the release tail is flagged rather than claimed as a working teardown.

## Open questions

The identity of the +400 screen; whether the exit branch is reached; and what the three pointers were meant to hold.
