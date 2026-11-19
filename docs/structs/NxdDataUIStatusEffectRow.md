# NxdDataUIStatusEffectRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 36 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_status_effect table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="ui_status_effect_category"></a>`0x8` | ui_status_effect_category | `int32` | V | Read in the code: The UIStatusEffectCategory row under which this status is listed in the equipment detail lists (0 = none). The code filters by it for Permanent (1) and Applies (3); values 12 (Initial Effect) and 13 (Special Effect) rest on the rows only. Observed in the stock rows: 0 to 13, 5 distinct values. |
| <a id="name"></a>`0xC` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 42 distinct values, 4 empty. |
| <a id="caption"></a>`0x10` | caption | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 36 distinct values, 10 empty. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 66, 31 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 23, 3 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int16` | ? | Not decoded. Observed in the stock rows: -1 to 1004, 43 distinct values. |
| <a id="unknown22"></a>`0x22` | unknown22 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIStatusEffect](../tables/NxdDataUIStatusEffect.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 7 of 10 columns not decoded.
