# Formula_02_WeaponCastsSpell

- **Address:** `0x140307140`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_02(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** sub_140306C90, Formula_PhysAttackFull
- **Dispatch ID:** 2

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Weapon attack that can cast a spell: the whole weapon attack, and on the 19 percent status roll the weapon's inflict byte becomes the ability resolved next instead of a status.

## Behavior

- V: sub_140306C90 first (the physical evade gate); a miss ends the handler.
- V: then Formula_PhysAttackFull, the whole stock weapon attack (weapon stat, bonus, modifiers, critical, damage, element affinity).
- V: when that returns 0 (the hit stands and Formula_StatusChance19's 19 percent roll succeeded) it does not apply the status: it writes the inflict byte (g_FormulaBlock +0x0D, the weapon record's byte +7) to the request word at 0x1407B0768 and 1 to the word after it; Battle_ResolveAction takes the next ability id from that word when the flag word is non-zero (see g_FormulaBlock), so the weapon's byte names a follow-up ability.
- V: it copies the byte at 0x1407B0761 to 0x1407B0792, and when the flag byte at 0x1407B0790 (g_FormulaBlock +0x20) has its sign bit set it clears the byte and ANDs result word +18 with 0xBFFF (bit 0x4000, the knockback request), as Formula_ZeroResult does.
- I: so a weapon with formula 2 casts the ability its inflict byte names on about one hit in five; the stock users are rods, a flail, a bow, a spear and a sword.

## Calculation

```text
Hit: physical evade (sub_140306C90)
Damage: as formula 1 (weapon type A and B, + weapon bonus, modifiers, critical, A x B, element)
On the 19 % roll: follow-up ability = weapon record byte +7
```

## State touched

- Calls: [sub_140306C90](sub_140306C90.md), [Formula_PhysAttackFull](Formula_PhysAttackFull.md)

## Notes

Read whole in IDA 2026-11-18 (current build).

## Open questions

? what the byte copied from 0x1407B0761 to 0x1407B0792 means.
