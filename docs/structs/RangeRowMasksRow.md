# RangeRowMasksRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the RangeRowMasks table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="mask"></a>`0x0` | mask | `int16` | V | 16-bit row mask, a centred run of set bits (0x0100, 0x0380, 0x07C0, 0x0FE0 ... 0xFFFE); the run grows by one bit per side per entry |

## Referenced by

- Described by tables: [RangeRowMasks](../tables/RangeRowMasks.md)

## Open questions

None recorded.
