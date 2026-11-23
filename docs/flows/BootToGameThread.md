# BootToGameThread

- **Kind:** flow
- **Area:** [Application and startup](../areas/app-startup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The hand-over from boot to the game's task threads: boot state 2 creates 17 task threads, installs the game-thread entry in the task-0 command slot, then stops the boot dispatcher. The entry runs on a task thread and reaches the game's outer loop; the Win32 message pump stays on the main thread.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [Boot_UpdateVideo](../functions/Boot_UpdateVideo.md) | V | Boot state 2 with display sub-state 0: the handler polls `sub_1403D2940` and calls `Boot_StartThreads` only on a return of 0. |
| <a id="2"></a>2 | [Boot_StartThreads](../functions/Boot_StartThreads.md) | V | Creates 17 TaskThread objects in the manager block (96-byte stride, 0x60000 stacks) and starts them through `sub_14006A67C`. |
| <a id="3"></a>3 | [Boot_StartThreads](../functions/Boot_StartThreads.md) | V | Installs `sub_140348658` in the task-0 command slot at 0x143791D78, sets the scheduler flags and leaves the display sub-state at 2. |
| <a id="4"></a>4 | [Boot_UpdateVideo](../functions/Boot_UpdateVideo.md) | V | When `dword_142E7FB00` is non-zero the same handler fades out and calls `Boot_SetState(7)`; `Boot_Frame` then returns without its tail, so the boot dispatcher stops. `dword_142E7FB00` is non-zero on this path, so the state-2 exit does not destroy the task manager. |
| <a id="5"></a>5 |  | V | Each task thread runs `sub_140037BD8` then `sub_1402F3698`; that loop copies the slot at +8 into +0 and calls the copy, so task 0 executes the installed entry. |
| <a id="6"></a>6 | [Game_ThreadMain](../functions/Game_ThreadMain.md) | V | The installed entry `Game_ThreadMain` never returns: it initialises the render base, calls `sub_1403485E8`, resets the effect file base pointers and calls `Game_MainLoopReset`, which calls `Game_MainLoop`. |
| <a id="7"></a>7 | [App_ProcessMessages](../functions/App_ProcessMessages.md) | V | The Win32 message pump stays on the main thread: `Game_Main` alternates `App_RunFrame` and `App_ProcessMessages`, so the pump and the game loop run on different threads. |

## Behavior

- V: the 17 threads and the 17 scheduler blocks are the same count; `GameTasks_RunFrameSteps` walks ids 0..16 and signals each thread's start event.
- V: the manager's own event at +1640 is what the frame stepper waits on after releasing each task.
- I: state 2's exit action destroys the task manager only when no movie is requested (`g_MovieRequestId == -1`) and `dword_142E7FB00` is 0 (one 64-bit compare); the non-zero path keeps the manager and its 268-byte companion alive.
- I: the task-0 slot is a one-deep command slot (copy +8 to +0 and call), so the installed entry is picked up on task 0's next turn (rests on the loop in `sub_1402F3698`).
- I: `dword_142E7FB00` has no writer in this build (rests on a cross-reference search outside this page), so the 7 branch is an unused escape path.
- ?: which front-end action leaves `dword_140D3A8D4` at 0 when state 2 is entered; the launcher path enters state 2 with 2.

## Notes

The entry address is 0x140348658 (44 bytes). Step 6 links the `Game_ThreadMain` page.

## Open questions

The front-end route into the sub-state-0 path and the writer of `dword_142E7FB00`.
