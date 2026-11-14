# EventScript_SkipTick

- **Address:** `0x14023987C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `? EventScript_SkipTick(void)`
- **Callers:** The event script runner's per-frame tick
- **Callees:** SceneCallback_Dispatch, SceneVar_Read, SceneVar_Write, Input_TestAction, Input_ActionBit

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The event fast-forward tick: while the skip action is held it raises the skip state that makes the event text advance.

## Behavior

- V: it writes 1 into the high dword of g_ScreenFade (the skip state) at 0x140239D33; it is the only writer of that value in the image.
- V: the write is gated on the skip action (action 0x1F) being masked in, or the event UI node being in state 3, and on four further flags.
- V: it reads and writes scene variables and tests input actions through the shared helpers.
- V: it calls SceneCallback_Dispatch for its scene callbacks, so it is itself part of the event task chain.
- V: live testing showed Ctrl and Shift do not reach this write (C6's negative result).
- I: the fast-forward is a held action, not a key: the tick raises the state while the action stays down.
- V (2026-11-09): the trigger is `a2 == Input_ActionBit(0x1F)` only when g_ShopModeGate (0x1407D453C, the enhanced-edition flag) is 0; with the flag set the trigger is g_EventControl state (+8) == 3, which EventControl_PausedTick sets when the pause-overlay hold completes.
- V (2026-11-09): the gate is the same five-field test as EventSkip_IsAvailable: g_EventSkipEnabled (0x142E7FB3C) != 0, g_EventSkipVeto (0x142FF9E54) == 0, the armed dword 0x142FF9E50 != 0, the skip state (high dword of g_ScreenFade) == 0; then, when g_EventSkipOnce (0x142FF9EBC) is not 2, it writes skip state 1, fade mode 1, and turns g_EventSkipOnce 1 into 2.
- I: in the enhanced edition the skip action alone never raises the state, which is why held keys did not reach the write; only the pause overlay's hold does.

## State touched

- Calls: [SceneCallback_Dispatch](SceneCallback_Dispatch.md), [SceneVar_Read](SceneVar_Read.md), [SceneVar_Write](SceneVar_Write.md), [Input_TestAction](Input_TestAction.md)
- Reads: [g_SkipRequestSource](../globals/g_SkipRequestSource.md)
- Writes: [g_ScreenFade](../globals/g_ScreenFade.md)

## Referenced by

- Called by: [sub_140236468](sub_140236468.md)

## Notes

Name from C6, which identifies the function by this name. Evidence: C6 finding 1 (the only writer of 1), the body scan (19 calls). 2,103 bytes.

## Open questions

None recorded.
