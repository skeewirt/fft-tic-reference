# NxdDataBookRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 44 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.book table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4, 5 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | ? | Not decoded. Observed in the stock rows: 818 to 832, 5 distinct values. |
| <a id="icon"></a>`0x10` | icon | `int32` | M | Measured over every stock row: Every value is a key of nxd.Icon. Observed in the stock rows: 217 to 231, 5 distinct values. |
| <a id="title"></a>`0x14` | title | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 5 distinct values, 0 empty. |
| <a id="description"></a>`0x18` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 5 distinct values, 0 empty. |
| <a id="description_formatted"></a>`0x1C` | description_formatted | `string (int32 offset)` | M | Measured over every stock row: The description text with its layout codes. Observed in the stock rows: 5 distinct values, 1 empty. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int16` | ? | Not decoded. Observed in the stock rows: 225 to 233, 5 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32` | ? | Not decoded. Observed in the stock rows: 538 to 552, 5 distinct values. |

## Referenced by

- Described by tables: [NxdDataBook](../tables/NxdDataBook.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 7 of 11 columns not decoded.
