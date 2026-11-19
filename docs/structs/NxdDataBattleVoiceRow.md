# NxdDataBattleVoiceRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 44 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.battle_voice table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="cue"></a>`0x8` | cue | `int32` | V | Read in the code: The cue number played from the speaker's voice bank (the VoicePattern +8 .sab file loaded into the controller). Observed in the stock rows: -1 to 14800, 53 distinct values. |
| <a id="chance_column"></a>`0xC` | chance_column | `int32` | V | Read in the code: Which column of the speaker's BattleVoiceGroupRate row (0..49) gives the line's play chance. Observed in the stock rows: 0 to 49, 50 distinct values. |
| <a id="battle_voice"></a>`0x10` | battle_voice | `int32` | V | Read in the code: A BattleVoice row (table 183) spoken instead when the speaker's voice pattern has its flag set (VoicePattern +0x14). Observed in the stock rows: 0 to 27, 5 distinct values. |
| <a id="battle_voice_2"></a>`0x14` | battle_voice_2 | `int32` | V | Read in the code: A BattleVoice row spoken instead when the speaker uses one of the two shared voice patterns 100 / 101. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="battle_voice_3"></a>`0x18` | battle_voice_3 | `int32` | V | Read in the code: A BattleVoice row spoken instead when the speaker's voice pattern is 63. Observed in the stock rows: 0 to 17, 5 distinct values. |
| <a id="delay"></a>`0x1C` | delay | `float32` | V | Read in the code: A delay before the line is spoken: above ~0 the cue is queued and played when the delay has run out. Observed in the stock rows: 0 to 1.5, 2 distinct values. |
| <a id="side"></a>`0x20` | side | `int32` | V | Read in the code: Which side the line is about: 0 any, 1 the other side, 2 the speaker's own side (tested on the targets, or on one unit with side_test_one_unit). Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="side_test_on_unit"></a>`0x28` | side_test_on_unit | `uint8` | V | Read in the code: When set, the line's side condition (+0x20: 1 = other side, 2 = same side) is tested on one unit, the voice request's unit (request +12; the speaker itself when 0xFF), instead of on every target of the action; the line is never spoken when that unit is the speaker itself. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="replaceable"></a>`0x29` | replaceable | `uint8` | V | Read in the code: When set, the line is swapped before it is spoken: the request's byte +65 set -> BattleVoice row 3 is spoken instead, byte +64 set -> row 2; otherwise the line itself (each after the suppress test). Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataBattleVoice](../tables/NxdDataBattleVoice.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
