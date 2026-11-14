# MovieControl_IdleHint

- **Address:** `0x14027A128`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void MovieControl_IdleHint(MovieControl *mc)`
- **Callers:** MovieController_UpdateSkip
- **Callees:** sub_1400F12C0, Time_GetTimestamp, sub_1400EB65C, sub_1400EB5F4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

While a movie plays unpaused, shows the 'Pause' button hint for about 5 seconds after any input.

## Behavior

- V: when sub_1400F12C0 reports input it stores the time at +16 and shows the hint; while +24 is set the hint stays until 5 s (timestamp units / 300000) have passed.
- V: when the shown state changes it calls sub_1400EB65C(9102, -1) on show and sub_1400EB5F4 with the new state, and stores it at +24.
- I: UIButtonGuide row 9102 is one entry, 'Pause' (text 2645, action 95).

## State touched

- Calls: [Time_GetTimestamp](Time_GetTimestamp.md)
- Writes: [MovieControl.hint_time](../structs/MovieControl.md#hint_time), [MovieControl.hint_shown](../structs/MovieControl.md#hint_shown)

## Referenced by

- Called by: [MovieController_UpdateSkip](MovieController_UpdateSkip.md)

## Open questions

None recorded.
