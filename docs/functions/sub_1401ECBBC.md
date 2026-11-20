# sub_1401ECBBC

- **Address:** `0x1401ECBBC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void sub_1401ECBBC(BattleVoiceController *c, const uint32_t *event)`
- **Callers:** sub_1401ED45C
- **Callees:** StatusVoice_SpeakEvent, BattleVoice_SpeakSwapped

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Routes one battle voice event to its handler by the event kind.

## Behavior

- V: an event whose first dword is non-zero asks the controller (virtual slot 5) and, when it answers 0, speaks that line (slot 3).
- V: otherwise event kind 9 (dword +8) calls StatusVoice_SpeakEvent; kind 1 reads the controller's virtual slot 7 result and calls BattleVoice_SpeakSwapped with 1 (result 0 or 1) or 6 (result 2), nothing for another result; other kinds with a non-zero dword +4 call virtual slot 6.

## State touched

- Calls: [StatusVoice_SpeakEvent](StatusVoice_SpeakEvent.md), [BattleVoice_SpeakSwapped](BattleVoice_SpeakSwapped.md)

## Notes

Only the dispatch was read.

## Open questions

? the other event kinds.
