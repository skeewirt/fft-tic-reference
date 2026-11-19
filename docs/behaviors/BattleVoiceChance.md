# BattleVoiceChance

- **Kind:** observed behaviour
- **Scope:** engine (battle voices)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [BattleVoice_RollAndPlay](../functions/BattleVoice_RollAndPlay.md), [BattleVoiceGroupRate_Chance](../functions/BattleVoiceGroupRate_Chance.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Whether a line plays is a roll of the speaker group's percentage in the line's column; fast-forward silences voices.

## Behavior

- V: the chance is the dword at +8 + 4k of the BattleVoiceGroupRate row of the controller's group key, k the BattleVoice chance_column (below 50), capped at 100; the line plays when a roll below 100 is under it.
- V: nothing plays while the fast-forward mode is 1 or 2.
- M: the group rows 2..5 hold 80, 60, 60 and 30 percent with 100 in some columns; rows 0 and 1 are all 0.

## Open questions

None recorded.
