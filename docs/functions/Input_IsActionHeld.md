# Input_IsActionHeld

- **Address:** `0x1400F0D4C`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `bool Input_IsActionHeld(InputRows *rows, uint32 action)`
- **Callers:** 36 call sites, among them BattleControl_FrameUpdate, WorldMap_UpdateFastForward, EventControl_RunningTick, sub_1400F02BC, sub_1400EFB50
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True while any of the three bindings of an action row (one pad button, two keys) is held down.

## Behavior

- V: returns 1 when the byte +12 of the row's pad binding, or of either key binding (16 bytes apart), is non-zero; the row is rows + 1352 + 48 * action.
- V: rows is the input module + 8 (callers pass g_InputModule + 8), so the row is at the module + 1360 + 48 * action.

## State touched

- Reads: [InputActionRow.held](../structs/InputActionRow.md#held)

## Referenced by

- Called by: [BattleControl_FrameUpdate](BattleControl_FrameUpdate.md), [EventControl_RunningTick](EventControl_RunningTick.md), [FreeCursor_StepFromSticks](FreeCursor_StepFromSticks.md), [WorldMap_UpdateFastForward](WorldMap_UpdateFastForward.md)

## Notes

Its two siblings read other bytes of the same bindings: Input_IsActionMapped byte +10 (pressed this frame) and sub_1400F0D98 byte +14 (repeat).

## Open questions

None recorded.
