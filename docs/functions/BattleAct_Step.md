# BattleAct_Step

- **Address:** `0x140206A0C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleAct_Step(void)`
- **Callers:** sub_14020CFEC, sub_140210AF0
- **Callees:** BattleAct_BuildResult, sub_140204FF0, sub_14020CABC, ItemSprite_LoadPalettes, Effect_AbilityHasNoEffect, BattleAct_NoEffectStep, BattleAct_SetupEffect

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The scene step that executes the acting object's action: builds the result, sets the effect word and chooses the presentation path.

## Behavior

- V: BattleAct_BuildResult(unit, obj +0x1A8); the effect word +0x142 = the result word +0x1BC.
- V: a word that is 0, 512 (the sentinel), another word than +0x1C2 when that is set, or one Effect_AbilityHasNoEffect accepts goes to BattleAct_NoEffectStep; every other word to BattleAct_SetupEffect (charge byte, element, effect number).
- V: the test `+0x1BC == 512 && +0x1BF == 1 && +0x1BA == 1 && +0x1CC` marks the sentinel case (only the sentinel write sets +0x1BF with 512).
- V (2026-11-12): the unit argument of BattleAct_BuildResult is the byte +0x1BC of the battle unit the object points at (+0x148); BattleAct_BuildResult reads the action's ability word at g_BattleUnitTable + that slot * 0x200 + 0x1A2 for the result word, so at BattleAct_SetupEffect that word is still the action's whole ability id.
- V: gets the acting scene object with sub_14026079C; when the action has an effect it sets the battle state dword_140C6B1CC = 43 (0x140206BD3: the effect plays, then state 43 runs BattleAct_NoEffectStep's apply loop); with none it calls BattleAct_NoEffectStep at once (0x140206BE6).
- V: writes the acting unit's animation and state fields and loads the item palettes (ItemSprite_LoadPalettes).
- I: the effect is chosen before the results are applied so the hit or miss can select the impact animation.

## State touched

- Calls: [BattleAct_BuildResult](BattleAct_BuildResult.md), [ItemSprite_LoadPalettes](ItemSprite_LoadPalettes.md), [Effect_AbilityHasNoEffect](Effect_AbilityHasNoEffect.md), [BattleAct_NoEffectStep](BattleAct_NoEffectStep.md), [BattleAct_SetupEffect](BattleAct_SetupEffect.md)

## Referenced by

- Called by: [sub_140210AF0](sub_140210AF0.md)

## Notes

An ability word of 512 is taken for the sentinel here (no effect, the weapon motion: a punch in game 2026-10-30). Called on the frame after the command state machine reaches state 47 (sub_14020CFEC). Earlier sheet name: Battle_ExecuteAction.

## Open questions

None recorded.
