# BattleAct_SetupEffect

- **Address:** `0x1402060F4`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64_t BattleAct_SetupEffect(int abilityId, void *sceneObject)`
- **Callers:** `Battle_ExecuteAction` (`0x140206BDF`)
- **Callees:** `memset`, `sub_140260ABC`, `SceneObject_FindBySlot`, `Item_GetWeaponRecord`, `AbilityAction_GetRecord`, `Effect_SelectForAbility` (`0x140206317`)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Selects the visual effect for an ability: builds the list of units on screen, reads the ability's charge
byte from `g_AbilityAnim`, combines it with the ability element and calls the effect-number selector.

## Behavior

- V: reads the acting unit's ability id (`a2[14].vt` in the decompile) and its slot (`a2[18]...`).
- V: builds a 0xE4-byte unit/position list from the scene objects (`SceneObject_FindBySlot`).
- V: reads `g_AbilityAnim[abilityId].charge` at `0x1402062CB` (`unk_140672DA0 + 3*id`).
- V: when the ability id is < 368, ORs the ability action record's element (`AbilityAction_GetRecord(id)[7] << 16`) into the effect word (`0x140206300`).
- V: calls `Effect_SelectForAbility(effectWord, abilityId, &list)` at `0x140206317`.
- V (2026-11-12): `rdi` holds the scene object from `0x14020611E` to the call at `0x140206317` (no instruction in between writes it; the callees keep it); the effect word is in `edx` at the call.
- I: the resulting effect is the spell/impact visual played by the target hit sequence; the motion is
  chosen separately by `BattleAnim_SelectMotion`.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [AbilityAction_GetRecord](AbilityAction_GetRecord.md), [Effect_SelectForAbility](Effect_SelectForAbility.md)

## Referenced by

- Called by: [Battle_ExecuteAction](Battle_ExecuteAction.md)
- Observed behaviours: [BattleEffectsAreOneFilePerNumber](../behaviors/BattleEffectsAreOneFilePerNumber.md)

## Notes

`g_AbilityAnim` is `0x140672DA0`, 3 bytes per row (charge, motion, battle text), 454 rows (X3 sheet).
The same charge byte is used by `sub_140206C14` to pick a cast motion.

## Open questions

- How `Effect_SelectForAbility`'s return value reaches the effect spawner (not traced).
