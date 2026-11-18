# NxdDataGossipRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.gossip table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 2 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 90, 3 distinct values. |
| <a id="title"></a>`0xC` | title | `string (int32 offset)` | I | Title text. Observed in the stock rows: 23 distinct values, 0 empty. |
| <a id="text"></a>`0x10` | text | `string (int32 offset)` | I | Text text. Observed in the stock rows: 23 distinct values, 0 empty. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 3 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 3 distinct values. |
| <a id="user_situation_id"></a>`0x24` | user_situation_id | `int32` | I | Row id of UserSituation, a story-progress condition. Observed in the stock rows: 0 to 3510, 4 distinct values. |
| <a id="icon_id"></a>`0x28` | icon_id | `int32` | I | Row id of Icon (a reference by column name). Observed in the stock rows: 0 to 26, 3 distinct values. |
| <a id="flag_2c"></a>`0x2C` | flag_2c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataGossip](../tables/NxdDataGossip.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

5 of 10 columns not decoded.
