# EventControl_Update

- **Address:** `0x1401DB3CC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventControl_Update(EventControl *ctl)`
- **Callers:** sub_14020DC78 and sub_14020E174 (both from sub_140210AF0), each when the event tick returned 1; otherwise they call EventControl_Reset
- **Callees:** EventControl_TryOpenPause, EventControl_PausedTick, sub_1401DB6C4, sub_1401DBBB0, sub_1401DBD14, sub_140135DC8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame state machine of the event pause overlay (state 0 off, 1 running, 2 paused, 3 skip chosen).

## Behavior

- V: runs only when the low dword of g_EventScriptActive (0x142FF9EC0) is non-zero, g_ShopModeGate (0x1407D453C, the enhanced-edition flag) is non-zero and the dword at +92 of the object at qword_143CD9DD0 is 0.
- V: state (+8) 0: resets the overlay, sets +12 = old state and +8 = 1.
- V: state 1: calls EventControl_TryOpenPause; when that returns 0 it calls sub_1401DB6C4 (the unpaused tick).
- V: state 2: calls EventControl_PausedTick.
- V: state 3 has no branch here; EventScript_SkipTick reads it (EventControl +8 == 3 while g_ShopModeGate is set) as the skip request.

## State touched

- Calls: [EventControl_TryOpenPause](EventControl_TryOpenPause.md), [EventControl_PausedTick](EventControl_PausedTick.md)
- Reads: [g_EventScriptActive](../globals/g_EventScriptActive.md), [g_ShopModeGate](../globals/g_ShopModeGate.md), [g_EventControl](../globals/g_EventControl.md), [EventControl.state](../structs/EventControl.md#state)
- Writes: [EventControl.state](../structs/EventControl.md#state), [EventControl.prev_state](../structs/EventControl.md#prev_state)

## Open questions

? What the dword at qword_143CD9DD0 + 92 is (its writers were not found by direct address).
