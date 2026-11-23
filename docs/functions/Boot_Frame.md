# Boot_Frame

- **Address:** `0x1400B5A7C`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void __fastcall Boot_Frame(void)`
- **Callers:** ffto::Game::GameApplicationListener_vfunc_8 (0x140010B88, indirect call through AppMain vtable slot +64); the vtable data reference at 0x140700FE0
- **Callees:** sub_1401E7EF8, Input_TestAction, Boot_SetState, Boot_UpdateVideo, sub_1402569F8, sub_1402F3284, sub_1402F34E4, Boot_MovieFrame, Boot_Update, sub_1402F35D4, sub_1403D29D0, sub_1403D1A54, sub_1402BAB78, sub_1401E6D10, sub_1403D1B44, sub_1403CC7C0, sub_1403CC8E0, sub_1403CCA6C, sub_1401E8364

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

One frame of the boot sequence: the per-frame dispatcher for boot states 0..4. It is installed in the AppMain vtable, reached through the application listener's vfunc_8, runs the state handler and then the shared cursor/music tail.

## Behavior

- V: reads the boot state in `dword_140D3AD50` (0x140D3AD50) and dispatches it to state 0 `sub_1401E7EF8` (on a zero return it then calls `sub_1401E8364`), state 1's confirm test, state 2 `Boot_UpdateVideo`, state 3 `Boot_MovieFrame` and state 4 `Boot_Update`; any other value returns at once, without the frame tail.
- V: before the switch it computes the frame duration in seconds from the application timing object at `g_Application+1160` using the same counter x frequency / 300000 product as `App_RunFrame`, stores the float bits in `dword_140D3A894` and passes the value to `sub_1403D29D0`.
- V: when the UI/render object `qword_140C69680` exists and `dword_1407D4538` equals 3, it takes two integers at +2680 and +2684, offers them to `sub_1401E6D10` or `sub_1403D1B44` according to the bytes at +2708 and +2716, and with the byte at +2704 set records them in the display block `qword_140D3A8D8` at +136 and +176: the first slot directly when the block's count is 0, otherwise the first slot whose selector dword at +16 is 1.
- V: clears the low three bits of the byte at `qword_140D3AD60+768` before the switch.
- V: state 1 tests action 81 through `Input_TestAction` and, on a hit, calls `Boot_SetState(2)`; it then sets the first two floats of the UI state object to `dword_1407829EC` and `dword_1407829F0` (1920 and 1080 in this build), passes 1002 to `sub_1403CC7C0` and runs the fade helpers.
- V: state 2 calls `Boot_UpdateVideo`; on a zero return it calls `sub_1402569F8`, runs the `dword_140D3A8D0` countdown and, at zero, calls `sub_1402F34E4`, which releases the three video textures.
- V: state 3 runs `Boot_MovieFrame`; on a zero return it calls `sub_1402F3284` and, when `dword_140D3A8D0` is already 0 or less, `sub_1402F34E4` (state 3 does not decrement the countdown; only state 2 does).
- V: state 4 calls `Boot_Update`; a non-zero return first calls `Boot_SetState(2)`, then the state-ended tail.
- V: the return code of the state handler selects the tail: 1 runs `sub_1403D1A54` and returns; -1 returns with no tail; any other value runs `sub_1403D1A54` and then the pending music request `sub_1402BAB78`.
- I: `sub_1403D1A54` is per-window pointer housekeeping (rests on the display-block fields it walks and the slot states it resets).
- V: installed at slot +0x40 in the AppMain vtable `vftable_ffto::Game::AppMain_140700FA0`; `ffto::Game::GameApplicationListener_vfunc_8` calls that slot when the object it holds at +40 has its byte at +8 at least 5.
- I: states 5..7 are not boot-frame states; the dispatcher has no branch for them and no tail runs (rests on the switch structure and the immediate return).

## State touched

- Calls: [sub_1401E7EF8](sub_1401E7EF8.md), [Input_TestAction](Input_TestAction.md), [Boot_SetState](Boot_SetState.md), [Boot_UpdateVideo](Boot_UpdateVideo.md), [Boot_MovieFrame](Boot_MovieFrame.md), [Boot_Update](Boot_Update.md), [sub_1402BAB78](sub_1402BAB78.md)
- Reads: [g_Application](../globals/g_Application.md), [g_UIStateFade](../globals/g_UIStateFade.md)

## Referenced by

- Appears in flows: [BootStateMachine](../flows/BootStateMachine.md)

## Notes

Whole body read from the decompiled view and checked against the IDB xrefs; the vtable slot and the caller come from the AppMain and GameApplicationListener vtables. The first block's two integers and `dword_1407D4538` are not named in the database.

## Open questions

What the two integers at `qword_140C69680+2680` and `+2684` mean and what `dword_1407D4538` selects; what fills `dword_140D3A8D0`; and which front-end action leaves the state-2 sub-state at 0 so the thread factory runs.
