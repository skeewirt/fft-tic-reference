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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 4 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_30"></a>`0x30` | unk_30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_34"></a>`0x34` | unk_34 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_38"></a>`0x38` | unk_38 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_3c"></a>`0x3C` | unk_3c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_40"></a>`0x40` | unk_40 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_44"></a>`0x44` | unk_44 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_48"></a>`0x48` | unk_48 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_4c"></a>`0x4C` | unk_4c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_50"></a>`0x50` | unk_50 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_54"></a>`0x54` | unk_54 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_58"></a>`0x58` | unk_58 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_5c"></a>`0x5C` | unk_5c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_60"></a>`0x60` | unk_60 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_64"></a>`0x64` | unk_64 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_68"></a>`0x68` | unk_68 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_6c"></a>`0x6C` | unk_6c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_70"></a>`0x70` | unk_70 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_74"></a>`0x74` | unk_74 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_78"></a>`0x78` | unk_78 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_7c"></a>`0x7C` | unk_7c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_80"></a>`0x80` | unk_80 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_84"></a>`0x84` | unk_84 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_88"></a>`0x88` | unk_88 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_8c"></a>`0x8C` | unk_8c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_90"></a>`0x90` | unk_90 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_94"></a>`0x94` | unk_94 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_98"></a>`0x98` | unk_98 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_9c"></a>`0x9C` | unk_9c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_a0"></a>`0xA0` | unk_a0 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_a4"></a>`0xA4` | unk_a4 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_a8"></a>`0xA8` | unk_a8 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_ac"></a>`0xAC` | unk_ac | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_b0"></a>`0xB0` | unk_b0 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 80, 4 distinct values. |
| <a id="unk_b4"></a>`0xB4` | unk_b4 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_b8"></a>`0xB8` | unk_b8 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_bc"></a>`0xBC` | unk_bc | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_c0"></a>`0xC0` | unk_c0 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_c4"></a>`0xC4` | unk_c4 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_c8"></a>`0xC8` | unk_c8 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |
| <a id="unk_cc"></a>`0xCC` | unk_cc | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataBattleVoiceGroupRate](../tables/NxdDataBattleVoiceGroupRate.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

50 of 52 columns not decoded.
