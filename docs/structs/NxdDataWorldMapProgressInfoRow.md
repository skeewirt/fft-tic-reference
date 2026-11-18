# NxdDataWorldMapProgressInfoRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 44 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.world_map_progress_info table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="town_id1"></a>`0x8` | town_id1 | `int32` | I | Row id of Town-en (a reference by column name). Observed in the stock rows: 0 to 47, 22 distinct values. |
| <a id="town_id2"></a>`0xC` | town_id2 | `int32` | I | Row id of Town-en (a reference by column name). Observed in the stock rows: 7 to 47, 23 distinct values. |
| <a id="route_ids"></a>`0x10` | route_ids | `int32[] {int32 offset; uint32 count}` | I | Route ids (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 25 distinct values. |
| <a id="caption"></a>`0x18` | caption | `string (int32 offset)` | I | Caption text. Observed in the stock rows: 54 distinct values, 36 empty. |
| <a id="user_situation_id1"></a>`0x1C` | user_situation_id1 | `int32` | I | Row id of UserSituation (a reference by column name). Observed in the stock rows: 0 to 3230, 4 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 2782, 13 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 1643, 13 distinct values. |
| <a id="unk_28"></a>`0x28` | unk_28 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_29"></a>`0x29` | flag_29 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataWorldMapProgressInfo](../tables/NxdDataWorldMapProgressInfo.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

4 of 11 columns not decoded.
