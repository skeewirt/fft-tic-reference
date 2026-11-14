# KeyTrack_FindKey

- **Address:** `0x14040222C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int KeyTrack_FindKey(KeyTrack *t, int frame)`
- **Callers:** KeyTrackVec2_Eval, KeyTrackBool_Eval and the other KeyTrack evaluators (sub_140407B14, sub_1404080C4, sub_140408218, sub_140408328)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Binary search in a keyframe track: returns the index of the last key whose frame (u16 at key+0) is <= frame, or -1 when every key is later.

## Behavior

- V: the track is a small vector: count = int at t+72; keys 0..3 are stored inline at t + 16*i, keys 4.. in the heap array at *(t+64) + 16*(i-4). A key is 16 bytes: u16 frame (+0), u16 span (+2), u32 curve id (+4), 8 bytes of value (+8, +12).
- V: lo = 0, hi = count, mid = count / 2; a key later than frame moves hi, otherwise lo; the result is the last mid that was <= frame (-1 when none).

## Referenced by

- Called by: [KeyTrackBool_Eval](KeyTrackBool_Eval.md), [KeyTrackVec2_Eval](KeyTrackVec2_Eval.md), [UIAnim_SampleColorTrack](UIAnim_SampleColorTrack.md), [UIAnim_SampleInt2Track](UIAnim_SampleInt2Track.md), [UIAnim_SampleIntTrack](UIAnim_SampleIntTrack.md)

## Notes

The name is ours (IDB: sub_14040222C). Callers pass the frame truncated to int (cvttss2si for the float evaluators).

## Open questions

None recorded.
