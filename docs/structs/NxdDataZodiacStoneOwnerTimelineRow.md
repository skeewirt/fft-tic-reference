# NxdDataZodiacStoneOwnerTimelineRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.zodiac_stone_owner_timeline table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 10 distinct values, 2 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 10 distinct values, 2 empty. |

## Referenced by

- Described by tables: [NxdDataZodiacStoneOwnerTimeline](../tables/NxdDataZodiacStoneOwnerTimeline.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

2 of 4 columns not decoded.
