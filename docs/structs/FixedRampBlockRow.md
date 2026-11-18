# FixedRampBlockRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of EffectPoseBlendKeys.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="keys"></a>`0x0` | keys | `uint8[16]` | I | eight 16-bit fixed point values (4096 = 1.0): ramps copied to stack arrays by the update |

## Referenced by

- Described by tables: [EffectPoseBlendKeys](../tables/EffectPoseBlendKeys.md)

## Open questions

None recorded.
