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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int16` | ? | Not decoded. Observed in the stock rows: 1 to 39, 17 distinct values. |
| <a id="unknown06"></a>`0x6` | unknown06 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="chara_control_id"></a>`0x8` | chara_control_id | `int16` | M | Measured over every stock row: Every value is a key of nxd.CharaControlId. Observed in the stock rows: 0 to 1006, 56 distinct values. |
| <a id="unknown0a"></a>`0xA` | unknown0a | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int16` | ? | Not decoded. Observed in the stock rows: 0 to 509, 22 distinct values. |
| <a id="unknown0e"></a>`0xE` | unknown0e | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int16` | ? | Not decoded. Observed in the stock rows: 0 to 886, 390 distinct values. |
| <a id="unknown12"></a>`0x12` | unknown12 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 65 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown1e"></a>`0x1E` | unknown1e | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int16` | ? | Not decoded. Observed in the stock rows: 0 to 14, 4 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |

## Referenced by

- Described by tables: [NxdDataEnhancedBattleEvent](../tables/NxdDataEnhancedBattleEvent.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 13 of 14 columns not decoded.
