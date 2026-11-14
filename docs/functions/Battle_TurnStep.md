# Battle_TurnStep

- **Address:** `0x1402029DC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int __fastcall Battle_TurnStep(void)`
- **Callers:** `Battle_CommandTask` (`0x140202B4E`)
- **Callees:** `Battle_TurnEngine`, `sub_140260ABC`, `sub_14030A488`, `sub_140283784`, `sub_140268F68`, `SceneObject_FindBySlot`, `sub_14026801C`, `sub_1401FAF54`, `ScenePreview_ClaimForUnit`, `sub_1402607C0`, `sub_1401FA7D4`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs one step of the turn engine on the player path and dispatches the returned action code to the scene/UI.

## Behavior

- V: calls `Battle_TurnEngine(0)` (`0x1402029E8`) and stores `result & 0xFF00` in `dword_140D3A868`
  (`0x1402029FB`).
- V: returns immediately when the code is `0xFF00` (engine gave up).
- V: looks the unit up with `sub_140260ABC(low byte)` (`0x140202A0E`); a missing unit ends the step.
- V: `0x100` (turn start) -> `ScenePreview_ClaimForUnit(slot)` (`0x140202AD2`), which sets the scene object's
  active words.
- V: `0x300` -> `sub_14030A488(slot)` (end-of-turn effects) at `0x140202A53`; if it returns `-1`, the unit is
  removed (`sub_140283784`, `sub_140268F68`).
- V: `0x400` -> the same end-of-turn call plus `SceneObject_FindBySlot`, `sub_14026801C` and `sub_1401FAF54`
  (scene refresh), at `0x140202AA6`.
- V: the returned unit node's `+8` byte is stored in `dword_140CF873C` and `sub_1402607C0` is used to re-run the
  current-unit lookups.

## State touched

- Calls: [Battle_TurnEngine](Battle_TurnEngine.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [ScenePreview_ClaimForUnit](ScenePreview_ClaimForUnit.md)

## Referenced by

- Called by: [Battle_CommandTask](Battle_CommandTask.md)

## Notes

This is the player-side adapter between the engine's action codes and the scene; the AI side has its own adapter in
`Battle_AITurnRun`.

## Open questions

What distinguishes the `0x400` path from `0x300` (the extra scene calls suggest a join/leave or a scene-unit claim).
