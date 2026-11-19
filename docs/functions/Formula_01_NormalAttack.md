# Formula_01_NormalAttack

- **Address:** `0x140307120`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_01(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 1

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Normal attack: the physical evade gate, then the whole weapon attack (weapon-type value x WP with the physical modifiers, critical and element), and the weapon's status on the 19 percent roll.

## Behavior

- V: re-read 2026-11-18 (IDA, whole body): the earlier calculation (PA += WP, PA x Y) did not match the body: B is the weapon power, A the weapon-type value; no ability X or Y is read.
- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 32 bytes.
- V: Typical abilities: Attack, Choco Beak, Tackle, Bite, Claw, all monster basic attacks (16 total).

## Calculation

```text
Gate: sub_140306C90 (physical evade)
Formula_PhysAttackFull: A, B from the weapon type (sub_140305A48), A += weapon bonus,
  element boost, Formula_PhysMods, critical, Damage = A x B, element affinity, absorb
19 % roll (Formula_StatusChance19): Formula_StatusTailKeepHit adds the weapon's status
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
