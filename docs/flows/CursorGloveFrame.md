# CursorGloveFrame

- **Kind:** flow
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

What happens to the finger cursor's glove in one UI frame, in order: its Loop clock advances, scrubs the Hand's Loop, the Hand's IconHand position is sampled as an integer, and the cursor reference node glides toward the focused panel. The two integers meet only in the node matrices.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [UI_FrameUpdate](../functions/UI_FrameUpdate.md) | V | Start of the UI frame: the UI time ui+13480 = dt * g_UIDataModule+28 (1.0), dt being the application's frame time (at least 1/60 s). |
| <a id="2"></a>2 | [UIAgentCursor_Show](../functions/UIAgentCursor_Show.md) | V | Only when a show is pending (show_state 2): the restart runs now and ends in UIAddonFingerCursor_PlayLoop: the Loop clock of the main component is zeroed, running, dirty, looping. |
| <a id="3"></a>3 | [UIAddonFingerCursor_PlayLoop](../functions/UIAddonFingerCursor_PlayLoop.md) | V | Loop state: time = frame = prev_frame = 0, loop flag 1, running and dirty set; nothing is applied to nodes here. |
| <a id="4"></a>4 | [GUICursorHand_Update](../functions/GUICursorHand_Update.md) | V | The agent update: the cursor reference node moves one glide step (integer, roundf) toward the focused panel's rect; independent of the Loop clock. |
| <a id="5"></a>5 | [GUICore_BeginFrame](../functions/GUICore_BeginFrame.md) | V | g_GUICore+2100 = the UI time. |
| <a id="6"></a>6 | [GUICore_TickWidget](../functions/GUICore_TickWidget.md) | V | The widget tick: dt = 0 when a block bit is set, else g_GUICore+2100 (selector 0) or +2104 (selector 1). |
| <a id="7"></a>7 | [GUIWidget_Tick](../functions/GUIWidget_Tick.md) | V | Calls the main component's virtual +32, GUIComponent_Update. |
| <a id="8"></a>8 | [GUINodeState_Advance](../functions/GUINodeState_Advance.md) | V | GUINode_UpdateStates: the main component's Loop advances: time = (dt * rate) + time, frame = time * 60.0; at frame >= 40 the loop sets frame and time to 0 (overshoot lost). It posts event 40 for its state link entry every tick. |
| <a id="9"></a>9 | [GUIAddon_OnStateEvent](../functions/GUIAddon_OnStateEvent.md) | V | The component handles the event: the child CursorRef's Loop state is enabled, paused, and its frame = min(max((frame - 0) * 40 / (40 - 0), 0), 40), time = frame / 60, dirty. |
| <a id="10"></a>10 | [GUIComponent_ApplyStateAnims](../functions/GUIComponent_ApplyStateAnims.md) | V | The Hand component's update (through the CursorRef reference node) samples its active states at their float frame; the Hand's paused Loop gives the scrubbed frame. |
| <a id="11"></a>11 | [UIAnim_SampleInt2Track](../functions/UIAnim_SampleInt2Track.md) | V | IconHand's position track: key search on the truncated frame, u and the curve in single precision, the result truncated toward zero to an integer pair. |
| <a id="12"></a>12 | [GUINode_SetPosition](../functions/GUINode_SetPosition.md) | V | The integer pair becomes IconHand's position (absolute state: it replaces the field); the node is marked dirty when it changed. |
| <a id="13"></a>13 | [GUINode_BuildLocalMatrix](../functions/GUINode_BuildLocalMatrix.md) | V | Node matrices: IconHand local = (pivot + position) - scale * pivot; times the Layer00 node (offset -86, -17) and the cursor reference node (the glide position) and the layer transform. No rounding anywhere in this chain. |

## Behavior

- V: steps 8 to 13 run on the UI frame time; step 4 has no time term.
- I: the first tick after a restart advances the Loop to about frame 1 before anything is applied (step 3 applies nothing, step 8 moves the frame).
- I: the order of step 4 relative to steps 5 to 13 within a frame is open, but the two positions do not depend on each other: each frame's picture uses that frame's glide position and that frame's bob.

## Referenced by

- Observed behaviours: [CursorGloveBob](../behaviors/CursorGloveBob.md)

## Notes

The Loop of the Hand component is never advanced by its own clock: it is paused by the link and only scrubbed (GUIAddon_OnStateEvent). Live read points: global qword_143CD9DA8 (addon manager) +16 = agent vector, element 1 = the agent (UIAgentCursor); agent +0x40 = the addon (UIAddonFingerCursor); addon +0x18 = the widget; widget +104 .. +112 = component pointers, the first with +536 = 1 is the main component; its states are the vector at +616 .. +624 (state +0 = the name text pointer, compare with the text Loop): time +0x4C, frame +0x50, previous frame +0x54, flags +0x68 .. +0x6F. The Hand component is addon +0x30 (same layout; its Loop frame equals the main Loop frame after step 9).

## Open questions

? The order of the cursor agent's update relative to the widget tick. (Answered 2026-10-31: the Loop does not restart when the Job Tree opens; see the next record.)
