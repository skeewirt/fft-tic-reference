# Unit_GetActionGateState

- **Address:** `0x14030DD1C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 __fastcall Unit_GetActionGateState(uint8_t *unit)`
- **Callers:** BTurn_IsUnitDone, BattleAction_ReleaseCharged, BattleCommand_BuildMenu, BattleCommand_BuildUnitList, BattleMenu_ConfirmRow, BattleMsg_UnitTurnScene, Formula_ReactionPrecheck and others
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Classifies a battle unit as 1, 0 or 2 from some status and flag bits and the terrain under it.

## Behavior

- V: returns 1 when byte +101 has bit 0x04 or byte +436 has bit 0x40.
- V: returns 0 when the unit's tile byte 3 (layer from bit 7 of +81, x at +79, y at +80) has its top three bits below 2, or +99 has any of 0x46, or +158 has any of 0xC8, or +436 has bit 7.
- V: otherwise returns 2.
- V: BattleCommand_BuildMenu and BattleMenu_ConfirmRow use the value 4099 when the result is 2; Formula_ReactionPrecheck returns it.
- I: 2 is the unrestricted state (rests on those two callers).

## Referenced by

- Called by: [Formula_AdjustHitForTargetFlag](Formula_AdjustHitForTargetFlag.md)

## Notes

Whole body read.

## Open questions

What the three results mean to a player.
