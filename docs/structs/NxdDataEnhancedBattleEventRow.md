# NxdDataEnhancedBattleEventRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.enhanced_battle_event table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="unk_type4"></a>`0x4` | unk_type4 | `int16` | I | Unk type4 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 1 to 39, 17 distinct values. |
| <a id="unk_06"></a>`0x6` | unk_06 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="chara_control_id"></a>`0x8` | chara_control_id | `int16` | I | Chara control id (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 1006, 56 distinct values. |
| <a id="unk_0a"></a>`0xA` | unk_0a | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int16` | ? | Not decoded. Observed in the stock rows: 0 to 509, 22 distinct values. |
| <a id="unk_0e"></a>`0xE` | unk_0e | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int16` | ? | Not decoded. Observed in the stock rows: 0 to 886, 390 distinct values. |
| <a id="unk_12"></a>`0x12` | unk_12 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 65 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_1e"></a>`0x1E` | unk_1e | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int16` | ? | Not decoded. Observed in the stock rows: 0 to 14, 4 distinct values. |
| <a id="comment"></a>`0x24` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |

## Referenced by

- Described by tables: [NxdDataEnhancedBattleEvent](../tables/NxdDataEnhancedBattleEvent.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

10 of 14 columns not decoded.
