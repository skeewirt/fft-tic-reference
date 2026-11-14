# Formula_MagicDamageTail

- **Address:** `0x140306F4C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `int Formula_MagicDamageTail(void)`
- **Callers:** Formula_105_WotLLevelScaledPhysical, Formula_32_DrawOutDamage, Formula_36_Geomancy, Formula_78_MAYPhysicalFullChain, Formula_MagicAvgDamage
- **Callees:** Formula_Zodiac, Formula_ElemBoostAction, Formula_CasterMagMods, Formula_TargetPassiveMag, Formula_TargetStatusMag, Formula_DamageAB, Formula_SceneVarElemMod, Formula_EarthFloatAndAffinity, Formula_FinalizeAbsorb, Formula_StatusTailKeepHit, Formula_StatusChance19

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The tail of every stock magic damage formula: the magic modifier chain on A, the damage, the scene and affinity steps, and the status tail.

## Behavior

- V: calls Formula_ElemBoostAction, Formula_CasterMagMods, Formula_TargetPassiveMag, Formula_TargetStatusMag, Formula_Zodiac, Formula_DamageAB, Formula_SceneVarElemMod, Formula_EarthFloatAndAffinity.
- V: when R+0 is still non-zero: Formula_FinalizeAbsorb, then Formula_StatusChance19; when that returns 0 it runs Formula_StatusTailKeepHit.
- V: no faith factor is applied here (the Formula_08 handler applies it itself).
- V: Formula_36, Formula_78 and Formula_105 reach it by a tail jump after setting A and B, Formula_32 too; Formula_MagicAvgDamage jumps into it.
- V: IDA labelled this address __acrt_eagerly_load_locale_apis (a library-name mislabel).

## State touched

- Calls: [Formula_Zodiac](Formula_Zodiac.md), [Formula_ElemBoostAction](Formula_ElemBoostAction.md), [Formula_CasterMagMods](Formula_CasterMagMods.md), [Formula_TargetPassiveMag](Formula_TargetPassiveMag.md), [Formula_TargetStatusMag](Formula_TargetStatusMag.md), [Formula_DamageAB](Formula_DamageAB.md), [Formula_SceneVarElemMod](Formula_SceneVarElemMod.md), [Formula_EarthFloatAndAffinity](Formula_EarthFloatAndAffinity.md), [Formula_FinalizeAbsorb](Formula_FinalizeAbsorb.md), [Formula_StatusTailKeepHit](Formula_StatusTailKeepHit.md), [Formula_StatusChance19](Formula_StatusChance19.md)

## Notes

Block B45 (MagicDamageTail, 2026-11-12): 80 bytes, read whole. The caller sets A (usually MA) and B first.

## Open questions

None recorded.
