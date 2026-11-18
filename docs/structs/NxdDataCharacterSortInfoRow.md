# NxdDataCharacterSortInfoRow

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.character_sort_info table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int16` | ? | Not decoded. Observed in the stock rows: -1 to 22, 14 distinct values. |
| <a id="unk_06"></a>`0x6` | unk_06 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_07"></a>`0x7` | unk_07 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataCharacterSortInfo](../tables/NxdDataCharacterSortInfo.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

3 of 4 columns not decoded.
