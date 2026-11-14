# UIAnim_SampleFloatTrack

- **Address:** `0x140407B14`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char UIAnim_SampleFloatTrack(KeyTrack *trk, float t, float *out)`
- **Callers:** GUINode_ApplyAnimChannels (rotation, opacity, floats), GUIComponent code (about 8 callers)
- **Callees:** sub_14040222C, UIAnim_Curve

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Samples a float keyframe track at time t with the easing curve of the key before t.

## Behavior

- V: key record = 16 bytes: u16 time (+0), u16 (+2), u32 curve id (+4), float value (+8), value2 (+12). The first 4 keys are stored inline at trk+0..+63, further keys in the vector at trk+64 (index - 4); count at trk+72.
- V: i = sub_14040222C(trk, (int)t): a binary search for the last key whose time <= (int)t (t truncated to an integer frame for the search); -1 (no key yet) or a key whose curve id (+4) is 0 returns 0 (the channel is not applied).
- V: for i < last: u = (t - key[i].time) / (float)(key[i+1].time - key[i].time) (float t, not truncated); out = UIAnim_Curve(curve id of key[i], u) * (key[i+1].value - key[i].value) + key[i].value. For i = last, out = key[last].value (hold).

## State touched

- Calls: [UIAnim_Curve](UIAnim_Curve.md)
- Reads: [KeyTrack.keys_inline](../structs/KeyTrack.md#keys_inline), [KeyTrack.keys_heap](../structs/KeyTrack.md#keys_heap), [KeyTrack.count](../structs/KeyTrack.md#count), [KeyTrackKey.frame](../structs/KeyTrackKey.md#frame), [KeyTrackKey.curve](../structs/KeyTrackKey.md#curve), [KeyTrackKey.value](../structs/KeyTrackKey.md#value)

## Referenced by

- Called by: [GUIComponentScrollBar_StepKnob](GUIComponentScrollBar_StepKnob.md), [GUIComponent_ApplyAnimChannels](GUIComponent_ApplyAnimChannels.md), [GUINode_ApplyAnimChannels](GUINode_ApplyAnimChannels.md)

## Notes

The name is ours (IDB: sub_140407B14). The easing curve belongs to the key at the left of the interval.

## Open questions

None recorded.
