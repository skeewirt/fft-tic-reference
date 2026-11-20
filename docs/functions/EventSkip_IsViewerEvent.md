# EventSkip_IsViewerEvent

- **Address:** `0x1402397F8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool EventSkip_IsViewerEvent(void)`
- **Callers:** EventSkip_IsAvailable, EventScript_SkipTick (0x140239CE8), EventControl_PausedTick (0x1401DBA84)
- **Callees:** SceneVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The second way an event becomes skippable: event variable 508 set (an event started from a viewer path), with the event number outside 410..425 and a blocking flag clear.

## Behavior

- V: returns true when SceneVar_Read(508) is non-zero, SceneVar_Read(39) - 410 is above 15 (unsigned), and dword_141849E10 is 0; otherwise false.
- V: the two writers of event variable 508 = 1 found here, EventViewer_EntryPage and sub_1402D28C8, also write event variable 39 (the event number), set both dwords of g_EventSkipFlags to 1 and set dword_141849E10 to (EventChain_Find(event) != -1).
- I: sub_1402D28C8 is reached from a menu handler (sub_140169404) that starts an event by number and keeps a return value in dword_142FF9F4C, which SceneTransition_CheckTables later writes back to variable 39: an event replay / viewer path. In normal story play variable 508 is expected to be 0, so this branch is false.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md)
- Reads: [g_EventViewerChained](../globals/g_EventViewerChained.md)

## Referenced by

- Called by: [EventControl_PausedTick](EventControl_PausedTick.md), [EventSkip_IsAvailable](EventSkip_IsAvailable.md)

## Notes

Event variable 508 is a flag bit: store + 556, bit 28 (I: the layout of the event-variable store).

## Open questions

? Whether any event opcode also writes variable 508 (only direct EventVar_Write callers were checked).
