# EventControl_RunningTick

- **Address:** `0x1401DB6C4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventControl_RunningTick(EventControl *ctl)`
- **Callers:** EventControl_Update (state 1, when the pause overlay did not open)
- **Callees:** GlobalWork_GetFastForwardMode, Input_TestAction, Input_IsActionMapped, Input_IsActionHeld, EventControl_ShowFastForwardLabel, EventControl_UpdateGuide, sub_140135DC8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The unpaused frame of the event overlay: toggles dialogue auto-advance on action 91 and runs the fast-forward hold (actions 89 / 90) with its press gate and its one-second ramp.

## Behavior

- V: auto-advance part, skipped while the fast-forward level is non-zero in mode 2 or the hold timer (+36) is above 0: 'allowed' = byte +55 is 0 and byte +57 is 0 (or byte +56 when the dword +28 is non-zero), and byte +51 is 0.
- V: when allowed and action 91 was pressed this frame (Input_TestAction with action 0x5B), or when allowed, auto is off and g_EventKeepAutoLatch is 1, or when not allowed and auto is on: auto (+47) is inverted, the qword +16 is cleared and the auto indicator of the dialogue window is shown or hidden (sub_140135DC8).
- V: in the allowed case the latch g_EventKeepAutoLatch becomes 1 when auto is being switched on and the config byte +59 (enableEventKeepAuto) is set, else 0.
- V: fast-forward part, only when GlobalWork_GetFastForwardMode returns 2: pressed = action 89 or 90 pressed this frame (Input_IsActionMapped, the press-edge test), held = action 89 or 90 held (Input_IsActionHeld).
- V: while the float +40 is below 0.75 it only grows by the frame time; once it is 0.75 or more, a press sets the armed byte +53.
- V: while armed, held and byte +50 is 0: the float +36 grows by the frame time, the 'Fast-forwarding' label is shown if it was not (EventControl_ShowFastForwardLabel) and the auto indicator is hidden.
- V: otherwise (not armed, or released, or byte +50 set): the label is hidden if shown (and the auto indicator shown again when auto is on), +36 = 0 and armed = 0.
- V: level written to GlobalWork +88 every frame of this part: 0 while +36 is below 1.0; from 1.0 on, 2 when action 90 is held, else 1.
- V: ends in EventControl_UpdateGuide.
- I: the frame time is the application timer's tick count times its period divided by 300000, the same units the 5-second hint timers use, so 0.75 and 1.0 are seconds.
- I: a button already down when +40 reaches 0.75 never arms: only the press edge does. Releasing and pressing again arms at once, the label appears on that frame, and the speed-up and the automatic page advance begin 1.0 s later.

## State touched

- Calls: [GlobalWork_GetFastForwardMode](GlobalWork_GetFastForwardMode.md), [Input_TestAction](Input_TestAction.md), [Input_IsActionHeld](Input_IsActionHeld.md), [EventControl_ShowFastForwardLabel](EventControl_ShowFastForwardLabel.md), [EventControl_UpdateGuide](EventControl_UpdateGuide.md)
- Reads: [g_GlobalWork](../globals/g_GlobalWork.md), [g_InputModule](../globals/g_InputModule.md), [g_ConfigData](../globals/g_ConfigData.md), [InputActionRow.pressed](../structs/InputActionRow.md#pressed), [InputActionRow.held](../structs/InputActionRow.md#held), [EventControl.ff_block](../structs/EventControl.md#ff_block)
- Writes: [GlobalWork.ff_level](../structs/GlobalWork.md#ff_level), [EventControl.ff_hold_time](../structs/EventControl.md#ff_hold_time), [EventControl.run_time](../structs/EventControl.md#run_time), [EventControl.ff_armed](../structs/EventControl.md#ff_armed), [EventControl.auto_mode](../structs/EventControl.md#auto_mode), [g_EventKeepAutoLatch](../globals/g_EventKeepAutoLatch.md)

## Referenced by

- Observed behaviours: [FastForwardState](../behaviors/FastForwardState.md)

## Notes

The floats +36 and +40 are zeroed by EventControl_Reset, which runs on every frame without an event tick; so the 0.75 s count starts when an event script begins to tick. Input_IsActionMapped is an older name: the routine tests the 'pressed this frame' bytes of an action row.

## Open questions

? What sets the bytes +50, +51, +55, +56, +57 and the dword +28 apart from the message / panel tasks already listed on the EventControl record.
