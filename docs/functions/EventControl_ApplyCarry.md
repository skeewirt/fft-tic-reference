# EventControl_ApplyCarry

- **Address:** `0x14021EEC4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventControl_ApplyCarry(void)`
- **Callers:** EventScript_Run
- **Callees:** sub_14021EE0C, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_140260ABC, sub_140268E04, sub_140135DC8, EventControl_ShowFastForwardLabel, sub_140270BA4, sub_1401DB4E4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

When an event script starts, restores auto-advance and fast-forward from the previous event if the new event's EventId row allows it.

## Behavior

- V: reads the EventId (NXD 156) row of the current event number (dword_140782A94).
- V: row byte +34 set and EventControl +48 set: auto (+47) = 1, the auto indicator is shown, +48 = 0.
- V: row byte +35 set and EventControl +54 set: armed (+53) = 1, hold timer (+36) = 1.0, level (GlobalWork +88) = 1, the 'Fast-forwarding' label is shown, +54 = 0.
- V: row byte +41 set: EventControl +57 = 1 (auto-advance not allowed in this event).
- V: when sub_140270BA4(event) is true: bytes +34, +35, +49, +50 and +51 are set to 1 (the last two block the hold and the auto toggle).
- V: before that, when the row's byte +42 is clear or the row is missing, a loop over the 21 battle unit records calls sub_140268E04 for the units whose five status bytes at +97 have none of the bits of a fixed 5-byte mask.
- I: with byte +35 a fast-forward that was running at the end of one event continues in the next without a new press and without the one-second ramp, as long as the button stays held.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [EventControl_ShowFastForwardLabel](EventControl_ShowFastForwardLabel.md)
- Reads: [EventControl.auto_carry](../structs/EventControl.md#auto_carry), [EventControl.ff_carry](../structs/EventControl.md#ff_carry)
- Writes: [EventControl.auto_mode](../structs/EventControl.md#auto_mode), [EventControl.ff_armed](../structs/EventControl.md#ff_armed), [EventControl.ff_hold_time](../structs/EventControl.md#ff_hold_time), [GlobalWork.ff_level](../structs/GlobalWork.md#ff_level)

## Referenced by

- Observed behaviours: [FastForwardState](../behaviors/FastForwardState.md)

## Open questions

? What the status-mask loop is for.
