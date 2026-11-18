# NxdDataTownRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 52 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.town table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="description"></a>`0x4` | description | `string (int32 offset)` | I | Description text. Observed in the stock rows: 47 distinct values, 2 empty. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 3035, 46 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1942, 42 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="place_name_id"></a>`0x14` | place_name_id | `int32` | I | Row id of PlaceName-en (a reference by column name). Observed in the stock rows: 0 to 1470, 47 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 46 distinct values, 3 empty. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 26, 26 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 510, 46 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="user_situation_id"></a>`0x28` | user_situation_id | `int32` | I | Row id of UserSituation (a reference by column name). Observed in the stock rows: 0 to 14600, 8 distinct values. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `int16` | ? | Not decoded. Observed in the stock rows: -1 to 42, 25 distinct values. |
| <a id="unk_2e"></a>`0x2E` | unk_2e | `int16` | ? | Not decoded. Observed in the stock rows: -1 to 43, 44 distinct values. |
| <a id="unk_30"></a>`0x30` | unk_30 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_31"></a>`0x31` | flag_31 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_32"></a>`0x32` | unk_32 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_33"></a>`0x33` | unk_33 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataTown](../tables/NxdDataTown.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

13 of 17 columns not decoded.
