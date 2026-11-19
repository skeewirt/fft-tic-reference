# Formula_26_StatSap

- **Address:** `0x1403079A8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_26(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 26

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stat lowering by magic: the magic evade gate, then a chance of MA + Y (magic modifiers, zodiac, Faith); on success the stat the ability id selects drops by X. No damage.

## Behavior

- V: re-read 2026-11-18 (IDA, whole body): the earlier calculation called it MA x Y damage; the body writes no damage, Y is the chance base and X the amount.
- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 121 bytes.
- V: Typical abilities: Speedsap, Powersap, Mindsap.

## Calculation

```text
Gate: sub_140306D70 (magic evade)
Chance: A = MA, B = Y; element boost, Formula_CasterMagMods, target passive and status,
  Formula_ChanceSum (A + zodiac(B)), Formula_FaithScale, Formula_ChanceRoll
Success: sub_1403064D8: ability 143 / 197 -> Speed (R+20), 144 / 198 -> PA (R+22),
  145 / 199 -> MA (R+23) lowered by X & 0x7F; any other ability: no change
Failure: result word +18 bit 0x04 cleared
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
