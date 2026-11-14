# g_EventSkipOnce

- **Kind:** global
- **Address:** `0x142FF9EBC`
- **Type:** `uint32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

0 = the script may be skipped, 1 = skippable once, 2 = no (more) skip: EventScript_Run sets 0 or 1 at its start (1 when EventId byte +36 is set, when the battle's NXD 96 row has byte +147, +148 or +149 set, or for events 524, 530 and 569); EventScript_SkipTick turns 1 into 2 when it starts a skip; EventScript_LoadCurrent writes 2 when it arms an event.

## Referenced by

- Read by: [EventSkip_IsAvailable](../functions/EventSkip_IsAvailable.md)

## Open questions

None recorded.
