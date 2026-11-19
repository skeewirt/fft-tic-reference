# MovieController_UpdateSkip

- **Address:** `0x1400D8168`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void MovieController_UpdateSkip(MovieController *ctlPlus8)`
- **Callers:** virtual call through vftable_ffto::Game::GameUI::MovieController_140702D30 slot 4
- **Callees:** MovieControl_PausedTick, MovieControl_TryOpenPause, MovieControl_IdleHint, sub_14027A2B0, sub_1404BA570, sub_1400EBABC, sub_1400D8B9C, sub_14009D68C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame movie pause / skip handling of the GameUI MovieController (a virtual of its second vtable): publishes whether the playing movie can be skipped and runs the MovieControl state machine.

## Behavior

- V: receives the controller pointer + 8; the movie flags are at +16 of that (controller +24) and the result bits at +20 (controller +28).
- V: when flags bit 0x8 is clear and result bit 0 is clear and g_MovieControl (0x143CDA078) is set, it writes MovieControl +25 = (flags & 0x10) != 0 every frame.
- V: only when flags bit 0x20 is set, and g_ShopModeGate (enhanced flag) is non-zero, it steps MovieControl state +8: 0 -> 1; 1 -> MovieControl_TryOpenPause (or MovieControl_IdleHint when that returns 0, when the player at qword_143CD9C28 has +16 == 3, or when a UI dialog node byte +74/+75 is set); 2 -> MovieControl_PausedTick.
- V: when flags bit 0x10 is set, it copies (MovieControl +8 == 3) into result bit 0 (the skip is taken).

## State touched

- Calls: [MovieControl_PausedTick](MovieControl_PausedTick.md), [MovieControl_TryOpenPause](MovieControl_TryOpenPause.md), [MovieControl_IdleHint](MovieControl_IdleHint.md)
- Reads: [g_MovieControl](../globals/g_MovieControl.md), [g_ShopModeGate](../globals/g_ShopModeGate.md), [MovieController.movie_flags](../structs/MovieController.md#movie_flags), [MovieControl.state](../structs/MovieControl.md#state)
- Writes: [MovieControl.skippable](../structs/MovieControl.md#skippable), [MovieControl.state](../structs/MovieControl.md#state), [MovieController.result_flags](../structs/MovieController.md#result_flags)

## Referenced by

- Appears in flows: [MovieStart](../flows/MovieStart.md)
- Observed behaviours: [MovieSkipKinds](../behaviors/MovieSkipKinds.md), [SceneSkipState](../behaviors/SceneSkipState.md)

## Notes

Movie_Start sets the flags from the MovieData (NXD 65) row: byte +36 -> 0x20, +37 -> 0x10, +38 -> 0x8. The controller is at *(qword_143CD9DC8) + 0xC8 (Boot_UpdateVideo passes that address to Movie_Start).

## Open questions

? What the player state 3 (qword_143CD9C28 + 16) is.
