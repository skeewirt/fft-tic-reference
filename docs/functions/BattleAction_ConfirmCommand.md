# BattleAction_ConfirmCommand

- **Address:** `0x140203620`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void __fastcall BattleAction_ConfirmCommand(char a1)`
- **Callers:** sub_140210AF0 (battle frame update), Battle_TimelineFocusCamera, sub_140209218 (timeline), sub_140206F90, sub_14020A18C (map cursor), sub_140203690, sub_1402071F4, sub_14020AFA4; data references at 0x143D3748C and 0x143D37498
- **Callees:** Battle_FindUnitNodeAt, sub_140203450, sub_14020327C, sub_140202F34

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses one of the three command-confirm handlers for the unit under the cursor and records the cursor unit's id. The chosen handler starts presentation script 3 and moves the battle state.

## Behavior

- V: resolves the unit node at the three cursor tile coordinates with `Battle_FindUnitNodeAt` and returns when there is no node.
- V: copies the node's byte +8 into `dword_140C6AD8C`.
- V: when `dword_140D3A840` is non-zero, or the node's byte +8 differs from the current actor id `dword_140CF873C`, it calls `sub_140203450`.
- V: otherwise, when the node's byte +340 has bit 8 set, it calls `sub_14020327C`.
- V: otherwise it calls `sub_140202F34`.
- I: the first two handlers set `g_BattleState` to 4 and the third sets it to 5; all three start presentation script 3 with `BattleAction_StartScript(3, ..., 0)` (rests on the handler bodies, which are not part of this function).
- I: the three-way choice is: a unit other than the current actor (or the `dword_140D3A840` state) takes the unit-targeting handler, the current actor with byte +340 bit 8 takes the flagged handler, and everything else takes the plain handler. (rests on the handler bodies and the sub_140203450 sheet.)

## State touched

- Calls: [Battle_FindUnitNodeAt](Battle_FindUnitNodeAt.md), [sub_140203450](sub_140203450.md), [sub_14020327C](sub_14020327C.md)

## Referenced by

- Appears in flows: [BattleTimelineCameraFlow](../flows/BattleTimelineCameraFlow.md)
- Called by: [Battle_TimelineFocusCamera](Battle_TimelineFocusCamera.md), [sub_140206F90](sub_140206F90.md)

## Notes

Whole body read (112 bytes). The three handlers have their own sheets; this function only chooses between them and records the cursor unit id.

## Open questions

What does `dword_140D3A840` select? What does the node byte +340 bit 8 mean? Why does the plain handler move the battle state to 5 rather than 4?
