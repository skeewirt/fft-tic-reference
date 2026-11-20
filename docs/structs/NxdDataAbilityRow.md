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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="icon"></a>`0x4` | icon | `int32` | V | Index into ability/textureparts/a_%03d_uitx (Icon row 11). Observed in the stock rows: 0 to 54, 27 distinct values. |
| <a id="name"></a>`0x8` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 474 distinct values, 21 empty. |
| <a id="description"></a>`0xC` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 480 distinct values, 7 empty. |
| <a id="plural"></a>`0x10` | plural | `string (int32 offset)` | V | Read in the code: The plural form of the ability name in counted-noun text tags of category 'Ability' (used for a count of 2 or more). Observed in the stock rows: empty in every row. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int16` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="noun_class"></a>`0x16` | noun_class | `uint8` | V | Read in the code: Per-language noun class byte of the 'Ability' text tag record (tag record +24). Copied unchanged into the tag record and read only by the counted-noun tag builders. Observed in the stock rows: 0 in every row. |
| <a id="noun_number_form"></a>`0x17` | noun_number_form | `uint8` | V | Read in the code: Per-language noun number-form byte (tag record +25). Copied unchanged into the tag record and read only by the counted-noun tag builders. Observed in the stock rows: 1 in every row. |
| <a id="noun_class_2"></a>`0x18` | noun_class_2 | `uint8` | V | Read in the code: Second per-language noun class byte (tag record +26). Copied unchanged into the tag record and read only by the counted-noun tag builders. Observed in the stock rows: 0 in every row. |
| <a id="noun_prefix_flag"></a>`0x19` | noun_prefix_flag | `uint8` | V | Read in the code: Per-language prefix switch byte (tag record +27). Copied unchanged into the tag record and read only by the counted-noun tag builders. Observed in the stock rows: 0 in every row. |
| <a id="unknown1a"></a>`0x1A` | unknown1a | `int16` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="ui_text"></a>`0x20` | ui_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 0 to 1042, 3 distinct values. |
| <a id="battle_voices"></a>`0x24` | battle_voices | `int32[] {int32 offset; uint32 count}` | M | Measured over every stock row: Every value is a key of nxd.BattleVoice. Observed in the stock rows: 40 distinct values. |
| <a id="ui_text_2"></a>`0x2C` | ui_text_2 | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 0 to 812, 6 distinct values. |
| <a id="drawback"></a>`0x30` | drawback | `int32` | V | Read in the code: A value of 2 marks an innate ability as a drawback: the job detail window plays the 'Bad' state on its slot instead of 'Good'. Observed in the stock rows: 0 to 2, 2 distinct values. |
| <a id="sort_order"></a>`0x34` | sort_order | `int32` | V | Read in the code: The key by which abilities are sorted in the job-screen ability pages (ascending; 0 or a missing row counts as 999999, ties by ability id). Observed in the stock rows: 0 to 3210, 81 distinct values. |
| <a id="ability_reaction_voice_type"></a>`0x38` | ability_reaction_voice_type | `int32` | V | Read in the code: Key of AbilityReactionVoiceType (nxd 330): a row of 11 rule values; a yes/no question about the unit picks one of them (0 = yes, 1 = no, 2/3 = a test of the unit, 4 = yes once per unit, other = yes). Observed in the stock rows: 0 to 3, 3 distinct values. |
| <a id="shows_unknown_info"></a>`0x3C` | shows_unknown_info | `int32` | V | Read in the code: 1 or 2 makes the battle command list cursor play the 'ShowUnknown' state (otherwise 'HideUnknown') on its info node. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="jp_cost_low"></a>`0x40` | jp_cost_low | `uint8` | V | Low byte of the ability's JP cost. Observed in the stock rows: 0 to 250, 38 distinct values. |
| <a id="jp_cost_high"></a>`0x41` | jp_cost_high | `uint8` | V | High byte of the JP cost. Observed in the stock rows: 0 to 39, 9 distinct values. |
| <a id="random_icon"></a>`0x42` | random_icon | `uint8` | V | Read in the code: Non-zero shows the 'random' icon (GUI node IconRandom) next to the damage number in the battle action panel when this ability is the action shown. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="random_status"></a>`0x43` | random_status | `uint8` | V | 1 for five abilities (random status). Byte at +67 is returned by sub_1401086B4. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [Ability](../tables/Ability.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
