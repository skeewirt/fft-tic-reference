# BattleVoiceController

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 136 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One battle voice controller (ffto CharacterBattleVoiceController, vtable 0x140713F68): the voice pattern of a unit or of a shared group, the flags that pick replacement lines and the queue of delayed cues. The controllers sit in BattleControl at +689112 + 136 * slot.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="pattern_flags"></a>`0x8` | pattern_flags | `uint32` | V | Bit 0 = the pattern row's flag byte (VoicePattern +0x14: use BattleVoice battle_voice); bit 1 set for patterns 100 and 101 (use battle_voice_2). Set by BattleVoice_SetPattern. | [BattleVoice_SetPattern](../functions/BattleVoice_SetPattern.md) |  |
| <a id="pattern_id"></a>`0xC` | pattern_id | `int32` | V | The voice pattern id (63 selects battle_voice_3). Set by BattleVoice_SetPattern. | [BattleVoice_SetPattern](../functions/BattleVoice_SetPattern.md) |  |
| <a id="group_key"></a>`0x10` | group_key | `int32` | V | Key of the BattleVoiceGroupRate row (VoicePattern +0xC). | [BattleVoice_SetPattern](../functions/BattleVoice_SetPattern.md) | [BattleVoice_RollAndPlay](../functions/BattleVoice_RollAndPlay.md) |
| <a id="voice_bank"></a>`0x18` | voice_bank | `pointer` | V | The voice bank resource opened from the pattern row's path (VoicePattern +8). | [BattleVoice_SetPattern](../functions/BattleVoice_SetPattern.md) |  |
| <a id="cue_queue"></a>`0x20` | cue_queue | `deque` | V | Queued (cue, delay) pairs (+32..+72): pushed by BattleVoice_RollAndPlay, counted down by BattleVoice_TickQueue. | [BattleVoice_RollAndPlay](../functions/BattleVoice_RollAndPlay.md), [BattleVoice_TickQueue](../functions/BattleVoice_TickQueue.md) |  |
| <a id="speaker"></a>`0x50` | speaker | `pointer` | V | Reference to the speaking unit: its record is read at +8 for the side test (BattleVoice_IsSuppressed). |  |  |

## Behavior

- V: reached only through virtual calls: slot 3 BattleVoice_Speak, slot 5 BattleVoice_IsSuppressed, slot 7 a choice by phase.

## Notes

Name is ours.

## Open questions

? the rest of the 136 bytes.
