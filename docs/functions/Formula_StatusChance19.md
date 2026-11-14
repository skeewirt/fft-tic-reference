# Formula_StatusChance19

- **Address:** `0x140306C10`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `int Formula_StatusChance19(void)`
- **Callers:** Formula_08_BlackMagickSummonDamage, Formula_09_Gravity, Formula_31_IaidoNether, Formula_49_MonkPhysicalAveraged, Formula_83_MonsterHPDamageMagicChain, Formula_MagicDamageTail, and 2 more (IDA code references)
- **Callees:** Rng_Percent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The chance that a status effect goes with a damage hit: a 19 percent roll (Nanoflare-style id 219 uses a MA difference) that sets R+18 bit 0x200.

## Behavior

- V: not simulating: ability id (g_FormulaBlock +8) 219 uses caster MA - target MA + 45 as the chance (a negative chance skips the roll); any other id uses 19.
- V: Rng_Percent(100, chance) false (the roll fell under the chance) sets R+18 bit 0x200.
- V: returns true when bit 0x200 is clear (no status), and false when g_BattleSimulating is 2.
- V: the composites run Formula_StatusTailKeepHit only when this returns 0.

## State touched

- Calls: [Rng_Percent](Rng_Percent.md)

## Referenced by

- Called by: [Formula_MagicDamageTail](Formula_MagicDamageTail.md)
- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md)

## Notes

Formula block B37 (2026-11-12): 127 bytes, read whole.

## Open questions

? what ability 219 is (named only by id).
