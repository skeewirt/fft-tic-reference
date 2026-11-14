# Action_SetWeaponItem

- **Address:** `0x1403098CC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Action_SetWeaponItem(void *action)`
- **Callers:** `Battle_ResolveAction`, `Battle_ResolveTargets`
- **Callees:** `AbilityAction_GetRecord`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the weapon item id of a battle action from the acting unit's equipped weapon, with 255 standing for empty hands and
zero written for an empty or out-of-range id.

## Behavior

- V: It stores the action record passed in rcx and reads a global action/ability kind before deciding which weapon to use.
- V: The weapon word comes from one of three global words, selected by that kind and by the action's own state byte.
- V: The weapon id is compared with 255; a match means no weapon.
- V: A second path accepts the id only when it is below 261, so an id above the stock range is treated as no weapon.
- V: An empty or rejected id is written as 0 into word 5 of the current-action block at 0x1407B0770 (offset +0xA); an
  accepted id is written as itself.
- V: When the id is accepted it resolves the ability action record through AbilityAction_GetRecord, so the weapon id and
  the action's ability row stay linked.
- I: The 255 test and the 261 bound are the same empty/bound pair used by the other equipment readers; the function is the
  action-side writer of that value.
- ?: Whether the action record's weapon field is a plain item id or an index into the ability action table is not settled
  by the code read.

## State touched

- Calls: [AbilityAction_GetRecord](AbilityAction_GetRecord.md)

## Referenced by

- Called by: [Battle_ResolveAction](Battle_ResolveAction.md), [Battle_ResolveTargets](Battle_ResolveTargets.md), [sub_1403099B0](sub_1403099B0.md)

## Notes

- V: Its two callers are Battle_ResolveAction (the sheet for 0x1403099B0) and Battle_ResolveTargets, which places it on
  the action build path.

## Open questions

None recorded.
