# Formula_23_Gravija

- **Address:** `0x140307960`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_23(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 23

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gravija: a magic hit check that reduces the target to 1 HP.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 72 bytes.
- V: Typical abilities: Gravija.
- V: The earlier sheet described percentage damage; the current code reduces the target to 1 HP.

## Calculation

```text
Hit check: magic (MA + X) chain
Damage = target current HP - 1 (minimum 0)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
