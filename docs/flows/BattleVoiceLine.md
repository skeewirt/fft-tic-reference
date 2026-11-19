# BattleVoiceLine

- **Kind:** flow
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How a battle event becomes a spoken voice cue: suppress test, status gate, chance roll, replacement, play or queue.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="1"></a>1 | [BattleVoice_SpeakAbilityPhase](../functions/BattleVoice_SpeakAbilityPhase.md) | V | An ability line is chosen from the Ability row's voice list by the request phase. |
| <a id="2"></a>2 | [BattleVoice_SpeakSwapped](../functions/BattleVoice_SpeakSwapped.md) | V | A replaceable line is swapped for row 3 or 2 by the request flags. |
| <a id="3"></a>3 | [BattleVoice_IsSuppressed](../functions/BattleVoice_IsSuppressed.md) | V | Side test: a non-zero result stops the line. |
| <a id="4"></a>4 | [BattleVoice_Speak](../functions/BattleVoice_Speak.md) | V | Status gate: statuses that forbid speech stop the line (line 21 always passes). |
| <a id="5"></a>5 | [BattleVoice_RollAndPlay](../functions/BattleVoice_RollAndPlay.md) | V | Skipped while fast-forward runs; rolls the group chance. |
| <a id="6"></a>6 | [BattleVoiceGroupRate_Chance](../functions/BattleVoiceGroupRate_Chance.md) | V | Chance in percent of the line's column in the speaker's group row. |
| <a id="7"></a>7 | [BattleVoice_ResolveLine](../functions/BattleVoice_ResolveLine.md) | V | Cue number, with the three replacement rows. |
| <a id="8"></a>8 | [BattleVoice_TickQueue](../functions/BattleVoice_TickQueue.md) | V | A delayed cue is queued and played when its delay has run out. |

## Notes

The pattern of each controller is set by BattleVoice_AssignPatterns and BattleVoice_SetPattern when a unit is built.

## Open questions

? who builds the request.
