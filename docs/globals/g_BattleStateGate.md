# g_BattleStateGate

- **Kind:** global
- **Address:** `0x14186AF9C`
- **Area:** [Battle](../areas/battle.md)
- **Type:** `uint32`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle state word that suspends the reaction helper while it is non-zero.

## Behavior

- V: sub_14030AFEC returns immediately when it is set.
- V: it is set to 1 around a reaction or secondary action (BattleAction_BuildReaction, Battle_ActorResultLevels, Battle_ExecuteSecondaryAction) and read by Battle_ScaleByDifficulty, which picks the command 21 percentages only while it is 0.
- V: it is a different dword from g_BattleContextGate (IDA g_BattleSimulating) at 0x14186AF80.

## Referenced by

- Observed behaviours: [PlayModeDamagePercent](../behaviors/PlayModeDamagePercent.md)
- Read by: [sub_14030AFEC](../functions/sub_14030AFEC.md)

## Open questions

None recorded.
