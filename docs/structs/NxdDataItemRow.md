# NxdDataItemRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.item table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="name"></a>`0x4` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="singular"></a>`0x8` | singular | `string (int32 offset)` | M | Measured over every stock row: The name in its singular form. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="plural"></a>`0xC` | plural | `string (int32 offset)` | M | Measured over every stock row: The name in its plural form. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="description"></a>`0x10` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 259 distinct values, 3 empty. |
| <a id="name_2"></a>`0x14` | name_2 | `string (int32 offset)` | M | Measured over every stock row: A second copy of the name. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="unknown18"></a>`0x18` | unknown18 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown19"></a>`0x19` | unknown19 | `uint8` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unknown1a"></a>`0x1A` | unknown1a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown1b"></a>`0x1B` | unknown1b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="ui_status_effect"></a>`0x1C` | ui_status_effect | `int32` | M | Measured over every stock row: Every value is a key of nxd.UIStatusEffect-en. Observed in the stock rows: 0 to 1002, 3 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="ui_item_category"></a>`0x24` | ui_item_category | `int32` | M | Measured over every stock row: Every value is a key of nxd.UIItemCategory-en. Observed in the stock rows: 0 to 34, 35 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 6106, 260 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown2d"></a>`0x2D` | unknown2d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [Item](../tables/Item.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 9 of 16 columns not decoded.
