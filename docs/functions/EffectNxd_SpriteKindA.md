# EffectNxd_SpriteKindA

- **Address:** `0x1400D28E4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int EffectNxd_SpriteKindA(int kind, ..., int effect)`
- **Callers:** sub_140348924, sub_14034B9F0, sub_14034CC14, sub_14034DE90 and others
- **Callees:** sub_1400D2D30, EffectNxd_HasFlag24, sub_1400D2C74

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses an effect sprite's draw kind, then, when the effect has its own texture, its texture slot.

## Behavior

- V: calls EffectNxd_AdjustSpriteKind first, then, when the effect row's own_texture byte is set (EffectNxd_HasFlag24), EffectNxd_SelectPageTexture.

## State touched

- Calls: [EffectNxd_HasFlag24](EffectNxd_HasFlag24.md)

## Notes

Name is ours.

## Open questions

None recorded.
