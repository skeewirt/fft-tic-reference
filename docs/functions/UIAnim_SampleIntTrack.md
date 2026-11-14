# UIAnim_SampleIntTrack

- **Address:** `0x140408218`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char UIAnim_SampleIntTrack(KeyTrack *trk, float t, int *out)`
- **Callers:** GUINode_ApplyAnimChannels (its integer tracks: sort order and the per-kind int fields)
- **Callees:** KeyTrack_FindKey, UIAnim_Curve

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Samples an integer keyframe track at a (float) frame with the easing curve of the key before it.

## Behavior

- V: i = KeyTrack_FindKey(trk, (int)t); i < 0 or the key's curve id (key+4) = 0 returns 0 (value left alone).
- V: for i < last: s = (t - (float)key.frame) / (float)(next.frame - key.frame); e = UIAnim_Curve(key.curve, s); out = (int)(e * (float)(next.value - key.value) + (float)key.value), a C truncation of the float result; the int difference is taken in integers before the float conversion. For the last key out = key.value. Returns 1.
- V: key layout is the one of UIAnim_SampleFloatTrack: 16 bytes, +0 u16 frame, +4 u32 curve, +8 int value; keys 0..3 inline, the rest at *(trk+64) - 4 entries; count at trk+72.

## State touched

- Calls: [KeyTrack_FindKey](KeyTrack_FindKey.md), [UIAnim_Curve](UIAnim_Curve.md)

## Notes

The name is ours (IDB: sub_140408218). Same structure as KeyTrackVec2_Eval and UIAnim_SampleFloatTrack, with a truncating integer result.

## Open questions

? which node fields use the int track (see GUINode_ApplyAnimChannels).
