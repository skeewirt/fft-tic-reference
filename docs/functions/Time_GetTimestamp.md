# Time_GetTimestamp

- **Address:** `0x14006A9B4`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall Time_GetTimestamp(void)`
- **Callers:** App_RunFrame, App_ProcessMessages and 70+ UI/render/input call sites (see the IDB xrefs).
- **Callees:** Indirect clock-provider vtable calls (+8, +16); no direct game calls.

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns a monotonic timestamp in 1/300000-second units. The value is derived from a clock provider's counter and frequency; callers divide by 300000.0 to get seconds.

## Behavior

- V: reads the clock provider at `qword_143CD9BC8`; when it and its `+8` object are non-null, calls the object's vtable slot +8 and uses the result as the counter; otherwise the counter is 0.
- V: calls the same object's vtable slot +16 for the divisor; when the object is missing the divisor is 1.
- V: computes `300000 * counter / divisor`; a large period constant (`0x1BF647612F36`) is used to split the counter and keep the result monotonic across a wrap.
- V: `App_RunFrame` divides the return value by 300000.0 to obtain seconds and uses the same value for the 1/60 s frame limiter and the second frame cap.
- I: the vtable slot +8 returns the counter and slot +16 returns the frequency; the object is a platform clock provider.
- I: the large period constant corrects for a counter wrap, not for a unit conversion.

## State touched

- Reads: [g_ClockProvider](../globals/g_ClockProvider.md)

## Referenced by

- Called by: [App_ProcessMessages](App_ProcessMessages.md), [App_RunFrame](App_RunFrame.md), [EventControl_UpdateGuide](EventControl_UpdateGuide.md), [GameTasks_RunFrameSteps](GameTasks_RunFrameSteps.md), [MovieControl_IdleHint](MovieControl_IdleHint.md)
- Observed behaviours: [BattleForkDeterminism](../behaviors/BattleForkDeterminism.md)

## Notes

This is the project name for the timestamp source; the game's clock object is not otherwise documented.

## Open questions

The concrete clock implementation behind `qword_143CD9BC8` and the exact wrap period.
