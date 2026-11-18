# EffectSound_PickSlotValue

- **Address:** `0x14031BBDC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int EffectSound_PickSlotValue(int slot)`
- **Callers:** EffectScript_OpRunTimeline
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Picks the value a battle effect's sound slot plays this time, by the slot's mode and its play counter.

## Behavior

- V: the slot is 4 bytes at section 6 (qword_1411A3828) + 8 + 4 slot: mode, v0, v1, v2; the play counter is a byte per slot at dword_1418732CC, incremented on every call.
- V: mode 0 returns v0; 1 v0 / v1 by the counter parity; 2 v0 on the first call, v1 after; 3 v0 on the first call, then v1 / v2 by parity; 4 v0, v1, v2 by counter % 3; another mode returns 0.
- V: EffectScript_OpRunTimeline plays SoundCue_Play(value + dword_14114B124 - 1) when the value is not 0.

## Referenced by

- Reads file formats: [EffectSoundTracks](../formats/EffectSoundTracks.md)

## Notes

Name is ours (was sub_14031BBDC).

## Open questions

None recorded.
