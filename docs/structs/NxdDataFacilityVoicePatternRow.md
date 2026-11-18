# NxdDataFacilityVoicePatternRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.facility_voice_pattern table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="facility_sound_file_path"></a>`0x8` | facility_sound_file_path | `string (int32 offset)` | I | File path string. Observed in the stock rows: 7 distinct values, 1 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `struct[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 7 distinct values. |

## Referenced by

- Described by tables: [NxdDataFacilityVoicePattern](../tables/NxdDataFacilityVoicePattern.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 4 columns not decoded.
