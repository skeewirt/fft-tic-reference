# UIStateClock

- **Kind:** observed behaviour
- **Scope:** every UIB state (timeline)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [UI_FrameUpdate](../functions/UI_FrameUpdate.md), [GUICore_BeginFrame](../functions/GUICore_BeginFrame.md), [GUICore_TickWidget](../functions/GUICore_TickWidget.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md), [GUINodeState.time](../structs/GUINodeState.md#time), [GUINodeState.frame](../structs/GUINodeState.md#frame)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the clock of a UI state runs: real elapsed time per UI frame (never less than 1/60 s), summed in single precision, frame = time * 60.0 as a float; the end or a loop resets frame and time and drops the overshoot.

## Behavior

- V: the application's frame limiter (App_RunFrame) waits until the elapsed frame time (ticks * scale / 300000.0, in double) reaches 1/60 s, so an application frame is never shorter than 1/60 s at scale 1; the step it stores for the frame is the elapsed time clamped by the timer's maximum step (timer +16, value not read).
- V: the UI scene callers form dt = (float)(ticks * scale / 300000.0) from an object with the same two fields.
- I: that object is the same frame timer, so UI_FrameUpdate's dt is the clamped application frame step.
- V: UI_FrameUpdate multiplies dt by g_UIDataModule+28 (1.0 in the table the module is created with) and GUICore_BeginFrame stores it at g_GUICore+2100; a second value goes to +2104.
- V: GUICore_TickWidget gives each widget dt = 0 while a block bit is set that the widget's mask lacks, else +2100 (widget selector 0) or +2104 (selector 1); other selector values skip the widget.
- V: GUINodeState_Advance: time = (dt * rate) + time and frame = time * 60.0, both single precision; a state that reaches its end frame either loops (frame and time = range start, overshoot dropped) or stops on the end frame; a jump marker passed sets frame and time to its start frame the same way.
- V: the sampled frame is the float, not an integer: only the key search truncates it; the position within a key interval uses the float.
- I: at 60 Hz the frame advances by 1 plus a small excess per UI frame (the excess is the part of the real frame time above 1/60 s), so a 40-frame loop takes 40 UI frames; on a slow frame the clock jumps by more than one frame (real time is kept).
- V (live read, 2026-10-30): the live Loop frames carry fractions well above the single-precision excess of exact 1/60 s steps (27.83, 31.36), so the real frame steps were longer than 1/60 s: a running game's phase is ahead of the ideal 60 Hz count by the summed overruns, and it differs between runs. A viewer can only reproduce a given phase exactly, not predict the live one.

## Notes

The glide of the finger cursor is not on this clock: GUICursorHand_StepToward moves a fixed fraction per UI frame.

## Open questions

? The frame timer's maximum step and the value of g_GUICore+2104.
