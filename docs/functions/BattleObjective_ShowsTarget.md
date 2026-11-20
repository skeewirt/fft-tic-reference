# BattleObjective_ShowsTarget

- **Address:** `0x1401EB5D0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleObjective_ShowsTarget(uint32_t spawnFlags)`
- **Callers:** TurnPanel_SetUnitPanel, TurnPanel_SetTag, BattleFormation_DrawUnits, sub_140291490, sub_1401EA2F0
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when a unit's spawn flag set marks it as an objective target and the current battle objective asks for targets to be shown.

## Behavior

- V: returns 1 when (argument & 0x04) and the current objective's (dword_140D3AD54) BattleObjective row byte +0x0C (column show_targets) is non-zero.
- V: callers pass unit dword +504 (the spawn flag set, bit 2 = OverrideEntryData flag_2): TurnPanel_SetUnitPanel, TurnPanel_SetTag (tag kind 2), BattleFormation_DrawUnits (marker kind 2), sub_140291490 ('ShowTarget' / 'HideTarget') and sub_1401EA2F0 (focus camera on each such unit).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [sub_1401EA2F0](sub_1401EA2F0.md)
- Observed behaviours: [UnitEventFlagWord](../behaviors/UnitEventFlagWord.md)

## Open questions

None recorded.
