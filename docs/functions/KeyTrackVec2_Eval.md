# KeyTrackVec2_Eval

- **Address:** `0x140407C18`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char KeyTrackVec2_Eval(KeyTrack *t, float frame, float out[2])`
- **Callers:** sub_140400840 (GUINode_ApplyTracks, scale track a1[8]), sub_1404015C0 (component-level tracks, five call sites)
- **Callees:** KeyTrack_FindKey, UIAnim_Curve

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Evaluates a two-float keyframe track (the scale track of a UIB state) at a frame: finds the key, eases between it and the next key with UIAnim_Curve and writes the interpolated pair.

## Behavior

- V: key index = KeyTrack_FindKey(t, (int)frame) (the frame is TRUNCATED for the search). Index < 0 returns 0 (no value: the caller leaves the property alone). The key's curve id (u32 at key+4) = 0 also returns 0.
- V: when the key is not the last one: next = key + 1; s = (frame - (float)key.frame) / (float)(next.frame - key.frame) with the UNtruncated float frame; e = UIAnim_Curve(key.curve, s); out.x = (next.x - key.x) * e + key.x and out.y = (next.y - key.y) * e + key.y (single precision, this operation order).
- V: when the key is the last one the output is that key's pair unchanged (the value holds after the last key); the function returns 1.
- I: the easing of a segment is chosen by the curve id of the segment's FIRST key.

## State touched

- Calls: [KeyTrack_FindKey](KeyTrack_FindKey.md), [UIAnim_Curve](UIAnim_Curve.md)

## Referenced by

- Called by: [GUIComponent_ApplyAnimChannels](GUIComponent_ApplyAnimChannels.md)

## Notes

The name is ours (IDB: sub_140407C18). sub_140407B14 (one float, rotation and opacity tracks) and the int / colour evaluators sub_1404080C4, sub_140408218, sub_140408328 follow the same key layout (not read here).

## Open questions

? The key's u16 at +2 is not read by this evaluator (KeyTrackBool_Eval uses it as a hold length).
