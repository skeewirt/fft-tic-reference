# BattleAnim_SelectMotion

- **Address:** `0x140269988`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int16_t BattleAnim_SelectMotion(int64_t sceneObject, int64_t targetObject)`
- **Callers:** `Battle_ApplyActionResults` (`0x1402069DF`), itself indirectly via BattleAnim_SelectWeaponMotion
- **Callees:** BattleAnim_SelectWeaponMotion (`0x1402699E8`), `sub_140266890`, BattleAnim_StartMotion

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses the battle motion (animation id) for an ability: weapon attack, cast/ranged special, or a fixed
motion from the per-ability table, then starts it on the unit.

## Behavior

- V: reads `g_AbilityAnim[abilityId].motion` at `0x1402699D6` (`unk_140672DA1 + 3*id`); the ability id
  is `[sceneObject+0x142]`.
- V: motion 0 -> BattleAnim_SelectWeaponMotion (weapon motion by weapon animation type; the byte at unit `+0x152` is read inside BattleAnim_SelectWeaponMotion, not here).
- V: motion 1 -> `sub_140266890(obj, [obj+0x150])` then a distance test against the target; adjacent or
  same-tile -> motion 58, otherwise an arcing motion via BattleAnim_StartMotion(76, ...).
- V: other motion values -> `motion + 1`.
- M (data test, 2026-11-14): the motion numbers of the ability table and the weapon table are pair indices of the classic animation file: animation pointer `2 x motion` is the front view and `2 x motion + 1` the back view. Weapon motions land on animations that draw the attack frames and carry the hit marker (one weapon type's animations carry none); of 57 distinct ability motion values 34 were tested: values from 40 up land on animations that draw action frames, the low ones on single-frame poses, one on an empty pointer. `2 x motion + 2` lands on the next animation of the same group, so the choice of `2 x motion` rests on the high / middle / low ordering of a weapon type's three motions (see BattleAnim_SelectWeaponMotion). The code that turns the +0x10 number into the pointer is not located.
- V: stores the chosen id at `[sceneObject+0x10]` (`0x140269A95`) and calls
  BattleAnim_StartMotion(motion, [sceneObject+0x7C], sceneObject).
- V: the weapon path (BattleAnim_SelectWeaponMotion) picks from `aAbAbAbAbAbAbAb` by weapon type `[unit+0x152]` and
  also calls BattleAnim_StartMotion.

## State touched

- Calls: [BattleAnim_SelectWeaponMotion](BattleAnim_SelectWeaponMotion.md), [sub_140266890](sub_140266890.md), [BattleAnim_StartMotion](BattleAnim_StartMotion.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [Battle_ApplyActionResults](Battle_ApplyActionResults.md)
- Observed behaviours: [BattleMotionNumbers](../behaviors/BattleMotionNumbers.md)
- Reads tables: [SpriteLookAttributes](../tables/SpriteLookAttributes.md)

## Notes

`g_AbilityAnim` `0x140672DA0`: byte 0 charge type, byte 1 motion, byte 2 battle text. The battle
text byte is consumed by `sub_140210AF0` at `+0x18C`.

## Open questions

- Answered: the +1 is added by BattleAnim_StartMotion (the stored animation number is motion + 1); the classic animation pair index is the motion itself (see above).
