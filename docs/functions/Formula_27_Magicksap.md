# Formula_27_Magicksap

- **Address:** `0x140307A24`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_27(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 27

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Magicksap: a magic hit check that deals MP damage based on the target's maximum MP.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 76 bytes.
- V: Typical abilities: Magicksap.
- V: The earlier sheet described a drain to the caster; the current code only deals MP damage.

## Calculation

```text
Hit check: magic (MA + X) chain
MP damage = (Y × target MaxMP + 99) / 100
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
