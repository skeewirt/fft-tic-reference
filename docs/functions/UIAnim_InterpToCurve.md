# UIAnim_InterpToCurve

- **Address:** `0x1403F8818`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int UIAnim_InterpToCurve(void *ctx, int interpId)`
- **Callers:** UIAnim_ApplyTrack, UIAnim_ApplyComponentTrack
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps a UIB keyframe interpolation id to the easing curve id used by UIAnim_Curve: n -> n + 1 for 0 to 35, anything else -> 2 (linear).

## Behavior

- V: n -> n + 1 for n = 0 .. 35 (0 -> 1, 1 -> 2, 2 -> 3, ..., 35 -> 36); there are no other exceptions; any other value (negative or above 35) -> 2.
- V (data): the Hand's Loop keys carry file ids 19, 18 and 1, so curves 20 (sin), 19 (1 - cos) and 2 (linear).

## Referenced by

- Called by: [UIAnim_ApplyComponentTrack](UIAnim_ApplyComponentTrack.md), [UIAnim_ApplyTrack](UIAnim_ApplyTrack.md)
- Resolves registries: [UIAnimCurves](../registries/UIAnimCurves.md)

## Open questions

None recorded.
