# KeyTrack

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

A keyframe track of one property of one target: sorted keys, the first four stored inline. Sampled by UIAnim_SampleFloatTrack, UIAnim_SampleInt2Track and their siblings; built by UIAnim_StoreKey.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by |
|---|---|---|---|---|---|
| <a id="keys_inline"></a>`0x0` | keys_inline | `KeyTrackKey[4]` | V | Keys 0 to 3 (16 bytes each). | [UIAnim_SampleFloatTrack](../functions/UIAnim_SampleFloatTrack.md), [UIAnim_SampleInt2Track](../functions/UIAnim_SampleInt2Track.md) |
| <a id="keys_heap"></a>`0x40` | keys_heap | `KeyTrackKey *` | V | Keys 4 and up: key i is at keys_heap + 16 * (i - 4). | [UIAnim_SampleFloatTrack](../functions/UIAnim_SampleFloatTrack.md), [UIAnim_SampleInt2Track](../functions/UIAnim_SampleInt2Track.md) |
| <a id="count"></a>`0x48` | count | `int32` | V | Number of keys. | [UIAnim_SampleFloatTrack](../functions/UIAnim_SampleFloatTrack.md), [UIAnim_SampleInt2Track](../functions/UIAnim_SampleInt2Track.md) |

## Behavior

- V: KeyTrack_FindKey returns the last key whose frame is <= the integer frame searched (a binary search).

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? The rest of the object (a capacity field and the channel bookkeeping).
