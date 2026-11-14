# Formula_FinalizeAbsorb

- **Address:** `0x140306224`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_FinalizeAbsorb(void)`
- **Callers:** Formula_08_BlackMagickSummonDamage, Formula_09_Gravity, Formula_104_WotLDistanceScaledPhysical, Formula_31_IaidoNether, Formula_45_HolySword, Formula_46_DarkSwordCrush, and 6 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the kind bits of a damage result and turns an absorbed hit into a heal.

## Behavior

- V: does nothing when R+2 is 5 (a nullified result).
- V: otherwise R+39 &= 0x08 (keeps only the status-pending bit). With R+18 bit 0x400 set (absorbed): R+8 = R+6, R+39 |= 0x40, R+6 = 0; else R+39 |= 0x80.

## Referenced by

- Called by: [Formula_MagicDamageTail](Formula_MagicDamageTail.md), [Formula_PhysAttackFull](Formula_PhysAttackFull.md)

## Notes

Formula block B31 (2026-11-12): 52 bytes, read whole. Crosscheck: 0x80 is an 8-bit immediate stored sign-extended (-0x80) in the OR, so the checker constant scan does not see it.

## Open questions

None recorded.
