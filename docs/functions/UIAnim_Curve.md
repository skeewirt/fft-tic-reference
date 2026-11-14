# UIAnim_Curve

- **Address:** `0x14040242C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `float UIAnim_Curve(int curveId, float t)`
- **Callers:** KeyTrackBool_Eval, UIAnim_SampleFloatTrack, KeyTrackVec2_Eval, UIAnim_SampleInt2Track, UIAnim_SampleIntTrack, UIAnim_SampleColorTrack
- **Callees:** sub_140402BB8 (circular in-out), sub_140402C14 (elastic), sub_140402CA0 (bounce), sub_140402D38 (Bezier)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Easing curve evaluator for keyframes: maps the position t within a key interval (0 to 1) to the blend factor of that interval. Curve ids are those of the registry UIAnimCurves.

## Behavior

- V: the id arrives in the first integer register and t in the second float register (the decompiler shows the second parameter as an integer); every curve is evaluated in single precision (sinf, cosf, powf, sqrtf, float literals), and t is not clamped except where a case tests it. The callers pass t = (frame - key frame) / (next key frame - key frame).
- V: ids 1 to 21: 1 step, 2 linear, 3 smoothstep t*t*(3 - 2t), 4 t*t, 5 t*(2 - t), 6 in-out quad, 7 t^3, 8 1 + (t - 1)^3, 9 in-out cubic, 10 t^4, 11 1 - (1 - t)^4, 12 in-out quart, 13 t^5, 14 1 - (1 - t)^5, 15 in-out quint, 16 2^(10t - 10), 17 1 - 2^(-10t), 18 in-out expo, 19 1 - cos(t * pi / 2), 20 sin(t * pi / 2), 21 (1 - cos(t * pi)) / 2.
- V: ids 22 to 39: 22 1 - sqrt(1 - t*t), 23 sqrt(1 - (t - 1)^2), 24 circular in-out (sub_140402BB8), 25 back in, 26 back out, 27 back in-out, 28 elastic in, 29 elastic out, 30 elastic in-out (sub_140402C14), 31 bounce in, 32 bounce out, 33 bounce in-out (sub_140402CA0), 34 to 39 cubic Bezier easings solved for t (sub_140402D38). Any other id, and id 0, gives the step: 0 below t = 1, else 1. The full formulas are in the registry UIAnimCurves.
- V: pi is the single-precision constant 3.1415927; curve 20 = sinf((t * pi) * 0.5) and curve 19 = 1 - cosf((t * pi) * 0.5), in that operand order.
- V: the evaluator never rounds; the sampling functions that call it do (UIAnim_SampleInt2Track truncates to an integer).

## State touched

- Reads: [UIAnimCurves](../registries/UIAnimCurves.md)

## Referenced by

- Called by: [KeyTrackBool_Eval](KeyTrackBool_Eval.md), [KeyTrackVec2_Eval](KeyTrackVec2_Eval.md), [UIAnim_SampleColorTrack](UIAnim_SampleColorTrack.md), [UIAnim_SampleFloatTrack](UIAnim_SampleFloatTrack.md), [UIAnim_SampleInt2Track](UIAnim_SampleInt2Track.md), [UIAnim_SampleIntTrack](UIAnim_SampleIntTrack.md)
- Observed behaviours: [CursorGloveBob](../behaviors/CursorGloveBob.md)
- Resolves registries: [UIAnimCurves](../registries/UIAnimCurves.md)

## Notes

Owner-visible effects: UnitJob CursorOver (curve 5), Hand Loop (20 then 19). Callers earlier recorded as UIAnim_ApplyTrack were wrong: that function only stores curve ids, it never evaluates.

## Open questions

None recorded.
