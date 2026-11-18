# EffectScript_OpUpdateParticles

- **Address:** `0x14031B768`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 EffectScript_OpUpdateParticles(EffectScriptCtx *ctx)`
- **Callers:** EffectScript_Run (through tbl_EffectScriptHandlers, opcode 0x25)
- **Callees:** EffectParticle_StepPhysics, EffectEmitter_Spawn, Effect_TintByNxdScale, sub_14038449C, sub_1400D2FA4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Effect script opcode 0x25: moves every particle of the effect, draws it, runs its child emitters and removes it when its life ends.

## Behavior

- V: EffectParticle_StepPhysics on the particle list (ctx +216), then per particle the draw routine of its kind (+84 >> 12, through the table at 0x140693070: the stock kinds 0..3 all draw with Effect_TintByNxdScale).
- V: a particle whose +86 & 0xC is 4 or 8 spawns its every-step child emitter (+91) at each step; its age (+88) counts 0..159 and wraps.
- V: the life (+74) counts down; -1 means until its sprite animation holds its last frame (node +22 = 0); at the end a particle whose +86 & 3 is 1 or 2 spawns its death child emitter (+90), then it is removed (sub_14038449C).
- V: a particle with a stop radius (+86 >> 4 & 0x30) ends when it comes within that distance of its homing point (+68).

## State touched

- Calls: [EffectParticle_StepPhysics](EffectParticle_StepPhysics.md), [EffectEmitter_Spawn](EffectEmitter_Spawn.md), [Effect_TintByNxdScale](Effect_TintByNxdScale.md)

## Notes

Name is ours (was sub_14031B768). Effect_TintByNxdScale is reached through the draw table at 0x140693070, not as a direct call.

## Open questions

None recorded.
