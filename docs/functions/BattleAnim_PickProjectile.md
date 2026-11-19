# BattleAnim_PickProjectile

- **Address:** `0x1401FAD94`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleAnim_PickProjectile(void *obj)`
- **Callers:** sub_14026B310, sub_14026BC60
- **Callees:** sub_1401FAAC8, sub_140310C24

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses the projectile of a throw motion by the effect word.

## Behavior

- V: word 148 (Throw Stone): projectile 6 (the stone); 382 or 368..393 (Throw item): 16; else byte_140673678[obj +0x152]; then sub_140310C24.

## Notes

One of the equality tests on stock ids (the effect word of a stock ability): an id not tested gets the weapon-kind projectile.

## Open questions

None recorded.
