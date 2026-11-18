# SoundCuesAreRemappedBeforeTheyPlay

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [SoundCue_Play](../functions/SoundCue_Play.md), [IdRemap_Lookup](../functions/IdRemap_Lookup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Every sound cue goes through SoundCue_Play, which first remaps it with IdRemap_Lookup (table g_IdRemapPairs, 406 rows of 7 from/to pairs) and drops any result above 0x2B1. Large cue ids (the effect bank values, e.g. 0x730000 for the Potion chime) are playable only through that table.

## Behavior

- V (code): IdRemap_Lookup passes ids up to 0xA7 through; above that it walks rows of 56 bytes from g_IdRemapPairs and compares the row pointer with the address after the table (lea at 0x1402BA9FD) to stop; a match returns the pair's 'to' dword (-1 = no sound), no match returns the id.
- V (code): SoundCue_Play returns -1 without playing when the remapped cue is above 0x2B1; an unremapped effect cue (0x73xxxx) is always above it.
- V (live 2026-11-12): a battle effect's sound events reach SoundCue_Play from EffectScript_OpRunTimeline with cue = track value + dword_14114B124 - 1; the stock Potion sends 0x730000 (remapped to 0x137, plays) and 0x730001 (remapped to -1, nothing).

## Open questions

? which other cue ranges besides the effect bank depend on the remap rows (event and UI cues below 0xA8 pass through).
