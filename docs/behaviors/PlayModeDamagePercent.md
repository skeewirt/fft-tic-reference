# PlayModeDamagePercent

- **Kind:** observed behaviour
- **Scope:** engine (play mode)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_ScaleByDifficulty](../functions/Battle_ScaleByDifficulty.md), [SaveLoadList_FillItem](../functions/SaveLoadList_FillItem.md), [g_BattleStateGate](../globals/g_BattleStateGate.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The play mode (configuration byte +196) is the key of a DifficultyLevel row; the row's four percentages scale the HP and MP damage of every resolved action, one pair for each side of the target and a second pair for command 21.

## Behavior

- V: Battle_ScaleByDifficulty takes the row whose key is the play mode; +0x8 (damage_to_enemies) applies to a target whose side bits (unit byte +494 & 0x30) are non-zero, +0xC (damage_to_party) to a target whose side bits are 0.
- V: when the action request's command byte is 21 and g_BattleStateGate is 0, +0x10 (damage_to_enemies_command_21) and +0x14 (damage_to_party_command_21) replace the two percentages.
- V: g_BattleStateGate (0x14186AF9C) is a different dword from g_BattleSimulating (0x14186AF80): the first is set to 1 around a reaction or secondary action (BattleAction_BuildReaction, Battle_ActorResultLevels), the second marks a forecast.
- V: each output is percentage x damage / 100 (unsigned), capped at 999; with the Enhanced flag clear only the cap applies.
- V: the only other reader of the table is SaveLoadList_FillItem, which shows the row's +0x18 (ui_text) as the play mode's name in a save slot.

## Open questions

? which command id 21 stands for in play.
