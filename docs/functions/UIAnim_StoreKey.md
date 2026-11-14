# UIAnim_StoreKey

- **Address:** `0x1403F8708`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UIAnim_StoreKey(UIAnimLoader *ld, int *track, GUINodeState *state, UIName *target, int propType, unsigned frame, short word, void *value, int curveId)`
- **Callers:** UIAnim_ApplyTrack, UIAnim_ApplyComponentTrack
- **Callees:** sub_1404003F4, sub_1404020E4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stores one keyframe of a UIB state track into the state's runtime key track for a target and property type.

## Behavior

- V: the key track is found (or made) with sub_1404003F4(state, target, propType); sub_1404020E4(keytrack, frame) returns the key slot for that frame (nothing is stored when it is negative).
- V: the slot gets: value (8 bytes) at key+8, word at key+2, curve id at key+4. The key's frame (u16 at +0) is set by sub_1404020E4.
- V: the function ends with a call of the loader object's virtual +40 with (ld, track, state, target name, propType); what it does was not read.

## State touched

- Writes: [KeyTrackKey.curve](../structs/KeyTrackKey.md#curve), [KeyTrackKey.value](../structs/KeyTrackKey.md#value), [KeyTrackKey.word](../structs/KeyTrackKey.md#word)

## Referenced by

- Called by: [UIAnim_ApplyComponentTrack](UIAnim_ApplyComponentTrack.md), [UIAnim_ApplyTrack](UIAnim_ApplyTrack.md)

## Notes

The name is ours (IDB: sub_1403F8708). Property type 3 is the integer position pair (tag 5002); the key layout is that of struct KeyTrack.

## Open questions

? sub_1404020E4 (ordered insert) and the loader callback were not read.
