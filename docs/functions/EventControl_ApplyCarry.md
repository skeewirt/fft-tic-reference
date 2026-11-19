# EventControl_ApplyCarry

- **Address:** `0x14021EEC4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventControl_ApplyCarry(void)`
- **Callers:** EventScript_Run
- **Callees:** sub_14021EE0C, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_140260ABC, BattleAnim_StartMotion, sub_140135DC8, EventControl_ShowFastForwardLabel, sub_140270BA4, sub_1401DB4E4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

When an event script starts, restores auto-advance and fast-forward from the previous event if the new event's EventId row allows it.

## Behavior

- V: reads the EventId (NXD 156) row of the current event number (dword_140782A94).
- V: row byte +34 set and EventControl +48 set: auto (+47) = 1, the auto indicator is shown, +48 = 0.
- V: row byte +35 set and EventControl +54 set: armed (+53) = 1, hold timer (+36) = 1.0, level (GlobalWork +88) = 1, the 'Fast-forwarding' label is shown, +54 = 0.
- V: row byte +41 (column no_pause) set: EventControl +57 = 1; that byte (pause_block_b) is the second blocker tested by EventControl_TryOpenPause, so the pause overlay (and with it skipping) cannot open in this event.
- V: when sub_140270BA4(event) is true: bytes +34, +35, +49, +50 and +51 are set to 1 (the last two block the hold and the auto toggle).
- V: before that, a loop over the 21 battle unit records runs unless row byte +42 (column reset_unit_motion) is 0: it runs when the byte is set or the row is missing. Every present unit whose five status bytes at +97..+101 hold none of the statuses Crystal, KO, Undead, Jumping, Stone, Chest and Critical (ids 1, 2, 3, 5, 8, 15, 23) gets BattleAnim_StartMotion(2).
- I: with byte +35 a fast-forward that was running at the end of one event continues in the next without a new press and without the one-second ramp, as long as the button stays held.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [BattleAnim_StartMotion](BattleAnim_StartMotion.md), [EventControl_ShowFastForwardLabel](EventControl_ShowFastForwardLabel.md)
- Reads: [EventControl.auto_carry](../structs/EventControl.md#auto_carry), [EventControl.ff_carry](../structs/EventControl.md#ff_carry)
- Writes: [EventControl.auto_mode](../structs/EventControl.md#auto_mode), [EventControl.ff_armed](../structs/EventControl.md#ff_armed), [EventControl.ff_hold_time](../structs/EventControl.md#ff_hold_time), [GlobalWork.ff_level](../structs/GlobalWork.md#ff_level)

## Referenced by

- Observed behaviours: [FastForwardState](../behaviors/FastForwardState.md)
- Reads tables: [NxdDataEventId](../tables/NxdDataEventId.md)

## Open questions

? Which motion BattleAnim_StartMotion(2) is (what the unit is made to do at the start of the event).
