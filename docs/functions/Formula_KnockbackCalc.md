# Formula_KnockbackCalc

- **Address:** `0x140304DC0`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_KnockbackCalc(void)`
- **Callers:** Formula_55_RushBasicPhysical, Formula_CritRoll
- **Callees:** sub_140283AB8, sub_140304F44

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Works out the tile a hit target is knocked back to and queues it as a request.

## Behavior

- V: runs only when the byte 0x1407B078F is 1, the target is not the caster, the target's +0x05 bit 0x04 is clear, +0x1B4 is 0 and (+0x05 & 3) != 3.
- V: the direction is along the larger of the two tile differences (tiles at +0x4F / +0x50); the tile one step away is checked through sub_140304F44 and g_BattleTileTable (a flag bit, the height nibble <= 2, terrain 18 and 28 refused).
- V: on success g_FormulaBlock +0x20 = 0x81 when sub_140283AB8(target) is not negative or the target's +0x63 bits 0x06 are set, else 0x82, the request's bytes +12..+14 at 0x1407B076C get the new tile, and R+18 |= 0x4000.

## State touched

- Calls: [sub_140304F44](sub_140304F44.md)

## Referenced by

- Called by: [Formula_CritRoll](Formula_CritRoll.md)

## Notes

386 bytes, read whole. Called by Formula_CritRoll and Formula_55_RushBasicPhysical.

## Open questions

? the exact meaning of 0x81 versus 0x82 (I: the knockback kind) and of the +0x1B4 test.
