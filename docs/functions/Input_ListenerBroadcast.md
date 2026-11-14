# Input_ListenerBroadcast

- **Address:** `0x1400E3AD8`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `void *Input_ListenerBroadcast(int64_t unused, uint32_t *state)`
- **Callers:** listener table (data), sub_1400E28D0
- **Callees:** sub_1400F17D4, GUICore_OnInputState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Delivers the frame's merged input state to the UI core: merges the input object's state into `state`, calls GUICore_OnInputState, then copies the 0x548-byte state back.

## Behavior

- V: body: `sub_1400F17D4(g_Input, state); GUICore_OnInputState(g_GUICore, state); memmove(state, g_Input + 8, 0x548)`.
- V: the only call to GUICore_OnInputState is at 0x1400E3AFE; the wheel notches arrive at state+8.
- V: one code reference from sub_1400E28D0 and two data references (listener table).

## State touched

- Calls: [GUICore_OnInputState](GUICore_OnInputState.md)
- Reads: [g_GUICore](../globals/g_GUICore.md)

## Open questions

None recorded.
