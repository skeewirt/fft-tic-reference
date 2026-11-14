# g_EventSkipFlags

- **Kind:** global
- **Address:** `0x142FF9E4C`
- **Type:** `uint32[2]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Low dword 'allowed': 1 only on the event-viewer paths (sub_1402D2578, sub_1402D28C8 write both dwords 1); when 1, EventScript_LoadCurrent arms every event. High dword 0x142FF9E50 'armed': set by EventScript_LoadCurrent when the event number changes (EventId byte +32, or the 8-event list at 0x1407142E0, or allowed == 1), cleared when the script ends; one of the inputs of EventSkip_IsAvailable.

## Referenced by

- Read by: [EventSkip_IsAvailable](../functions/EventSkip_IsAvailable.md)

## Open questions

None recorded.
