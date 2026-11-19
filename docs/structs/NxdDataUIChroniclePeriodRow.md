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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="user_situation"></a>`0xC` | user_situation | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 0 to 16000, 27 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 6, 6 distinct values. |
| <a id="ui_chronicle_chara_list"></a>`0x14` | ui_chronicle_chara_list | `int32` | M | Measured over every stock row: Every value is a key of nxd.UIChronicleCharaList. Observed in the stock rows: 0 to 30, 31 distinct values. |
| <a id="icon"></a>`0x18` | icon | `int32` | M | Measured over every stock row: Every value is a key of nxd.Icon. Observed in the stock rows: 0 to 490, 12 distinct values. |
| <a id="caption"></a>`0x1C` | caption | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 31 distinct values, 1 empty. |
| <a id="world_situation_balloon"></a>`0x20` | world_situation_balloon | `int32` | M | Measured over every stock row: Every value is a key of nxd.WorldSituationBalloon. Observed in the stock rows: 0 to 30, 31 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIChroniclePeriod](../tables/NxdDataUIChroniclePeriod.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 5 of 10 columns not decoded.
