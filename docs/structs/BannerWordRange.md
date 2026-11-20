# BannerWordRange

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the BannerWordRanges table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="first_cell"></a>`0x0` | first_cell | `uint32` | V | first cell index in BannerWordCells; cells = next entry - this entry |

## Referenced by

- Described by tables: [BannerWordRanges](../tables/BannerWordRanges.md)

## Open questions

None recorded.
