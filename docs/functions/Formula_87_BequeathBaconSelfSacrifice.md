# Formula_87_BequeathBaconSelfSacrifice

- **Address:** `0x140309060`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_87(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 87

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sacrifice: fills the target's HP and MP words with its own maximums, then, when the target is below level 99, turns the result into a stat change (flag word 0x80) and applies the ability's status to the caster.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above (re-read 2026-11-18: the maximums and the level test are the target's, g_BattleActingUnit, not the caster's).
- V: Current-build symbol size is 146 bytes.
- V: Typical abilities: Bequeath Bacon.

## Calculation

```text
R+6 = target max HP, R+12 = target max MP, kind bits 0x90, then Formula_HealSwap
Target level (+0x29) < 99: kind bits = 1 (stat change), flag word (+18) = 0x80;
    the unit and result pointers are swapped and Formula_56 applies the status to the caster
Target level 99: hit 0, reason 7, hit percent 0
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
