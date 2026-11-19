# EffectNxd_SpriteKindB

- **Address:** `0x1400D2964`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int EffectNxd_SpriteKindB(int kind, ..., int effect)`
- **Callers:** EffectSprite_EmitPieces, sub_140380FB8
- **Callees:** sub_1400D2D30, EffectNxd_HasFlag24, sub_1400D2C74

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

A second form of EffectNxd_SpriteKindA used by the piece emitter.

## Behavior

- V: same steps as EffectNxd_SpriteKindA: sprite kind adjustment, then, with own_texture set, the page texture selection.

## State touched

- Calls: [EffectNxd_HasFlag24](EffectNxd_HasFlag24.md)

## Notes

Name is ours.

## Open questions

None recorded.
