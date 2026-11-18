# NxdDataC_Mes_Id_SampleRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.battle_message_text table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 1384 distinct values, 236 empty. |
| <a id="unk_08"></a>`0x8` | unk_08 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 7 distinct values, 1728 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unk_10"></a>`0x10` | unk_10 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_11"></a>`0x11` | unk_11 | `uint8` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unk_12"></a>`0x12` | unk_12 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_13"></a>`0x13` | unk_13 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="flag_14"></a>`0x14` | flag_14 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [C_Mes_Id_Sample](../tables/C_Mes_Id_Sample.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

8 of 9 columns not decoded.
