# NxdDataGameProgressRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.game_progress table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="world_map_progress_info_id_k1"></a>`0x8` | world_map_progress_info_id_k1 | `int32` | I | World map progress info id k1 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 1000, 3 distinct values. |
| <a id="world_map_progress_info_id_k2"></a>`0xC` | world_map_progress_info_id_k2 | `int32` | I | World map progress info id k2 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 270, 50 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 430, 42 distinct values. |

## Referenced by

- Described by tables: [NxdDataGameProgress](../tables/NxdDataGameProgress.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 5 columns not decoded.
