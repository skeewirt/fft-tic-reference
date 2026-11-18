# NxdDataBGMTransitionRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.bgm_transition table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="sound_enhanced_id"></a>`0x8` | sound_enhanced_id | `int32` | I | Row id of SoundEnhanced (a reference by column name). Observed in the stock rows: 0 to 239, 10 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `float32` | ? | Not decoded. Observed in the stock rows: 0.5 to 1.5, 2 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `float32` | ? | Not decoded. Observed in the stock rows: 0.5 in every row. |

## Referenced by

- Described by tables: [NxdDataBGMTransition](../tables/NxdDataBGMTransition.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

2 of 5 columns not decoded.
