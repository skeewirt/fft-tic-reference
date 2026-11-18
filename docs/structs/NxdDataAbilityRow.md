# NxdDataAbilityRow

- **Kind:** structure
- **Area:** [Ability data](../areas/ability-data.md)
- **Size:** 68 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ability table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | DLC gate bit set (0 everywhere). Observed in the stock rows: 0 in every row. |
| <a id="icon_id"></a>`0x4` | icon_id | `int32` | V | Index into ability/textureparts/a_%03d_uitx (Icon row 11). Observed in the stock rows: 0 to 54, 27 distinct values. |
| <a id="name"></a>`0x8` | name | `string (int32 offset)` | V | Ability name. Observed in the stock rows: 474 distinct values, 21 empty. |
| <a id="description"></a>`0xC` | description | `string (int32 offset)` | I | Ability description. Observed in the stock rows: 480 distinct values, 7 empty. |
| <a id="unk_10"></a>`0x10` | unk_10 | `string (int32 offset)` | I | Extra text slot (null in every row). Observed in the stock rows: empty in every row. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int16` | ? | 0 in every row. Observed in the stock rows: 0 in every row. |
| <a id="unk_16"></a>`0x16` | unk_16 | `uint8` | ? | 0 in every row. Observed in the stock rows: 0 in every row. |
| <a id="unk_17"></a>`0x17` | unk_17 | `uint8` | ? | 1 in every row. Observed in the stock rows: 1 in every row. |
| <a id="unk_18"></a>`0x18` | unk_18 | `uint8` | ? | 0 in every row. Observed in the stock rows: 0 in every row. |
| <a id="unk_19"></a>`0x19` | unk_19 | `uint8` | ? | 0 in every row. Observed in the stock rows: 0 in every row. |
| <a id="unk_1a"></a>`0x1A` | unk_1a | `int16` | ? | 0 in every row. Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x1C` | comment | `string (int32 offset)` | I | Null/designer text. Observed in the stock rows: empty in every row. |
| <a id="ui_id"></a>`0x20` | ui_id | `int32` | V | UIText key (1041, 1042 in two rows); passed to UIText_Get as the ability's description override. Observed in the stock rows: 0 to 1042, 3 distinct values. |
| <a id="battle_voice_ids"></a>`0x24` | battle_voice_ids | `int32[] {int32 offset; uint32 count}` | I | BattleVoice rows played when the ability is used (values 1..52). Observed in the stock rows: 40 distinct values. |
| <a id="ui_id2"></a>`0x2C` | ui_id2 | `int32` | V | UIText key (800/801/802/809/812) for a second description line. Observed in the stock rows: 0 to 812, 6 distinct values. |
| <a id="unk_30"></a>`0x30` | unk_30 | `int32` | V | 0 except one row (2). Read as 'Good'/'Bad' marker (== 2 -> 'Good'). Observed in the stock rows: 0 to 2, 2 distinct values. |
| <a id="unk_34"></a>`0x34` | unk_34 | `int32` | ? | Mostly 0; ten rows 3110..3210 (a text/sound id). Observed in the stock rows: 0 to 3210, 81 distinct values. |
| <a id="ability_reaction_voice_type_id"></a>`0x38` | ability_reaction_voice_type_id | `int32` | I | Reaction voice type (0, 2, 3). Observed in the stock rows: 0 to 3, 3 distinct values. |
| <a id="unk_3c"></a>`0x3C` | unk_3c | `int32` | V | 0 or 1 (15 rows). Compared against 1 and 2 by the UI. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="jp_cost1"></a>`0x40` | jp_cost1 | `uint8` | V | Low byte of the ability's JP cost. Observed in the stock rows: 0 to 250, 38 distinct values. |
| <a id="jp_cost2"></a>`0x41` | jp_cost2 | `uint8` | V | High byte of the JP cost. Observed in the stock rows: 0 to 39, 9 distinct values. |
| <a id="is_random_damage"></a>`0x42` | is_random_damage | `uint8` | I | 1 for six abilities (random damage). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="is_random_status"></a>`0x43` | is_random_status | `uint8` | V | 1 for five abilities (random status). Byte at +67 is returned by sub_1401086B4. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [Ability](../tables/Ability.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

7 of 23 columns not decoded.
