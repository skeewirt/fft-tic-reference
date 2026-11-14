# BattleAnim_SelectMotion

- **Address:** `0x140269988`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int16_t BattleAnim_SelectMotion(int64_t sceneObject, int64_t targetObject)`
- **Callers:** `Battle_ApplyActionResults` (`0x1402069DF`), itself indirectly via `sub_140269790`
- **Callees:** `sub_140269790` (`0x1402699E8`), `sub_140266890`, `sub_140268E04`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Chooses the battle motion (animation id) for an ability: weapon attack, cast/ranged special, or a fixed
motion from the per-ability table, then starts it on the unit.

## Behavior

- V: reads `g_AbilityAnim[abilityId].motion` at `0x1402699D6` (`unk_140672DA1 + 3*id`); the ability id
  is `[sceneObject+0x142]`.
- V: motion 0 -> `sub_140269790` (weapon motion by weapon animation type at unit `+0x152`).
- V: motion 1 -> `sub_140266890(obj, [obj+0x150])` then a distance test against the target; adjacent or
  same-tile -> motion 58, otherwise an arcing motion via `sub_140268E04(76, ...)`.
- V: other motion values -> `motion + 1`.
- V: stores the chosen id at `[sceneObject+0x10]` (`0x140269A95`) and calls
  `sub_140268E04(motion, [sceneObject+0x7C], sceneObject)`.
- V: the weapon path (`sub_140269790`) picks from `aAbAbAbAbAbAbAb` by weapon type `[unit+0x152]` and
  also calls `sub_140268E04`.

## State touched

- Calls: [sub_140266890](sub_140266890.md)

## Referenced by

- Appears in flows: [AbilityLifecycle](../flows/AbilityLifecycle.md)
- Called by: [Battle_ApplyActionResults](Battle_ApplyActionResults.md)

## Notes

`g_AbilityAnim` `0x140672DA0`: byte 0 charge type, byte 1 motion, byte 2 battle text (X3). The battle
text byte is consumed by `sub_140210AF0` at `+0x18C`.

## Open questions

- Meaning of the +1 offset for motions >= 2 (probably table row bias).
