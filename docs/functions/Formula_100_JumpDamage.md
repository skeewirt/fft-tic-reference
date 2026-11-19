# Formula_100_JumpDamage

- **Address:** `0x140309474`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_100(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`); its address sits at 0x140682EE8, slot 100 of the formula registry
- **Callees:** Item_GetRecord, Formula_CasterStatusMods, Formula_TargetPassivePhys, Formula_TargetStatusPhys, Formula_Zodiac, Formula_DamageAB (tail jump)
- **Dispatch ID:** 100

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Jump damage: PA x WP, with PA x 3/2 when the weapon is a spear and PA x (PA x Brave / 100) bare-handed, through the caster and target modifiers. No hit roll.

## Behavior

- V: it reads the item word at `0x1407B077A` (g_FormulaBlock +0x0A) and takes its category from the item record's byte +5 (Item_GetRecord).
- V: category 15 sets A (`0x1407B0770`) to caster +0x3E (PA) x 3 / 2 and B to the weapon power byte `0x1407B07AC`; every other non-zero category sets A = PA and B = the weapon power.
- V: category 0 sets B = PA x caster +0x2B (Brave) / 100, raised to 1 when it is 0.
- V: then Formula_CasterStatusMods, Formula_TargetPassivePhys, Formula_TargetStatusPhys, Formula_Zodiac and a tail jump to Formula_DamageAB.
- V: the item table's category 15 holds the spears.
- V: Battle_ResolveAction clears the item word (g_FormulaBlock +0x0A) after this handler, for formula 100 only.
- I: no stock action row names formula 100; it is the jump formula (a jump's landing; the spear bonus matches it).

## Calculation

```text
spear (category 15):   A = PA x 3 / 2, B = WP
other weapon:          A = PA,         B = WP
bare hands (cat. 0):   A = PA,         B = max(1, PA x Brave / 100)
Damage = A x B after caster status, target passive and status modifiers and zodiac
```

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md), [Formula_CasterStatusMods](Formula_CasterStatusMods.md), [Formula_TargetPassivePhys](Formula_TargetPassivePhys.md), [Formula_TargetStatusPhys](Formula_TargetStatusPhys.md), [Formula_Zodiac](Formula_Zodiac.md), [Formula_DamageAB](Formula_DamageAB.md)

## Notes

- V: the whole function was read (IDA, 2026-11-18).

## Open questions

? which request supplies formula 100 for a jump (the jump abilities' action rows do not name it).
