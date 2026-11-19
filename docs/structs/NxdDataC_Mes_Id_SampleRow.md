# NxdDataC_Mes_Id_SampleRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.battle_message_text table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="text"></a>`0x4` | text | `string (int32 offset)` | V | Read in the code: The message text (strings at +4 / +8 / +0xC are offsets from +4). Observed in the stock rows: 1384 distinct values, 236 empty. |
| <a id="singular"></a>`0x8` | singular | `string (int32 offset)` | V | Read in the code: The singular form used by the text tags that count a noun (count 1); empty -> text is used. Observed in the stock rows: 7 distinct values, 1728 empty. |
| <a id="plural"></a>`0xC` | plural | `string (int32 offset)` | V | Read in the code: The plural form used by the counting text tags for counts of 2 or more. Observed in the stock rows: empty in every row. |
| <a id="unknown10"></a>`0x10` | unknown10 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown11"></a>`0x11` | unknown11 | `uint8` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unknown12"></a>`0x12` | unknown12 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown13"></a>`0x13` | unknown13 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="error_banner"></a>`0x14` | error_banner | `uint8` | V | Read in the code: When set, the battle message is shown as the timed red error banner (window state 'Error' with its 'timer', UI sound cue 0x6A) instead of the normal message box. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [C_Mes_Id_Sample](../tables/C_Mes_Id_Sample.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 4 of 9 columns not decoded.
