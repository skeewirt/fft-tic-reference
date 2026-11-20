# EventSkip_IsAvailable

- **Address:** `0x140239834`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `bool EventSkip_IsAvailable(void)`
- **Callers:** EventControl_PausedTick (0x1401DB9B4), EventControl_TryOpenPause (0x1401DBC89)
- **Callees:** EventSkip_IsViewerEvent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Says whether the running event script may be skipped now. The event pause overlay asks it when it opens (to show or hide the Skip hint) and on every paused frame (to accept the hold).

## Behavior

- V: returns true at once when EventSkip_IsViewerEvent returns true (call at 0x140239838).
- V: otherwise returns true only when all of these hold: g_EventSkipEnabled (0x142E7FB3C) is non-zero (0x140239847); the low dword of g_EventSkipVeto (0x142FF9E54) is 0 (0x14023984F); the high dword of g_EventSkipFlags (0x142FF9E50, 'armed') is non-zero (0x140239857); the high dword of g_ScreenFade (0x142FF9E0C, the skip state) is 0 (0x14023985F); g_EventSkipOnce (0x142FF9EBC) is not 2 (0x140239867).
- V: it only reads globals: no input, no UI object, no write. The result is a pure function of state that exists while the script runs, so it can be evaluated from memory at any time.
- V: EventScript_SkipTick applies the same five-field test before it raises the skip state (at 0x140239D02..0x140239D26, addresses inside EventScript_SkipTick, not this function).
- I: g_EventSkipEnabled is always 1 (its only writer, VideoState_InitDefaults, stores 1), so in practice the test is armed != 0, veto == 0, skip state == 0 and skip-once != 2.

## State touched

- Calls: [EventSkip_IsViewerEvent](EventSkip_IsViewerEvent.md)
- Reads: [g_EventSkipEnabled](../globals/g_EventSkipEnabled.md), [g_EventSkipVeto](../globals/g_EventSkipVeto.md), [g_EventSkipFlags](../globals/g_EventSkipFlags.md), [g_EventSkipOnce](../globals/g_EventSkipOnce.md)

## Referenced by

- Called by: [EventControl_PausedTick](EventControl_PausedTick.md), [EventControl_TryOpenPause](EventControl_TryOpenPause.md)
- Observed behaviours: [SceneSkipState](../behaviors/SceneSkipState.md), [StoryChoiceBalloon](../behaviors/StoryChoiceBalloon.md)

## Notes

The low dword of 0x142FF9E4C is not part of this test; it is the event-viewer flag (see g_EventSkipFlags). The dword at 0x142FF9E50 is.

## Open questions

None recorded.
