# BattleVoice_SpeakSwapped

- **Address:** `0x1401ECC44`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleVoice_SpeakSwapped(void *controller, void *request, int line)`
- **Callers:** sub_1401ECBBC, sub_1401ECC90, sub_1401ED708
- **Callees:** none (virtual calls)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Speaks a replaceable line, swapped for row 3 or 2 by the request flags.

## Behavior

- V: the line becomes 3 when request byte +65 is set, else 2 when request byte +64 is set, else stays; then it calls virtual slot 5 (BattleVoice_IsSuppressed) and, when not suppressed, slot 3 (BattleVoice_Speak).

## Referenced by

- Appears in flows: [BattleVoiceLine](../flows/BattleVoiceLine.md)

## Notes

Name is ours.

## Open questions

? what request bytes +64 and +65 record.
