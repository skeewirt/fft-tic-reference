# NxdDataBattleObjectiveRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.battle_objective table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="name"></a>`0x4` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 33 distinct values, 35 empty. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="show_targets"></a>`0xC` | show_targets | `uint8` | V | Read in the code: Non-zero: while this is the battle objective, units whose spawn flag bit 0x04 is set (OverrideEntryData flag_2) get the target marker (ShowTarget, turn-panel tag, formation marker). Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataBattleObjective](../tables/NxdDataBattleObjective.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 4 columns not decoded.
