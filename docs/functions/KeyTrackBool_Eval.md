# KeyTrackBool_Eval

- **Address:** `0x1403F4604`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char KeyTrackBool_Eval(KeyTrack *t, int frame, bool *out)`
- **Callers:** sub_140400840 (GUINode_ApplyTracks, visibility track a1[14])
- **Callees:** KeyTrack_FindKey, UIAnim_Curve

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Evaluates the boolean (visibility) track of a UIB state at an integer frame; the result drives node byte +144.

## Behavior

- V: key = KeyTrack_FindKey(t, frame); none -> return 0 (property untouched). Let span = u16 key+2, f = key.frame (u16 +0), v = (key+8 != 0).
- V: span != 0: frame > f + span -> *out = 0, otherwise *out = v (a key with a span is a pulse of that many frames); return 1.
- V: span == 0 and frame == f: *out = v. Span == 0 and the key's curve id (key+4) != 0: not the last key: s = (frame - f) / (next.frame - f) (int to float divide), e = UIAnim_Curve(curve, s), *out = (e < 1.0) ? v : next.v, so the value flips to the next key's value exactly when the eased curve reaches 1.0; last key: *out = v. Curve id 0 -> return 0.

## State touched

- Calls: [KeyTrack_FindKey](KeyTrack_FindKey.md), [UIAnim_Curve](UIAnim_Curve.md)

## Notes

The name is ours (IDB: sub_1403F4604). In sub_140400840 the output is stored as node+144 = out (absolute mode, a4 != 0) or node+144 = out && node+144 (relative mode, a4 == 0): a relative visibility track can only hide.

## Open questions

? Which UIB property this track is called in the editor (only its node effect +144 was read).
