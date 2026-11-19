# NxdDataUIElementAttributeRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_element_attribute table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="name"></a>`0x4` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 8 distinct values, 0 empty. |
| <a id="unknown08"></a>`0x8` | unknown08 | `uint8` | ? | Not decoded. Observed in the stock rows: 1 to 8, 8 distinct values. |
| <a id="unknown09"></a>`0x9` | unknown09 | `uint8` | ? | Not decoded. Observed in the stock rows: 1 to 8, 8 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIElementAttribute](../tables/NxdDataUIElementAttribute.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 3 of 4 columns not decoded.
