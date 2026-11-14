# Formula_83_MonsterHPDamageMagicChain

- **Address:** `0x140308F28`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_83(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 83

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Monster % HP damage: a magic hit check then percentage-of-target-max-HP damage.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 117 bytes.
- V: Typical abilities: Twister, Tri-Breath.
- V: The earlier sheet called this physical and used caster MaxHP; the current code is magic and uses target MaxHP.

## Calculation

```text
Magic hit check (MA + X chain)
Damage = (Y × target MaxHP + 99) / 100
then weather, element, post-damage, counter, status
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
