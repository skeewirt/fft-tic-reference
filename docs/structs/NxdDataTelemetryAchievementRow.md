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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 50, 51 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 49, 51 distinct values. |
| <a id="id_text"></a>`0x10` | id_text | `string (int32 offset)` | M | Measured over every stock row: The id written as text. Observed in the stock rows: 53 distinct values, 2 empty. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 10, 4 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4, 5 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1000, 2 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1049, 51 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 6, 2 distinct values. |
| <a id="quantity_text"></a>`0x2C` | quantity_text | `string (int32 offset)` | M | Measured over every stock row: A quantity written as text. Observed in the stock rows: 5 distinct values, 4 empty. |
| <a id="name"></a>`0x30` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 52 distinct values, 3 empty. |
| <a id="description"></a>`0x34` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 51 distinct values, 4 empty. |
| <a id="unknown38"></a>`0x38` | unknown38 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 857, 51 distinct values. |
| <a id="unknown3c"></a>`0x3C` | unknown3c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown3d"></a>`0x3D` | unknown3d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataTelemetryAchievement](../tables/NxdDataTelemetryAchievement.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 13 of 17 columns not decoded.
