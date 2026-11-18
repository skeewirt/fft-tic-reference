# NxdDataBGMModeRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.bgm_mode table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="tab_index"></a>`0x8` | tab_index | `int32` | I | Tab index (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 97 distinct values, 0 empty. |
| <a id="title"></a>`0x10` | title | `string (int32 offset)` | I | Title text. Observed in the stock rows: 97 distinct values, 0 empty. |
| <a id="sound_enhanced_id"></a>`0x14` | sound_enhanced_id | `int32` | I | Row id of SoundEnhanced (a reference by column name). Observed in the stock rows: 150 to 246, 97 distinct values. |

## Referenced by

- Described by tables: [NxdDataBGMMode](../tables/NxdDataBGMMode.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 6 columns not decoded.
