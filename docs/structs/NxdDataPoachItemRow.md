# NxdDataPoachItemRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 56 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.poach_item table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unk_10"></a>`0x10` | unk_10 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unk_14"></a>`0x14` | unk_14 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unk_18"></a>`0x18` | unk_18 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_1d"></a>`0x1D` | unk_1d | `uint8` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unk_1e"></a>`0x1E` | unk_1e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_1f"></a>`0x1F` | unk_1f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="cost"></a>`0x24` | cost | `int32` | I | Cost (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 5 to 30000, 38 distinct values. |
| <a id="sell_price"></a>`0x28` | sell_price | `int32` | I | Sell price (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 3 to 15000, 38 distinct values. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `int32` | ? | Not decoded. Observed in the stock rows: 4 to 253, 82 distinct values. |
| <a id="icon_id"></a>`0x30` | icon_id | `int32` | I | Row id of Icon (a reference by column name). Observed in the stock rows: 1 to 48, 48 distinct values. |
| <a id="is_rare"></a>`0x34` | is_rare | `uint8` | I | Is rare (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_35"></a>`0x35` | unk_35 | `uint8` | ? | Not decoded. Observed in the stock rows: 1 to 98, 96 distinct values. |
| <a id="unk_36"></a>`0x36` | unk_36 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [PoachItem](../tables/PoachItem.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

13 of 19 columns not decoded.
