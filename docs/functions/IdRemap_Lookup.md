# IdRemap_Lookup

- **Address:** `0x1402BA9C8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint32_t IdRemap_Lookup(uint32_t id)`
- **Callers:** EventChannel_StepTask, sub_140210AF0, sub_14024A6E8, sub_1402B20E4, SoundCue_Play, sub_140346648
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Remaps an id above 0xA7 through the 406-row table `g_IdRemapPairs` (7 pairs of two dwords per row, 56 bytes); returns the replacement, or the id itself when it is not in the table.

## Behavior

- V (decompile): ids <= 0xA7 are returned unchanged.
- V: otherwise walks 406 rows x 7 pairs (table 0x140718C50, end 0x14071E520); on a match with the first dword of a pair returns the second dword; if that is -1 the result is -1.
- V: no match returns the id.
- V: the loop stops when the row pointer reaches the address loaded at 0x1402BA9FD (the end of the table); the table start is loaded at 0x1402BA9D0 and the match path reads the pair through that same start register.
- V (live 2026-11-12): sound cues go through it from SoundCue_Play: the Potion's effect cue 0x730000 becomes 0x137 (played) and 0x730001 becomes -1 (nothing).

## Referenced by

- Called by: [SoundCue_Play](SoundCue_Play.md)
- Observed behaviours: [SoundCuesAreRemappedBeforeTheyPlay](../behaviors/SoundCuesAreRemappedBeforeTheyPlay.md)
- Reads file formats: [EffectSoundTracks](../formats/EffectSoundTracks.md)
- Reads tables: [IdRemapPairs](../tables/IdRemapPairs.md)

## Notes

J8 note: 406 x 56 bytes. I: the ids are sound cue ids (every caller of SoundCue_Play passes a cue); the other callers' ids are not checked here.

## Open questions

? whether the callers other than SoundCue_Play (EventChannel_StepTask, sub_140210AF0, sub_14024A6E8, sub_1402B20E4, sub_140346648) pass sound ids too.
