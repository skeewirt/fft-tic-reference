# NxdDataCharaNameRow

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.chara_name table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="name"></a>`0x8` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 829 distinct values, 180 empty. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `union {int32 kind; int32 id}` | ? | Not decoded. Observed in the stock rows: 74 distinct values. |
| <a id="own_name"></a>`0x14` | own_name | `uint8` | V | Read in the code: Non-zero: a unit with this name key is shown with its own stored name string (when it has one) instead of this row's name. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataCharaName](../tables/NxdDataCharaName.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 3 of 5 columns not decoded.
