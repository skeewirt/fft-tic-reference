# Formula_ElemBoostWeapon

- **Address:** `0x140305BB8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_ElemBoostWeapon(void)`
- **Callers:** Formula_104_WotLDistanceScaledPhysical, Formula_45_HolySword, Formula_46_DarkSwordCrush, Formula_PhysAttackFull, sub_1403071DC
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Element boost from the weapon's element: A = 5 * A / 4 when the caster's element mask has the weapon's element.

## Behavior

- V: tests the caster's +0x7A against the weapon record copy's element byte (0x1407B07AE); when they share a bit A = 5 * A / 4.

## Referenced by

- Called by: [Formula_PhysAttackFull](Formula_PhysAttackFull.md)

## Notes

Source: block B15. 45 bytes, read whole. Twin of Formula_ElemBoostAction (which tests the ability record's element).

## Open questions

None recorded.
