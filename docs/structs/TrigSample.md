# TrigSample

- **Kind:** structure
- **Area:** [Math](../areas/math.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the CosineTable table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="cos"></a>`0x0` | cos | `uint32` | V | cosine scaled by 4096 (4096 = 1.0, 0 at a quarter turn, -4096 at a half turn) |

## Referenced by

- Described by tables: [CosineTable](../tables/CosineTable.md), [SineTable](../tables/SineTable.md)

## Open questions

None recorded.
