# EffectFlashProfilesRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 14 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EffectFlashProfiles table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="p0"></a>`0x0` | p0 | `int16` | V | parameter 0 |
| <a id="p1"></a>`0x2` | p1 | `int16` | V | parameter 1 |
| <a id="p2"></a>`0x4` | p2 | `int16` | V | parameter 2 |
| <a id="p3"></a>`0x6` | p3 | `int16` | V | parameter 3 |
| <a id="p4"></a>`0x8` | p4 | `int16` | V | parameter 4 |
| <a id="p5"></a>`0xA` | p5 | `int16` | V | parameter 5 (low byte used) |
| <a id="p6"></a>`0xC` | p6 | `int16` | V | low byte parameter 6, high byte blend weight row |

## Referenced by

- Described by tables: [EffectFlashProfiles](../tables/EffectFlashProfiles.md)

## Open questions

None recorded.
