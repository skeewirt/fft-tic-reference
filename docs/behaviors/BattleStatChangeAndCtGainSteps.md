# BattleStatChangeAndCtGainSteps

- **Kind:** observed behaviour
- **Scope:** engine
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Battle_TurnEngine](../functions/Battle_TurnEngine.md), [Unit_ChangeBattleStat](../functions/Unit_ChangeBattleStat.md), [Unit_ApplyEquipment](../functions/Unit_ApplyEquipment.md), [Formula_TargetStatusPhys](../functions/Formula_TargetStatusPhys.md), [Formula_TargetStatusMag](../functions/Formula_TargetStatusMag.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Unit_ChangeBattleStat changes PA / MA / Speed at the base +0x38..+0x3A with the totals +0x3E..+0x40; Move / Jump are at +0x42 / +0x43; the Haste / Slow CT step is in phase 0 of Battle_TurnEngine; Protect and Shell scale the A value in Formula_TargetStatusPhys / Mag.

## Behavior

- V (code read): PA / MA / Speed change at the base +0x38..+0x3A with the totals +0x3E..+0x40 kept as Unit_ChangeBattleStat does; Move / Jump are at +0x42 / +0x43, which a job row reload rebuilds.
- V (code read): the Haste / Slow step of CT gain is in phase 0 (BTurn_StatusFlags); Formula_TargetStatusPhys / Mag are called at 18 places and scale the A value where Protect and Shell apply.

## Open questions

None recorded.
