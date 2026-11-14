# EventControl_TryOpenPause

- **Address:** `0x1401DBC24`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool EventControl_TryOpenPause(EventControl *ctl)`
- **Callers:** EventControl_Update
- **Callees:** Input_TestAction, sub_1400F144C, EventSkip_IsAvailable, sub_1401DBBB0, sub_1400EB65C, sub_1400EB5F4, sub_1401D1E30, PauseManager_Push

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the event pause overlay on the pause action and picks its button hints: with Skip when EventSkip_IsAvailable is true, without it otherwise.

## Behavior

- V: does nothing (returns 0) unless Input_TestAction(action 0x5F) is true and the bytes +49, +52 and +57 of the EventControl are all 0.
- V: sets +12 = old state, +8 = 2 (paused), arms the hold action 0x5D (sub_1400F144C).
- V: calls EventSkip_IsAvailable; button-guide mask -1 when it is true, -3 when false; passes 502 and the mask to sub_1400EB65C.
- V: sets +32 = 1, +24 = 502, clears qword_143CD9DD0 + 88 and pushes pause id 1 (PauseManager_Push).
- I: UIButtonGuide row 502 has entry 0 = Resume (text 2646, action 95) and entry 1 = Skip (text 2634, action 94); mask -3 clears bit 1, i.e. hides the Skip hint.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [EventSkip_IsAvailable](EventSkip_IsAvailable.md), [sub_1401D1E30](sub_1401D1E30.md), [PauseManager_Push](PauseManager_Push.md)
- Reads: [EventControl.pause_block_a](../structs/EventControl.md#pause_block_a), [EventControl.pause_block_load](../structs/EventControl.md#pause_block_load), [EventControl.pause_block_b](../structs/EventControl.md#pause_block_b)
- Writes: [EventControl.state](../structs/EventControl.md#state), [EventControl.guide_id](../structs/EventControl.md#guide_id), [EventControl.overlay_open](../structs/EventControl.md#overlay_open)

## Referenced by

- Called by: [EventControl_Update](EventControl_Update.md)
- Observed behaviours: [SceneSkipState](../behaviors/SceneSkipState.md)

## Notes

Opening the overlay changes no skip state: the decision is EventSkip_IsAvailable over globals, which are readable without opening it.

## Open questions

None recorded.
