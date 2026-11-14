# MovieControl_PausedTick

- **Address:** `0x14027A1CC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `uint8_t MovieControl_PausedTick(MovieControl *mc)`
- **Callers:** MovieController_UpdateSkip
- **Callees:** sub_1400EB7EC, sub_1400F144C, sub_1400F1510, Input_TestAction, sub_14027A2B0, sub_1401D6F9C, sub_1400F4BCC, sub_1400F0E98

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Paused frame of the movie overlay: a completed hold with byte +25 set takes the skip (state 3); the pause or back action resumes.

## Behavior

- V: when byte +25 is non-zero and Input_TestAction(action 0x5D) fires, it closes the overlay, sets +8 = 3, calls sub_1401D6F9C(qword_143CD9DD8, 7, 0) and sub_1400F4BCC(0xBA).
- V: otherwise, on action 0x5F or 0x1B (and the hold not in progress), sets +8 = 0 and calls sub_1401D6F9C(qword_143CD9DD8, 7, 0).

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [sub_1400F4BCC](sub_1400F4BCC.md)
- Reads: [MovieControl.skippable](../structs/MovieControl.md#skippable)
- Writes: [MovieControl.state](../structs/MovieControl.md#state)

## Referenced by

- Called by: [MovieController_UpdateSkip](MovieController_UpdateSkip.md)

## Open questions

None recorded.
