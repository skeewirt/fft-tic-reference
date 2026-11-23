# OpeningTask_9

- **Address:** `0x14037F188`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall sub_14037F188(void)`
- **Callers:** SceneLoop_Run (0x140331D2D), SceneLoop_RunAlt (0x14039DE79), both indirect through SceneTaskTable; pushed by SceneLoop_RunAlt (0x14039DE06)
- **Callees:** sub_140257384, sub_140257440

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task 9: the first task of the alternate scene loop (`SceneLoop_RunAlt`); nothing ties it to the opening scene beyond sharing the opening's task table. It clears the movie wait bit when no movie is pending, marks the scene flag word, pops itself, requests PSP movie-file row 0x10, records event id 16 and pushes task 10.

## Behavior

- V: it reads `dword_141876EE8`; when `g_MovieRequestId` is below zero it clears bit 1 (0x02) of the local copy and stores the word back. When a movie is still requested it leaves bit 1 set.
- V: it then sets bit 6 (0x40), decrements the task depth `dword_141877480` (a pop of task 9) and stores the updated flag word.
- V: it calls `sub_140257384(0x10)` and then `sub_140257440()`. That pair looks up row 0x10 of NXD table 66 (the PSP movie-file entries) and stores the row's movie id in `g_MovieRequestId`; the same pair is used with row 9 by `SceneLoop_RunAlt` and with rows 17 and 0 by `OpeningScene_Start`.
- V: it writes 16 (0x10) to `dword_143807794`, the event-chain id that `EventChain_Find` also fills and `EventScript_Run` compares with 2.
- V: it pushes task 10 by storing 10 at `dword_1418772E0[depth]` and incrementing the depth.
- V: the exact order is: movie-bit update and bit-6 set, depth pop, flag store, the row-0x10 request, the event id, then the push of 10.
- V: `SceneLoop_RunAlt` seeds the stack with id 9 at 0x14039DE06; no other function stores 9.
- I: row 0x10 of the PSP movie-file table is the transition movie this loop plays (rests on the lookup pair and on task 10 waiting for `g_MovieRequestId`; the row's file name is not established).
- ?: which movie row 0x10 is, why the event id is 16, and whether any caller other than SceneLoop_RunAlt can reach task 9.

## State touched

- Reads: [g_MovieRequestId](../globals/g_MovieRequestId.md)

## Referenced by

- Appears in flows: [OpeningTransitionTasks](../flows/OpeningTransitionTasks.md)

## Notes

Whole body read (104 bytes). The 0x10 used for the movie row and the 0x10 written to the event id are different globals. The decompiler keeps the bit-1 clear and the bit-6 set in the right order; the depth decrement happens before the UI-row request, and the push happens last.

## Open questions

Which movie row 0x10 is; why the event-chain id is 16; and what sector data the alternate loop loads before it starts.
