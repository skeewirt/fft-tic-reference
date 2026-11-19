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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="path"></a>`0x8` | path | `string (int32 offset)` | M | Measured over every stock row: File paths. Observed in the stock rows: 594 distinct values, 800 empty. |
| <a id="frame"></a>`0xC` | frame | `int32` | V | Read in the code: The frame (part number) of the icon's texture that is drawn. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataIcon](../tables/NxdDataIcon.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
