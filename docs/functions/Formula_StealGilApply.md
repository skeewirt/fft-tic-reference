# Formula_StealGilApply

- **Address:** `0x140305FA8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_StealGilApply(void)`
- **Callers:** Formula_39_StealGil, Formula_42_Speechcraft
- **Callees:** SceneVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gil theft result: the caster gains and the target loses an amount from level, Speed and Y.

## Behavior

- V: amount = caster level (+0x29) * caster Speed (+0x40) * (Y + 1), with Y the ability record copy's byte +10 (block +0x2E).
- V: when the target's +0x05 & 0x30 is 0 (a player-side target) the amount is capped by SceneVar 44, the party's gil.
- V: non-zero amount: RC+14 = amount, RC+0 = 1, RC+39 = 1; R+14 = -amount, R+39 = 1. Zero: R+0 = 0, R+2 = 7, R+44 = 0.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md)

## Notes

Block B40 (2026-11-12): 131 bytes, read whole. The cap applies when the target IS player side ((+5 & 0x30) == 0), not when it is not. Crosscheck: Y (block +0x2E) is the byte at 0x1407B079E, byte 14 of the item at 0x1407B0790, a RIP-relative operand.

## Open questions

None recorded.
