# NxdDataSortieConfirmRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.sortie_confirm table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="map_id"></a>`0x4` | map_id | `int32` | I | Row id of Map (a reference by column name). Observed in the stock rows: 0 to 91, 28 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 14, 5 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: -1 in every row. |
| <a id="event_ui_id"></a>`0x10` | event_ui_id | `int32` | I | UI text key (a row of the UI text table), from the column name. Observed in the stock rows: 0 to 1507, 3 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 3, 2 distinct values. |
| <a id="max_unit_ui_id"></a>`0x18` | max_unit_ui_id | `int32` | I | UI text key (a row of the UI text table), from the column name. Observed in the stock rows: 0 to 1502, 3 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 172, 31 distinct values. |
| <a id="threat_rating_ui_id"></a>`0x20` | threat_rating_ui_id | `int32` | I | UI text key (a row of the UI text table), from the column name. Observed in the stock rows: 0 to 1505, 4 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | ? | Not decoded. Observed in the stock rows: 48 in every row. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 2 distinct values. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataSortieConfirm](../tables/NxdDataSortieConfirm.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

7 of 12 columns not decoded.
