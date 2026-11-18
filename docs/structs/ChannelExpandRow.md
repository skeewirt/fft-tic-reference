# ChannelExpandRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of GfxBitExpandTables.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="expand4"></a>`0x0` | expand4 | `uint8[16]` | V | 4-bit to 8-bit: n * 0x11 |
| <a id="expand5"></a>`0x10` | expand5 | `uint8[32]` | V | 5-bit to 8-bit: (n * 255 + 15) / 31 style steps 0, 8, 16, 24, 32, 41 ... 255 |
| <a id="expand6"></a>`0x30` | expand6 | `uint8[64]` | V | 6-bit to 8-bit: steps of about 4 up to 255 |

## Referenced by

- Described by tables: [GfxBitExpandTables](../tables/GfxBitExpandTables.md)

## Open questions

None recorded.
