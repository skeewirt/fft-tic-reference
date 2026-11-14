# Formula_36_Geomancy

- **Address:** `0x140307E34`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_36(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 36

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Geomancy: MA and an averaged Y through the magic chain, with a terrain element.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 63 bytes.
- V: Typical abilities: All 12 Geomancy skills (Sinkhole → Magma Surge).
- V: The earlier sheet described weapon damage; the current code uses MA and the magic chain.

## Calculation

```text
PA = MA
Y = (ability_Y + caster PA) / 2
Damage = MA × Y through the magic chain
 (element, caster boost, Shell, Sleep, Zodiac, weather, element)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
