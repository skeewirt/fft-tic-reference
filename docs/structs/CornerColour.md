# CornerColour

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the BannerWordColours table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="rgb"></a>`0x0` | rgb | `bytes[3]` | V | corner colour |
| <a id="pad"></a>`0x3` | pad | `uint8` | I | unused by this reader |

## Referenced by

- Described by tables: [BannerWordColours](../tables/BannerWordColours.md)

## Open questions

None recorded.
