# Formula_91_DragonSGiftSpeciesGatedHPMPGift

- **Address:** `0x140309214`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_91(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 91

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Dragon's Gift: a species-gated self-damage plus target heal.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 114 bytes.
- V: Typical abilities: Dragon's Gift.

## Calculation

```text
Species gate: caster+398 must be 15 or 16 (Dragon type)
    If not dragon: auto-miss
On success: secondary-damage field = caster_MaxHP / 5 (damage to self)
            HP-heal field = 2 × (MaxHP/5)           (HP heal to target)
Then: status applied via F56
(Structure identical to F60 Chant — self-damage + target heal)
```

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

None recorded.
