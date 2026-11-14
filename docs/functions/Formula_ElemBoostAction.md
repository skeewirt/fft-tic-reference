# Formula_ElemBoostAction

- **Address:** `0x140305BE8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_ElemBoostAction(void)`
- **Callers:** Formula_08_BlackMagickSummonDamage, Formula_11_FaithBasedBuff, Formula_12_MagicalHealing, Formula_13_RaiseRevive, Formula_14_DeathInstantKill, Formula_26_StatSap, and 7 more (IDA code references)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Element boost from the ability's element: A = 5 * A / 4 when the caster's element mask has the ability record's element.

## Behavior

- V: tests the caster's +0x7A against the ability record copy's element byte (block +0x2B, record +7); when they share a bit A = 5 * A / 4.

## Referenced by

- Called by: [Formula_MagicDamageTail](Formula_MagicDamageTail.md), [Formula_MagicHitElem](Formula_MagicHitElem.md), [Formula_MagicHitNoFaith](Formula_MagicHitNoFaith.md)

## Notes

Formula block B16 (2026-11-12): 45 bytes, read whole. Crosscheck: block +0x2B (record +7, the element) is byte 11 of the item at 0x1407B0790, a RIP-relative operand.

## Open questions

None recorded.
