# SlotPermutationRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of SceneSlotPermutations.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="order"></a>`0x0` | order | `uint8[16]` | V | four dwords: a permutation of 0..3 (a zero ends the walk in the reader) |

## Referenced by

- Described by tables: [SceneSlotPermutations](../tables/SceneSlotPermutations.md)

## Open questions

None recorded.
