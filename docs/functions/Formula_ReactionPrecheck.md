# Formula_ReactionPrecheck

- **Address:** `0x14030AF88`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `int Formula_ReactionPrecheck(void)`
- **Callers:** Battle_ApplyActionResult, Formula_42_Speechcraft, sub_140309380, sub_14030B4F0, sub_14030BBA8, sub_14030BC64
- **Callees:** Unit_HasStatusGroup, sub_14030DD1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gate of the reaction-style handlers (Speechcraft, Throw): decides whether the reaction roll applies.

## Behavior

- V: returns 1 at once when g_BattleStateGate is non-zero.
- V: otherwise it asks Unit_HasStatusGroup(target, 4); a non-zero answer is returned as it is.
- I: with no status in the group it tests the request words at 0x1407B0768 / 0x1407B076A against a register value the decompile lost and returns 1, the result of sub_14030DD1C or 2; the callers (formulas 42 and 99) branch on 0.

## State touched

- Calls: [Unit_HasStatusGroup](Unit_HasStatusGroup.md)

## Referenced by

- Called by: [Formula_99_SpeedTimesWeaponPower](Formula_99_SpeedTimesWeaponPower.md)

## Notes

Block B43 (2026-11-12): 97 bytes, read whole. Head read; the register-lost compares are I.

## Open questions

? what the request words 0x1407B0768 / 0x1407B076A are compared with (settles by the disassembly of 0x14030AF88).
