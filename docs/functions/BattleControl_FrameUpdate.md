# BattleControl_FrameUpdate

- **Address:** `0x1401EA110`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleControl_FrameUpdate(BattleControl *bc)`
- **Callers:** sub_140210AF0 (the battle frame routine, one call near its end)
- **Callees:** GlobalWork_GetFastForwardMode, Input_IsActionHeld, sub_1401EC6F8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame update of the battle control object; its first part sets the fast-forward level in battle straight from the held buttons.

## Behavior

- V: does nothing unless g_ShopModeGate (the enhanced-edition flag) is non-zero.
- V: when bit 4 of the PauseManager byte +24 is clear, GlobalWork_GetFastForwardMode returns 1 and dword_140D3A840 is 0: level (GlobalWork +88) = 2 when action 90 is held, else 1 when action 89 is held, else 0 (Input_IsActionHeld).
- V: it is a level test: no press edge, no delay and no timer; the level follows the button on every frame this branch runs.
- V: when one of the three conditions fails the level is left as it is (not cleared here).
- V: the rest updates the 21 per-unit voice controllers and four more, and swaps two small buffers.

## State touched

- Calls: [GlobalWork_GetFastForwardMode](GlobalWork_GetFastForwardMode.md), [Input_IsActionHeld](Input_IsActionHeld.md)
- Reads: [g_GlobalWork](../globals/g_GlobalWork.md), [g_InputModule](../globals/g_InputModule.md), [g_ShopModeGate](../globals/g_ShopModeGate.md), [InputActionRow.held](../structs/InputActionRow.md#held)
- Writes: [GlobalWork.ff_level](../structs/GlobalWork.md#ff_level)

## Referenced by

- Observed behaviours: [FastForwardState](../behaviors/FastForwardState.md)

## Notes

The mode it tests is written earlier in the same battle frame routine (record FastForwardState).

## Open questions

? What dword_140D3A840 stands for (set 1 by Battle_CommandTask in one branch, cleared by three battle input routines).
