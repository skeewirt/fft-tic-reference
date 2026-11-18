# EffectParticle_StepPhysics

- **Address:** `0x140388170`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void EffectParticle_StepPhysics(EffectParticle *list)`
- **Callers:** EffectScript_OpUpdateParticles
- **Callees:** sub_140274B34

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Moves every effect particle one step: position by velocity, velocity by gravity, drag and force, force by its change or by homing.

## Behavior

- V: 12-bit fixed point: pos (+20, +24, +28) += vel (+32, +36, +40); vel = (gravity * weight (+18) >> 12) + ((mass (+16) - drag) * vel + force (+44, +48, +52) << 12) / mass.
- V: with no homing strength (+82 = 0) the force grows by its change (+56, +60, +64) each step; with one, v = strength * unit vector to the homing point (+68, +70, +72), and force = v + force + k * (change - v) / 127 with k = the particle curve (+77, read at age +88) - 128, or -128 without a curve.
- V: gravity and drag are the globals EffectScript_OpLoadPhysics fills from section 3.

## Referenced by

- Called by: [EffectScript_OpUpdateParticles](EffectScript_OpUpdateParticles.md)

## Notes

Name is ours (was sub_140388170).

## Open questions

None recorded.
