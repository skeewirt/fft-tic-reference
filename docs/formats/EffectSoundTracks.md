# EffectSoundTracks

- **Kind:** file format
- **Area:** [Battle](../areas/battle.md)
- **Read by:** [EffectScript_OpRunTimeline](../functions/EffectScript_OpRunTimeline.md), [EffectSound_PickSlotValue](../functions/EffectSound_PickSlotValue.md), [SoundCue_Play](../functions/SoundCue_Play.md), [IdRemap_Lookup](../functions/IdRemap_Lookup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

An effect file names its sounds in three places: three sound tracks in section 7 say when, a slot list in section 6 says which value, and section 8 gives the cue base. The cue is base + value - 1, and SoundCue_Play remaps it to a sound of the common bank.

## Layout

| Offset | Part | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="steps"></a>section 7 + 8 + 54 t + 696 | steps | `s16` | V | Step count of sound track t (0..2). |
| <a id="lengths"></a>section 7 + 8 + 54 t + 644 | lengths | `u16[]` | V | Length of each step in frames. |
| <a id="slots"></a>section 7 + 8 + 54 t + 678 | slots | `u8[]` | V | Per step: a value above 1 plays sound slot (value - 2). |
| <a id="slot"></a>section 6 + 8 + 4 s | slot | `u8[4]` | V | Mode, v0, v1, v2. Mode 0 always v0; 1 v0 and v1 alternating; 2 v0 the first time, v1 after; 3 v0 the first time, then v1 / v2 alternating; 4 v0, v1, v2 in turn (a per-slot play counter, dword_1418732CC). |
| <a id="cue_base"></a>section 8 + 10 | cue_base | `u16` | V | Shifted left by 16 into dword_14114B124; the cue is base + value - 1. |

## Behavior

- V: SoundCue_Play passes the cue through IdRemap_Lookup (g_IdRemapPairs, 406 rows of 7 (cue, sound) pairs); -1 or a result above 0x2B1 plays nothing.
- V (data): the Potion effect (260) gives cue 0x730000 -> sound 311 (heard live 2026-11-12); the Skeleton family's effects give Chop (341) 0x1200000 -> 475, Thunder Anima (342) 0xD0000 -> 181, Water Anima (343) 0x480000 -> 261, Ice Anima (344) 0x2E0000 -> 221, Wind Anima (345) 0xFB0000 -> 427; their second and later cues remap to -1 (silent in this version).
- V (live 2026-11-18): calling SoundCue_Play on the game thread with those cues returned channel 13 (played).

## Open questions

None recorded.
