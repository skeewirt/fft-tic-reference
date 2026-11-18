# NxdDataJournalRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.journal table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 117, 117 distinct values. |
| <a id="user_situation_id"></a>`0xC` | user_situation_id | `int32` | I | Row id of UserSituation (a reference by column name). Observed in the stock rows: 3510 to 16000, 61 distinct values. |
| <a id="title"></a>`0x10` | title | `string (int32 offset)` | I | Title text. Observed in the stock rows: 117 distinct values, 0 empty. |
| <a id="text"></a>`0x14` | text | `string (int32 offset)` | I | Text text. Observed in the stock rows: 117 distinct values, 0 empty. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 488, 66 distinct values. |
| <a id="place_name_id"></a>`0x1C` | place_name_id | `int32` | I | Row id of PlaceName-en (a reference by column name). Observed in the stock rows: 0 in every row. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 6, 2 distinct values. |
| <a id="flag_24"></a>`0x24` | flag_24 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_25"></a>`0x25` | flag_25 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_26"></a>`0x26` | flag_26 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataJournal](../tables/NxdDataJournal.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

6 of 12 columns not decoded.
