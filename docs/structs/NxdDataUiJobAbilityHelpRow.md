# NxdDataUiJobAbilityHelpRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_job_ability_help table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | DLC gate bit set (0 everywhere). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Null everywhere. Observed in the stock rows: empty in every row. |
| <a id="text"></a>`0x8` | text | `string (int32 offset)` | V | Rich-text help page (Job Overview / Usable Equipment / Select Abilities) with <color>/<icon> tags. The equipment list is TEXT only: it does not drive the equip rules. Observed in the stock rows: 35 distinct values, 1 empty. |

## Referenced by

- Described by tables: [NxdDataUiJobAbilityHelp](../tables/NxdDataUiJobAbilityHelp.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
