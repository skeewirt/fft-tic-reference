# Formula_MagicHitNoFaith

- **Address:** `0x140307088`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `int Formula_MagicHitNoFaith(void)`
- **Callers:** Formula_61_MagicStatusOnly, Formula_65_CelestialStasis, Formula_83_MonsterHPDamageMagicChain, Formula_85_PeckPhysicalHitPADrain, Formula_86_BeamPhysicalHitMADrain, Formula_89_LevelDrainPhysicalHitLevelSteal, Formula_98_PhysicalBasedBraveModify
- **Callees:** Formula_Zodiac, Formula_ElemBoostAction, Formula_CasterMagMods, Formula_TargetPassiveMag, Formula_TargetStatusMag, Formula_ChanceSum, Formula_ChanceRoll

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Magic hit chance without the faith factor: A = MA, B = X, then the element boost, the magic modifier chain and the chance roll.

## Behavior

- V: A = caster MA (+0x3F); B = X (block +0x2D).
- V: calls Formula_ElemBoostAction, Formula_CasterMagMods, Formula_TargetPassiveMag, Formula_TargetStatusMag, Formula_Zodiac, Formula_ChanceSum, Formula_ChanceRoll in that order; Formula_FaithScale is not called.
- V: returns 1 when R+0 is 0 after the roll, else 0.

## State touched

- Calls: [Formula_Zodiac](Formula_Zodiac.md), [Formula_ElemBoostAction](Formula_ElemBoostAction.md), [Formula_CasterMagMods](Formula_CasterMagMods.md), [Formula_TargetPassiveMag](Formula_TargetPassiveMag.md), [Formula_TargetStatusMag](Formula_TargetStatusMag.md), [Formula_ChanceSum](Formula_ChanceSum.md), [Formula_ChanceRoll](Formula_ChanceRoll.md)

## Notes

Source: block B06. 90 bytes, read whole. Crosscheck: X (block +0x2D) is the byte at 0x1407B079D, byte 13 of the item at 0x1407B0790, a RIP-relative operand.

## Open questions

None recorded.
