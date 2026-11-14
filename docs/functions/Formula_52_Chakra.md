# Formula_52_Chakra

- **Address:** `0x140308874`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_52(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 52

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chakra: PA x Y healing split between HP and MP, with no Faith scaling.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 95 bytes.
- V: Typical abilities: Chakra.

## Calculation

```text
Base = PA × Y × [×3/2 Berserk] × Zodiac(50-150%)
capped at 32767
HP heal = Base, MP heal = Base / 2
(MULTIPLICATIVE, no faith)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
