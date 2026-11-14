# Formula_ZeroResult

- **Address:** `0x140305504`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_ZeroResult(void)`
- **Callers:** Formula_38_StealEquipment, Formula_EarthFloatAndAffinity, Formula_ElementAffinity, Formula_RevivePrecheck
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The stock no-effect result: nothing happens and the reason is 5 (nullified).

## Behavior

- V: R+0 = 0, R+6 = 0, R+44 = 0, R+18 = 0, R+2 = 5, R+39 = 0.
- V: when the request word at 0x1407B076A is non-zero it clears the dword at 0x1407B0768 and R+18 bit 0x200; when the flag byte g_FormulaBlock +0x20 has bit 0x80 it clears that byte and R+18 bit 0x4000 (the knockback request).

## State touched

- Writes: [ActionResult.hit](../structs/ActionResult.md#hit), [ActionResult.miss_reason](../structs/ActionResult.md#miss_reason), [ActionResult.hit_percent](../structs/ActionResult.md#hit_percent)

## Referenced by

- Called by: [Formula_EarthFloatAndAffinity](Formula_EarthFloatAndAffinity.md), [Formula_ElementAffinity](Formula_ElementAffinity.md), [Formula_RevivePrecheck](Formula_RevivePrecheck.md)
- Observed behaviours: [FormulaHandlerContract](../behaviors/FormulaHandlerContract.md)

## Notes

Formula block B46 (2026-11-12): 79 bytes, read whole. Crosscheck: the cleared bits 0x0200 and 0x4000 are complemented 16-bit immediates; g_FormulaBlock +0x20 is the byte at 0x1407B0790 (RIP-relative).

## Open questions

None recorded.
