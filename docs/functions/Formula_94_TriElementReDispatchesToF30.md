# Formula_94_TriElementReDispatchesToF30

- **Address:** `0x140307C10`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_94(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 94

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Tri-Element: shares the F30 target; the ability supplies the element and parameters.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 23 bytes.
- V: Typical abilities: Tri-Thunder, Tri-Flame, Dark Whisper.
- V: F30, F94 and F95 resolve to the same function in the current build.

## Calculation

```text
Shares the F30 target.
The ability supplies the element and parameters; the F30 magic chain runs unchanged.
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
