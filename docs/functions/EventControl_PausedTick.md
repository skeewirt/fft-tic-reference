# EventControl_PausedTick

- **Address:** `0x1401DB978`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint8_t EventControl_PausedTick(EventControl *ctl)`
- **Callers:** EventControl_Update
- **Callees:** sub_1400EB7EC, sub_1400F144C, sub_1400F1510, EventSkip_IsAvailable, Input_TestAction, sub_1401DBBB0, PauseManager_Tick, sub_1400F4BCC, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, EventSkip_IsViewerEvent, sub_1402B1FB4, sub_1402B2004, sub_1402BAAA8, sub_1401D7760, sub_1400F0E98, sub_14013BAD0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Paused frame of the event overlay: accepts the completed hold as a skip (state 3) or resumes on the pause / back action.

## Behavior

- V: when EventSkip_IsAvailable is true and Input_TestAction(action 0x5D) fires (the hold completed), it resets the overlay, sets +12 = old state, +8 = 3, ticks the PauseManager and calls sub_1400F4BCC(0xBA).
- V: then, for an event number >= 0 (dword_140782A94), reads EventId (NXD 156) row byte +33; when that byte is 0, or EventSkip_IsViewerEvent is true, or the row is missing, it calls sub_1402B1FB4(0) and sub_1402B2004.
- V: event numbers 213, 296, 309 and 489 call sub_1402BAAA8 with fixed ids (649/651, 650, 653/647, 662/640).
- V: otherwise, on action 0x5F or 0x1B (and the hold not in progress), sets +8 = 0 and ticks the PauseManager (resume).

## State touched

- Calls: [EventSkip_IsAvailable](EventSkip_IsAvailable.md), [Input_TestAction](Input_TestAction.md), [PauseManager_Tick](PauseManager_Tick.md), [sub_1400F4BCC](sub_1400F4BCC.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [EventSkip_IsViewerEvent](EventSkip_IsViewerEvent.md)
- Writes: [EventControl.state](../structs/EventControl.md#state)

## Referenced by

- Called by: [EventControl_Update](EventControl_Update.md)
- Reads tables: [NxdDataEventId](../tables/NxdDataEventId.md)

## Open questions

? What sub_1402B1FB4 / sub_1402B2004 and the fixed ids passed to sub_1402BAAA8 do.
