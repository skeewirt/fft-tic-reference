# EffectNxd_SelectPageTexture

- **Address:** `0x1400D2C74`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int EffectNxd_SelectPageTexture(int page, ..., int effect)`
- **Callers:** sub_1400D28E4, sub_1400D2964
- **Callees:** EffectNxd_HasFlag25, sub_14041E448

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Picks the texture slot for an effect sprite on a refined texture page (6, 7 or 8) and records its flag.

## Behavior

- V: for pages 6, 7 and 8 returns the effect's own texture slot (10291 / 10307 / 10323 plus the effect) and stores dword_142E7FEE8 / EC / F0 = 2 * effect + 1426.
- V: stores the unknown_19 flag of the effect row (EffectNxd_HasFlag25) per page in dword_140C6ADA0 / A4 / A8; no reader of those three globals was found.

## State touched

- Calls: [EffectNxd_HasFlag25](EffectNxd_HasFlag25.md)

## Notes

Name is ours.

## Open questions

None recorded.
