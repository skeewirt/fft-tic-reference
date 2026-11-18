# NxdDataLandRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.land table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="ability_id"></a>`0x4` | ability_id | `int32` | I | Geomancer terrain ability (126..137). Observed in the stock rows: 0 to 137, 13 distinct values. |
| <a id="name"></a>`0x8` | name | `string (int32 offset)` | I | Name text. Observed in the stock rows: 49 distinct values, 16 empty. |
| <a id="description"></a>`0xC` | description | `string (int32 offset)` | I | Description text. Observed in the stock rows: 49 distinct values, 16 empty. |
| <a id="icon_id"></a>`0x10` | icon_id | `int32` | I | Row id of Icon (a reference by column name). Observed in the stock rows: 0 to 647, 48 distinct values. |

## Referenced by

- Described by tables: [NxdDataLand](../tables/NxdDataLand.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
