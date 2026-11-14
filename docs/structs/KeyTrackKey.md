# KeyTrackKey

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One keyframe: its frame, the curve that shapes the interval to the next key, and the value.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by | Indexed by registries |
|---|---|---|---|---|---|---|---|
| <a id="frame"></a>`0x0` | frame | `uint16` | V | Key frame (60 per second). | [UIAnim_SampleFloatTrack](../functions/UIAnim_SampleFloatTrack.md), [UIAnim_SampleInt2Track](../functions/UIAnim_SampleInt2Track.md) |  |  |
| <a id="word"></a>`0x2` | word | `uint16` | V | Stored by UIAnim_StoreKey; zero for position, scale, rotation, colour and opacity tracks. |  | [UIAnim_StoreKey](../functions/UIAnim_StoreKey.md) |  |
| <a id="curve"></a>`0x4` | curve | `uint32` | V | Curve id of the interval from this key to the next (registry UIAnimCurves); 0 = the channel is not applied. | [UIAnim_SampleFloatTrack](../functions/UIAnim_SampleFloatTrack.md), [UIAnim_SampleInt2Track](../functions/UIAnim_SampleInt2Track.md) | [UIAnim_StoreKey](../functions/UIAnim_StoreKey.md) | [UIAnimCurves](../registries/UIAnimCurves.md) |
| <a id="value"></a>`0x8` | value | `8 bytes` | V | The value: an int pair (position, size), a float pair (scale), one float (rotation, opacity) or colour bytes. | [UIAnim_SampleFloatTrack](../functions/UIAnim_SampleFloatTrack.md), [UIAnim_SampleInt2Track](../functions/UIAnim_SampleInt2Track.md) | [UIAnim_StoreKey](../functions/UIAnim_StoreKey.md) |  |

## Behavior

- V: the interval from key i to key i + 1 uses the curve of key i; the last key holds its value.

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
