# EventControl_IsAutoAdvancing

- **Address:** `0x1401DB498`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool EventControl_IsAutoAdvancing(EventControl *ctl)`
- **Callers:** EventMessage_Task, EventMessage_Scripted, sub_14022284C, sub_1402DA018
- **Callees:** GlobalWork_GetFastForwardMode

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when dialogue auto-advance should act this frame: the overlay is in its running state, auto is on and no fast-forward hold is in progress.

## Behavior

- V: false unless state (+8) is 1 and auto (+47) is non-zero.
- V: false when the mode is 2 and the level is non-zero, or when the hold timer +36 is not 0.
- V: otherwise returns the value its callers pass in the third argument register (1 at the call sites read).

## State touched

- Calls: [GlobalWork_GetFastForwardMode](GlobalWork_GetFastForwardMode.md)
- Reads: [EventControl.state](../structs/EventControl.md#state), [EventControl.auto_mode](../structs/EventControl.md#auto_mode), [EventControl.ff_hold_time](../structs/EventControl.md#ff_hold_time), [GlobalWork.ff_level](../structs/GlobalWork.md#ff_level)

## Notes

EventMessage_Task leaves its wait-for-input loop when the mode is not 0 and the level is non-zero, or when this returns true, or on the confirm / cancel actions.

## Open questions

? How long auto-advance leaves a finished page on screen (the callers' timing was not read).
