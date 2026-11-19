# Formula_StatusTailKeepHit

- **Address:** `0x140306944`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_StatusTailKeepHit(void)`
- **Callers:** Formula_01_NormalAttack, Formula_08_BlackMagickSummonDamage, Formula_09_Gravity, Formula_104_WotLDistanceScaledPhysical, Formula_31_IaidoNether, Formula_45_HolySword, and 8 more (IDA code references)
- **Callees:** Formula_56_StatusOnlyApplication

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the status application on the inflict record and restores the hit fields it may have touched.

## Behavior

- V: saves R+2, R+44 and R+0, calls Formula_56_StatusOnlyApplication, then writes the three back.
- I: so a status riding on a damage hit adds to R+29..38 and R+39 / R+18 but never turns the damage into a miss.

## State touched

- Calls: [Formula_56_StatusOnlyApplication](Formula_56_StatusOnlyApplication.md)

## Referenced by

- Called by: [Formula_05_WeaponAttackNoElement](Formula_05_WeaponAttackNoElement.md), [Formula_MagicDamageTail](Formula_MagicDamageTail.md), [Formula_RevivePrecheck](Formula_RevivePrecheck.md)

## Notes

Source: block B35. 70 bytes, read whole. Called by the damage handlers that carry a status tail and by Formula_RevivePrecheck.

## Open questions

None recorded.
