# Formula_56_StatusOnlyApplication

- **Address:** `0x14030698C`
- **Area:** [Battle formulas](../areas/formulas.md)
- **Prototype:** `void Formula_56(void)`
- **Callers:** Formula dispatcher (`Formula_106_ReDispatchChainFormula`)
- **Callees:** shared formula pipeline (see [Battle formulas](../areas/formulas.md))
- **Dispatch ID:** 56

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Status-only application: the shared status engine used by many formulas; no damage component.

## Behavior

- V: Current-build decompilation confirms the chain and arithmetic shown above.
- V: Current-build symbol size is 580 bytes.
- V: Typical abilities: Salve, Petrify, Shadowbind, Bad Breath, Grand Cross (22 total).
- V: reads the inflict record copy (g_FormulaBlock +0x40, flag byte then five status bytes) and writes the add set R+29..33 and the remove set R+34..38 (Status_FilterPendingSets' names for them); it is the status step of 16 handlers directly.
- V: flag bit 0x20 first divides R+44 by 4; flag bit 0x80 (or bit 0x40 / 0x20 while g_BattleSimulating is non-zero) copies the five status bytes into R+29..33; bit 0x40 picks one listed status at random (Battle_Rand15); bit 0x20 drops each listed status when Rng_Percent(100, 24) is true (kept on a 24 percent roll; a preview at level 2 drops all) and adds the rest; bit 0x10 copies the five bytes into the remove set R+34..38 instead (V for the offsets; the sheet text above calls it a secondary add table).
- V: at the end, when any status bit is set and Status_FilterPendingSets(0) is non-zero: R+39 |= 0x08, and R+18 |= 0x40 only when R+30 has bit 0x40; otherwise R+0 = 0, R+2 = 7, R+44 = 0 (no effect).
- V: the damage formulas reach it through Formula_StatusTailKeepHit, which restores R+0, R+2 and R+44 afterwards.

## Calculation

```text
status engine with 4 modes:
 bit 0x80: add statuses directly from ability data
 bit 0x40: random status from target's current statuses
 bit 0x20: remove matching statuses (faith roll)
 bit 0x10: add from secondary status table
No damage component — status only
```

## Referenced by

- Called by: [Formula_StatusTailKeepHit](Formula_StatusTailKeepHit.md)
- Observed behaviours: [StatusLoopsInflictCopyAndBattleTableLifetime](../behaviors/StatusLoopsInflictCopyAndBattleTableLifetime.md)

## Notes

Address and size are current-build values from `symbols/functions.json`. The calculation was verified by decompiling the current function; the earlier formula research was used only as a starting point.

## Open questions

Which status mode each caller uses is not mapped.
