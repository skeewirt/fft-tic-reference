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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="world_map_progress_info"></a>`0x8` | world_map_progress_info | `int32` | V | Read in the code: First key of a WorldMapProgressInfo (nxd 123) row: the world-map progress entry that applies at this counter value. Observed in the stock rows: 0 to 1000, 3 distinct values. |
| <a id="world_map_progress_info_2"></a>`0xC` | world_map_progress_info_2 | `int32` | V | Read in the code: Second key of the WorldMapProgressInfo (nxd 123) row named by world_map_progress_info. Observed in the stock rows: 0 to 270, 50 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 430, 42 distinct values. |

## Referenced by

- Described by tables: [NxdDataGameProgress](../tables/NxdDataGameProgress.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 3 of 5 columns not decoded.
