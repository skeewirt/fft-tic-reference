# Formula_DrawOutGate

- **Address:** `0x14030655C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_DrawOutGate(void)`
- **Callers:** Formula_32_DrawOutDamage, Formula_33_DrawOutDamageStatus, Formula_34_DrawOutBuff, Formula_35_DrawOutHeal
- **Callees:** Rng_Percent

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The Draw Out katana break roll: writes the caster-side result with the broken-or-kept flag.

## Behavior

- V: skipped when the caster's job (+3) is 0x5D.
- V: otherwise it sets RC+0 = 1, RC+4 = the caster's word +0x1A8 (the katana's item id) and RC+2 = 8.
- V: RC+18 = 0x1000 (broken) when g_BattleSimulating is non-zero or Rng_Percent(100, the weapon record copy's byte 0x1407B07AC) is false (the roll fell under the break percent); else RC+18 = 8 (kept).
- I: so the preview always shows the katana as breaking; the weapon record byte +4 is the break chance.

## State touched

- Calls: [Rng_Percent](Rng_Percent.md)

## Notes

102 bytes, read whole. Called by Formula_32 to Formula_35 (the Draw Out formulas).

## Open questions

? what the RC flags 0x1000 and 8 make the result applier do (the consumer was not read here).
