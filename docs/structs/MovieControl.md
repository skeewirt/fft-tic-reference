# MovieControl

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 32 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

ffto::Game::Movie::MovieControl (vtable 0x1407154B0), at g_MovieControl: pause overlay and hold-to-skip of a playing movie.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="state"></a>`0x8` | state | `int32` | V | 0 new, 1 playing, 2 paused (overlay up), 3 skip chosen (MovieController_UpdateSkip then sets the controller's result bit 0). | [MovieControl_PausedTick](../functions/MovieControl_PausedTick.md), [MovieControl_TryOpenPause](../functions/MovieControl_TryOpenPause.md), [MovieController_UpdateSkip](../functions/MovieController_UpdateSkip.md) | [MovieController_UpdateSkip](../functions/MovieController_UpdateSkip.md) |
| <a id="hint_time"></a>`0x10` | hint_time | `int64` | V | Time of the last input, for the 5 s 'Pause' hint (MovieControl_IdleHint). | [MovieControl_IdleHint](../functions/MovieControl_IdleHint.md) |  |
| <a id="hint_shown"></a>`0x18` | hint_shown | `uint8` | V | 1 while the 'Pause' hint (guide 9102) is shown. | [MovieControl_IdleHint](../functions/MovieControl_IdleHint.md) |  |
| <a id="skippable"></a>`0x19` | skippable | `uint8` | V | Rewritten every frame by MovieController_UpdateSkip from movie flag 0x10 (MovieData byte +37); the paused tick accepts the hold only when it is set, and the overlay shows the Skip hint only when it is set. | [MovieController_UpdateSkip](../functions/MovieController_UpdateSkip.md) | [MovieControl_PausedTick](../functions/MovieControl_PausedTick.md), [MovieControl_TryOpenPause](../functions/MovieControl_TryOpenPause.md) |

## Behavior

- V: created by Movie_Start when g_MovieControl is null; g_MovieControl is cleared by sub_1400D80DC, sub_14027A0E8, sub_14027A41C and sub_1402F2E40.

## Notes

Detail and evidence: the function sheets named on this page.

## Open questions

? Exactly when the object is released relative to the end of a movie (the four clearing functions were not read).
