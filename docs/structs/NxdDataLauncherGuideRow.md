# NxdDataLauncherGuideRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.launcher_guide table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_04"></a>`0x4` | unk_04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1006, 7 distinct values. |
| <a id="caption"></a>`0x8` | caption | `string (int32 offset)` | I | Caption text. Observed in the stock rows: 13 distinct values, 10 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_0d"></a>`0xD` | flag_0d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataLauncherGuide](../tables/NxdDataLauncherGuide.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

3 of 5 columns not decoded.
