# Formula_22_Disempower

- **Address:** `0x140307928`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_22(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 22

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Disempower: a magic hit check that deals MP damage equal to the target's current MP.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 53 bytes.
- V: Typical abilities: Disempower.
- V: The earlier sheet described a stat loss; the current code deals MP damage.

## Calculation

```text
Hit check: magic (MA + X) chain
On success: MP damage equal to the target's current MP
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
