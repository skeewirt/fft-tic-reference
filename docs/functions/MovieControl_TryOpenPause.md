# MovieControl_TryOpenPause

- **Address:** `0x14027A35C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool MovieControl_TryOpenPause(MovieControl *mc)`
- **Callers:** MovieController_UpdateSkip
- **Callees:** Input_TestAction, sub_1400F144C, sub_14027A2B0, sub_1400EB65C, sub_1400EB5F4, sub_1401D1E30, sub_1401D6F9C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the movie pause overlay on the pause action, with or without the Skip hint by MovieControl +25.

## Behavior

- V: returns 0 unless Input_TestAction(action 0x5F) is true.
- V: sets +8 = 2, arms the hold action 0x5D, and passes 502 with mask -1 when byte +25 is set, -3 when not, to sub_1400EB65C.
- V: clears qword_143CD9DD0 + 88 and calls sub_1401D6F9C(qword_143CD9DD8, 7, 1).

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [sub_1401D1E30](sub_1401D1E30.md)
- Reads: [MovieControl.skippable](../structs/MovieControl.md#skippable)
- Writes: [MovieControl.state](../structs/MovieControl.md#state)

## Referenced by

- Called by: [MovieController_UpdateSkip](MovieController_UpdateSkip.md)
- Observed behaviours: [SceneSkipState](../behaviors/SceneSkipState.md)

## Notes

Same button guide (502) as the event overlay.

## Open questions

None recorded.
