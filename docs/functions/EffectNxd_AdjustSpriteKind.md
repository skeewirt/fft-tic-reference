# EffectNxd_AdjustSpriteKind

- **Address:** `0x1400D2D30`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int EffectNxd_AdjustSpriteKind(int kind, int effect)`
- **Callers:** sub_1400D28E4, sub_1400D2964, sub_140310CE4
- **Callees:** EffectNxd_HasFlag28

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Changes an effect sprite's draw kind when the effect row's flag asks for it.

## Behavior

- V: when the effect row's flag byte is set (unknown_1c, read by EffectNxd_HasFlag28), draw kind 20 becomes 21 and 23 becomes 24.

## State touched

- Calls: [EffectNxd_HasFlag28](EffectNxd_HasFlag28.md)

## Notes

Name is ours.

## Open questions

? what draw kinds 20, 21, 23 and 24 are.
