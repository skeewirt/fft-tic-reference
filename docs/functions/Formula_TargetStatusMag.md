# Formula_TargetStatusMag

- **Address:** `0x140305E64`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_TargetStatusMag(void)`
- **Callers:** Formula_08_BlackMagickSummonDamage, Formula_14_DeathInstantKill, Formula_26_StatSap, Formula_31_IaidoNether, Formula_33_DrawOutDamageStatus, Formula_MagicDamageTail, and 4 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The target's status modifiers against a magic hit.

## Behavior

- V: target +0x64 bit 0x10 (status 27, Shell): A = A * 2 / 3.
- V: target +0x63 bits 0x06 (Chicken, Toad): A = A * 3 / 2.

## Referenced by

- Called by: [Formula_MagicDamageTail](Formula_MagicDamageTail.md), [Formula_MagicHitElem](Formula_MagicHitElem.md), [Formula_MagicHitNoElem](Formula_MagicHitNoElem.md), [Formula_MagicHitNoFaith](Formula_MagicHitNoFaith.md)
- Observed behaviours: [BattleStatChangeAndCtGainSteps](../behaviors/BattleStatChangeAndCtGainSteps.md)

## Notes

Source: block B23 (2026-11-12). 79 bytes, read whole. Unlike the physical twin it has no Sleep / Readying step. It is a leaf function (no unwind entry).

## Open questions

None recorded.
