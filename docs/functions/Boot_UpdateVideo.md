# Boot_UpdateVideo

- **Address:** `0x1402561D0`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall Boot_UpdateVideo(void)`
- **Callers:** Boot_Frame (0x1400B5BEF)
- **Callees:** sub_1403D2940, Boot_StartThreads, sub_1401D4544, sub_1402572BC, sub_1403D1DC0, sub_1403D1988, sub_140256DB4, sub_1403D1798, sub_1403CCA6C, sub_1401E86E4, sub_1401E84BC, sub_140348344, sub_140348524, GameTasks_RunFrameSteps, sub_1402185A4, sub_1400C3B84, sub_1400C480C, sub_14025724C, Movie_Start, Boot_SetState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The per-frame handler of boot state 2. It updates the video and fade state, runs the game task step when the display sub-state is 2, and performs the state's transitions: back to the launcher, to a movie, to the game-thread hand-over, or abort the frame.

## Behavior

- V: with the display sub-state `dword_140D3A8D4` at 0, it checks the object `qword_143CDA848` and calls `sub_1403D2940`; a return of 0 calls `Boot_StartThreads`, a return of 1 makes the handler return -1, and any other value returns 0.
- V: `Boot_StartThreads` leaves the sub-state at 2, so the same call falls through into the video body.
- V: the body clears the second dword of the 16-byte block at 0x142E7FB40 (calling `sub_1401D4544` when it was non-zero) and the third dword, applies the display block `qword_140D3A8D8` +136/+176 through `sub_1403D1DC0` and `sub_1403D1988`, refreshes four entries with `sub_1403D1798`, clears the qword at +324, increments the frame counter at +6144 and calls `sub_140256DB4` when the sub-state is 2.
- V: when `dword_142E7FB00` is non-zero it fades out, calls `Boot_SetState(7)` and returns 1.
- V: for sub-state 2 only it writes `dword_142E7FC90` from the comparison of `dword_140782A94` with 29, calls `sub_1401E86E4` or `sub_1401E84BC` on the second dword of the block at 0x142FF9EC8, calls `sub_140348344` on the two blocks at 0x142E942D0 and 0x142E94330 with indices 0 and 1, and calls `sub_140348524`, `GameTasks_RunFrameSteps` and `sub_1402185A4`.
- V: depending on the block at 0x142FF9E38 it then flushes the slot through `sub_1400C3B84` (selector 1), calls `sub_14025724C(qword_143CDA848,1)` for 2 and 0x14, calls the same helper with 0 for 3, or goes to the common block.
- V: the common block ticks `sub_1400C480C` when `g_SaveManager` is non-null; if the byte at `g_UIStateFade+41` is set it fades out, calls `Boot_SetState(4)` and returns 1; if `g_MovieRequestId` is not -1 it calls `Movie_Start` on `g_GameUIManager+200`, calls `Boot_SetState(3)` and returns 1.
- V: otherwise it decrements `dword_142FF9DC8`, clears the low dword of `g_ScreenFadeMode` (0x142FF9E00) when the countdown reaches zero, and returns 0.
- V: when the fade/render state `dword_142FF9DCC` is greater than 1, the whole sub-state-2 block is skipped and the handler goes straight to the countdown.
- I: sub-state 0 is the start-the-threads step, 1 is a wait step and 2 is the running video/title frame (rests on the factory writing 2 and on the two branch structures).
- V: the only caller is `Boot_Frame`; the only caller of `Boot_StartThreads` is this function.

## State touched

- Calls: [Boot_StartThreads](Boot_StartThreads.md), [GameTasks_RunFrameSteps](GameTasks_RunFrameSteps.md), [sub_1402185A4](sub_1402185A4.md), [sub_1400C3B84](sub_1400C3B84.md), [sub_1400C480C](sub_1400C480C.md), [Movie_Start](Movie_Start.md), [Boot_SetState](Boot_SetState.md)
- Reads: [g_UIStateFade](../globals/g_UIStateFade.md), [g_MovieRequestId](../globals/g_MovieRequestId.md), [g_SaveManager](../globals/g_SaveManager.md), [g_GameUIManager](../globals/g_GameUIManager.md), [g_SaveRequestManager](../globals/g_SaveRequestManager.md)

## Referenced by

- Appears in flows: [BootStateMachine](../flows/BootStateMachine.md), [BootStateMachine](../flows/BootStateMachine.md), [BootToGameThread](../flows/BootToGameThread.md), [BootToGameThread](../flows/BootToGameThread.md)
- Called by: [Boot_Frame](Boot_Frame.md)

## Notes

Whole body read. An older description treated this function as a save/title update; it is state 2 of the boot dispatcher and the source of the task-thread creation.

## Open questions

The exact states of the loader slot that `sub_1403D2940` reports, the trigger that leaves `dword_140D3A8D4` at 0 when state 2 is entered, what sets `dword_142E7FB00`, and what the 0x14/2/3/1 selector at 0x142FF9E38 represents.
