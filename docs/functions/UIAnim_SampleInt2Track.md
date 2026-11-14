# UIAnim_SampleInt2Track

- **Address:** `0x1404080C4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char UIAnim_SampleInt2Track(KeyTrack *trk, float t, int out[2])`
- **Callers:** GUINode_ApplyAnimChannels (position a[6], size a[7]), sub_140407D85
- **Callees:** sub_14040222C, UIAnim_Curve

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Same as UIAnim_SampleFloatTrack for a track of integer pairs (position and size).

## Behavior

- V: key search and u as in UIAnim_SampleFloatTrack; for i < last each component = (int)((float)(next - cur) * curve(u) + (float)cur) (integer difference converted to float, truncating conversion toward zero, so a fractional position is dropped toward 0, not floored); i = last returns the key's pair unchanged.
- V (disassembly; the decompiler hides the interval position): the frame searched is (int)t; u = (t - (float)key.frame) / (float)(next.frame - key.frame) in single precision with the float t; curve = UIAnim_Curve(key.curve, u); x = truncate(fl(fl((float)(next.x - key.x) * curve) + (float)key.x)), y likewise. The product, the sum and u are each rounded to single precision.
- V: returns 0 (the field is left alone) when no key is at or before the frame, or when the key's curve id is 0. The caller stores the pair with GUINode_SetPosition, so a position track yields integer positions.

## State touched

- Calls: [UIAnim_Curve](UIAnim_Curve.md), [KeyTrack_FindKey](KeyTrack_FindKey.md)
- Reads: [KeyTrack.keys_inline](../structs/KeyTrack.md#keys_inline), [KeyTrack.keys_heap](../structs/KeyTrack.md#keys_heap), [KeyTrack.count](../structs/KeyTrack.md#count), [KeyTrackKey.frame](../structs/KeyTrackKey.md#frame), [KeyTrackKey.curve](../structs/KeyTrackKey.md#curve), [KeyTrackKey.value](../structs/KeyTrackKey.md#value)

## Referenced by

- Appears in flows: [CursorGloveFrame](../flows/CursorGloveFrame.md)
- Observed behaviours: [CursorGloveBob](../behaviors/CursorGloveBob.md)

## Notes

The name is ours (IDB: sub_1404080C4). sub_140408218 is the single-int sibling used for sort order and per-kind ints; sub_140408328 interpolates colours per byte.

## Open questions

None recorded.
