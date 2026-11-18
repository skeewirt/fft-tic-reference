# NxdDataIconRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.icon table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | DLC gate bit set. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Null. Observed in the stock rows: empty in every row. |
| <a id="icon_file_path"></a>`0x8` | icon_file_path | `string (int32 offset)` | V | Path (or printf template) of the UI texture part under ui/ffto/icon/ (600 of 1400 rows have one). Observed in the stock rows: 594 distinct values, 800 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | 0 in every row. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataIcon](../tables/NxdDataIcon.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 4 columns not decoded.
