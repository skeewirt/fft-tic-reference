# Formula_04_MagicGun

- **Address:** `0x1403071DC`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_04(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** Battle_Rand15, AbilityAction_GetRecord, Mem_CopyChecked, Formula_ElemBoostWeapon, Formula_CasterMagMods, Formula_TargetPassiveMag, Formula_TargetStatusMag, Formula_Zodiac, Formula_DamageAB, Formula_SceneVarElemMod, Formula_EarthFloatAndAffinity, Formula_FaithScale, Formula_FinalizeAbsorb
- **Dispatch ID:** 4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Magic gun: picks one of three spells of the weapon's element by a random roll and deals its damage as (WP + bonus) x the spell's Y through the magic chain.

## Behavior

- V: the roll is Battle_Rand15 scaled to 0..99; under 10 picks the third ability of the set, 10..39 the second, 40 and above the first.
- V: the set comes from the weapon element byte 0x1407B07AE: the sign bit (tested with jns) gives 16..18, bit 0x40 gives 20..22, anything else 24..26.
- V: the chosen id is written to g_FormulaBlock +8 and to caster +0x1A2, and its 20-byte action record (AbilityAction_GetRecord) is copied over the block's ability record copy with Mem_CopyChecked.
- V: B = the copied record's Y (the byte at 0x1407B079E, block +0x2E); A = the weapon power byte 0x1407B07AC plus the weapon bonus (the low byte of the word at 0x1407B0787, block +0x17).
- V: then Formula_ElemBoostWeapon, Formula_CasterMagMods, Formula_TargetPassiveMag, Formula_TargetStatusMag, Formula_Zodiac, Formula_DamageAB, Formula_SceneVarElemMod and Formula_EarthFloatAndAffinity; when the hit flag still stands, Formula_FaithScale and Formula_FinalizeAbsorb.
- I: abilities 16..18, 20..22 and 24..26 are the three-tier fire, lightning and ice spells; the stock users are three guns, one per element.

## Calculation

```text
roll 0..99: < 10 -> third tier, < 40 -> second tier, else first tier
element byte bit 0x80 -> abilities 16 / 17 / 18; bit 0x40 -> 20 / 21 / 22; otherwise 24 / 25 / 26
A = WP + weapon bonus, B = the chosen spell's Y
Damage = A x B with element boost, caster and target magic modifiers, zodiac, weather, faith
```

## State touched

- Calls: [Battle_Rand15](Battle_Rand15.md), [AbilityAction_GetRecord](AbilityAction_GetRecord.md), [Mem_CopyChecked](Mem_CopyChecked.md), [Formula_ElemBoostWeapon](Formula_ElemBoostWeapon.md), [Formula_CasterMagMods](Formula_CasterMagMods.md), [Formula_TargetPassiveMag](Formula_TargetPassiveMag.md), [Formula_TargetStatusMag](Formula_TargetStatusMag.md), [Formula_Zodiac](Formula_Zodiac.md), [Formula_DamageAB](Formula_DamageAB.md), [Formula_SceneVarElemMod](Formula_SceneVarElemMod.md), [Formula_EarthFloatAndAffinity](Formula_EarthFloatAndAffinity.md), [Formula_FaithScale](Formula_FaithScale.md), [Formula_FinalizeAbsorb](Formula_FinalizeAbsorb.md)

## Notes

Read whole in IDA 2026-11-18 (current build).

## Open questions

None recorded.
