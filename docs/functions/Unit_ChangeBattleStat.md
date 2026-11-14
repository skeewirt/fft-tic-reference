# Unit_ChangeBattleStat

- **Address:** `0x14030C080`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Unit_ChangeBattleStat(char change, uint8_t *stat, uint8_t cap, uint8_t min)`
- **Callers:** Battle_ApplyActionResult
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies one stat change of an action result to a unit stat byte, clamped, and keeps the stat total in step.

## Behavior

- V: change bit 7 set = an increase by the low 7 bits, clear = a decrease; with cap 0xFF and an amount of 127 the amount becomes 255.
- V: the new value is clamped to min..cap; it returns 0 when the value does not change, else writes it and returns 1.
- V: when min is 1 it also writes stat[6] = min(value + stat[3], cap): for the base stats +0x38..+0x3A (the pointer the caller passes) this is the total +0x3E..+0x40 = base + equipment bonus +0x3B..+0x3D.
- V: the caller passes the change and the byte: Battle_ApplyActionResult calls it for result block +0x14 on +0x3A (Speed, cap 50, min 1), +0x15 on +0x41 (CT, cap 255, min 0), +0x16 on +0x38 (PA, cap 99, min 1), +0x17 on +0x39 (MA, cap 99, min 1), +0x18 on +0x2B (Brave, cap 100) and +0x19 on +0x2D (Faith, cap 100, min 0) (offsets of the caller, not of this function).

## State touched

- Writes: [UnitWorkRecord.pa_base](../structs/UnitWorkRecord.md#pa_base), [UnitWorkRecord.pa_total](../structs/UnitWorkRecord.md#pa_total)

## Referenced by

- Observed behaviours: [BattleStatChangeAndCtGainSteps](../behaviors/BattleStatChangeAndCtGainSteps.md)

## Notes

Name is ours. Whole function read.

## Open questions

None recorded.
