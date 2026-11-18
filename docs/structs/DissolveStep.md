# DissolveStep

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 64 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the DissolveOffsets table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="offset[32]"></a>`0x0` | offset[32] | `bytes[64]` | V | 32 u16 pixel offsets inside one 1024-byte line group; each row is a permutation of the offsets copied in that step |

## Referenced by

- Described by tables: [DissolveOffsets](../tables/DissolveOffsets.md)

## Open questions

None recorded.
