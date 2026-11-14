# UIAnim_SampleColorTrack

- **Address:** `0x140408328`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char UIAnim_SampleColorTrack(KeyTrack *trk, float t, uint32_t *out)`
- **Callers:** GUINode_ApplyAnimChannels, GUIComponent_ApplyAnimChannels, sub_140407DF8 (the four-colour kind-6 tracks)
- **Callees:** KeyTrack_FindKey, UIAnim_Curve, UIAnim_LerpColor

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Samples a packed-RGBA colour keyframe track at a frame: the key before t blends to the next with its easing curve through UIAnim_LerpColor.

## Behavior

- V: i = KeyTrack_FindKey(trk, (int)t); i < 0 or curve id of the key = 0 returns 0.
- V: for i < last: s = (t - (float)key.frame) / (float)(next.frame - key.frame); e = UIAnim_Curve(key.curve, s); out = UIAnim_LerpColor(key.colour, next.colour, e) (colour = the dword at key+8, read byte by byte). For the last key out = key.colour. Returns 1.

## State touched

- Calls: [KeyTrack_FindKey](KeyTrack_FindKey.md), [UIAnim_Curve](UIAnim_Curve.md), [UIAnim_LerpColor](UIAnim_LerpColor.md)

## Referenced by

- Called by: [GUIComponent_ApplyAnimChannels](GUIComponent_ApplyAnimChannels.md)

## Notes

The name is ours (IDB: sub_140408328). Colours are sampled per byte, so an animated alpha is interpolated and truncated like the RGB channels.

## Open questions

None recorded.
