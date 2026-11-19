# NxdDataUIPadDefineRow

- **Kind:** structure
- **Area:** [Input](../areas/input.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_pad_define table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="glyph"></a>`0x4` | glyph | `int32` | V | Read in the code: The glyph (icon number) drawn for the pad button whose id is the row key. Observed in the stock rows: 0 to 99999, 19 distinct values. |
| <a id="glyph_2"></a>`0x8` | glyph_2 | `int32` | V | Read in the code: A second glyph for a button chord: when non-zero, a separator ('+', sub_1400F3940) and this glyph follow icon. Observed in the stock rows: 0 to 66, 3 distinct values. |
| <a id="glyph_alt"></a>`0xC` | glyph_alt | `int32` | V | Read in the code: Replaces icon when the caller asks for the alternate glyph (sub_1400F2648 asks for it for action 57) and this column is non-zero. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataUIPadDefine](../tables/NxdDataUIPadDefine.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
