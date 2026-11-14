# WorldMap_UpdateFastForward

- **Address:** `0x14015C0DC`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void WorldMap_UpdateFastForward(void)`
- **Callers:** sub_14015A860, sub_14015AB34, sub_1402482F8
- **Callees:** GlobalWork_GetFastForwardMode, Input_IsActionHeld

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

On the world map (mode 3) sets the fast-forward level to 1 while action 89 is held, else 0.

## Behavior

- V: when GlobalWork_GetFastForwardMode returns 3, GlobalWork +88 = Input_IsActionHeld(action 89) (0 or 1).
- V: action 90 is not read here, so the world map has no level 2.
- V: mode 3 is written by sub_14033EC0C (the world map set-up); several world UI routines clear the level when they open a panel while the mode is 3 (sub_14014DC80, sub_140157864, sub_140157C30, sub_14015B7C4, sub_140247A4C, sub_1402CC2E0).

## State touched

- Calls: [GlobalWork_GetFastForwardMode](GlobalWork_GetFastForwardMode.md), [Input_IsActionHeld](Input_IsActionHeld.md)
- Reads: [g_GlobalWork](../globals/g_GlobalWork.md), [g_InputModule](../globals/g_InputModule.md)
- Writes: [GlobalWork.ff_level](../structs/GlobalWork.md#ff_level)

## Referenced by

- Observed behaviours: [FastForwardState](../behaviors/FastForwardState.md)

## Open questions

? Which world-map states its three callers cover.
