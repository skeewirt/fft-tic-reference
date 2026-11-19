# Formula_FaithScale

- **Address:** `0x140306258`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_FaithScale(void)`
- **Callers:** Formula_08_BlackMagickSummonDamage, Formula_11_FaithBasedBuff, Formula_12_MagicalHealing, Formula_13_RaiseRevive, Formula_14_DeathInstantKill, Formula_18_Quick, and 4 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scales R+6 by the caster's and the target's faith: R+6 = R+6 * casterFaith * targetFaith / 10000.

## Behavior

- V: for the caster (+0x65) bit 0x80 (Faith) sets the faith byte g_FormulaBlock +5 to 100 and bit 0x40 (Atheist) sets it to 0; for the target the same two bits decide g_FormulaBlock +4; otherwise the bytes keep the values Battle_ResolveAction stored.
- V: then R+6 = R+6 * (+5 byte) * (+4 byte) / 10000.
- I: the stored bytes are the unit Faith values; the formulas that scale damage or a chance by faith call this block.

## Referenced by

- Called by: [Formula_04_MagicGun](Formula_04_MagicGun.md), [Formula_MagicHitElem](Formula_MagicHitElem.md), [Formula_MagicHitNoElem](Formula_MagicHitNoElem.md)

## Notes

152 bytes, read whole. Crosscheck: the bit 0x80 tests are sign tests of the status byte (bit 7), so no 0x80 immediate appears.

## Open questions

None recorded.
