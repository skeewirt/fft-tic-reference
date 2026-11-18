# NxdDataAchievementArrayRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 28 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.achievement_groups table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="achievement_ids1"></a>`0x4` | achievement_ids1 | `int32[] {int32 offset; uint32 count}` | I | Achievement ids1 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 6 distinct values. |
| <a id="achievement_ids2"></a>`0xC` | achievement_ids2 | `struct[] {int32 offset; uint32 count}` | I | Achievement ids2 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 7 distinct values. |
| <a id="achievement_ids3"></a>`0x14` | achievement_ids3 | `int32[] {int32 offset; uint32 count}` | I | Achievement ids3 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataAchievementArray](../tables/NxdDataAchievementArray.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
