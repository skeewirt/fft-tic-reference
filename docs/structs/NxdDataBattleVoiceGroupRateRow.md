# NxdDataBattleVoiceGroupRateRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 208 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.battle_voice_group_rate table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="chance_0"></a>`0x8` | chance_0 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 0, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_1"></a>`0xC` | chance_1 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 1, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_2"></a>`0x10` | chance_2 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 2, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 4 distinct values. |
| <a id="chance_3"></a>`0x14` | chance_3 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 3, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_4"></a>`0x18` | chance_4 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 4, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_5"></a>`0x1C` | chance_5 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 5, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_6"></a>`0x20` | chance_6 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 6, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_7"></a>`0x24` | chance_7 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 7, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_8"></a>`0x28` | chance_8 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 8, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_9"></a>`0x2C` | chance_9 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 9, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_10"></a>`0x30` | chance_10 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 10, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_11"></a>`0x34` | chance_11 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 11, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_12"></a>`0x38` | chance_12 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 12, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_13"></a>`0x3C` | chance_13 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 13, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_14"></a>`0x40` | chance_14 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 14, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_15"></a>`0x44` | chance_15 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 15, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_16"></a>`0x48` | chance_16 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 16, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_17"></a>`0x4C` | chance_17 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 17, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_18"></a>`0x50` | chance_18 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 18, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_19"></a>`0x54` | chance_19 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 19, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_20"></a>`0x58` | chance_20 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 20, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_21"></a>`0x5C` | chance_21 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 21, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_22"></a>`0x60` | chance_22 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 22, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_23"></a>`0x64` | chance_23 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 23, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_24"></a>`0x68` | chance_24 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 24, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_25"></a>`0x6C` | chance_25 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 25, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_26"></a>`0x70` | chance_26 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 26, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_27"></a>`0x74` | chance_27 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 27, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_28"></a>`0x78` | chance_28 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 28, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_29"></a>`0x7C` | chance_29 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 29, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_30"></a>`0x80` | chance_30 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 30, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_31"></a>`0x84` | chance_31 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 31, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_32"></a>`0x88` | chance_32 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 32, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_33"></a>`0x8C` | chance_33 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 33, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_34"></a>`0x90` | chance_34 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 34, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_35"></a>`0x94` | chance_35 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 35, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_36"></a>`0x98` | chance_36 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 36, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_37"></a>`0x9C` | chance_37 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 37, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_38"></a>`0xA0` | chance_38 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 38, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_39"></a>`0xA4` | chance_39 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 39, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_40"></a>`0xA8` | chance_40 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 40, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_41"></a>`0xAC` | chance_41 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 41, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_42"></a>`0xB0` | chance_42 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 42, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="chance_43"></a>`0xB4` | chance_43 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 43, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_44"></a>`0xB8` | chance_44 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 44, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_45"></a>`0xBC` | chance_45 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 45, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_46"></a>`0xC0` | chance_46 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 46, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_47"></a>`0xC4` | chance_47 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 47, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_48"></a>`0xC8` | chance_48 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 48, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="chance_49"></a>`0xCC` | chance_49 | `int32` | V | Read in the code: The play chance in percent (capped at 100) of the BattleVoice lines whose chance_column is 49, for speakers whose VoicePattern +0xC is this row. Observed in the stock rows: 0 to 100, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataBattleVoiceGroupRate](../tables/NxdDataBattleVoiceGroupRate.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
