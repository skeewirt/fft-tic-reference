# Formula_87_BequeathBaconSelfSacrifice

- **Address:** `0x140309060`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_87(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 87

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Bequeath Bacon: a self-sacrifice effect that writes HP/MP values and applies a status to the caster.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 146 bytes.
- V: Typical abilities: Bequeath Bacon.

## Calculation

```text
Sets HP-damage field = caster MaxHP, MP-heal field = caster MaxMP
Initial flags: 0x90 (HP_Damage | MP_Healing)
Then sub_1402FCFDC processes the values
If caster level < 99: flags OVERWRITTEN to 1 (StatChange)
    Swaps pointers → applies status to the caster via F56
    Then restores pointers
If caster level ≥ 99: auto-miss
Note: the 0x90 flag is overwritten before engine reads it,
so HP/MP fields may only matter for sub_1402FCFDC processing.
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
