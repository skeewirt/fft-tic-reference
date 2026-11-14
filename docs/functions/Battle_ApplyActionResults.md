# Battle_ApplyActionResults

- **Address:** `0x140206758`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64_t Battle_ApplyActionResults(void)`
- **Callers:** `Battle_ExecuteAction` (`0x140206BE6`), `sub_140210AF0` (`0x140212D69`, battle state 43)
- **Callees:** `sub_14026079C`, `sub_140204CDC`, `sub_140260ABC`, `Battle_ApplyActionResult` (`0x1402067DF`), `sub_140283784`, `sub_14027192C`, `sub_140268EE0`, `BattleAnim_SelectMotion` (`0x1402069DF`), `sub_140269790` (`0x1402069EB`)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the resolved action to every target and starts each target's hit animation; this is the step that
turns the formula result into live HP/MP/status changes and visible hits.

## Behavior

- V: sets `dword_140C6B1CC = 44` (`0x140206770`) and gets the acting scene object with `sub_14026079C`.
- V: clears the acting object's animation word `+0x0C`.
- V: loops over the target list on the acting object: count at `+0x1A9` (425), slots at `+0x1AA` (426).
- V: for each slot: gets its scene object with `sub_140260ABC`, then calls
  `Battle_ApplyActionResult(slot)` at `0x1402067DF` and stores the return value on the target object.
- V: on return -1 calls `sub_140283784(slot, unitRecord+0x1A0)` (action-request cleanup) and
  `sub_140268F68` (death/crystal handling).
- V: on the first successful hit, sets the target's `+0x1F5 = actorSlot` and increments the actor's hit
  counter at `BattleControl + 4*slot + 0xA94D4` (capped 9999).
- V: after the loop, checks special action ids 74/75/76 and unit flags; then calls
  `BattleAnim_SelectMotion(obj, targetObj)` at `0x1402069DF` or the weapon-motion
  `sub_140269790` at `0x1402069EB` for each target.
- V: after the loop, for a 512-target or no-target case it calls `sub_140269790(obj, targetObj)` or
  `BattleAnim_SelectMotion(obj, targetObj)`; otherwise it runs the per-target finishing calls
  `sub_14027192C` and `sub_140268EE0`.
- V: returns 0 (or 1 when the first target is a special action) and leaves the scene object's animation
  id at `+0x10` for the renderer.

## State touched

- Calls: [Battle_ApplyActionResult](Battle_ApplyActionResult.md), [BattleAnim_SelectMotion](BattleAnim_SelectMotion.md)

## Referenced by

- Called by: [Battle_ExecuteAction](Battle_ExecuteAction.md)

## Notes

`BattleControl` is the singleton at `0x143CD9EF0`; the hit counter table starts at `+0xA94D4`
(`693396`).

## Open questions

- Whether the loop applies every target at once or one per frame (the call site in `sub_140210AF0` is a
  state, so likely one pass; a delayed copy also exists in `sub_1402029DC`).
