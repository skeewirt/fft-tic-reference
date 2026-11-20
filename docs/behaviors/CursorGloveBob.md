# CursorGloveBob

- **Kind:** observed behaviour
- **Scope:** finger cursor (the glove on the Job Tree)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [UIAnim_SampleInt2Track](../functions/UIAnim_SampleInt2Track.md), [UIAnim_Curve](../functions/UIAnim_Curve.md), [GUINodeState_Advance](../functions/GUINodeState_Advance.md), [UIAddonFingerCursor_PlayLoop](../functions/UIAddonFingerCursor_PlayLoop.md), [GUICursorHand_StepToward](../functions/GUICursorHand_StepToward.md), [UIAnimCurves](../registries/UIAnimCurves.md), [CursorGloveFrame](../flows/CursorGloveFrame.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The glove's idle bob: a 40-frame, looping, position track on the IconHand node of the Hand component, played on the UI frame time, sampled as an integer, and added to the glove's glide only in the node matrices. This record gives the rule exactly (decoded from the code and the two cursor UIB files).

## Behavior

- V (data): the Hand component's Loop state is 40 frames; its IconHand position track has keys at frame 0 (0, -2) curve id 20 (OutSine), frame 20 (-20, -2) curve id 19 (InSine) and frame 40 (0, -2) curve id 2 (the file stores interpolation ids 19, 18 and 1). A second track (tag 5031) is a jump marker from frame 40 to frame 0.
- V (data): the Widget component of ffto_finger_cursor.uib has its own Loop state of 40 frames whose only track links frames 0 to 40 to state Loop of the CursorRef node (the Hand): frame 0 -> child frame 0, frame 40 -> child frame 40.
- V: sampling at the Hand's frame f (a float): the key is the last one with frame <= (int)f; u = (f - key frame) / (next frame - key frame) in single precision; for f < 20: x = trunc(fl(fl(-20 * sin((u*pi)*0.5)) + 0)) with u = f / 20; for 20 <= f < 40: x = trunc(fl(fl(20 * (1 - cos((u*pi)*0.5))) + (-20))) with u = (f - 20) / 20; y = trunc(-2) = -2. trunc is the conversion toward zero, so x is an integer from -20 to 0 and sits at or to the right of the continuous value (for example frame 1: -1.569 -> -1).
- V: IconHand's position is the sampled pair (absolute state). Its local matrix is translation (pivot + position) - 0.8 * pivot with the node's pivot (100, 20) and scale 0.8, so the glove's top-left in the 1920 x 1080 layout space is glide + (-86, -17) + (x, y) + (20, 4) (pivot * (1 - 0.8)), then the layer transform. The glide position (an integer from roundf) and the bob (an integer from truncation) are summed in float matrices; nothing rounds the sum.
- V: the bob is in layout pixels (not scaled by the glove's 0.8); the screen scale applies afterwards like for every UI pixel.
- V: the phase is the main component's Loop frame. It is advanced once per UI frame by dt (see UIStateClock) and wrapped by the loop at frame >= 40: frame and time become 0, the overshoot is dropped.
- V: restart (phase 0) happens on every UIAddonFingerCursor_PlayLoop, called by UIAgentCursor_Show and UIAddonFingerCursor_ResetPose; the Loop stops (and later restarts at 0) on UIAgentCursor_Hide, UIAddonFingerCursor_SetPose / FreezePose and static mode. Moving the glove (glide, arrival, retarget, hiding the node for lack of a target) does not touch the clock.
- V: none of the Job Tree addon's functions refers directly to the cursor functions (decompile text search).
- I: so panel-to-panel cursor moves inside the Job Tree do not restart the bob; a call through a helper was not excluded.
- I (computed from the decoded rule in single precision, not read from the game): with dt of exactly 1/60 s the frame at the k-th tick after a restart is k for k = 1 .. 39 and 0 at the 40th (the loop sets it to 0 because 40.0 >= 40), so the displayed frame sequence is 1, 2, ..., 39, 0, 1, ...; the x sequence is 0 at frame 0, then -1, -3, -4, -6, -7, -9, -10, -11, -12, -14, ... down to -20 at frame 20 and back up symmetrically. With dt between 5000 and 5100 ticks of 1/300000 s the cycle is still 40 ticks (frames k * dt * 60); at 4999 ticks it would be 41.
- I: after a restart the first applied frame is about 1 (GUINode_PlayState applies nothing; the next update advances first).
- V (live, 2026-10-30, 12 phases from 0 to 39 with the clock frozen): IconHand's position read from the game equals this rule at every phase (0, -1, -7, -14, -18, -19, -20, -19, -18, -12, -4, -1 at frames 0, 1, 5, 10, 15, 19, 20, 21, 25, 31, 37, 39), and a viewer drawing the glove at glide + (-86, -17) + (20 + x, 4 - 2) on the game's own background reproduces the captured glove to within 2 levels (93 % of the pixels exact).
- V (live read, 2026-10-30, Job Tree): the main component's Loop runs (+0x69 = 1) with the loop byte set (+0x6C = 1) and range 0 .. 0 (so 0 .. 40); the Hand's Loop is paused (+0x6B = 1) and its frame is the main frame through the link's single-precision (f * 40) / 40 (31.363609 -> 31.363611). Writing rate 0 and a frame F into the main Loop held the clock at F (12 phases from 0 to 39 read back unchanged after a capture) and the captured glove moved between F = 0 and F = 20.
- V (live read, 2026-10-31): the bob does NOT restart when the Job Tree opens: with the main Loop held at frame 20 (rate 0) on the jobs list, X (Job Progress) opened the Job Tree and the same Loop state object still read rate 0, time 1/3, frame 20. The finger cursor is shared by the menus, so the phase on the Job Tree is whatever the clock had on the screen before.

## Notes

Rule for a viewer that reproduces the glove (what differs from a continuous sine): (1) take the phase f as the UI tick's frame, not as seconds * 60 wrapped by modulo; (2) x = the truncated value above, an integer; (3) y = -2; (4) top-left = glide origin + (-86 + x, -17 - 2) + (20, 4). The curve values are float32 results; only values within about 1e-5 of an integer could round differently from a double-precision evaluation.

## Open questions

? The frame timer's maximum step, which would shorten dt on a very slow frame.
