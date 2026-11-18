# EffectEmitter_Spawn

- **Address:** `0x1403847D8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 EffectEmitter_Spawn(int16 ctx, int t, int emitter, EffectParticle *parent)`
- **Callers:** EffectScript_RunEmitterTracks, EffectScript_OpUpdateParticles (child emitters), sub_14031B964, sub_14031C964 and the sub_14034xxx special renderers
- **Callees:** EffectAnchor_GetPoint, SceneObject_FindBySlot, sub_14027471C, sub_140274BC0, sub_140274B34, sub_140387AD4, sub_140249000

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Spawns the particles of one effect emitter at time t: count, position, velocity, mass, forces, life, homing and children from its 196-byte record.

## Behavior

- V: record = section 3 + 196 * emitter; offsets below are the code's (they include the 20-byte section header). A value pair (a, b) is a + curve * (b - a) / 256 with curve c = a byte of section 4 at 4 + 160 (c - 1) + t % 160 (c = 0: a alone).
- V: it spawns only when t % interval (+200 -> +202, curve +35 & 15) is 0, then count particles (+196 -> +198, curve +32 >> 20 & 15); each gets sprite animation +21 of section 1 and frame set +24 (EffectSprite_StepAnimation).
- V: position = anchor (+22 & 0xE00: 0x200 a map tile, 0x400 the caster, 0x600 the target, 0x800 the parent particle, 0xA00 the map centre, 0xC00 a scene unit) + offset (+40 xyz -> +46, curve +28 & 15) + random -s..s per axis (s = +52 xyz -> +58, curve +28 >> 4 & 15).
- V: velocity by +26 & 0x410: 0x10 = toward the emitter point at a speed random in +112..+114 (-> +116 / +118, curve +28 >> 28); otherwise a vector (0, speed, 0) turned by angles +64 xyz (-> +70, curve +28 >> 8) plus a random part within +76 xyz (-> +82, curve +28 >> 12; half the start value without a curve), 4096 = one turn; both are multiplied by 8 into the 12-bit velocity.
- V: mass +16 = random +88..+90 (-> +92 / +94, curve +28 >> 16); weight +18 = random +104..+106 (-> +108 / +110, curve +28 >> 24); force +44 = random between (+120, +124, +128) and (+122, +126, +130) (-> +132.., curve +32 & 15); force change +56 = random between (+144, +148, +152) and (+146, +150, +154) (-> +156.., curve +32 >> 4); life +74 = random +168..+170 (-> +172 / +174, curve +32 >> 8; -1 = until the animation ends).
- V: homing point +68 = by +22 & 0xE0 (0x60 the caster, 0x80 the target, 0x40 a map position, 0xA0 the map centre, 0 / 0x20 fixed) + (+176 xyz -> +182, curve +32 >> 12); homing strength +82 = random +204..+206 (-> +208 / +210, curve +32 >> 28 & 3); particle curve +77 = +32 >> 30; children: +212 on death, +213 every step (+26 & 3, & 0xC say when).
- V: the caster and target points come from EffectAnchor_GetPoint: a unit's scene position, or a tile as (28 x + 14, -12 height, 28 z + 14).
- V (data): every stock emitter record decodes by these rules; simulated, Blood Drain (effect 210: 10 emitters over 105 frames; effect 335: 5 emitters over 64 frames) shows droplets at the target and blood carried to the caster.

## State touched

- Calls: [EffectAnchor_GetPoint](EffectAnchor_GetPoint.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Referenced by

- Called by: [EffectScript_OpUpdateParticles](EffectScript_OpUpdateParticles.md), [EffectScript_RunEmitterTracks](EffectScript_RunEmitterTracks.md)

## Notes

Name is ours (was sub_1403847D8). The random numbers come from the game xorshift state (xmmword_1408E5FC8).

## Open questions

? the flag modes 0x410 (a camera-relative variant) and 0x1040 in full; ? the curve rate for the spawner (t is the phase time).
