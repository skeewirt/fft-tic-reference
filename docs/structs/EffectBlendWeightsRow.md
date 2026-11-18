# EffectBlendWeightsRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 7 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EffectBlendWeights table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="weights"></a>`0x0` | weights | `bytes[7]` | V | seven blend factors (or palette slot numbers in row 4) |

## Referenced by

- Described by tables: [EffectBlendWeights](../tables/EffectBlendWeights.md)

## Open questions

None recorded.
