# EventSlots_ResetAll

- **Address:** `0x1402B2004`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventSlots_ResetAll(void)`
- **Callers:** EventControl_PausedTick
- **Callees:** sub_1402B1ED0, sub_1402B1E74, sub_1401D9784

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resets the event's parameter slots and empties the event sound entry list.

## Behavior

- V: calls sub_1402B1ED0 (resets xmmword_140D3A900 from xmmword_140723AE0 and clears qword_1418623A8, dword_1418623A0 and qword_1418623B0).
- V: calls sub_1402B1E74(1) and sub_1402B1E74(2): clear slot n (qword_1418623C0[n], qword_1418623F8[n], dword_142E7FB08[n]; dword_142E7FB24 = -1 when it was n - 1).
- V: calls sub_1401D9784 on the list at qword_143CD9DD8 + 1384, which calls EventSoundEntry_SetStateById for every entry of the list and empties it.
- I: EventControl_PausedTick runs it on a skip unless the EventId skip_no_reset byte is set (the test is in the caller).

## Referenced by

- Called by: [Game_MainLoop](Game_MainLoop.md), [Music_StartSceneTracks](Music_StartSceneTracks.md), [OpeningTask_7](OpeningTask_7.md), [SceneLoop_RunAlt](SceneLoop_RunAlt.md), [Scene_Init](Scene_Init.md)

## Open questions

None recorded.
