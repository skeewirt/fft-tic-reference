# BattleVoiceRequest

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The request a battle event hands to a voice controller: which ability, which phase, which units and what flags.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="ability"></a>`0x4` | ability | `int32` | V | Ability of the action. |
| <a id="phase"></a>`0x8` | phase | `int32` | V | Phase of the action: BattleVoice_SpeakAbilityPhase picks an entry of the Ability row's voice list by it (3 / 4 entries 0..1, 5 entry 0, 6 entry 1 or 2, 7 / 8 entry 0 or 1). |
| <a id="unit"></a>`0xC` | unit | `uint8` | V | The unit the line is about (0xFF = the speaker itself); used by the one-unit side test. |
| <a id="targets"></a>`0x18` | targets | `pointer range` | V | Target list (+24..+32) of the action; the side test runs over it. |
| <a id="amount"></a>`0x30` | amount | `int32` | V | Amount (+48): not used by the functions read. |
| <a id="swap_row_2"></a>`0x40` | swap_row_2 | `uint8` | V | When set, a replaceable line is swapped for BattleVoice row 2. |
| <a id="swap_row_3"></a>`0x41` | swap_row_3 | `uint8` | V | When set, a replaceable line is swapped for BattleVoice row 3 (checked before the +64 flag). |
| <a id="flag_66"></a>`0x42` | flag_66 | `uint8` | V | Read (+66); its use was not followed. |

## Behavior

- V: the code that builds the request was not found (the controllers are reached through virtual calls).

## Notes

Name is ours.

## Open questions

? who builds the request and what bytes +64, +65 and +66 record.
