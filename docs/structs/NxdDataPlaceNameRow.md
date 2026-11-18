# NxdDataPlaceNameRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.place_name table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="place_name_id"></a>`0x8` | place_name_id | `int32` | I | Place name id (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="title"></a>`0xC` | title | `string (int32 offset)` | I | Title text. Observed in the stock rows: 154 distinct values, 62 empty. |
| <a id="unk_10"></a>`0x10` | unk_10 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 3 distinct values, 255 empty. |

## Referenced by

- Described by tables: [NxdDataPlaceName](../tables/NxdDataPlaceName.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 5 columns not decoded.
