# EffectScript_RunEmitterTracks

- **Address:** `0x14031BC8C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void EffectScript_RunEmitterTracks(EffectScriptCtx *ctx)`
- **Callers:** EffectScript_OpRunTimeline
- **Callees:** EffectEmitter_Spawn, sub_14031BA38

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the five emitter tracks of the effect timeline: each track is a list of phases, and the emitter of the running phase is asked to spawn particles.

## Behavior

- V: the tracks are 128 bytes each from section 7 + 8 (qword_1411A3818); phase k (from 1) starts at track word 1 + k and ends at word 2 + k (frames), byte 53 + k is its emitter + 1 (0 = none), word 39 + k & 7 is its mode, word 39 + k is also handed to sub_14031BA38 when the phase starts.
- V: mode 0 calls EffectEmitter_Spawn(ctx, t, emitter, 0) with t = the frames since the phase began; a mode 1..7 calls the ctx callback slot (ctx +224 + 8 (mode - 1)) instead.
- V: the IDA database had this function under a library name (EffectScript_RunEmitterTracks); the body is the effect scheduler.

## State touched

- Calls: [EffectEmitter_Spawn](EffectEmitter_Spawn.md)

## Referenced by

- Called by: [EffectScript_OpRunTimeline](EffectScript_OpRunTimeline.md)

## Notes

Name is ours (was __ld12mul_1, a wrong library match).

## Open questions

? what sub_14031BA38 does with the phase word.
