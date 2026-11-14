# g_EventSkipEnabled

- **Kind:** global
- **Address:** `0x142E7FB3C`
- **Type:** `uint32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Event skip master switch; its only writer, VideoState_InitDefaults, stores 1. Read by EventSkip_IsAvailable, EventScript_SkipTick, EventScript_LoadCurrent and the message tasks.

## Referenced by

- Read by: [EventMessage_Task](../functions/EventMessage_Task.md), [EventSkip_IsAvailable](../functions/EventSkip_IsAvailable.md)

## Open questions

None recorded.
