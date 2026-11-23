# EffectScript_OpRunTimeline

- **Address:** `0x14031C2DC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 EffectScript_OpRunTimeline(EffectScriptCtx *ctx)`
- **Callers:** EffectScript_Run (through tbl_EffectScriptHandlers, opcode 0x28)
- **Callees:** EffectScript_RunEmitterTracks, EffectScript_RunColourTracks, SoundCue_Play, sub_14038387C, sub_140381C08, sub_140381F50, EffectCamera_SetVector, sub_140310B64

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Effect script opcode 0x28: runs one step of the effect's timeline (emitter tracks, colour tracks, sound tracks, camera tracks) and counts the frame.

## Behavior

- V: calls EffectScript_RunEmitterTracks and EffectScript_RunColourTracks, then steps three sound tracks of section 7 + 8 (54 bytes apart: +644 durations, +678 sound bytes, +696 count; a byte above 1 plays SoundCue_Play(cue + dword_14114B124 - 1)) and three camera tracks (section 7 +1748 / +1850 / +1952 points, +2054 times).
- V: the frame counter is ctx +44 (incremented when bit 2 of dword_1407B0758 is set); opcode 0x1D loops back until it reaches the u16 at section 7 + 8 + 2, the effect length in frames.
- V (data): the 2-byte opcodes are read through tbl_EffectScriptHandlers (index & 0x1FF); section 2 of every stock file checked is the same short program: 0x2A reset, 0x27 load physics, then a loop of 0x28 / 0x25 until 0x1D says the length is reached.

## State touched

- Calls: [EffectScript_RunEmitterTracks](EffectScript_RunEmitterTracks.md), [EffectScript_RunColourTracks](EffectScript_RunColourTracks.md), [SoundCue_Play](SoundCue_Play.md), [EffectCamera_SetVector](EffectCamera_SetVector.md)

## Referenced by

- Reads file formats: [EffectSoundTracks](../formats/EffectSoundTracks.md)

## Notes

Name is ours (was sub_14031C2DC). The opcode numbers (0x1D, 0x25, 0x27, the 0x1FF mask) belong to EffectScript_Run and the handler table, not to this body.

## Open questions

? the camera track records (+1748..+2054) in detail.
