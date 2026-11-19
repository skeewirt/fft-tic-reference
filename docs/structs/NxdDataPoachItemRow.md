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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unknown10"></a>`0x10` | unknown10 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unknown14"></a>`0x14` | unknown14 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unknown18"></a>`0x18` | unknown18 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown1d"></a>`0x1D` | unknown1d | `uint8` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unknown1e"></a>`0x1E` | unknown1e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown1f"></a>`0x1F` | unknown1f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown24"></a>`0x24` | unknown24 | `int32` | ? | Not decoded. Observed in the stock rows: 5 to 30000, 38 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32` | ? | Not decoded. Observed in the stock rows: 3 to 15000, 38 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `int32` | ? | Not decoded. Observed in the stock rows: 4 to 253, 82 distinct values. |
| <a id="icon"></a>`0x30` | icon | `int32` | M | Measured over every stock row: Every value is a key of nxd.Icon. Observed in the stock rows: 1 to 48, 48 distinct values. |
| <a id="unknown34"></a>`0x34` | unknown34 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown35"></a>`0x35` | unknown35 | `uint8` | ? | Not decoded. Observed in the stock rows: 1 to 98, 96 distinct values. |
| <a id="unknown36"></a>`0x36` | unknown36 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [PoachItem](../tables/PoachItem.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 18 of 19 columns not decoded.
