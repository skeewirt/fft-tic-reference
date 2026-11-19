# NxdDataWorldMapProgressInfoRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 44 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.world_map_progress_info table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="town"></a>`0x8` | town | `int32` | M | Measured over every stock row: Every value is a key of nxd.Town-en. Observed in the stock rows: 0 to 47, 22 distinct values. |
| <a id="town_2"></a>`0xC` | town_2 | `int32` | M | Measured over every stock row: Every value is a key of nxd.Town-en. Observed in the stock rows: 7 to 47, 23 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 25 distinct values. |
| <a id="caption"></a>`0x18` | caption | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 54 distinct values, 36 empty. |
| <a id="user_situation"></a>`0x1C` | user_situation | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 0 to 3230, 4 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 2782, 13 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 1643, 13 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown29"></a>`0x29` | unknown29 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataWorldMapProgressInfo](../tables/NxdDataWorldMapProgressInfo.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 7 of 11 columns not decoded.
