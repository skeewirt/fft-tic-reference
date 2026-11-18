# NxdDataUIChroniclePeriodRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_chronicle_period table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x8` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="user_situation_id"></a>`0xC` | user_situation_id | `int32` | I | Row id of UserSituation (a reference by column name). Observed in the stock rows: 0 to 16000, 27 distinct values. |
| <a id="type"></a>`0x10` | type | `int32` | I | Type (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 6, 6 distinct values. |
| <a id="ui_chronicle_chara_list_id"></a>`0x14` | ui_chronicle_chara_list_id | `int32` | I | Row id of UIChronicleCharaList (a reference by column name). Observed in the stock rows: 0 to 30, 31 distinct values. |
| <a id="icon_id"></a>`0x18` | icon_id | `int32` | I | Row id of Icon (a reference by column name). Observed in the stock rows: 0 to 490, 12 distinct values. |
| <a id="caption"></a>`0x1C` | caption | `string (int32 offset)` | I | Caption text. Observed in the stock rows: 31 distinct values, 1 empty. |
| <a id="world_situation_balloon_id"></a>`0x20` | world_situation_balloon_id | `int32` | I | Row id of WorldSituationBalloon (a reference by column name). Observed in the stock rows: 0 to 30, 31 distinct values. |
| <a id="flag_24"></a>`0x24` | flag_24 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIChroniclePeriod](../tables/NxdDataUIChroniclePeriod.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

2 of 10 columns not decoded.
