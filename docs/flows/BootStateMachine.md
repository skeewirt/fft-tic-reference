# BootStateMachine

- **Kind:** flow
- **Area:** [Application and startup](../areas/app-startup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The boot dispatcher's states 0..4 and the 5..7 hand-over codes. State 0 loads the settings and the save data, state 1 is the confirm skip, state 2 runs the video/title frame and owns the task threads, state 3 plays a movie, and state 4 is the Enhanced/Classic launcher. A change runs the old state's exit actions before the new state's entry actions.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="0"></a>0 |  | V | `sub_1401E7EF8` loads the config and settings; it walks its own 0..7 sub-state through the loader slot (`sub_1403D2940`), the NXD registry check, the settings file and the save manager. I: the move to state 4 is made through `sub_1401E7C0C`, the recorded `Boot_SetState` caller for state 4 (no direct call from `sub_1401E7EF8` appears in the cross-references). |
| <a id="1"></a>1 | [Boot_Frame](../functions/Boot_Frame.md) | V | The dispatcher tests action 81 (confirm) and calls `Boot_SetState(2)`; the state also resets the UI state object's screen size and surface. No boot code calls `Boot_SetState(1)` in this build, so the state is never entered. |
| <a id="2"></a>2 | [Boot_UpdateVideo](../functions/Boot_UpdateVideo.md) | V | The video/title state: at sub-state 0 it starts the task threads, then runs the video body and either starts a movie (3), returns to the launcher (4) or takes the exit flag to the hand-over code 7. |
| <a id="3"></a>3 | [Boot_MovieFrame](../functions/Boot_MovieFrame.md) | V | Plays the requested movie; on the end conditions it calls `Boot_SetState` with the previous-state mirror, returning to the state that started the movie (state 2 in the video path). |
| <a id="4"></a>4 | [Boot_Update](../functions/Boot_Update.md) | V | The Enhanced/Classic launcher: startup screen, title cushion and launcher. Result 1 calls `Boot_SetState(2)`, result 2 starts the Classic program, 3 runs the load route and 4 opens the options. |
| <a id="5"></a>5 |  | ? | No handler in `Boot_Frame` and no writer in the executable; not decoded. |
| <a id="6"></a>6 |  | ? | No handler in `Boot_Frame` and no writer in the executable; not decoded. |
| <a id="7"></a>7 | [Boot_UpdateVideo](../functions/Boot_UpdateVideo.md) | V | Hand-over code written only by `Boot_UpdateVideo` when `dword_142E7FB00` is non-zero; `Boot_Frame` has no branch and returns before its frame tail. |

## Behavior

- V: order inside one change: the old state's exit switch runs first, then the three state writes, then the new state's entry switch.
- V: state 2 owns the task threads: `Boot_UpdateVideo` starts them with `Boot_StartThreads`; `Boot_SetState`'s entry 2 only refreshes the video state. I: the state-2 exit destroys the manager only when no movie is requested and `dword_142E7FB00` is 0 (the code compares the 64-bit value at `dword_142E7FB00` with 0xFFFFFFFF00000000).
- V: the initial state is 0: the boot init `sub_1400B532C` writes 0 and the variable starts zeroed in the data segment.
- V: state 4 is the only state that allocates a boot UI object; its exit frees the object and closes the add-ons.
- V: the two mirrors are written on every change: `dword_1407829E8` keeps the previous state and is read by `Boot_MovieFrame`; `dword_1407829E4` keeps the new state and has no reader.
- I: states 5 and 6 are unused numbers, and 7 is an exit code rather than a state the dispatcher can run (rests on the missing branches and call sites).

## Notes

State handler addresses: 0 `sub_1401E7EF8` (0x1401E7EF8), 1 the confirm test in `Boot_Frame`, 2 `Boot_UpdateVideo` (0x1402561D0), 3 `Boot_MovieFrame` (0x1402F2E40), 4 `Boot_Update` (0x1401DE164).

## Open questions

What states 5 and 6 were meant for; what sets `dword_142E7FB00`; and what leaves `dword_140D3A8D4` at 0 when state 2 is entered so the thread factory runs.
