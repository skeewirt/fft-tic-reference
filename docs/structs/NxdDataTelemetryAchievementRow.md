# NxdDataTelemetryAchievementRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 64 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.telemetry_achievement table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 50, 51 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 49, 51 distinct values. |
| <a id="id_string"></a>`0x10` | id_string | `string (int32 offset)` | I | Id string text. Observed in the stock rows: 53 distinct values, 2 empty. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 10, 4 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4, 5 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1000, 2 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1049, 51 distinct values. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 6, 2 distinct values. |
| <a id="quantity_string"></a>`0x2C` | quantity_string | `string (int32 offset)` | I | Quantity string text. Observed in the stock rows: 5 distinct values, 4 empty. |
| <a id="name"></a>`0x30` | name | `string (int32 offset)` | I | Name text. Observed in the stock rows: 52 distinct values, 3 empty. |
| <a id="description"></a>`0x34` | description | `string (int32 offset)` | I | Description text. Observed in the stock rows: 51 distinct values, 4 empty. |
| <a id="unk_38"></a>`0x38` | unk_38 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 857, 51 distinct values. |
| <a id="unk_3c"></a>`0x3C` | unk_3c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_3d"></a>`0x3D` | unk_3d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataTelemetryAchievement](../tables/NxdDataTelemetryAchievement.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

11 of 17 columns not decoded.
