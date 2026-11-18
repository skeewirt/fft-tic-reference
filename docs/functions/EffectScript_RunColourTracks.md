# EffectScript_RunColourTracks

- **Address:** `0x14031BE2C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void EffectScript_RunColourTracks(EffectScriptCtx *ctx)`
- **Callers:** EffectScript_OpRunTimeline
- **Callees:** sub_1402F7A90, sub_1402F7C20, sub_1402F5C20, sub_1402F52D8, sub_1402F5428, sub_1402F5B28

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the colour-fade tracks of the effect timeline: palette fades on the screen, the caster and the targets.

## Behavior

- V: four tracks in section 7 + 8: +806 durations (x 8 frames) with +971 mode bytes and +872.. colour offsets, +1006 / +1171, +1206 / +1371, +1406 / +1670; a mode byte with bit 7 starts a fade (sub_1402F7A90, sub_1402F7C20 per target unit, sub_1402F5C20 / sub_1402F5428 for the screen).

## Referenced by

- Called by: [EffectScript_OpRunTimeline](EffectScript_OpRunTimeline.md)

## Notes

Name is ours (was sub_14031BE2C).

## Open questions

? the exact meaning of each track (screen, caster, target).
