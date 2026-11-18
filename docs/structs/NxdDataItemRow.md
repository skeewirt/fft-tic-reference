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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="name"></a>`0x4` | name | `string (int32 offset)` | I | Name text. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="name_singular"></a>`0x8` | name_singular | `string (int32 offset)` | I | Name singular text. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="name_plural"></a>`0xC` | name_plural | `string (int32 offset)` | I | Name plural text. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="description"></a>`0x10` | description | `string (int32 offset)` | I | Description text. Observed in the stock rows: 259 distinct values, 3 empty. |
| <a id="name2"></a>`0x14` | name2 | `string (int32 offset)` | I | Name2 text. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="unk_18"></a>`0x18` | unk_18 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_19"></a>`0x19` | unk_19 | `uint8` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unk_1a"></a>`0x1A` | unk_1a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_1b"></a>`0x1B` | unk_1b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="ui_status_effect_id"></a>`0x1C` | ui_status_effect_id | `int32` | I | Row id of UIStatusEffect-en (a reference by column name). Observed in the stock rows: 0 to 1002, 3 distinct values. |
| <a id="comment"></a>`0x20` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="ui_item_category_id"></a>`0x24` | ui_item_category_id | `int32` | I | Row id of UIItemCategory-en (a reference by column name). Observed in the stock rows: 0 to 34, 35 distinct values. |
| <a id="sort_order"></a>`0x28` | sort_order | `int32` | I | Sort order value. Observed in the stock rows: 0 to 6106, 260 distinct values. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="is_random_damage"></a>`0x2D` | is_random_damage | `uint8` | I | Is random damage (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [Item](../tables/Item.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

5 of 16 columns not decoded.
