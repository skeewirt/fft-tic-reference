# BattleVoiceSuppressReason

- **Kind:** registry
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The result of BattleVoice_IsSuppressed: 0 speak, or the reason a line is not spoken.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="speak"></a>0 | `speak` | `0` | V | The line is spoken. |
| <a id="speaker_is_unit"></a>3 | `speaker_is_unit` | `3` | V | The one-unit side test names the speaker itself. |
| <a id="not_all_other_side"></a>4 | `not_all_other_side` | `4` | V | A target is not on the other side (side 1 lines). |
| <a id="not_all_same_side"></a>5 | `not_all_same_side` | `5` | V | A target is not on the speaker's side (side 2 lines). |
| <a id="reason_1"></a>1 | `reason_1` | `1` | ? | Returned by the function; the condition was not noted. |
| <a id="reason_2"></a>2 | `reason_2` | `2` | ? | Returned by the function; the condition was not noted. |

## Behavior

- V: a non-zero result stops the line.

## Notes

Reasons 1..5 are the range the function returns.

## Open questions

? reasons 1 and 2.
