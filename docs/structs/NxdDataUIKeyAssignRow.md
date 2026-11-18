# NxdDataUIKeyAssignRow

- **Kind:** structure
- **Area:** [Input](../areas/input.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_key_assign table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 24, 25 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 60, 28 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 24, 20 distinct values. |
| <a id="main_key_code"></a>`0x10` | main_key_code | `int32` | I | Main key code (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 161, 35 distinct values. |
| <a id="alternate_key_code"></a>`0x14` | alternate_key_code | `int32` | I | Alternate key code (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 164, 10 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 86 distinct values, 168 empty. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unk_20"></a>`0x20` | unk_20 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_21"></a>`0x21` | unk_21 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_22"></a>`0x22` | unk_22 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="main_key_unk23"></a>`0x23` | main_key_unk23 | `uint8` | I | Main key unk23 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="main_key_unk24"></a>`0x24` | main_key_unk24 | `uint8` | I | Main key unk24 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="main_key_unk25"></a>`0x25` | main_key_unk25 | `uint8` | I | Main key unk25 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="main_key_unk26"></a>`0x26` | main_key_unk26 | `uint8` | I | Main key unk26 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="alternate_key_unk27"></a>`0x27` | alternate_key_unk27 | `uint8` | I | Alternate key unk27 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="alternate_key_unk28"></a>`0x28` | alternate_key_unk28 | `uint8` | I | Alternate key unk28 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="alternate_key_unk29"></a>`0x29` | alternate_key_unk29 | `uint8` | I | Alternate key unk29 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="unk_2a"></a>`0x2A` | unk_2a | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_2b"></a>`0x2B` | unk_2b | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_2d"></a>`0x2D` | unk_2d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIKeyAssign](../tables/NxdDataUIKeyAssign.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

12 of 22 columns not decoded.
