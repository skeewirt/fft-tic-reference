# GameTasks_RunFrameSteps

- **Address:** `0x1402574E0`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void GameTasks_RunFrameSteps(void)`
- **Callers:** Boot_UpdateVideo
- **Callees:** GlobalWork_GetSpeedMultiplier, CharaRenderer_Update, Time_GetTimestamp, sub_1403CA794, sub_140062118, sub_14041880C, sub_1403CA810, sub_1403CA7D0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the game's task threads for one displayed frame: the whole per-frame step is repeated GlobalWork_GetSpeedMultiplier times, which is how fast-forward speeds the game up.

## Behavior

- V: reads the multiplier once, then loops step = 0 .. multiplier - 1; each step stores the step number in GlobalWork +92, resets the per-frame draw lists, calls CharaRenderer_Update and resumes the task threads in order until one reports the end of the frame.
- V: when the multiplier is above 1 it sets three 'do not draw' bytes (in the sprite renderer and two of its sub-objects) to 1 on every step but the last and to 0 on the last, so only the last step of a frame is drawn.
- V: after the loop GlobalWork +92 is 0.
- I: every task that waits by frames (event scripts, battle animation, walking, effects, message timers) therefore advances 3 or 5 times per displayed frame; nothing is skipped, the steps are simply run more often.

## State touched

- Calls: [GlobalWork_GetSpeedMultiplier](GlobalWork_GetSpeedMultiplier.md), [CharaRenderer_Update](CharaRenderer_Update.md), [Time_GetTimestamp](Time_GetTimestamp.md)
- Reads: [g_GlobalWork](../globals/g_GlobalWork.md)
- Writes: [GlobalWork.frame_step](../structs/GlobalWork.md#frame_step)

## Referenced by

- Observed behaviours: [AFaultInAGameTaskFreezesTheGame](../behaviors/AFaultInAGameTaskFreezesTheGame.md), [FastForwardState](../behaviors/FastForwardState.md)

## Notes

EventControl_Update runs only while GlobalWork +92 is 0, so the event overlay and the hold logic tick once per displayed frame, on the first step.

## Open questions

? The task-thread hand-off itself (the event objects and the states -1 / -2 it waits for) was read only as far as the loop needs.
