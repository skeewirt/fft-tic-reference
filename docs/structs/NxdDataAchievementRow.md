# NxdDataAchievementRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 28 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.achievement table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="telemetry_achievement_id"></a>`0x4` | telemetry_achievement_id | `int32` | I | Row id of TelemetryAchievement-en (a reference by column name). Observed in the stock rows: 0 to 1049, 51 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2040, 8 distinct values. |
| <a id="novel_related"></a>`0x10` | novel_related | `int32` | I | Novel related (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 4, 2 distinct values. |
| <a id="journal_related"></a>`0x14` | journal_related | `int32` | I | Journal related (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 159, 2 distinct values. |
| <a id="description"></a>`0x18` | description | `string (int32 offset)` | I | Description text. Observed in the stock rows: 51 distinct values, 1 empty. |

## Referenced by

- Described by tables: [NxdDataAchievement](../tables/NxdDataAchievement.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

2 of 7 columns not decoded.
