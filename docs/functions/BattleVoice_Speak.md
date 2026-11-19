# BattleVoice_Speak

- **Address:** `0x1401ED3A0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleVoice_Speak(void *controller, void *request, int line)`
- **Callers:** none (virtual call)
- **Callees:** sub_1401EC958

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Speaks a line unless the speaker's statuses forbid it (controller virtual, slot 3).

## Behavior

- V: skips when the speaker's status bytes (unit +97..+101 bits) forbid speech; line 21 always passes.
- V: otherwise calls BattleVoice_RollAndPlay.

## Referenced by

- Appears in flows: [BattleVoiceLine](../flows/BattleVoiceLine.md)

## Notes

Name is ours.

## Open questions

None recorded.
