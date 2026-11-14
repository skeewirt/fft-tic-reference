# EventControl_ShowFastForwardLabel

- **Address:** `0x1401DBD14`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventControl_ShowFastForwardLabel(EventControl *ctl, uint8 show, uint8 loop)`
- **Callers:** EventControl_RunningTick, EventControl_UpdateGuide, EventControl_Update, EventControl_ApplyCarry, sub_1401DBBB0, sub_1402C53F0
- **Callees:** sub_140137FD0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows or hides the fast-forward indicator of the dialogue window and remembers it in EventControl +44.

## Behavior

- V: when the event window addon exists it calls sub_140137FD0(addon, show - 1, loop), which shows or hides the node kept at addon +56 and plays or stops its 'ShowLoop' state.
- V: stores show in the byte at ctl +44.
- I: addon +56 is the node UIAddonFFTOEvent binds as 'TextBoardFF' (the binding site stores that name's node at +56); the label read live as 'Fast-forwarding'.

## State touched

- Writes: [EventControl.ff_label_shown](../structs/EventControl.md#ff_label_shown)

## Referenced by

- Called by: [EventControl_ApplyCarry](EventControl_ApplyCarry.md), [EventControl_RunningTick](EventControl_RunningTick.md), [EventControl_UpdateGuide](EventControl_UpdateGuide.md)

## Notes

So EventControl +44 is 'the label is on screen', which starts with the accepted press, one second before the level becomes 1.

## Open questions

None recorded.
