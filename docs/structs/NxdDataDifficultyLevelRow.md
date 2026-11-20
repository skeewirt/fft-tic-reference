# NxdDataDifficultyLevelRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 28 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.difficulty_level table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="damage_to_enemies"></a>`0x8` | damage_to_enemies | `int32` | V | Read in the code: Percentage applied to the HP and MP damage of a resolved action when the target's side bits (unit byte +494 & 0x30) are non-zero, i.e. the target is not on the player's side (enemies; guests count as the player's side). Observed in the stock rows: 70 to 110, 3 distinct values. |
| <a id="damage_to_party"></a>`0xC` | damage_to_party | `int32` | V | Read in the code: The same percentage for a target whose side bits (+494 & 0x30) are zero, the player's side. Observed in the stock rows: 50 to 120, 3 distinct values. |
| <a id="damage_to_enemies_command_21"></a>`0x10` | damage_to_enemies_command_21 | `int32` | V | Read in the code: Replaces +0x8 for the same test when the request's command byte (g_FormulaBlock +6 = byte +1 of the action request) is 21 and g_BattleStateGate (0x14186AF9C) is 0 (I: the gate is set to 1 by BattleAction_BuildReaction and Battle_ActorResultLevels and saved / restored by Battle_ExecuteSecondaryAction and BattleAction_ReleaseCharged, so 0 means a primary action). Observed in the stock rows: 35 to 110, 3 distinct values. |
| <a id="damage_to_party_command_21"></a>`0x14` | damage_to_party_command_21 | `int32` | V | Read in the code: Replaces +0xC for the player's side targets when command 21 is acted outside a forecast. Observed in the stock rows: 50 to 120, 3 distinct values. |
| <a id="ui_text"></a>`0x18` | ui_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 3547 to 3549, 3 distinct values. |

## Referenced by

- Described by tables: [NxdDataDifficultyLevel](../tables/NxdDataDifficultyLevel.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
