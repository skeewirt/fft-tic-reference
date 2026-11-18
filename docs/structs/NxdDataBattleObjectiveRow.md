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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="name"></a>`0x4` | name | `string (int32 offset)` | I | Name text. Observed in the stock rows: 33 distinct values, 35 empty. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="is_protection_mission"></a>`0xC` | is_protection_mission | `uint8` | I | Is protection mission (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataBattleObjective](../tables/NxdDataBattleObjective.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 4 columns not decoded.
