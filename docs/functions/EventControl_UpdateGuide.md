# EventControl_UpdateGuide

- **Address:** `0x1401DBD54`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventControl_UpdateGuide(EventControl *ctl, bool ffRunning)`
- **Callers:** EventControl_RunningTick
- **Callees:** GlobalWork_GetFastForwardMode, EventControl_ShowFastForwardLabel, sub_140135DC8, sub_1400F12C0, Time_GetTimestamp, sub_1400EB65C, sub_1400EB5F4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses the button guide shown under an event: 503 while fast-forward is held or running, 504 in auto-advance, otherwise 501 / 506 for five seconds after an input.

## Behavior

- V: guide 503 when the mode is 2 and the level is non-zero, or the hold timer +36 is above 0.
- V: otherwise, when ffRunning was passed (the level was non-zero at the start of the tick): hides the 'Fast-forwarding' label and, with auto on, shows the auto indicator and guide 504.
- V: otherwise guide = the dword +28 when set, 504 when auto is on, else 506 when byte +55 is set and 501 when not; it is shown while an input other than the listed actions (26, 91 when auto is allowed, 89 and 90 in mode 2, 21) arrived in the last 5 seconds.
- V: when the mode is not 2 the guides 501, 504 and 506 are opened with mask -3.

## State touched

- Calls: [GlobalWork_GetFastForwardMode](GlobalWork_GetFastForwardMode.md), [EventControl_ShowFastForwardLabel](EventControl_ShowFastForwardLabel.md), [Time_GetTimestamp](Time_GetTimestamp.md)
- Reads: [GlobalWork.ff_level](../structs/GlobalWork.md#ff_level), [EventControl.ff_hold_time](../structs/EventControl.md#ff_hold_time), [EventControl.auto_mode](../structs/EventControl.md#auto_mode)

## Referenced by

- Called by: [EventControl_RunningTick](EventControl_RunningTick.md)

## Open questions

? The texts of guides 501, 503, 504 and 506 (UIButtonGuide rows) were not read.
