# NxdDataCollectionRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 44 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.collection table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 801 to 863, 43 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int32` | ? | Not decoded. Observed in the stock rows: 200 to 265, 43 distinct values. |
| <a id="name"></a>`0x14` | name | `string (int32 offset)` | I | Name text. Observed in the stock rows: 43 distinct values, 0 empty. |
| <a id="description"></a>`0x18` | description | `string (int32 offset)` | I | Description text. Observed in the stock rows: 43 distinct values, 0 empty. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 43 distinct values, 0 empty. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 43, 43 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 43, 43 distinct values. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int32` | ? | Not decoded. Observed in the stock rows: 521 to 576, 43 distinct values. |

## Referenced by

- Described by tables: [NxdDataCollection](../tables/NxdDataCollection.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

7 of 11 columns not decoded.
