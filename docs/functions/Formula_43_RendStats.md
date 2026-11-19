# Formula_43_RendStats

- **Address:** `0x1403083F4`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_43(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 43

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stat lowering by force: the physical evade gate, then a chance of PA + Y with the physical modifiers; on success the stat the ability id selects drops by X. No damage.

## Behavior

- V: re-read 2026-11-18 (IDA, whole body): the earlier calculation called it PA x Y damage; the body writes no damage.
- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 82 bytes.
- V: Typical abilities: Rend Speed, Rend Power, Rend Magick.
- V: The earlier sheet used MA; the current code uses PA and the physical chain.

## Calculation

```text
Gate: sub_140306C90 (physical evade)
Chance: A = PA, B = Y; Formula_PhysMods, Formula_ChanceSum, Formula_ChanceRoll
Success: sub_1403064D8 (ability 143 / 197 Speed, 144 / 198 PA, 145 / 199 MA, lowered by X & 0x7F)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
