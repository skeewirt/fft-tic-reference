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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="ability"></a>`0x4` | ability | `int32` | M | Measured over every stock row: Every value is a key of nxd.Ability-en. Observed in the stock rows: 0 to 137, 13 distinct values. |
| <a id="name"></a>`0x8` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 49 distinct values, 16 empty. |
| <a id="description"></a>`0xC` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 49 distinct values, 16 empty. |
| <a id="icon"></a>`0x10` | icon | `int32` | M | Measured over every stock row: Every value is a key of nxd.Icon. Observed in the stock rows: 0 to 647, 48 distinct values. |

## Referenced by

- Described by tables: [NxdDataLand](../tables/NxdDataLand.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 1 of 5 columns not decoded.
