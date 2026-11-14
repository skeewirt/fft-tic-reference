# Formula_26_StatSap

- **Address:** `0x1403079A8`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_26(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 26

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stat sap: magic damage that also reduces the target's stat.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 121 bytes.
- V: Typical abilities: Speedsap, Powersap, Mindsap.

## Calculation

```text
Damage = MA × Y × [×5/4 element] × [×4/3 caster magic boost]
 × [×2/3 target Shell] × [×3/2 target Sleep/Charging]
 × Zodiac(50-150%) × Faith(caster×target/10000)
capped at 32767, then saps target stat + status applied
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
